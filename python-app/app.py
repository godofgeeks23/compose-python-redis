import redis
import os

# Get Redis connection details from environment variables
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port, charset="utf-8", decode_responses=True)

# Set a key-value pair
r.set('my_key', 'Hello, Redis!')

# Retrieve the value for the key
value = r.get('my_key')
print("Retrieved value from Redis:", value)
