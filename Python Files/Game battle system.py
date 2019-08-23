#import random
#print (random.randint(-15,25))
#Game battle system test
print("welcome...")
def tt():
    import time
    time.sleep(2)
def to():
    import time
    time.sleep(1)
def fadescreen():
    fade=0
    while fade < 8:
        print(".   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .")
        import time
        time.sleep(0.005)
        fade = fade + 1
    fade = 0
    while fade < 8:
        print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        import time
        time.sleep(0.005)
        fade = fade + 1
    fade = 0
    while fade < 8:

        print("/ . / . / . / . / . / . / . / . / . / . / . / . / . / . / . / . / . / . / . /")
        import time
        time.sleep(0.005)
        fade = fade + 1
    fade = 0
    while fade < 8:

        print("/ | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | /")

        import time
        time.sleep(0.005)
        fade = fade + 1
    fade = 0
    while fade < 6:
        print("//|///|///|///|///|///|///|///|///|///|///|///|///|///|///|///|///|///|///|//")
        import time
        time.sleep(0.005)
        fade = fade + 1
    fade = 0
    while fade < 5:
        print("/////////////////////////////////////////////////////////////////////////////")
        import time
        time.sleep(0.0075)
        fade = fade + 1
    fade = 0
    while fade < 4:

        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        import time
        time.sleep(0.01)
        fade = fade + 1
    fade = 0
    while fade < 3:

        print("/////////////////////////////////////////////////////////////////////////////")
        import time
        time.sleep(0.15)
        fade = fade + 1
    fade = 0
    while fade < 2:

        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        import time
        time.sleep(0.2)
        fade = fade + 1
    fade = 0
    while fade < 1:

        print("IIII.IIII.IIII.IIII.IIII.IIII.IIII.IIII.IIII.IIII.IIII.IIII.IIII.IIII.IIII.II")
        import time
        time.sleep(0.25)
        fade = fade + 1
    fade = 0
    

tt()
print("I know that you're new, but you must fight.")
tt()
print("we haven't a choice either.")
to()
print("--But worry not, as I shall help you throughout your first round,")
print("and learn you the mechanics of this world.")
tt()
print('Enemy One: "we live in a society"')
to()
print("here they come!")

fadescreen()

#this marks the beginning of the newly imported pokemon program
def lmd():  #dosen't work as a definition
  if amhp > 0:
    namehp = 25.0
    for samuel in range(1):
    
      
      import random
      oof = random.randint(1.0,5.0)
      namehp = namehp - oof
      print("the monster dealt", oof, "damage")
      print ("you have", namehp, "hp left") 

def randmon():
    import random
    amhp = random.randint(54.0,55.0)
    water = 15.0
    sand = 10.0
    enemy = "placeholder text"
    import random
    monster = random.randint(1,7)
    if monster == 1:
        enemy = "Big Chungus"
        oofmult = 1
        import random
        amhp = random.randint(20,35)
        water = 15.0
        sand = 10.0
    elif monster == 2:
        enemy = "Daddy ;)"
        oofmult = 1.5
        import random
        amhp = random.randint(30,40)
        water = 25.0
        sand = 5.0
    elif monster == 3:
        enemy = "Blues clues"
        oofmult = 1
        import random
        amhp = random.randint(50,70)
        water = 15.0
        sand = 20.0
    elif monster == 4:
        enemy = "little chungus"
        oofmult = 0.5
        import random
        amhp = random.randint(15,30)
        water = 15.0
        sand = 10.0
    elif monster == 5:
        enemy = "Air pods"
        oofmult = 2
        import random
        amhp = random.randint(30,35)
        water = 20.0
        sand = 12.0
    elif monster == 6:
        enemy = "Janis Rose"
        print("prepare for the jan slam")
        oofmult = 2.5
        import random
        amhp = random.randint(15,25)
        water = 5.0
        sand = 20.0
    elif monster == 7:
        enemy = "cabbage"
        oofmult = 0
        import random
        amhp = random.randint(200,250)
        water = 15.0
        sand = 45.0
    else:
        enemy = "this is bad"
        oofmult = 0
        import random
        amhp = random.randint(1,2)
        water = 1.0
        sand = 1.0
        
import random
amhp = random.randint(54.0,55.0)
water = 15.0
sand = 10.0
enemy = "placeholder text"

#begin
import random
monsterclass = random.randint(1,7)
if monsterclass == 1:
    enemy = "Big Chungus"
    oofmult = 1
    import random
    amhp = random.randint(20,35)
    water = 15.0
    sand = 10.0
elif monsterclass == 2:
    enemy = "Daddy ;)"
    oofmult = 1.5
    import random
    amhp = random.randint(30,40)
    water = 25.0
    sand = 5.0
elif monsterclass == 3: #no
    enemy = "Blues clues"
    oofmult = 1
    import random
    amhp = random.randint(50,70)
    water = 15.0
    sand = 20.0
elif monsterclass == 4:
    enemy = "little chungus"
    oofmult = 0.5
    import random
    amhp = random.randint(15,30)
    water = 15.0
    sand = 10.0
elif monsterclass == 5: #no
    enemy = "Air pods"
    oofmult = 2
    import random
    amhp = random.randint(30,35)
    water = 20.0
    sand = 12.0
elif monsterclass == 6: #no, but the output is: prepare for the jan slam 6 this is bad
    enemy = "Janis Rose"
    print("prepare for the jan slam")
    oofmult = 2.5
    import random
    amhp = random.randint(15,25)
    water = 5.0
    sand = 20.0
elif monsterclass == 7: #yo what this one worked?
    enemy = "cabbage"
    oofmult = 0
    import random
    amhp = random.randint(200,250)
    water = 15.0
    sand = 45.0
else:
    enemy = "this is bad"
    oofmult = 0
    import random
    amhp = random.randint(1000,20000)
    water = 1.0
    sand = 1.0

#end
randmon()
name = "defaultname"
namehp = 25
#end of the setup
print("a wild", enemy, "has appeared. It has", amhp, "health!")
print (amhp)
while amhp > 0:
  print("choose your attack 1 water 2 sand")
  choice = input()
  crit = 0

  import random
  crit = random.randint(1,4)
  if crit == 4:
    water = water*1.5
    sand = sand*1.5
  if choice == "1":
    print("water, I see.")
    import random
    amhp = amhp - water - random.randint(1.0,5.0)
    if amhp <= 0:
      amhp = 0
    print(amhp, "enemy hp remaining")
  else:
    print("sand, I see.")
    amhp = amhp - sand
    if amhp <= 0:
      amhp = 0
    print(amhp, "enemy hp remaining")
  if crit == 4:
    print("Critical Hit")
    water = water/1.5
    sand = sand/1.5
  if amhp > 0:
    import random
    oof = random.randint(1.0,5.0) * oofmult
    namehp = namehp - oof
    print("the monster dealt", oof, "damage")
    print ("you have", namehp, "hp left")
  if namehp <= 0:
      print("you have lost")
      exit()
print("you defeated the monster")
print("Continue? 1 - Yes, anything else - no")
contin = input()
if contin == "1":
    while contin == "1":
        import random
        monsterclass = random.randint(1,7)
        if monsterclass == 1:
            enemy = "Big Chungus"
            oofmult = 1
            import random
            amhp = random.randint(20,35)
            water = 15.0
            sand = 10.0
        elif monsterclass == 2:
            enemy = "Daddy ;)"
            oofmult = 1.5
            import random
            amhp = random.randint(30,40)
            water = 25.0
            sand = 5.0
        elif monsterclass == 3: #no
            enemy = "Blues clues"
            oofmult = 1
            import random
            amhp = random.randint(50,70)
            water = 15.0
            sand = 20.0
        elif monsterclass == 4:
            enemy = "little chungus"
            oofmult = 0.5
            import random
            amhp = random.randint(15,30)
            water = 15.0
            sand = 10.0
        elif monsterclass == 5: #no
            enemy = "Air pods"
            oofmult = 2
            import random
            amhp = random.randint(30,35)
            water = 20.0
            sand = 12.0
        elif monsterclass == 6: #no, but the output is: prepare for the jan slam 6 this is bad
            enemy = "Janis Rose"
            print("prepare for the jan slam")
            oofmult = 2.5
            import random
            amhp = random.randint(15,25)
            water = 5.0
            sand = 20.0
        elif monsterclass == 7: #yo what this one worked?
            enemy = "cabbage"
            oofmult = 0
            import random
            amhp = random.randint(200,250)
            water = 15.0
            sand = 45.0
        else:
            enemy = "this is bad"
            oofmult = 0
            import random
            amhp = random.randint(1000,20000)
            water = 1.0
            sand = 1.0
        
        
        #end of the setup
        print("a wild", enemy, "has appeared. It has", amhp, "health!")
        print (amhp)
        while amhp > 0:
          print("choose your attack 1 water 2 sand")
          choice = input()
          crit = 0

          import random
          crit = random.randint(1,4)
          if crit == 4:
            water = water*1.5
            sand = sand*1.5
          if choice == "1":
            print("water, I see.")
            import random
            amhp = amhp - water - random.randint(1.0,5.0)
            if amhp <= 0:
              amhp = 0
            print(amhp, "enemy hp remaining")
          else:
            print("sand, I see.")
            amhp = amhp - sand
            if amhp <= 0:
              amhp = 0
            print(amhp, "enemy hp remaining")
          if crit == 4:
            print("Critical Hit")
            water = water/1.5
            sand = sand/1.5
          if amhp > 0:
            import random
            oof = random.randint(1.0,5.0) * oofmult
            namehp = namehp - oof
            print("the monster dealt", oof, "damage")
            print ("you have", namehp, "hp left")
          if namehp <= 0:
              print("you have lost")
              exit()
        print("you defeated the monster")
        print("Continue? 1 - Yes, anything else - no")
        contin = input()
else:
    print("good fight, valiant solider")

##static = 1
##while static == 1:
##    line = ''
##    HP = int(input())
##    hpupct = 0
##    while hpupct != HP:
##        line = line + "-"
##        hpupct = hpupct + 1
##    print(line)


