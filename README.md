# Implementasi Redis dengan Python

Program Python sederhana yang mendemonstrasikan operasi dasar Redis menggunakan Docker.

## Operasi Redis yang Digunakan

| No | Operasi   | Perintah Redis | Keterangan                     |
|----|-----------|----------------|--------------------------------|
| 1  | SET       | `SET key value`| Menyimpan data                 |
| 2  | GET       | `GET key`      | Mengambil data                 |
| 3  | DEL       | `DEL key`      | Menghapus data                 |
| 4  | EXPIRE    | `EXPIRE key s` | Set waktu kadaluarsa (detik)   |

## Cara Menjalankan

### 1. Jalankan Redis via Docker

```bash
docker run -d --name tugas-redis -p 6379:6379 redis
```

Jika container sudah pernah dibuat, cukup start:

```bash
docker start tugas-redis
```

### 2. Install dependency Python

```bash
pip install -r requirements.txt
```

### 3. Jalankan program

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
