#Write a program that counts from 1 to 10 using a while loop.
'''i=1
while i<=10:
    print(i)
    i+=1'''

#Create a program that prints all odd numbers between 1 and 20 using a while loop.
'''i=1
while i<=20:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1'''

#Write a program that simulates a bus ticket booking system. The bus has 8 seats.
#  Each time a seat is booked, the available seats decrease. When there are no seats left, 
# the loop stops and displays a message saying "All seats are booked."
available_seats=8

'''while available_seats>0:
    print(f"{available_seats}seats available")
    booking=input("do you want to book a seat?(yes/no): ")
    if booking=="yes":
        available_seats-=1
        print("seat booked!")
    else:
        print("no booking made")
print("All seats are booked.")'''

#Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.
i=10
while i>=1:
    print(i)
    i-=1
print("happy new year")