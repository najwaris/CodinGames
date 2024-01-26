import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    first = ""
    second = ""
    final = ""
    
    EAST = (light_x - initial_tx)
    WEST = (initial_tx - light_x)
    NORTH = (initial_ty - light_y)
    SOUTH = (light_y - initial_ty)
    
    if NORTH > SOUTH:
        first = "N"
        initial_ty -=1
        if ( EAST > NORTH or WEST > NORTH ):
            first = ""
            initial_ty +=1
    elif NORTH < SOUTH:
        first = "S"
        initial_ty +=1
        if ( EAST > SOUTH or WEST > SOUTH ):
            first = ""
            initial_ty -=1

    if EAST > WEST:
        second = "E"
        initial_tx +=1
        if ( NORTH > EAST or SOUTH > EAST ):
            second = ""
            initial_tx -=1
    elif EAST < WEST:
        second = "W"
        initial_tx -=1
        if ( NORTH > WEST or SOUTH > WEST ):
            second = ""
            initial_tx +=1

    final = first + second    
    print(final)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # A single line providing the move to be made: N NE E SE S SW W or NW
