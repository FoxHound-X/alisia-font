# Alisia Source & Build Documentation

Berkas-berkas di direktori `sources/` ini merupakan *single source of truth* (file sumber asli) untuk keluarga huruf Alisia.

## Berkas Sumber

* `Alisia.designspace`: Definisi ruang desain (*designspace*) multi-master untuk sumbu bobot (*Weight axis* `wght`: 400 - 700).
* `Alisia-Regular.ttx`: Definisi XML lengkap dan lossless dari master Regular (400).
* `Alisia-Medium.ttx`: Definisi XML lengkap dan lossless dari master Medium (500).
* `Alisia-Bold.ttx`: Definisi XML lengkap dan lossless dari master Bold (700).
* `build.py`: Skrip kompilasi otomatis yang membaca file sumber, menerapkan kalibrasi metrik Google Fonts, dan menghasilkan binary `.ttf`, `.otf`, serta `.woff2`.

## Kebutuhan Lingkungan (Prerequisites)

* Python 3.10+
* `fonttools >= 4.50.0`
* `brotli >= 1.1.0` (untuk kompresi webfont WOFF2)

Instal dependensi:
```bash
pip install fonttools brotli
```

## Cara Menjalankan Build

Dari direktori root repositori:
```bash
python sources/build.py
```

Skrip ini akan:
1. Membaca sumber XML (`.ttx`) untuk masing-masing master bobot.
2. Mengalibrasi metrik vertikal Google Fonts (`sTypoLineGap = 0`, `hhea.lineGap = 0`, `USE_TYPO_METRICS = 1`).
3. Memastikan keselarasan tabel `name`, ID hak cipta, dan URL repositori resmi (`https://github.com/FoxHound-X/alisia-font`).
4. Mengeluarkan output ke:
   * `fonts/ttf/`
   * `fonts/otf/`
   * `fonts/woff2/`
