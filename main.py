'''
Code Breaker 1.0

Developed by Sean Kaczanowski
May 2020
No copyright

Simple Code Guessing Game
- 5 Colour Code
- 8 Colours to Choose From
'''


import time # For small delays
import random # For word selection

i = 0
while i == 0: # Main Game Loop

# Title Screen / Menu Screen
  print('')
  print('+--------------+')
  print('| Code Breaker |')
  print('+--------------+')
  print('') # Simple graphic to show colour codes
  print('Colours')
  print('-------')
  print('(R)ed, (O)range, (Y)ellow, (G)reen,')
  print('(B)lue, Blac(K), (P)ink, (W)hite')
  print('')
  print('Main Menu')
  print('---------')
  print('1. Play')
  print('2. Quit')
  print('')

  j = 0 # Main Menu Selection Loop
  while j == 0:
    play = input('Press # and Enter: ') 
    if play == '2' or play == '1':
      j = 1
    else: # To deal with incorrect input
      print('')
      print('Error. Please Try Again') 
  print('')

  if play == '2': # Exit Option
    quit()
  
  colours = ['R', 'O', 'Y', 'G', 'B', 'K', 'P', 'W'] # Colour options for code

  code = random.sample(colours, 5) # Code list sampled from colour options without replacement
  
  gameboard = [] # List of results to show game progress
  guess = [] # Empty list for guess
  while code != guess: # Game loop until guess = code
    guess = (input('Code Guess: ')) # Guess string
    guess = guess.upper() # Convert to uppercase
    guess = list(guess) # Convert to list

    gameboard.append(guess)

    result = [] # Result of turn to be added to gameboard
    for x, y in zip(code, guess): # Determine whether the guess is correct at each place in the code
      if x == y:
        result.append(x)
      else:
        result.append('-')

    set_guess = set(guess)
    set_code = set(code)
    common_colours = set_guess & set_code # Determines how many of the colours in the guess are in the code but not necessarily in the correct place
  
    
    
    print(' ')
    for i in range(len(gameboard)): # Gameboard printing
      print(' '.join(gameboard[i]))
    print(' '.join(result) + ' ' + str(len(common_colours))) # Gameboard result showing the correct/incorrect colour guesses and the number of colours that were guessed that are in the code
    print('')