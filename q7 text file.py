# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json



a={
    "Name": "Abhishek",
    "Designation": "CEO of      navgurukul",
    "Gender":"male",
    "Age": "29"
    }
b=open("data.json","w")
json.dump(a,b,indent=2,sort_keys=False)
b.close()



