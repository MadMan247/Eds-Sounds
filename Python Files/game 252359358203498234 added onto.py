goodname = 0
ding = 1
name = "defaultname"
name_attempt = 0
namelength = len(name)
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
    name = input()
    namelength = len(name)
    if namelength >= 25:
        print("although I'm glad you'd write a paragraph, please don't.")
        continue;
    if name == "penis" or name == "Penis" or name == "no" or name == "No" or name == "fuck" or name == "Fuck" or \
     name == "frick" or name == "Frick" or name == "poop" or  name == "Poop" or name == "Sam" or name == "Shit" or name == "" or \
      name == "silly" or name == "goose" or name == "silly goose" or name == "foreskin" or name == "parenthesis" or name == "colt" or name == "Colt" or name == "shoe":
        print ("your name's offensive to someone.")
        print("It was put on the bad-boy list. try a different name")
        
        goodname = 0
        
    else:
        namelength = len(name)
        
        print("Seems ok to me.")
        
        print("name length:", namelength)
        goodname = 1
        
        if goodname == 1:
            break;
        else:
            continue;

def tenspace():
    loopten = 1
    while loopten <= 10:
        print(" ")
        loopten = loopten + 1
    loopten = 1
def thirtyspace():
    loopten = 1
    while loopten <= 30:
        print(" ")
        loopten = loopten + 1
    loopten = 1
def tridot():
    dotthree = 1
    import time
    time.sleep(2)
    while dotthree <= 3:
        print(".")
        dotthree = dotthree + 1
        import time
        time.sleep(1)
    dotthree = 1
        
    
thirtyspace() #this worked! Oppa! this marks the end of the
#beginning, and the beginning of the end!
import time
time.sleep(2)
print(".")
import time
time.sleep(1)
print(".")
import time
time.sleep(1)
print(".")
import time
time.sleep(1)
print("Ah, so you're... ''" + name + "'', huh...?")
import time
time.sleep(3)
print(".")
import time
time.sleep(1)
print(".")
import time
time.sleep(1)
print(".")
import time
time.sleep(1)
print("... that IS your name, right?")
print("Y/n")
correctn = input()
if correctn == "lol no u" or correctn == "lol no you":
    print("uhh huhh... you've just stuck yourself with")
    print("something worse, bucko.")
    name = "pile of bootyhole"
    print("goodluck living that off, sir '", name, "'")
elif correctn == "yes" or correctn == "Yes" or correctn == "no" or correctn == "No" or correctn == "NO" or correctn == "YES" or correctn == "y" or correctn == "Y" or correctn == "n" or correctn == "N" or correctn == "":
    print("haha, Don't care. you're stuck with it anyways :)")
else:
    print("Yeah, I don't quite know what you said, but let's go with it anyways.")
import time
time.sleep(1)
tridot()
print("anyways, let's introduce ourselves. I'm sam")
import time
time.sleep(1)
print("I'm oliver")
import time
time.sleep(0.5)
print("and I'm...")
import time
time.sleep(1.5)
print("wait, who am I?")
import time
time.sleep(0.5)
print("what do you mean, 'who am I?' are you special needs?!")
import time
time.sleep(1)
print("don't speak to your brother that way! Be nice for once.")
tridot()
print('"yEs moM"')
import time
time.sleep(0.5)
print("shut the fuck up bitch ass")
import time
time.sleep(0.75)
print(":(")
import time
time.sleep(2)
print("ah, hey,", name + "... you know their name, don't you?")
import time
time.sleep(2)
print("well... do you?")
print("Y/n")
knowname = input()
goodvoice = 0
voice_attempt = 0
voice = "defaultvoice"
if knowname == "yes" or knowname == "Yes" or knowname == "YES" or knowname == "y" or knowname == "Y" or knowname == "":
    tridot()
    print("then what're you holding out on? spit it out!")
    voice = "defaultvoice"
    
#imported within these bounds
    while goodvoice == 0:
        voice = input()
        if voice_attempt == 5:
            print("y'know what? I thonk'd real hard, and his name's tom.")
            voice = "tom"
            import time
            time.sleep(2)
            break;
    
        print("name attempt:", voice_attempt)
        voice_attempt = voice_attempt + 1
        voicelength = len(name)
        if voicelength >= 25:
            print("although I'm glad you'd write a paragraph, please don't.")
            continue;
        if voice == "penis" or voice == "Penis" or voice == "no" or voice == "No" or voice == "fuck" or voice == "Fuck" or \
         voice == "frick" or voice == "Frick" or voice == "poop" or  voice == "Poop" or voice == "Sam" or voice == "Shit" or voice == "" or \
          voice == "silly" or voice == "goose" or voice == "silly goose" or voice == "foreskin" or voice == "parenthesis" or voice == "colt" or voice == "Colt" or voice == "shoe":
            print ("that's... not a good name. try again.")
        
            goodvoice = 0
        
        else:
            voicelength = len(voice)
        
            print("yeah... '" + voice + "' sounds about right to me")
        
            print("name length:", voicelength)
            goodvoice = 1
        
            if goodvoice == 1:
                break;
        

#imported within these bounds
    
else:
    if knowname == "n" or knowname == "N" or knowname == "no" or knowname == "No" or knowname == "NO":
        print("ah, well... It was worth a try, I guess.")
    else: 
            print("I mean, I imagined that you'd be a bit roughed up from the fall")
            
            print("all the way down here, but I'd still expect you to be able to speak")
            
            tridot()
            print(". I'll take that as a 'no, I don't know.'")
            import time
if voice == "tom" or voice == "tommy" or voice == "Tom" or voice == "Tommy":
    c = voice
    import time
    time.sleep(3)
elif voice == "defaultvoice":
    c = "tom"
    tridot()
    print("ah, y'know what? I think I remember his name now.")
    import time
    time.sleep(1)
    print("ah, do ya?")
    import time
    time.sleep(1)
    print("sure do. It's tom.")
    
    import time
    time.sleep(1)
    print("ah yeah. suppose it is.")
    import time
    time.sleep(1)
    print("fancy that. didn't need your help anyways. good thing too.")
    print("you'd've messed it up somehow if you did anyways i'm sure.")
    import time
    time.sleep(4)
else:
    c = "tom"
    import time
    time.sleep(2)
    print("ah.")
    import time
    time.sleep(1.5)
    print("what?")
    import time
    time.sleep(0.5)
    print("tbh don't think you got the right name")
    tridot()
    print("don't you look at me like that. YOU'RE the one who gave us a faulty")
    print("name. WE asked for a correct name, not just some jibber jabber")
    print("that you thought up the second that we asked you for it.")
    import time
    time.sleep(6)
    
    
    
