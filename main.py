import math

nothing = 0
room = "starting"

if room == "starting":
    print("You awake in a dark room, the walls are made of dark gray bricks, chains hang down from the walls, in front of you there is a doorway, and to the right there is a brick that looks out of place. (type 1 for the door and 2 for the brick)")
    choice1 = int(input("Enter either '1' or '2'. "))

if choice1 == 1:
    print("You slowly get up, your head is pounding, you walk slowly to the door and try to push it open, but it won't budge! (type 1 to investigate the brick")
    choicedoor = int(input("Enter '1'. "))
    if choicedoor == 1:
        choice1 = 2
if choice1 == 2:
    print("You pick at the brick and push on it and it makes a clicking noise, suddenly the door gets pushed open. (Type 1 to continue)")
    cont1 = int(input("Type '1' to continue. "))

if cont1 == 1:
     print("You push open the door and it goes into a lighted hallway, and the walls are made of gray bricks. As you look around the door you see a small goblin standing there with a dagger in his hand! (type 1 to look for ways to run or 2 to fight it head on)")
     fight_or_flight = int(input("Type '1' or '2'. "))

if fight_or_flight == 1:
    print("You look to your left and all you see is the end of the hallway, but there is a small barrel of water. (Type 1 to continue)")
    nothing = int(input("Type '1' to continue. "))
    if nothing == 1:
        fight_or_flight = 2

if fight_or_flight == 2:
    print("You run at the goblin, fists out and teeth gnashed. The goblin gets into a fighting stance and moves his hand to stab you with his dagger! (Type 1 to continue)")
    idk = int(input("Type '1' to continue. "))

if nothing == 1 and fight_or_flight == 2:
    print("As the goblin raises his dagger, you remember the barrel of water in the corner nearby you. You look again at the goblin and realize how light he must be, so, you pick up the goblin and as he his kicking his arms and flailing, you throw him right into the water bucket. He starts drowning because he is so small, and eventually he stops moving. (Type 1 to continue.)")
    yay = int(input("Type '1' to continue. "))
else:
    fight_or_flight += 1

if fight_or_flight == 3:
    print("The goblin stabs you in the gut with his dagger then again and again, you feel your blood spill out and you fall over, closing your eyes seeing the goblins ugly face for one last time. YOU DIED! (Maybe check your surroundings next time.)")

if yay == 1:
    print("You continue down the dungeon hall, and as you walk you see light ahead. You are free! You're out of the dungeon! But as you walk up to it the door slams shut! A loud, deep, booming voice speaks 'PASSCODE?' (Type 1 to give him the passcode, type 2 to look around.)") 
    choicepassword = int(input("Type '1' or '2'. "))


if choicepassword == 2:
    print("You continue down the hallway behind you, you come into a library. The shelves are empty. On the wall there is a poster that says RED PURPLE YELLOW GREEN. (Type 1 to continue in the library.)")
    library1 = int(input("Type '1' to continue. "))

if library1 == 1:
    print("You walk through the first aisle in it there is only 2 books. Both are red. (Type 1 to continue to the next aisle.)")
    library2 = int(input(print("Type '1' to go to the next aisle.")))

# 2 Red, 0 Purple, 0 Yellow, 0 Green

if library2 == 1:
    print("You go to the next aisle this time there are 7 books. 1 Red, 3 Purple, and 3 Yellow (Type 1 for the next aisle)")
    library3 = int(input("Type '1' to continue. "))

# 3 Red, 3 Purple, 3 Yellow 0 Green

if library3 == 1:
    print("You go to the next aisle and find 1 Purple book, 4 Yellow books, and 2 Green books. (That is all the aisles. Type 1 to return to the door")
    passgo = int(input("Type '1' to continue. "))

if passgo == 1:
    choicepassword = 1

if choicepassword == 1:
    print("The booming voice asks 'WHAT IS THE PASSCODE?' (Type the passcode.)")
    password = int(input("TYPE THE PASSWORD, DO NOT FAIL."))

if password == 3472:
    print("The door opens and the booming voice says 'GOOD JOB!' you walk out of the dungeon, free and ready to live the rest of your life.'")

if password != 3472:
    print("'WRONG! WRONG! WRONG! WRONG!' Suddenly, a large beam of fire envelops you and you die. THE END.")