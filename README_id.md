# honkai-star-rail-helper

`honkai-star-rail-helper` adalah utilitas yang dirancang untuk mengelola dan memproses data karakter, keterampilan, dan rekomendasi peninggalan untuk video game [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail). Alat ini membaca file input, memproses berbagai atribut seperti informasi karakter dan set keterampilan, dan menghasilkan hasil dalam format yang terorganisir. Data input berasal dari paket pembaruan resmi di repositori [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) dan output disimpan di folder khusus versi untuk kemudahan pengelolaan.

## Tabel Karakter Terbaru
<!-- CHARACTER_TABLE_START -->
|           |   | Destruction                | Hunt          | Erudition | Harmony     | Nihility      | Preservation | Abundance |
| --------- | - | -------------------------- | ------------- | --------- | ----------- | ------------- | ------------ | --------- |
| Physical  | 5 | Clara\|Trailblazer\|Yunli  | Boothill      | Argenti   | Robin       |               |              |           |
| Physical  | 4 |                            | Sushang       |           | Hanya       | Luka          |              | Natasha   |
| Fire      | 5 | Firefly                    | Topaz & Numby | Himeko    |             | Jiaoqiu       | Trailblazer  | Lingsha   |
| Fire      | 4 | Hook                       |               |           | Asta        | Guinaifen     |              | Gallagher |
| Ice       | 5 | Jingliu                    | Yanqing       |           | Ruan Mei    |               | Gepard       |           |
| Ice       | 4 | Misha                      |               | Herta     |             | Pela          | March 7th    |           |
| Lightning | 5 |                            |               | Jing Yuan |             | Acheron\|Kafka |              | Bailu     |
| Lightning | 4 | Arlan                      | Moze          | Serval    | Tingyun     |               |              |           |
| Wind      | 5 | Blade                      | Feixiao       |           | Bronya      | Black Swan    |              | Huohuo    |
| Wind      | 4 |                            | Dan Heng      |           |             | Sampo         |              |           |
| Quantum   | 5 |                            | Seele         | Jade      | Sparkle     | Silver Wolf   | Fu Xuan      |           |
| Quantum   | 4 | Xueyi                      |               | Qingque   |             |               |              | Lynx      |
| Imaginary | 5 | Dan Heng · Imbibitor Lunae | Dr. Ratio     |           | Trailblazer | Welt          | Aventurine   | Luocha    |
| Imaginary | 4 |                            | March 7th     |           | Yukong      |               |              |           |
<!-- CHARACTER_TABLE_END -->

## Fitur Utama
- Secara otomatis mengunduh data karakter, CV, set keterampilan, dan rekomendasi peninggalan.
- Memproses dan mengatur data ke dalam direktori input/output yang dibagi berdasarkan versi.
- Konfigurasi nomor versi melalui baris perintah untuk setiap pembaruan baru.

## Persyaratan

Pastikan Anda memiliki yang berikut:
- **Python 3.8+** (konfirmasi dengan `python3 --version`).
- Paket Python yang diperlukan tercantum dalam `requirements.txt`.

## Instalasi

1. **Clone repositori:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(Opsional) Buat dan aktifkan lingkungan virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Di Windows: venv\Scriptsctivate
   ```

3. **Instal dependensi (saat ini tidak diperlukan dependensi tambahan):**
   ```bash
   # Tidak perlu menginstal dependensi saat ini, tetapi jika diperlukan di masa mendatang:
   # pip install -r requirements.txt
   ```

## Penggunaan

### Jalankan Alat
   Arahkan ke direktori `src/` dan jalankan skrip utama dengan nomor versi yang diinginkan:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - Ganti `<version_number>` dengan versi saat ini (misalnya, `2.5`).
   - Jika Anda ingin melewati pengunduhan file, tambahkan opsi `--skip-download`.

   File input akan diunduh ke folder `input/{version}`, dan output akan disimpan di folder `output/{version}`.

### Contoh Penggunaan

- Untuk menjalankan skrip dengan versi `2.5` dan mengunduh file:
  ```bash
  python3 main.py --version 2.5
  ```

- Untuk menjalankan skrip dengan versi `2.5` dan melewati pengunduhan file:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- Untuk menjalankan skrip dengan versi 2.5 dan mengunduh file untuk bahasa tertentu (misalnya, EN dan JP):
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## Kontribusi

Kami menerima kontribusi! Anda dapat:
- Mengirimkan pull request untuk fitur baru atau perbaikan bug.
- Melaporkan masalah melalui pelacak masalah.
- Pastikan semua kontribusi mencakup pengujian dan dokumentasi yang relevan.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
