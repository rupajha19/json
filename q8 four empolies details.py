
import json
a={ 
     "emp1":{ "name":"Anjali",
       "Designation":"programmer",
       "Age":"34",
       "salary":"24000",
         },

    "emp2":
      { "name":"Ankita",
        "Designation":"Trainee",
        "Age":"24",
        "salary":"20000" ,
        },

 
    "emp3":
       { "name":"Rupa",
         "Designation":"HR",
         "Age":"25",
         "salary":"40000",
         },


    "emp4":
       { "name":"Divya",
         "Designation":"Manager",
         "Age":"29",
       }
 }
b=open("rupa.json","w")
json.dump(a,b,indent=2,sort_keys=False)
b.close()
