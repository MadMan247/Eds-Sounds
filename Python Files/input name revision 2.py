#"enter your name here" program

goodname = 0
dic = {}

ding = 1
def badname():
    name = input()
    
    if name == "penis" or name == "Penis" or name == "no" or name == "No" or name == "fuck" or name == "Fuck" or \
     name == "frick" or name == "Frick" or name == "poop" or  name == "Poop" or name == "Sam" or name == "Shit" or name == "" or \
      name == "silly" or name == "goose" or name == "silly goose" or name == "foreskin" or name == "parenthesis" or name == "colt" or name == "Colt" or name == "shoe":
        print ("your name's offensive to someone.")
        print("It was put on the bad-boy list. try a different name")
        
        goodname = 0
        
    else:
        print("Seems ok to me.")
        goodname = 1
        del dic['true']
        
def main():
    name_attempt = 0
    dic['true'] = 19
    print("enter your name here, and I'll tell you if it's ok or not.")
    print("don't take too long though. I'll kick you out after 5 attempts")
    while goodname == 0:
        if name_attempt == 5:
            print("you're done here. the damage has been done.")
            import time
            time.sleep(2)
            exit()
        
        print("name attempt:", name_attempt)
        name_attempt = name_attempt + 1
        badname()
        if goodname == 1:
            break;
        else:
            continue;
        
    
    print("you're out of the loop. yay.")

main()
