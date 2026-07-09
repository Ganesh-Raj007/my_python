'''cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)
#/////////////////////////
for i in range(1,11):
   print(i,end=" ")
#////////////////////////////////
for i in range(1,11,3):
  print(i,end=" ")
#//////////////////////////////////
bag=["red","greeen","blue"]
for ball in bag:
    print(ball)
#/////////////////////////////////////
name = "Karnataka"
for letter in name:
    print(letter)
#/////////////////////////////////
name = "Karnataka"
for index, letter in enumerate (name):
    print(letter*(index+1))
#/////////////////////////////////////
l=[123,456,234,43]
for index,num in enumerate(l):
    print(f"{num} is in {index}th index")
#//////////////////////////////////////
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        print(f"Found {city}!")
        break
    print(city)'''
#///////////////////////////////////////////
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Mysuru":
        continue
    print(city)