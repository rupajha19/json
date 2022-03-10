# Q6.Python object key unique key value ko access karne ka program likho?
import json
orizional_value='{"a": 1,"a": 2,"c": 3, "a": 4,"b": 1, "b": 2}'
unique_value=json.loads(orizional_value)
print(unique_value)
print(type(unique_value))
