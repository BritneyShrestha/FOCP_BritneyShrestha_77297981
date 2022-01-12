print("Stop! Who would cross the Bridge of Death,\nMust answer me these questions three, 'ere the other side he see.")
name=input("What is your name?") 
if  "arthur" not in name.lower(): #checks the name is not equal to arthur then go to next condition
    seek=input("What do you seek?")
    if "grail" in seek.lower(): #checks the grail is present in the quest or not
        colour=input("What is your favourite colour?")
        if name.lower()[0]==colour.lower()[0]: #checks the first character of the string
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
         print("Only those who seek the Grail may pass.")
else:
    print("My liege! You may pass!")
    