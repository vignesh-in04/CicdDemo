from fastapi import FastAPI
import redis
import os

app = FastAPI()
redis_host = os.getenv("REDIS_HOST", "localhost")

try:
    r = redis.Redis(host=redis_host, port=6379, decode_responses=True)
    r.ping()
except:
    r = None

@app.get("/")
def read_root():
    if r:
        r.incr("counter")
        count = r.get("counter")
    else:
        count = "no-redis"

    return {"message": "Vanakam 😆 Atheequr and Deephaa. from CI/CD 🚀", "visits": count}
