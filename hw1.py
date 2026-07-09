# 1.Write a for loop that prints all multiples of 3 between 1 and 30.
'''for i in range(1,31):
    print(f"3X{i}={3*i}")'''
# 2.Write a program using a for loop that calculates the sum of numbers from 1 to 10.
'''total_sum = 0

for i in range(1, 11):
    total_sum += i
print(f"sum of numbers from 1 to 10 is:{total_sum}")'''
# 3.Write a program that takes your name as input and prints each letter of your name using a for loop.
'''name=input("enter you name: ")
for letter in name:
    print(letter)'''
# 4.Write a program that counts how many vowels are in a given string using a for loop.
'''text = input("enter the text: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"The number of vowels in '{text}' is: {vowel_count}")'''
