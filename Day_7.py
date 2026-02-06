# Day_7

sets={"Karim", "Rahim", "Akkas", "Robin", "Sayed"}

print(type(sets))
print(len(sets))

sets.add("Tuhin") #add in first
sets.update(["Musfiq", "Ali"])
nList={"Monir", "Rafiq"}
sets.update(nList)
print(sets)

sets.pop()
sets.remove("Ali")
print(sets)


set_1={"A","B","C","D","E"}
set_2={"F","A","C","G","H"}
set_4={"A","B"}

print(set_1.difference(set_2))
print(set_2.difference(set_1))

set_3=set_1.union(set_2)
print(set_3)
set_3=set_1.intersection(set_2)
print(set_4.issubset(set_1))
print(set_1.issuperset(set_4))
print(set_3)

print("Is Karim is here?", "Karim" in sets)
whole_no={1,2,3,4,5,6,7,8,9}
some_no={1,3,5,7,9}
join_no={2,4,6,8}

odd_no=whole_no.difference(some_no)
print(odd_no)

print(join_no.isdisjoint(some_no))