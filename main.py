import redis
import time
import sys
import io

# Fix encoding untuk Windows terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============================================================
# Tugas Topik Khusus - Operasi Dasar Redis dengan Python
# ============================================================
# Program ini mendemonstrasikan penggunaan Redis melalui
# library redis-py, mencakup tipe data:
#   1. String   (SET, GET, DEL)
#   2. Hash     (HSET, HGETALL)
#   3. List     (LPUSH, RPUSH, LRANGE)
#   4. Set      (SADD, SMEMBERS)
#   5. Sorted Set (ZADD, ZRANGE)
#   6. Expiry / TTL (SETEX, TTL)
# ============================================================


def header(title: str):
    """Cetak header section agar output rapi."""
    print("\n" + "=" * 55)
    print(f"  {title}")
    print("=" * 55)


def main():
    # --- Koneksi ke Redis ---
    r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

    try:
        pong = r.ping()
        print("[OK] Berhasil terhubung ke Redis!" if pong else "[GAGAL] Tidak dapat terhubung.")
    except redis.ConnectionError:
        print("[GAGAL] Tidak dapat terhubung ke Redis. Pastikan Redis sudah berjalan.")
        return

    # ----------------------------------------------------------
    # 1. STRING — SET, GET, DEL
    # ----------------------------------------------------------
    header("1. STRING — SET, GET, DEL")

    r.set("nama", "Abid Mustaghfirin")
    r.set("kelas", "Topik Khusus")
    r.set("semester", "6")

    print(f"SET nama   = {r.get('nama')}")
    print(f"SET kelas  = {r.get('kelas')}")
    print(f"SET semester = {r.get('semester')}")

    r.delete("semester")
    print(f"DEL semester -> GET semester = {r.get('semester')}")  # None

    # ----------------------------------------------------------
    # 2. HASH — HSET, HGETALL
    # ----------------------------------------------------------
    header("2. HASH — HSET, HGETALL")

    r.hset("mahasiswa:1", mapping={
        "nim": "123456",
        "nama": "Abid Mustaghfirin",
        "jurusan": "Teknik Informatika",
        "angkatan": "2023",
    })

    data_mahasiswa = r.hgetall("mahasiswa:1")
    print("Data mahasiswa:1 =>")
    for key, value in data_mahasiswa.items():
        print(f"  {key}: {value}")

    # ----------------------------------------------------------
    # 3. LIST — LPUSH, RPUSH, LRANGE
    # ----------------------------------------------------------
    header("3. LIST — LPUSH, RPUSH, LRANGE")

    r.delete("antrian")  # bersihkan dulu
    r.rpush("antrian", "Alice", "Bob", "Charlie")
    r.lpush("antrian", "Zara")  # masuk di depan

    antrian = r.lrange("antrian", 0, -1)
    print(f"Antrian (LPUSH Zara, RPUSH Alice/Bob/Charlie): {antrian}")

    # ----------------------------------------------------------
    # 4. SET — SADD, SMEMBERS
    # ----------------------------------------------------------
    header("4. SET — SADD, SMEMBERS")

    r.delete("hobi")
    r.sadd("hobi", "Coding", "Gaming", "Membaca", "Coding")  # duplikat diabaikan

    hobi = r.smembers("hobi")
    print(f"Hobi (duplikat 'Coding' otomatis dihapus): {hobi}")

    # ----------------------------------------------------------
    # 5. SORTED SET — ZADD, ZRANGE
    # ----------------------------------------------------------
    header("5. SORTED SET — ZADD, ZRANGE")

    r.delete("nilai_mahasiswa")
    r.zadd("nilai_mahasiswa", {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 95,
    })

    ranking = r.zrange("nilai_mahasiswa", 0, -1, withscores=True)
    print("Ranking mahasiswa (skor terendah → tertinggi):")
    for i, (nama, skor) in enumerate(ranking, start=1):
        print(f"  {i}. {nama} — Nilai: {int(skor)}")

    # ----------------------------------------------------------
    # 6. EXPIRY / TTL — SETEX, TTL
    # ----------------------------------------------------------
    header("6. EXPIRY / TTL — SETEX, TTL")

    r.setex("otp_code", 10, "482913")  # berlaku 10 detik
    print(f"OTP Code : {r.get('otp_code')}")
    print(f"TTL      : {r.ttl('otp_code')} detik tersisa")

    print("\nMenunggu 3 detik...")
    time.sleep(3)
    print(f"OTP Code : {r.get('otp_code')}")
    print(f"TTL      : {r.ttl('otp_code')} detik tersisa")

    # ----------------------------------------------------------
    # Selesai
    # ----------------------------------------------------------
    header("SELESAI")
    print("[OK] Semua operasi Redis berhasil dijalankan!")
    print("   Tipe data yang didemonstrasikan:")
    print("   - String, Hash, List, Set, Sorted Set, Expiry/TTL")


if __name__ == "__main__":
    main()
