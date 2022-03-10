import  json
dict={
    "emp1":{
        'name':'elis',
        'age':'24',
        'designation':'programmmer',
        'salary':'54000'
    },
    "emp2":{
        'name':'lisa',
        'age':"22",
        'designation':'trainee',
        'salary':'60000'
    },
}
my_file=open("my_file.json","w")
json.dump(dict,my_file,indent=2)
my_file.close