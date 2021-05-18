import redis
r = redis.Redis(db = 0)

for key in r.scan_iter():
    r.delete(key)