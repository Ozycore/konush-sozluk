#!/usr/bin/env python3
"""manifest.json ile konush-sozluk.sqlite3 birbirini tutuyor mu? Yalnız standart kütüphane; hata varsa çıkış kodu 1.

Kontrol: dosya boyutu ve sha256, şema sürümü ve lisans (manifest ↔ meta tablosu), madde/anahtar/Türkçe karşılık
sayıları ve tür dağılımı (manifest ↔ gerçek tablolar), SQLite bütünlüğü. `sources` içindeki lisans metinleri
bilerek karşılaştırılmaz: manifestteki açıklama, dosya yeniden üretilmeden (sha256 değişmeden) netleştirilebilir.
"""
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    errors = []
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    db_path = ROOT / manifest["file"]

    if not db_path.is_file():
        print(f"HATA: {db_path.name} yok")
        return 1

    size = db_path.stat().st_size
    if size != manifest["size_bytes"]:
        errors.append(f"boyut {size} ≠ manifest {manifest['size_bytes']}")

    digest = hashlib.sha256()
    with db_path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    if digest.hexdigest() != manifest["sha256"]:
        errors.append(f"sha256 {digest.hexdigest()} ≠ manifest {manifest['sha256']}")

    db = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    meta = dict(db.execute("SELECT key, value FROM meta"))
    if meta.get("schema_version") != str(manifest["schema_version"]):
        errors.append(f"meta.schema_version {meta.get('schema_version')!r} ≠ manifest {manifest['schema_version']!r}")
    if meta.get("license") != manifest["license"]:
        errors.append(f"meta.license {meta.get('license')!r} ≠ manifest {manifest['license']!r}")
    if json.loads(meta.get("counts", "null")) != manifest["counts"]:
        errors.append("meta.counts manifest.counts ile aynı değil")

    counts = manifest["counts"]
    actual = {
        "entries": db.execute("SELECT count(*) FROM entry").fetchone()[0],
        "keys": db.execute("SELECT count(*) FROM skey").fetchone()[0],
        "with_tr": db.execute("SELECT count(*) FROM entry WHERE tr IS NOT NULL AND tr <> '[]'").fetchone()[0],
    }
    for name, value in actual.items():
        if value != counts[name]:
            errors.append(f"{name}: tabloda {value}, manifestte {counts[name]}")
    by_pos = dict(db.execute("SELECT pos, count(*) FROM entry GROUP BY pos"))
    if by_pos != counts["by_pos"]:
        errors.append(f"by_pos tabloda {by_pos}, manifestte {counts['by_pos']}")
    if sum(counts["by_pos"].values()) != counts["entries"]:
        errors.append("manifestte by_pos toplamı entries ile aynı değil")
    check = db.execute("PRAGMA quick_check").fetchone()[0]
    if check != "ok":
        errors.append(f"PRAGMA quick_check: {check}")

    if errors:
        print("HATA: manifest ve sözlük dosyası uyuşmuyor")
        for line in errors:
            print(f"  - {line}")
        return 1
    print(f"OK — {manifest['file']}: sha256 {manifest['sha256'][:12]}…, {counts['entries']} madde, "
          f"{counts['with_tr']} Türkçe karşılıklı, {counts['keys']} arama anahtarı")
    return 0


if __name__ == "__main__":
    sys.exit(main())
