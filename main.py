print("Welcome to the Decision Game!")
name = input("What is your name? ")
age = input("What is your age? ")

health = 10

if int(age) < 18:
  print("You are not old enough to play....")
else:
  print("You are old enough to play!")
  play = input("Do you want to play? ").lower()
  if play == "yes":
    print("Let's play. You start with 10 health.")

    ans = input("First choice.... Left or right (left/right) : ").lower()
    if ans == "left":
      ans = input("Nice, you follow the path and reach a lake..Do you swim or go around (across/around)? ").lower()

      if ans == "around":
        print("You went around and reached the other side of the lake.")
      elif ans == "across":
        print("You managed to get across, but were bit by something and lost 5 health.")
        health -= 5


      ans = input("You notice a house and a river. Where do you go? (river/house)? ")
      if ans == "house":
        print("You go to the house and are greeted by the owner. He hits you and lose 5 health.")
        health -= 5

        if health <= 0:
          print("You now have 0 health and lost the game")
        else:
          print("You survived. You win!")
      else:
        print("You fell and lost!")
    else:
      print("You fell and lost!")
    
  else:
    print("Bye!")