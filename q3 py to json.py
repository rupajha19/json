# Q.3 Python object ko json string mai convert karne ka program likho?
import json

a={"a":"rupa","b":"kavya","c":"dimple"}
b=json.dumps(a)
print(b)
print(type(b))


