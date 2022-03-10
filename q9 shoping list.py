# Apki dictionary ka use kar ke ek json file create karna hai.
# Aur apko kuch task perform karne hai jaise ki

# 1

# main dekhna chahta hu shopping list ko json file dekhna.

# 2

# phir main user se poochu ga ki kon sa item khareedna chahte ho.

# 3

# uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.

# 4

# phir aapka wo number of items json file se remove karna hai.

# 5

# Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.


import json
A = {"shopping_list":
        { 
            "choco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
 }
J = input("enter a item :")
S = int(input("enter the quantity :"))
for i in A :
    for j in A[i]:
        if J in A[i] and int(A[i][j])>=S:
            if j == J:
                b = int(A[i][j]) - S
                A[i][j] = str(b)
                break
        elif j != J:
          print("Not available")
          break
            
with open("shoping.json","w") as write_file:  
    json.dump( A, write_file , indent=4)  
with open("data1.json", "r") as read_file:  
    c =  read_file.read() 
print(c)
print(type(c))




