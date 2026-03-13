import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

print("Ping:", r.ping())

r.set("user:1", "Abid Mustaghfirin")
print("SET user:1 =", r.get("user:1"))

nama = r.get("user:1")
print("GET user:1 =", nama)

r.delete("user:1")
print("DEL user:1 -> GET user:1 =", r.get("user:1"))

r.set("session:1", "active")
r.expire("session:1", 5)  
print("SET session:1 = active (expire 5 detik)")
print("TTL session:1 =", r.ttl("session:1"), "detik")

time.sleep(3)
print("Setelah 3 detik -> TTL =", r.ttl("session:1"), "detik")
