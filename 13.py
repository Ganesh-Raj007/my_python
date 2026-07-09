'''cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)'''
#/////////////////////////
'''for i in range(1,11):
   print(i,end=" ")'''
#////////////////////////////////
'''for i in range(1,11,3):
  print(i,end=" ")'''
#//////////////////////////////////
'''bag=["red","greeen","blue"]
for ball in bag:
    print(ball)'''
#/////////////////////////////////////
'''name = "Karnataka"
for letter in name:
    print(letter)'''
#/////////////////////////////////
'''name = "Karnataka"
for index, letter in enumerate (name):
    print(letter*(index+1))'''
#/////////////////////////////////////
'''l=[123,456,234,43]
for index,num in enumerate(l):
    print(f"{num} is in {index}th index")'''
#//////////////////////////////////////
'''cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        print(f"Found {city}!")
        break
    print(city)'''
#///////////////////////////////////////////
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
'''for city in cities:
    if city == "Mysuru":
        continue
    print(city)'''
#//////////////////////////////////////////////
'''for city in cities:
    print(city)
else:
    print("No more cities!")'''
#///////////////////////////////////////////////
'''d = {"name":"ganesh","age":19,"income":7000000}
for key,value in d.items():
    print(key,"--",value)'''
#//////////////////////////////
'''for i in range(1,11):
    print(f"2X{i}={2*i}")'''
#///////////////////////////////
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")
#//////////////////////////////////////////
'''for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()'''
