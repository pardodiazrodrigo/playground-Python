# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Bro",21,"male")

print(student.count("Bro")) #cuenta las veces que aparece "Bro" en la tupla
print(student.index("male")) #index de male

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")