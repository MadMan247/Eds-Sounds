import random
name = "defaultname"
namehp = 25
def lmd():
  if amhp > 0:
    namehp = 25
    for samuel in range(1):
    
      
      import random
      oof = random.randint(1,5)
      namehp = namehp - oof
      print("the monster dealt", oof, "damage")
      print ("you have", namehp, "hp left") 
amhp = random.randint(25,55)
print (amhp)
while amhp > 0:
  print("choose your attack 1 water 2 sand")
  choice = input()
  crit = 0
  water = 15
  sand = 10
  import random
  crit = random.randint(1,4)
  if crit == 4:
    water = water*1.5
    sand = sand*1.5
  if choice == "1":
    print("water, I see.")
    import random
    amhp = amhp - water - random.randint(1,5)
    if amhp <= 0:
      amhp = 0
    print(amhp, "enemy hp remaining")
  else:
    print("use water next time")
    amhp = amhp - sand
    if amhp <= 0:
      amhp = 0
    print(amhp, "enemy hp remaining")
  if crit == 4:
    print("Critical Hit")
  if amhp > 0:
    import random
    oof = random.randint(1,5)
    namehp = namehp - oof
    print("the monster dealt", oof, "damage")
    print ("you have", namehp, "hp left")
print("you defeated the monster")
