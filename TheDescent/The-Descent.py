import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    mountain_i = 0  #for comparison between mountains
    mountain_j = 0  #to keep the index of highest mountains at the moment 
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_i <= mountain_h:
            mountain_i = mountain_h
            mountain_j = i
    print(mountain_j)    # The mountain to fire on.
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
