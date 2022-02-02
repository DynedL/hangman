import random #importing something python doesn't have

wordbank = [
  "videogame","game","pineapple","tomato","cucumber" "banana","snake","cigarette","methamphetamine","word","turnip","potato" "strawberry","cherry","trophy","hello","sparkling water","broccoli","watermelon","minecraft","fortnite","peanut","valorant","pokemon","magic the gathering","smoke and mirrors","coding, am i right?",
	] #container


randomIndex = random.randint(0,len(wordbank)-1) #finding a random number in the container
wordFromBank = wordbank[randomIndex] #takes the random number, and attaches it to a word

gameWord = [] 
hiddenWord = [] #variable and value

for letter in wordFromBank:
  gameWord.append(letter)
  hiddenWord.append(letter)
	
for i in range(len(hiddenWord)):
  if hiddenWord[i] not in [' ', '.', ',', '-']: 
    hiddenWord[i] = '_'

lives = 3
print("// --- WELCOME TO HANGMAN --- //")
print("YOU HAVE THREE LIVES")
print("HIDDEN WORD: ")
for char in hiddenWord: 
  print(char + " ", end="")
print 

while ('_' in hiddenWord and lives > 0):
  print()
  print("Enter a guess:")
  guess = input() 

  if guess in gameWord:
    print("CORRECT GUESS")
    for i in range(len(gameWord)):
      if gameWord[i] == guess:
       hiddenWord[i] = gameWord[i]
    for char in hiddenWord:
     print(char + " ", end="")
    print()
  else:
    print("INCORRECT GUESS")
    lives -= 1 
    print("Lives: "+str(lives))
    for char in hiddenWord:
      print(char + " ", end="")
    print()
if lives == 0:
  print("GAME OVER")
  print("YOU LOST")
  print("THE CORRECT WORD WAS: "+str(wordFromBank))
else:
  print("CONGRATS! YOU WON")
