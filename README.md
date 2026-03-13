# Implementasi Redis dengan Python (Docker)

Repository ini berisi implementasi sederhana penyimpanan dan manipulasi data menggunakan Python dan Redis yang dijalankan melalui Docker.

## Langkah Instalasi

### 1. Instalasi Docker

Pastikan Docker Desktop sudah terinstall di komputer kamu. Download di: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

Setelah terinstall, pastikan Docker sudah berjalan.

### 2. Menjalankan Redis via Docker

Buka terminal (PowerShell / Command Prompt) di Visual Studio Code (VSC) dan jalankan:

```bash
docker run -d --name tugas-redis -p 6379:6379 redis
```

Penjelasan perintah:
- `run` — Menjalankan container baru
- `-d` — Menjalankan di latar belakang (detached)
- `--name tugas-redis` — Memberi nama container
- `-p 6379:6379` — Menghubungkan port Redis ke localhost
- `redis` — Image resmi Redis dari Docker Hub

Cek apakah container sudah jalan:

```bash
docker ps
```

Jika container `tugas-redis` muncul di daftar, berarti Redis sudah berhasil berjalan!

### 3. Persiapan Lingkungan Python

Install library redis untuk Python:

```bash
pip install -r requirements.txt
```

## Operasi Redis yang Digunakan

| No | Operasi   | Perintah Redis   | Keterangan                          |
|----|-----------|------------------|-------------------------------------|
| 1  | SET       | `SET key value`  | Menyimpan data ke Redis             |
| 2  | GET       | `GET key`        | Mengambil data dari Redis           |
| 3  | DEL       | `DEL key`        | Menghapus data dari Redis           |
| 4  | EXPIRE    | `EXPIRE key detik` | Set waktu kadaluarsa (dalam detik) |

## Cara Menjalankan

Pastikan container Redis menyala:

```bash
docker start tugas-redis
```

Jalankan script:

```bash
python main.py
```

## Contoh Output

```
Ping: True
SET user:1 = Abid Mustaghfirin
GET user:1 = Abid Mustaghfirin
DEL user:1 -> GET user:1 = None
SET session:1 = active (expire 5 detik)
TTL session:1 = 5 detik
Setelah 3 detik -> TTL = 2 detik
```

## Cara Menghentikan Redis (Docker)

Jika sudah selesai dan ingin mematikan Redis:

Menghentikan container:

```bash
docker stop tugas-redis
```

Memastikan container sudah mati:

```bash
docker ps
```

Jika `tugas-redis` tidak muncul di daftar, berarti sudah berhasil dihentikan.

Untuk menjalankan kembali:

```bash
docker start tugas-redis
```
