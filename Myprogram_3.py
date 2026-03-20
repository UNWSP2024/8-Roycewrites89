#Royce Daniel 3/20/2026 "Great Test"
import random

print("Lock in, young student. It's time for a test. Answer the following eight questions as best you can")
test = {"Russia":"Moscow", "UK": "London", "France": "Paris", "China": "Beijing", "Japan":"Tokyo", "USA": "Washington D.C", "Germany": "Berlin" ,"Mexico":"Mexico City" }
nations=list(test.keys())
random.shuffle(nations)
score = 0
for nation in nations:
    answer = (input(f"What is the capital of {nation}?"))

    if answer.strip().lower() ==test[nation].lower():
                print ("That is correct!")
                score += 1

print("\n Test complete, Your Score is: ", score)
if score >= 5: print("Well done! You have passed!")
if score <=4: print("You failed the test. You'll have to try again later.")
