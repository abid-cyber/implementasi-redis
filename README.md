# Tugas Topik Khusus — Redis dengan Python

Program Python sederhana yang mendemonstrasikan operasi dasar Redis.

## Tipe Data yang Didemonstrasikan

| No | Tipe Data   | Operasi                    |
|----|-------------|----------------------------|
| 1  | String      | `SET`, `GET`, `DEL`        |
| 2  | Hash        | `HSET`, `HGETALL`          |
| 3  | List        | `LPUSH`, `RPUSH`, `LRANGE` |
| 4  | Set         | `SADD`, `SMEMBERS`         |
| 5  | Sorted Set  | `ZADD`, `ZRANGE`           |
| 6  | Expiry/TTL  | `SETEX`, `TTL`             |

## Prasyarat

- **Docker** (untuk menjalankan Redis)
- **Python 3.x**

## Cara Menjalankan

### 1. Jalankan Redis via Docker

```bash
docker run -d --name tugas-redis -p 6379:6379 redis
```

### 2. Install dependency Python

```bash
pip install -r requirements.txt
```

### 3. Jalankan program

```bash
python main.py
```

## Output

Program akan menampilkan hasil setiap operasi Redis di terminal, termasuk demonstrasi TTL (Time To Live) pada key yang memiliki waktu kadaluarsa.
