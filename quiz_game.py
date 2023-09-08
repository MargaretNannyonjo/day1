print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Okay Let's play :)")

score = 0

answer = input("1. What is 2x2 ? ")
if answer == "4":
  print("Correct")
  score += 1
else:
  print("Incorrect!")

answer = input("2. What is 2x3 ? ")
if answer == "6":
  print("Correct")
  score += 1
else:
  print("Incorrect!")

answer = input("3. What is 2x4 ? ")
if answer == "8":
  print("Correct")
  score += 1
else:
  print("Incorrect!")

answer = input("4. What is 2x5 ? ")
if answer == "10":
  print("Correct")
  score += 1
else:
  print("Incorrect!")

answer = input("5. What is 2x6 ? ")
if answer == "12":
  print("Correct")
  score += 1
else:
  print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")