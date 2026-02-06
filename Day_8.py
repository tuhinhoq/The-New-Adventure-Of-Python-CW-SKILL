#Dictionary

dic_1={
    "Name":"Tuhin",
    "Age": 34,
    "Phone No":"0123456789",
    "Skills":["Java","JS","Python"],
    "City":"Dhaka"
}

print(dic_1.keys())
print(dic_1.values())
dic_N=dic_1["Skills"].append('C#')
print("New Skills: ", dic_N)

dic_1["Blood Group"]="A+"
print(dic_1)
print(len(dic_1))
print("Name: ",dic_1["Name"])
print("Get Name: ",dic_1.get("Name"))
print("Skill: ",dic_1["Skills"][1])
print("Get Skill: ", dic_1.get("Skills"))


dic_1.update({"Name":"Jakiul"})
if "Name" in dic_1:
    print("Yes Get Name.")
    
print(dic_1.values())

for x in dic_1.values():
    print(x)
for x in dic_1.keys():
    print(x)
for x in dic_1.items():
    print(x)
    
    
    
    
    child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 
print(myfamily["child2"]["name"]) 
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])