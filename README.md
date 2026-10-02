# Konush sözlük verisi

Almanca–Türkçe başvuru sözlüğü: isim hâlleri, fiil çekimleri, sıfat çekim kökleri, edatların yönettiği hâl ve Türkçe karşılıklar.
[Konush](https://konush-web.ozycore.workers.dev) uygulamasının çevrimdışı sözlüğü bu dosyadır.

**Lisans: [CC BY-SA 4.0](LICENSE).** Bu veri, aşağıdaki kaynakların **değiştirilmiş** bir hâlidir ve aynı lisansla paylaşılır.

## Kaynaklar

- **Almanca Vikisözlük** (de.wiktionary.org) katkıcıları — isim, fiil, sıfat ve edat bilgileri. Çıkarım:
  [Wiktextract / kaikki.org](https://kaikki.org/dewiktionary/) (Vikisözlük dökümü 2026-09-01, çıkarım 2026-09-24).
- **[WikDict](https://www.wikdict.com)** de-tr (Karl Bartel; [DBnary](http://kaiko.getalp.org/about-dbnary/), Vikisözlük) — Türkçe karşılıklar
  (2026-06-23 sürümü).

Kaynak dosyaların adresi, tarihi ve sha256'sı `manifest.json` içindedir. WikDict de-tr (2026-06-23 sürümü) kendi sitesinde
([wikdict.com/page/about](https://www.wikdict.com/page/about), 2026-10-02'de okundu) veriyi "Creative Commons BY-SA" altında
sunar ve lisans bağlantısı **CC BY-SA 4.0**'a gider; bu sözlük de CC BY-SA 4.0 ile paylaşılır. Yukarı akıştaki DBnary
veri kümesi CC BY-SA 3.0 Unported der; BY-SA 3.0 uyarlamaların aynı unsurlara sahip sonraki sürümle paylaşılmasına izin verir
(§4(b)). Bu bir hukuki görüş değildir. Dosyanın içindeki `meta` tablosu eski ifadeyi ("CC BY-SA 3.0/4.0") taşır; açıklamada
`manifest.json` esas alınır, dosya bir sonraki üretimde güncellenecektir.

## Yapılan değişiklikler

- Yalnız Almanca madde başları alındı; çekimli biçim maddeleri ve özel adlar çıkarıldı. Türkçe kişi ve yer adı geçen
  madde başları ile Türkçe karşılıklar da çıkarıldı.
- İsim: dört hâl × tekil/çoğul; birden çok cinsli isimlerde bütün cinsler (`m,n`); aynı ismin aynı cinsli kayıtları birleştirildi.
  Sıfattan türeyen isimlerde (der Beamte) belirli artikelli biçim artikelsiz yazıldı.
- Fiil: Präsens ve Präteritum bütün kişiler, Partizip II ve yardımcı fiil, Imperativ, Konjunktiv II (ich).
- Sıfat: derece biçimleri ve çekim kökleri (`klein-`, `kleiner-`, `kleinst-`); hücreler kök + düzenli ekle üretilir.
  *lila, rosa, orange, beige, prima, super, klasse, extra, spitze* ve şehir adından türeyen *-er* sıfatları çekimsiz işaretlendi;
  Vikisözlük'te çekilmez etiketli sıfatlar ayrıca işaretlendi.
- Edat: yönettiği hâl (A1–A2 edatları elle tamamlandı); kaynaşmış edatlar (im = in dem, zum = zu dem …) edat olarak eklendi.
- Türkçe karşılık: WikDict'te her anlamın ilk çevirisi, puan sırasıyla, en fazla üç; yoksa Vikisözlük'ün Türkçe çevirisi.
- Arama anahtarları: küçük harf, aksansız (ä→a, ß→ss, ı→i), sabit kurallarla.
- Küfür ve hakaret (Konush 4+ bir uygulamadır): bütün anlamları Vikisözlük'te *vulgär* ya da *pejorativ* etiketli maddeler ve
  etiketi eksik sık küfür, cinsel argo ve etnik/grup hakaretleri çıkarıldı; kaba Türkçe karşılıklar alınmadı.

Veri otomatik üretilmiştir ve tek tek incelenmemiştir; hata içerebilir.

## Hata bildirimi

Yanlış ya da eksik bir madde, çekim ya da Türkçe karşılık görürsen
[GitHub Issues](https://github.com/Ozycore/konush-sozluk/issues) üzerinden yaz; mümkünse madde başını (ör. `Haus`), neyin
yanlış olduğunu ve doğrusunu ekle. Uygulamadan da yazabilirsin: Konush → Ayarlar → İletişim. Veri Vikisözlük ve WikDict'ten
otomatik üretildiği için kalıcı düzeltme çoğu zaman kaynağın kendisinde yapılır; hatayı orada da düzeltebilirsen yardımcı olur.
Sınır: 161.878 maddenin 40.671'inde Türkçe karşılık var, kalanında yok.

## Doğrulama

`python3 verify.py` dosya boyutunu ve sha256'yı, şema sürümünü, lisansı ve madde, anahtar, Türkçe karşılık ve tür sayılarını
`manifest.json` ile karşılaştırır; uyuşmazlıkta çıkış kodu 1. Aynı kontrol her değişiklikte GitHub Actions'ta
(`.github/workflows/verify.yml`) çalışır. Sözlük dosyasını yeniden üretirsen önce `manifest.json`'u güncelle.

## Dosyalar

| Dosya | İçerik |
|---|---|
| `konush-sozluk.sqlite3` | SQLite veritabanı (şema: [SCHEMA.md](SCHEMA.md)) |
| `manifest.json` | şema sürümü, kaynaklar, sayılar, dosyanın sha256'sı |
| `LICENSE` | CC BY-SA 4.0 lisans metni |
| `verify.py` | manifest ↔ dosya doğrulaması (standart kütüphane) |

---

# Konush dictionary data (English)

A German–Turkish reference dictionary: noun cases, verb conjugations, adjective declension stems, prepositional case government
and Turkish equivalents. It is the offline dictionary of the Konush app.

**License: [CC BY-SA 4.0](LICENSE).** This data is an **adapted** version of the sources below and is shared under the same license:
contributors to the German Wiktionary (de.wiktionary.org), extracted with [Wiktextract / kaikki.org](https://kaikki.org/dewiktionary/)
(dump 2026-09-01, extraction 2026-09-24), and [WikDict](https://www.wikdict.com) de-tr (Karl Bartel; DBnary, Wiktionary; 2026-06-23).
The changes are listed above in Turkish (headwords only, names and inflected-form entries removed, compact tables, merged
same-gender homographs, all genders kept, curated preposition cases and contractions, up to three Turkish equivalents,
entries and equivalents naming Turkish persons or places removed, vulgar and offensive entries and crude Turkish equivalents
removed).
The data was generated automatically and has not been reviewed entry by entry.

WikDict states on its own site ([wikdict.com/page/about](https://www.wikdict.com/page/about), read 2026-10-02) that its data is under
"Creative Commons BY-SA" and links CC BY-SA 4.0; upstream DBnary says CC BY-SA 3.0 Unported. `manifest.json` is authoritative
for the source licenses (the file's own `meta` table still carries the older wording and will be refreshed at the next build).

**Reporting errors:** open an issue at [GitHub Issues](https://github.com/Ozycore/konush-sozluk/issues) with the headword, what
is wrong and the correct form. Because the data is generated from Wiktionary and WikDict, fixing the source is often the lasting fix.
**Verification:** `python3 verify.py` checks file size, sha256, schema version, license and counts against `manifest.json`;
the same check runs in GitHub Actions on every change.
