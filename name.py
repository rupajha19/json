import json
from textwrap import indent
dict=[{"name":"kirtee patil","age":18,"college":"lalonde","clour":"pink"},
{"name":"Rupa jha","age":16,"college":"delhi uni","clour":"Black"},
{"name":"Sagarika shendge","age":20,"college":"Pune","clour":"Blue"},
{"name":"Ankita patil","age":21,"college":"delhi","clour":"purpal"},
{"name":"Anjali singh","age":56,"college":"delhi","clour":"yellow"},
{"name":"karishma bano","age":23,"college":"delhi","clour":"black"}],


a= json.dumps(dict, indent = 4)
with open("sample.json", "w") as outfile:
    outfile.write(a)
b=open("sample.json","r")
c=b.read()
print(c)
# b.close()
n=input("enter input::")
if (c("name")) in n:
    print(c("name"))


