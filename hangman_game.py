# CodeAlpha_Hangman_game
#importing the words from the module hangman_word

#importing the random module
import random

from hangman_word import words

word=random.choice(words)
#how many lives will the user have
total_lives=6 
#printing the blank spaces
guessed_word="_"*len(word)
while total_lives!=0:
  print(guessed_word)
  #asking the user to guess a letter
  letter = input("guess a letter:").lower()
  if letter in word:
    #checking if the letter is in the word or it has been guessed before
    for i in range(len(word)):
      if letter== guessed_word[i]:
        print("you have already guessed this letter")
      #taking the help of string to check each character
      if letter==word[i]:
#if the letter is in the word, it will be replacing the blanks with the letter
        guessed_word=guessed_word[:i]+letter+guessed_word[i+1:]
      
#if the user guesses the word, the game will end and the user will win
    if guessed_word==word:
      print(guessed_word)
      print("you win")
      break
# If the letter is not in the word
  else:
    total_lives-=1
    print("incorrect guess you loss a live")
    print("the remaining chances are",total_lives)
  #if the user total lives gets to 0, the game will end and the user will lose
else:
  print("game over")
  print("you lose")
  print("all the chances are exhausted")
  print("the correct word is:",word)
        
  