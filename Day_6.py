# Tuples
listA=('Tuhin', 'Karim', 'Rahim', 10,20,30, {'Name':'Tuhin', 'Roll':'02'})

print(listA.index("Rahim"))

# newL=len(list)
newL='Tuhin' in listA
if newL==True:
    print("Get")
else:
    print("Oh! No.")

print(newL)

nList=list(listA)
print(nList)

listOne=('A','B','C','D','E')
listTwo=('F','G','H','I','J')

conCate=listOne+listTwo
conCate='A' in conCate
print(conCate)