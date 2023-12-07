print("Game creation for play Rock, Paper, and Scissor game")
print()
rock = "R"
paper = "P"
scissors = "S"
noOfWinsPlayer01 = 0
noOfWinsPlayer02 = 0

while True:

  player_01 = input("Player 01 first move :")
  player_02 = input("Player 02 first move :" )

  if (player_01 == "R" and player_02 == "R") or (player_01 == "P" and player_02 == "P") or (player_01 == "S" and player_02 == "S"):
    print("Try again")
    continue
  elif (player_01 == "R" and player_02 == "S") or (player_01 == "P" and player_02 == "R") or (player_01 == "S" and player_02 == "P") :
    noOfWinsPlayer01 += 1
    if noOfWinsPlayer01 == 3:
      print("Player 01 win all 3 levels")
      break
    else:
      print("Player 01 is the winner")
      continue
  elif (player_01 == "R" and player_02 == "P") or (player_01 == "P" and player_02 == "S") or (player_01 == "S" and player_02 == "R"):
    noOfWinsPlayer02 += 1
    if noOfWinsPlayer02 == 3:
      print("Player 02 win all 3 levels")
      break
    else:
      print("Player 02 is the winner")
      continue
  else :
    print("Invalid Data")
    exit()

print("Game over")