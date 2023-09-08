name = input("What is your name? ")
print("Welcome", name, "to this adventure journey!")

answer = input("You are on a dirt road and it has come to an end, Which way do you like to go, left or right? ").lower()

if answer == "left":
  answer = input("You come to a river, Type walk to walk around it or swim to swim accross the river: ")

  if answer == "swim":
    print("You swam accross and were eaten by a crocodile.")

  elif answer == "walk":
    print("You walked for many miles, ran out of water and lost the game.")

  else:
    print("Not a valid option. You loose!")

elif answer == "right":
  answer = input("You come to a bridge, it looks woobly,Type cross to cross it or walk to walk back ")

  if answer == "back":
    print("You went back and loose!")

  elif answer == "cross":
    answer = input("You crossed the bridge and met a stranger! Type yes to talk or no to continue your journey ")
    if answer == "yes":
      print("You talked to the stranger and they gave you gold :) YOU WIN!")
    elif answer == "no":
      print("You ignored the stranger and they're offended and you loose :|")
    else:
      print("Not a valid option. You loose!")

  else:
    print("Not a valid option. You loose!")

else:
  print("Not a valid option. You loose!")
print("Thank you for playng", name)