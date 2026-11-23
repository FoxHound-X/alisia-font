# Laporan Kepatuhan & Rekonsiliasi Audit Google Fonts

Dokumen ini mencatat tindak lanjut dan penyelesaian teknis dari temuan audit awal pada file `audit-awal-alisia-font-google-fonts.md`.

---

## 1. Matriks Rekonsiliasi Audit

| No | Poin Temuan Audit | Kondisi Awal | Tindakan Perbaikan Teknis | Status |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Konsistensi URL Repository** | Terdapat perbedaan antara nama repo aktual (`alisia-font`) dengan rujukan di dokumen (`font-alisia`). | Seluruh rujukan URL di `README.md`, `METADATA.pb`, `OFL.txt`, `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `specimen.html`, serta **di dalam tabel `name` (NameID 0 & 11) seluruh file binary font** telah disinkronkan ke `https://github.com/FoxHound-X/alisia-font`. | **RESOLVED** |
| **2** | **Lokasi File TTF & Kesesuaian Metadata** | `METADATA.pb` mencantumkan `filename: "Alisia-Regular.ttf"` tanpa path, sedangkan file TTF sebelumnya hanya ada di `fonts/ttf/`. | Disediakan struktur yang selaras ganda: paket mandiri `fonts/ttf/` kini dilengkapi `METADATA.pb`, `DESCRIPTION.en_us.html`, dan `OFL.txt` siap impor ke `google/fonts/ofl/alisia/`, serta file TTF juga tersedia di root repositori. | **RESOLVED** |
| **3** | **Source Font & Reproducible Build** | Tidak ada file sumber terbuka yang dapat diedit dan tidak ada skrip build. | Dibuat direktori `sources/` yang memuat sumber master XML lossless (`.ttx`), konfigurasi ruang desain (`Alisia.designspace`), dokumentasi `sources/README.md`, dan pipeline otomatisasi `sources/build.py`. | **RESOLVED** |
| **4** | **Klaim Kepatuhan Prematur** | Dokumentasi sebelumnya mengklaim font telah memenuhi seluruh standar Google Fonts sebelum pengujian selesai. | Redaksi `README.md` direvisi secara objektif, menyajikan matriks kepatuhan teknis yang transparan, checklist onboarding, dan menanggalkan klaim absolut sepihak. | **RESOLVED** |
| **5** | **Pengujian Teknis & Vertical Metrics** | Metrik vertikal belum distandarisasi (`sTypoLineGap = 130`, `hhea` tidak cocok dengan `sTypo`, bit `USE_TYPO_METRICS` mati). | Metrik vertikal dikalibrasi penuh: `sTypoLineGap = 0`, `hhea.lineGap = 0`, `sTypoAscender = 980` == `hhea.ascent = 980`, `sTypoDescender = -220` == `hhea.descent = -220`, `usWinAscent = 1050`, `usWinDescent = 260`, dan bit 7 `USE_TYPO_METRICS` diaktifkan (1). Dibuat skrip validasi `qa_audit.py`. | **RESOLVED** |
| **6** | **Kepemilikan Hak Cipta** | Hubungan hak cipta antara `The Alisia Project Authors` dan desainer utama `FoxHound-X` perlu diperjelas. | Berkas `AUTHORS.txt`, `CONTRIBUTORS.txt`, dan `OFL.txt` diperbarui sesuai standar Google Fonts Guide dengan penjelasan peruntukan file dan atribusi desainer utama. | **RESOLVED** |

---

## 2. Rincian Kalibrasi Parameter Teknis

```
Parameter                  Sebelum Perbaikan      Sesudah Perbaikan (Standar GF)
--------------------------------------------------------------------------------
OS/2.sTypoAscender         810                    980
OS/2.sTypoDescender        -210                   -220
OS/2.sTypoLineGap          130 (FAIL)             0 (PASS)
OS/2.usWinAscent           1020 (Hazard < 1044)   1050 (PASS, > yMax 1044)
OS/2.usWinDescent          260                    260 (PASS, > |yMin| 237)
OS/2.fsSelection (bit 7)   0 (Non-aktif)          1 (USE_TYPO_METRICS Aktif)
hhea.ascent                980                    980 (Match typoAscender)
hhea.descent               -220                   -220 (Match typoDescender)
hhea.lineGap               0                      0 (Match typoLineGap)
nameID 0 (Copyright)       .../font-alisia        .../alisia-font
nameID 11 (Vendor URL)     .../font-alisia        .../alisia-font
```

---

## 3. Checklist Sebelum Pengajuan (Checklist Status)

- [x] Nama keluarga font unik dan tidak melanggar merek dagang (`Alisia`).
- [x] Semua style menggunakan lisensi SIL Open Font License 1.1 (`OFL.txt`).
- [x] Source asli tersedia dan dapat diedit (`sources/*.ttx` & `Alisia.designspace`).
- [x] Proses build didokumentasikan dan dapat direproduksi (`sources/build.py`).
- [x] Cakupan karakter memenuhi standar Latin Core.
- [x] Metadata keluarga, style, bobot, dan copyright konsisten di seluruh tabel.
- [x] File TTF tersedia pada lokasi yang cocok dengan referensi `METADATA.pb`.
- [x] Kalibrasi metrik vertikal Google Fonts teruji (`qa_audit.py`).
- [x] Rendering, spacing, kerning, dan outline diperiksa melalui `specimen.html`.
- [x] Dokumentasi repositori konsisten dan menyajikan status kepatuhan teknis yang transparan.
