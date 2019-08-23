#"enter your name here" program
goodname = 0
name_entered = 0
name = input()
print(name)
def badname():
    if name == "penis" or name == "Penis" or name == "no" or name == "No" or name == "fuck" or name == "Fuck" or \
     name == "frick" or name == "Frick" or name == "poop" or  name == "Poop" or name == "Sam" or name == "Shit" or name == "" or \
      name == "silly" or name == "goose" or name == "silly goose" or name == "foreskin" or name == "parenthesis" or name == "colt" or name == "Colt" or name == "shoe":
        print ("your name's offensive to someone. \
    It was put on the bad-boy list. try a different name")
        goodname = 0
        name = input()
    else:
        goodname = 1
        
while goodname == 0:
    badname()
