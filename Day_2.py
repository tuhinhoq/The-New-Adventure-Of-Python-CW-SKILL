
#Varible Declare & Type

first_name='Tuhin'
last_name='Hoque'
country='Bangladesh'
age=36
is_married=False
skills=['HTML', 'CSS', 'JS', 'REACT', 'PYTHON']
personal_info={
    'firstName': 'Tuhin Hoque',
    'lastName': 'Hoque',
    'maritalStatus':'Unmarried',
    'city': 'Dhaka',
    'Phone': '01711-223344'
}


print('Name:',first_name,' ',last_name)
print('Age:',age)
print('Married',is_married)
print('Skills:',skills)
print('First_Name',type(first_name))
print('Age:',type(age))
print('Skills',type(skills))
print('Personal_Info:',type(personal_info))




# Type Casting

gravity=9.81
num_int=10
num_str='10.10'

print('Float To Int:',int(gravity))
print('Int To Float:', float(num_int))
print('Float To String:', str(gravity))
print('String To Float:',float(num_str))


# Declaring Multiple Variable in a Line

name, age_now, married, skills_now='Tuhin Hoque', 36, False, ['HTML', 'CSS', 'JS', 'REACT', 'PYTHON']

print('Name:', name)
print('Age:', age_now)
print('Married:',married)
print('Skills:',skills_now )


print('----------------------Day 2 Done----------------------')