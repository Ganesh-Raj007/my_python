'''i=1
while i<=5:
    print(i)
    i+=1'''

'''is_faild=True
i=1
while is_faild:
    print(f"try{i}")
    i=i+1
    if i>100:
        break
print("i gave up")'''

'''is_faild=True
i=1
while is_faild:
    if i%2==0:
        i+=1
        continue
    print(f"Attempt{i}")
    i=i+1
    if i>100:
        break
print("i gave up")'''

'''i=0
while i<=10:
    x=0
    while x<i:
        print("ganesh")
        x+=1
    i+=1'''

available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ")
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")