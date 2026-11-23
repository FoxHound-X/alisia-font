# Alisia Typeface Family

**Alisia** adalah rupa huruf (*typeface*) kontemporer yang didesain khusus untuk **kenyamanan membaca tingkat tinggi (fatigue-free reading)** di bawah lisensi resmi **[SIL Open Font License, Version 1.1](https://openfontlicense.org)**. Font ini telah memenuhi seluruh standar arsitektur dan metadata teknis untuk dipublikasikan ke katalog **Google Fonts**.

Repositori Resmi: **[https://github.com/FoxHound-X/font-alisia](https://github.com/FoxHound-X/font-alisia)**

---

## 1. Lisensi SIL Open Font License (OFL 1.1)

Font ini dilisensikan secara bebas dan terbuka di bawah **SIL Open Font License v1.1**.
* Teks lisensi resmi: [OFL.txt](file:///C:/SetiaAI/Alisia/OFL.txt)
* Hak Cipta: `Copyright 2026 The Alisia Project Authors (https://github.com/FoxHound-X/font-alisia)`
* URL Lisensi & FAQ: [https://openfontlicense.org](https://openfontlicense.org)

---

## 2. Kesiapan Publikasi ke Google Fonts (Google Fonts Ready)

Paket font Alisia telah dikonfigurasi mengikuti pedoman resmi *Google Fonts Onboarding & Fontbakery Specification*:

1. **[OFL.txt](file:///C:/SetiaAI/Alisia/OFL.txt):** Header hak cipta resmi terhubung ke repositori `FoxHound-X/font-alisia`.
2. **[METADATA.pb](file:///C:/SetiaAI/Alisia/METADATA.pb):** Berkas manifest Google Fonts dengan desainer `FoxHound-X`, lisensi `OFL`, kategori `SANS_SERIF`, subset aksara `latin` dan `latin-ext`, serta pemetaan file `.ttf`.
3. **[DESCRIPTION.en_us.html](file:///C:/SetiaAI/Alisia/DESCRIPTION.en_us.html):** Deskripsi resmi keluarga font untuk tampilan katalog Google Fonts.
4. **[AUTHORS.txt](file:///C:/SetiaAI/Alisia/AUTHORS.txt) & [CONTRIBUTORS.txt](file:///C:/SetiaAI/Alisia/CONTRIBUTORS.txt):** Daftar pemilik hak cipta dan kontributor proyek.
5. **[FONTLOG.txt](file:///C:/SetiaAI/Alisia/FONTLOG.txt):** Catatan riwayat proyek dan *changelog* versi 1.000.
6. **OpenType `name` Table yang Valid:**
   * `NameID 0` (Copyright): `Copyright 2026 The Alisia Project Authors (https://github.com/FoxHound-X/font-alisia)`
   * `NameID 7` (Trademark): `Alisia is a trademark of FoxHound-X.`
   * `NameID 8 & 9` (Manufacturer & Designer): `FoxHound-X`
   * `NameID 11` (Vendor URL): `https://github.com/FoxHound-X/font-alisia`
   * `NameID 13` (License Description): Teks resmi OFL 1.1 tersemat di seluruh binary font.
   * `NameID 14` (License URL): `https://openfontlicense.org`
   * `OS/2.achVendID`: `FOXH`

---

## 3. Struktur Direktori Proyek

Folder proyek: `C:\SetiaAI\Alisia\`

```
C:\SetiaAI\Alisia\
├── OFL.txt                        (Teks Lisensi Resmi SIL OFL 1.1)
├── METADATA.pb                    (Manifest Google Fonts Onboarding)
├── DESCRIPTION.en_us.html         (Deskripsi Resmi Katalog Google Fonts)
├── AUTHORS.txt                    (Daftar Pemilik Hak Cipta)
├── CONTRIBUTORS.txt               (Daftar Kontributor Proyek)
├── FONTLOG.txt                    (Log Riwayat Pengembangan Proyek)
├── README.md                      (Dokumentasi Ergonomi & Panduan Teknis)
├── specimen.html                  (Spesimen Interaktif & Reader Mode Tester)
└── fonts\
    ├── ttf\                       (Format Standar Google Fonts)
    │   ├── Alisia-Regular.ttf     (Bobot Standar 400)
    │   ├── Alisia-Medium.ttf      (Bobot Sedang 500)
    │   └── Alisia-Bold.ttf        (Bobot Tebal 700)
    ├── otf\
    │   ├── Alisia-Regular.otf
    │   ├── Alisia-Medium.otf
    │   └── Alisia-Bold.otf
    └── woff2\                     (WebFont Terkompresi Brotli ~12 KB)
        ├── Alisia-Regular.woff2
        ├── Alisia-Medium.woff2
        └── Alisia-Bold.woff2
```

---

## 4. Cara Push ke GitHub & Mendaftarkan ke Google Fonts

```bash
# 1. Inisialisasi Git di folder Alisia
cd C:\SetiaAI\Alisia
git init
git add .
git commit -m "feat: initial release of Alisia font family v1.000 (OFL 1.1)"

# 2. Hubungkan dengan remote repository GitHub Anda
git remote add origin https://github.com/FoxHound-X/font-alisia.git
git branch -M main
git push -u origin main
```

Setelah di-push ke GitHub, Anda dapat mengajukan penambahan font ke repositori resmi [google/fonts](https://github.com/google/fonts) melalui Pull Request atau New Family Issue.
