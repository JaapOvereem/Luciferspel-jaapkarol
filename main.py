import time
import random

name = input("Welke naam wil je gebruiken? ")
print ("Hallo, " + name, "welkom bij galgje!")

print("")

woorden = ["auto", "fiets", "vrachtwagen", "vliegtuig", "deurklink", "zandloper", "euro", "afrika", "europa", "amerika", "rusland", "china", "loopfiets"]

galg = [
  "---------",
  "|       |",
  "|       O",
  "|       |",
  "|      -+-",
  "|       |",
  "|      / \\",
  "|",
  "|",
  "------------"
]

time.sleep(0.5)
print ("We gaan beginnen...")

woordkeuze = random.choice(woorden)
woord = woordkeuze

guesses = ""
kanzen = 10

while kanzen > 0:
   letters_not_guesed = 0             
   toonwoord = ""

   for char in woord:
      if char in guesses:
        toonwoord=toonwoord + (char)
      else:
        toonwoord=toonwoord + ("_") 
        letters_not_guesed +=1

   print ("Woord:" + toonwoord + ". Al gegokte letters:" + guesses)
   print ()
   

   if letters_not_guesed == 0:
        print ()
        print ("...")
           
        print ("Hoera," + name + "Je hebt gewonnen")
   
        break              

        print

        time.sleep(1)   
   guess = input ("Raad een letter: ") 

   guesses += guess  
  
   if guess not in woord:  
 
    kanzen -= 1        
        
    galgregel=kanzen
    nr_of_to_print_lines=(8-kanzen)
    while nr_of_to_print_lines>0:
      print (galg[galgregel])
      galgregel +=1 
      nr_of_to_print_lines -=1
    print ("")

    print ("Jammer, fout ...")

    print (name + " je hebt nog " + str (kanzen), "levens")
  
   if kanzen == 0:           
    
    print ()
    print ("...")
    time.sleep(1)   
    print ("Jammer " + name + " je hebt verloren, het woord was: " + woord)

