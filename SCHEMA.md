# Şema 1 — `konush-sozluk.sqlite3`

```sql
CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT NOT NULL) WITHOUT ROWID;
-- schema_version="1", license="CC BY-SA 4.0", sources=<json>, counts=<json>

CREATE TABLE entry(id INTEGER PRIMARY KEY, lemma TEXT NOT NULL, pos TEXT NOT NULL, genus TEXT, ipa TEXT, tr TEXT, data TEXT);
-- pos: noun | verb | adj | adv | prep | pron | conj | num | phrase | intj | other
-- genus (yalnız isim): m | f | n, birden çoksa "m,n" (das/der Kilo); yalnız çoğul: pl
-- tr: JSON dizi, en fazla 3 Türkçe karşılık; data: JSON, türe göre (aşağıda)

CREATE TABLE skey(k TEXT NOT NULL, entry INTEGER NOT NULL, kind INTEGER NOT NULL,
                  PRIMARY KEY (k, kind, entry)) WITHOUT ROWID;
-- k: katlanmış anahtar (küçük harf, ä→a ö→o ü→u ß→ss ı→i, aksanlar atılır)
-- kind: 0 madde başı · 1 çekimli biçim · 2 Türkçe karşılık
```

## `data`

| Tür | Biçim |
|---|---|
| isim | `{"c": [[nom.sg], [akk.sg], [dat.sg], [gen.sg], [nom.pl], [akk.pl], [dat.pl], [gen.pl]]}` — her hücre biçim dizisi, yoksa `[]` |
| fiil | `{"pres": [6], "past": [6], "pp": "…", "aux": ["haben"], "imp": ["sprich!", "sprecht!"], "k2": "…"}` — kişi sırası ich, du, er/sie/es, wir, ihr, sie/Sie; eksik `""` |
| sıfat | `{"deg": ["klein", "kleiner", "am kleinsten"], "st": ["klein", "kleiner", "kleinst"], "x": {hücre: biçim}}`; çekimsiz (Konush listesi, şehir adından -er) `{"deg": …, "indecl": true}`; Vikisözlük'te çekilmez etiketli `{"deg": …, "nodecl": true}` |
| edat | `{"cases": ["akk", "dat"]}`; kaynaşmış edat `{"cases": ["dat"], "contraction": "in dem"}` |

Sıfat hücresi = kök (`st`, derece sırasıyla) + ek. Hücre kodu `derece.tür.hâl.cins`: derece `pos|comp|sup`, tür `weak|mixed|strong`,
hâl `nom|akk|dat|gen`, cins `m|f|n|pl`. `x`, kök + ekten farklı olan hücreleri verir. Ekler:

| | m | f | n | pl |
|---|---|---|---|---|
| strong nom / akk / dat / gen | er / en / em / en | e / e / er / er | es / es / em / en | e / e / en / er |
| weak nom / akk / dat / gen | e / en / en / en | e / e / en / en | e / e / en / en | en / en / en / en |
| mixed nom / akk / dat / gen | er / en / en / en | e / e / en / en | es / es / en / en | en / en / en / en |

## Örnek sorgu

```sql
-- "Häusern" hangi kelimenin hangi biçimi?
SELECT e.lemma, e.pos, e.genus, e.data FROM skey s JOIN entry e ON e.id = s.entry WHERE s.k = 'hausern';
```
