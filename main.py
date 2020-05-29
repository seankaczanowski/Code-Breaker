'''
Code Breaker 1.0

Developed by Sean Kaczanowski
May 2020
No copyright

Simple Code Guessing Game
- 5 Colour Code
- 8 Colours to Choose From
- Gameboard showing current turn and past turns
- Indicator for how many colours guessed are in the code but not necessarily in the correct order
'''

import random # For word selection

i = 0
while i == 0: # Main Game Loop

# Title Screen / Menu Screen
  print('')
  print('+-----------------+')
  print('| C - - -         |')
  print('| C - D -         |')
  print('| C O D -         |')
  print('| C O D E BREAKER |')
  print('+-----------------+')
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
  
  turns = 0 # Number of turns
  gameboard = [['CODEBOARD'],['=========']] # List of results to append to show game progress

  guess = [] # Empty list for guess
  
  win = 0
  while win == 0: # Game loop until guess = code
  
    turns += 1 # Turns counter
    
    k = 1
    while k == 1: # Loop to control incorrect input for guess

      guess = (input('Code Guess: ')) # Guess
      guess = guess.upper() # Convert to uppercase
      guess = list(guess) # Convert to list
      
      if len(guess) != 5: # Check for correct length - 5
        print(' ')
        print('Error: Type in 5 Colours')
        print('Try Again.')
        print(' ')
      elif len(guess) > len(set(guess)): # Check for duplicates
        print(' ')
        print('Error: Same Colour Used More Than Once.')
        print('Try Again.')
        print(' ')
      elif len(set(guess) & set(colours)) < 5: # Check if the correct colours are used
        print(' ')
        print('Error: Incorrect Colour Used.')
        print('Try Again')
        print(' ')
      else:
        k = 0
         
    result = [] # Result of turn to be added to gameboard
    for x, y in zip(code, guess): # Determine whether the guess is correct at each place in the code
      if x == y:
        result.append(x)
      else:
        result.append('-')

    common_colours = set(guess) & set(code) # Determines how many of the colours in the guess are in the code but not necessarily in the correct place

    guess.append(str(len(common_colours))) # Add how many correct colours guessed but not necessarily in code
    gameboard.append(guess) # Add guess turn plus common colours to gameboard
  
    print(' ')
    for i in range(len(gameboard)): # Gameboard printing of previous turns plus current turn
      print(' '.join(gameboard[i]))
    print(' '.join(result)) # Gameboard result showing the correct/incorrect colour guesses and the number of colours that were guessed that are in the code
    
    if guess == code: # Win scenario
      win = 1
      print(' ')
      print('Correct! You Win!')
      print('Turns: ' + str(turns))
      print(' ')
    else:
      print(' ')