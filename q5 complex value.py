# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?

import json
a='{"a":3+j,"b":4+j}'
b=json.loads(a)
print(b)
print(type(b))


    