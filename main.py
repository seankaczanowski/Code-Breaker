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



  if play == '3': # Exit Option
    quit()
  else

  