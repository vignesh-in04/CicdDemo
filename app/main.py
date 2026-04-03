from fastapi import FastAPI
import redis
import os

app = FastAPI()

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.get("/")
def read_root():
    r.incr("counter")
    count = r.get("counter")
    return {"message": "Hello from CI/CD 🚀", "visits": count}