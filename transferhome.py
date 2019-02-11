import random
random_number = random.randint (1,100)
print random_number
#This ^^^^^^^^^^^^^ Is only to show what the answer is for testing purposes only, upon real implement delete it.

print "Test your luck with low a low stakes gamble! \nEnter your guess of a number. (1-100)"
guess = int(raw_input())

while not guess == random_number:
    if guess > random_number:
        print "Too high friend, guess again."
        
    elif guess < random_number:
        print "Too low friend, guess again."
    guess = int(raw_input())
print "Correct, congrates you win $5!\nPlay again?\nType 'yes' or 'no'"

#This code was designed by Andrew for tutorial/visual apeal purposes, all uses approved! =] 

if raw_input() == "yes":
    print "If only I knew how to do that ='["
else:
    print "No one likes you either..."
    

















import time

grades = [94, 91, 85, 99, 74, 70, 58, 82, 43, 100, 61]

for i in grades:
    if i > 70:
        print i
    
    time.sleep(1)









total = 0

nums = []
for z in range(6):
  nums.append(int(raw_input()))
  
for i in nums:  
  total += i
  
print total / float(len(nums))