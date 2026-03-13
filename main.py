import redis
import time

# Koneksi ke Redis
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Cek koneksi
print("Ping:", r.ping())

# 1. SET - Menyimpan data
r.set("user:1", "John Doe")
print("SET user:1 =", r.get("user:1"))

# 2. GET - Mengambil data
nama = r.get("user:1")
print("GET user:1 =", nama)

# 3. DEL - Menghapus data
r.delete("user:1")
print("DEL user:1 -> GET user:1 =", r.get("user:1"))

# 4. EXPIRE - Set waktu kadaluarsa
r.set("session:1", "active")
r.expire("session:1", 5)  # kadaluarsa dalam 5 detik
print("SET session:1 = active (expire 5 detik)")
print("TTL session:1 =", r.ttl("session:1"), "detik")

time.sleep(3)
print("Setelah 3 detik -> TTL =", r.ttl("session:1"), "detik")
