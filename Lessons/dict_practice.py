#practice with dictionaryies

student = {"name":"bob", 18:True, "music":['rock', 'classic'],
            "email":{"home":"bob@home", "work":"work@home"}
            } #key: value

#get the
print(student["name"])
print(student["music"])
print(student[18])

#Loop over dictionaries
for key, value in student.items():
    print(f"The key is {key} with value {value}")

#print work's email
print(student["email"]["work"])

if "address" in student: #asking if a key exists
    print(student["address"])
else:
    student["address"]="" #Crete the new key with on empty value