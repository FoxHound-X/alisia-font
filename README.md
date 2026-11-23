# Alisia Typeface Family

**Alisia** adalah keluarga rupa huruf (*typeface family*) kontemporer berjenis humanistik sans-serif yang didesain secara teliti untuk **kenyamanan membaca tingkat tinggi (*fatigue-free reading*)** pada layar digital maupun media cetak di bawah lisensi resmi **[SIL Open Font License, Version 1.1](https://openfontlicense.org)**.

Repositori Resmi: **[https://github.com/FoxHound-X/alisia-font](https://github.com/FoxHound-X/alisia-font)**

---

## 1. Lisensi SIL Open Font License (OFL 1.1)

Font ini dilisensikan secara bebas dan terbuka di bawah **SIL Open Font License v1.1**.
* Teks lisensi resmi: [OFL.txt](file:///C:/SetiaAI/Alisia/OFL.txt)
* Pernyataan Hak Cipta: `Copyright 2026 The Alisia Project Authors (https://github.com/FoxHound-X/alisia-font)`
* Panduan & FAQ Lisensi: [https://openfontlicense.org](https://openfontlicense.org)

---

## 2. Status Kesiapan & Onboarding Google Fonts

Keluarga huruf Alisia dipersiapkan dan distandarisasi secara ketat mengikuti pedoman teknis **Google Fonts Onboarding Guide** dan spesifikasi pengujian **Fontbakery**:

| Komponen / Parameter | Status Teknis | Keterangan Standar Google Fonts |
| :--- | :--- | :--- |
| **Lisensi & Copyright** | Terverifikasi | SIL OFL 1.1, atribusi `The Alisia Project Authors` |
| **Sumber Master (*Sources*)** | Lengkap | Sumber XML lossless (`.ttx`), konfigurasi `Alisia.designspace`, skrip `build.py` |
| **Metrik Vertikal (*Vertical Metrics*)** | Terstandarisasi | `sTypoLineGap = 0`, `hhea.lineGap = 0`, `USE_TYPO_METRICS` bit aktif |
| **Penyelarasan hhea & typo** | Terverifikasi | `sTypoAscender = 980` == `hhea.ascent = 980`; `sTypoDescender = -220` == `hhea.descent = -220` |
| **Bebas Clipping (*Win Metrics*)** | Terverifikasi | `usWinAscent = 1050` (yMax: 1044); `usWinDescent = 260` (yMin: -237) |
| **Konsistensi Penamaan & URL** | Terverifikasi | Tabel `name` (ID 0, 1, 2, 4, 6, 11) merujuk ke `FoxHound-X/alisia-font` |
| **Paket Onboarding** | Terverifikasi | `METADATA.pb`, `DESCRIPTION.en_us.html`, `OFL.txt`, dan file `.ttf` berada dalam jalur yang selaras |

> Rincian penyelesaian catatan audit awal dapat dibaca pada [AUDIT-COMPLIANCE.md](file:///C:/SetiaAI/Alisia/AUDIT-COMPLIANCE.md).

---

## 3. Struktur Direktori Proyek

```
alisia-font/
├── OFL.txt                        # Teks Lisensi Resmi SIL OFL 1.1
├── METADATA.pb                    # Manifest Google Fonts Onboarding
├── DESCRIPTION.en_us.html         # Deskripsi Katalog Google Fonts
├── AUTHORS.txt                    # Daftar Pemilik Hak Cipta Proyek
├── CONTRIBUTORS.txt               # Daftar Kontributor Proyek
├── FONTLOG.txt                    # Log Riwayat Pengembangan Versi 1.000
├── README.md                      # Dokumentasi Teknis Utama
├── AUDIT-COMPLIANCE.md            # Laporan Pemenuhan Standar & Catatan Audit
├── qa_audit.py                    # Skrip Validasi Teknis Mandiri
├── specimen.html                  # Spesimen Interaktif & Reader Mode Tester
├── sources/                       # Berkas Sumber Asli & Pipeline Build
│   ├── Alisia.designspace         # Definisi Sumbu Interpolasi (wght: 400 - 700)
│   ├── Alisia-Regular.ttx         # XML Source Master Regular (400)
│   ├── Alisia-Medium.ttx          # XML Source Master Medium (500)
│   ├── Alisia-Bold.ttx            # XML Source Master Bold (700)
│   ├── build.py                   # Skrip Kompilasi Reproducible
│   └── README.md                  # Dokumentasi Pengembangan Sumber
└── fonts/                         # Direktori Binary Terkompilasi
    ├── ttf/                       # Format TrueType (Google Fonts Distribution)
    │   ├── Alisia-Regular.ttf
    │   ├── Alisia-Medium.ttf
    │   ├── Alisia-Bold.ttf
    │   ├── METADATA.pb
    │   ├── DESCRIPTION.en_us.html
    │   └── OFL.txt
    ├── otf/                       # Format OpenType
    │   ├── Alisia-Regular.otf
    │   ├── Alisia-Medium.otf
    │   └── Alisia-Bold.otf
    └── woff2/                     # WebFont Terkompresi Brotli
        ├── Alisia-Regular.woff2
        ├── Alisia-Medium.woff2
        └── Alisia-Bold.woff2
```

---

## 4. Cara Membangun Font dari Sumber (*Build from Source*)

Pastikan Python 3.10+ telah terpasang bersama paket `fonttools` dan `brotli`:

```bash
pip install fonttools brotli
```

Jalankan kompilasi:

```bash
python sources/build.py
```

Skrip build akan secara otomatis membaca sumber master dari `sources/`, mengalibrasi metrik vertikal, menyelaraskan metadata nama, dan menghasilkan seluruh varian binary font (`.ttf`, `.otf`, `.woff2`).

---

## 5. Menjalankan Uji Kualitas Teknis (*QA Audit*)

Jalankan skrip audit mandiri untuk memverifikasi kepatuhan parameter teknis:

```bash
python qa_audit.py
```

---

## 6. Sinkronisasi Git & Push ke Repositori Resmi

```bash
# Inisialisasi atau periksa status Git
cd C:\SetiaAI\Alisia
git status

# Pastikan remote mengarah ke repositori resmi alisia-font
git remote set-url origin https://github.com/FoxHound-X/alisia-font.git

# Stage dan commit perubahan
git add .
git commit -m "chore: align repository structure and font metrics with Google Fonts specifications"

# Push ke cabang utama
git push origin main
```
