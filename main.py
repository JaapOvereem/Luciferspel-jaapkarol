import time
import random

name = input("Welke naam wil je gebruiken?")
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
   toonwoord = ''

   for char in woord:
      if char in guesses:
        toonwoord=toonwoord + (char)
      else:
        toonwoord=toonwoord + ('_') 
        letters_not_guesed +=1

   print ("Woord:" + toonwoord + ". Al gegokte letters:" + guesses)
   print ()
   

   if letters_not_guesed == 0:
        print ()
        print ('...')
           
        print ('Hoera,', naam, 'Je hebt gewonnen')
   
        break              

        print

        time.sleep(1)   
   guess = input ('Raad een letter: ') 

  guesses += guess  
  
  if guess not in woord:  
 
    turns -= 1        
        
    galgregel=turns
    nr_of_to_print_lines=(8-turns)
    while nr_of_to_print_lines>0:
      print (galg[galgregel])
      galgregel +=1 
      nr_of_to_print_lines -=1
    print ("")

    print ('Jammer, fout ...')