# Sistem Bimbingan Jurusan

## Deskripsi
Sistem Bimbingan Jurusan merupakan aplikasi backend berbasis REST API yang membantu siswa mengenali bidang minat dan menghubungkannya dengan pilihan jurusan. Aplikasi ini dibuat untuk membantu siswa SMA/SMK memperoleh gambaran awal mengenai jurusan yang sesuai dengan minatnya.

## Teknologi
- Python
- Flask
- Flask-SQLAlchemy
- PostgreSQL (Neon)
- JSON
- Vercel

## URL Deployment
https://sistem-bimbingan-jurusan.vercel.app/

## Struktur Database
Database terdiri dari lima tabel yang saling berhubungan:

1. Siswa: menyimpan data siswa.
2. Jurusan: menyimpan informasi jurusan, deskripsi, dan prospek karier.
3. Bidang Minat: menyimpan data bidang minat.
4. Siswa Minat: menghubungkan siswa dengan bidang minat.
5. Jurusan Minat: menghubungkan jurusan dengan bidang minat.

## Entity Relationship Diagram (ERD)
ERD menggambarkan hubungan antartabel melalui primary key dan foreign key.

Gambar ERD dapat dilihat pada file `erd.png` di repositori ini.

## Dokumentasi Endpoint API

### 1. Siswa

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/siswa` | Mengambil semua data siswa |
| POST | `/siswa` | Menambahkan data siswa |
| GET | `/siswa/<id>` | Mengambil detail siswa berdasarkan ID |
| PUT | `/siswa/<id>` | Mengubah data siswa |
| DELETE | `/siswa/<id>` | Menghapus data siswa |

Contoh body POST dan PUT:

```json
{
  "nama": "Andi",
  "kelas": "12",
  "asal_sekolah": "SMA Citra Bangsa"
}
```

### 2. Jurusan

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/jurusan` | Mengambil semua data jurusan |
| POST | `/jurusan` | Menambahkan data jurusan |
| PUT | `/jurusan/<id>` | Mengubah data jurusan |
| DELETE | `/jurusan/<id>` | Menghapus data jurusan |

Contoh body POST dan PUT:

```json
{
  "nama_jurusan": "Informatika",
  "deskripsi": "Mempelajari pemrograman dan teknologi komputer",
  "prospek_karier": "Programmer"
}
```

### 3. Bidang Minat

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/bidang-minat` | Mengambil semua bidang minat |
| POST | `/bidang-minat` | Menambahkan bidang minat |
| PUT | `/bidang-minat/<id>` | Mengubah bidang minat |
| DELETE | `/bidang-minat/<id>` | Menghapus bidang minat |

Contoh body POST dan PUT:

```json
{
  "nama_bidang": "Pemrograman",
  "deskripsi": "Minat dalam membuat program dan aplikasi"
}
```

### 4. Siswa Minat

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/siswa-minat` | Mengambil hubungan siswa dan minat |
| POST | `/siswa-minat` | Menambahkan hubungan siswa dan minat |
| PUT | `/siswa-minat/<id>` | Mengubah hubungan siswa dan minat |
| DELETE | `/siswa-minat/<id>` | Menghapus hubungan siswa dan minat |

Contoh body POST dan PUT:

```json
{
  "siswa_id": 2,
  "bidang_minat_id": 1
}
```

### 5. Jurusan Minat

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/jurusan-minat` | Mengambil hubungan jurusan dan minat |
| POST | `/jurusan-minat` | Menambahkan hubungan jurusan dan minat |
| PUT | `/jurusan-minat/<id>` | Mengubah hubungan jurusan dan minat |
| DELETE | `/jurusan-minat/<id>` | Menghapus hubungan jurusan dan minat |

Contoh body POST dan PUT:

```json
{
  "jurusan_id": 1,
  "bidang_minat_id": 1
}
```

## Penanganan Error
API menangani beberapa kondisi kesalahan menggunakan kode status HTTP:

- `200 OK`: permintaan berhasil.
- `201 Created`: data berhasil ditambahkan.
- `400 Bad Request`: input tidak lengkap atau tidak valid.
- `404 Not Found`: data tidak ditemukan.
- `405 Method Not Allowed`: metode HTTP tidak diizinkan pada endpoint.

## Cara Menjalankan Aplikasi Secara Lokal

1. Pastikan Python sudah terinstal.
2. Aktifkan virtual environment.
3. Instal dependensi dengan perintah:

   ```bash
   pip install -r requirements.txt
   ```

4. Siapkan variabel lingkungan `DATABASE_URL` untuk koneksi ke PostgreSQL Neon.
5. Jalankan aplikasi:

   ```bash
   python run.py
   ```

6. Akses aplikasi melalui `http://127.0.0.1:5000`.

## Pengujian API
Pengujian dilakukan menggunakan URL deployment Vercel untuk memeriksa fungsi API dan penyimpanan data.

Pengujian yang sudah dilakukan:
- GET untuk mengambil data.
- POST untuk menambahkan data.
- PUT untuk mengubah data siswa.
- DELETE untuk menghapus data siswa.
- Pengujian ID yang tidak ditemukan dengan respons `404`.
- Pengujian input tidak lengkap dengan respons `400`.

