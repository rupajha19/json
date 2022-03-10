# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
b=json.dumps(a,indent=3,sort_keys=True)
print(b)
print(type(b))

