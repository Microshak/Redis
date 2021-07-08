import redis
import json

redis_host = "localhost"
redis_port = 6379
redis_password = ""
data = {'foo': 'bar'}

r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)
r.execute_command('JSON.SET', 'doc', '.', json.dumps(data))
reply = json.loads(r.execute_command('JSON.GET', 'doc'))
print(reply)