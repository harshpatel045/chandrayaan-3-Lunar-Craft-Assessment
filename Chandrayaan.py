class SpaceCraft:
    def __init__(myPos,x,y,z,direction):
        myPos.x=x
        myPos.y=y
        myPos.z=z
        myPos.direction=direction

    #forward move
    def move_forward(myPos):
        if myPos.direction=='N':
            myPos.y+=1
        elif myPos.direction=='S':
            myPos.y-=1
        elif myPos.direction=='E':
            myPos.x+=1
        elif myPos.direction=='W':
            myPos.x-=1
        elif myPos.direction=='Up':
            myPos.z+=1
        elif myPos.direction=='Down':
            myPos.z-=1

    def move_backward(myPos):
        if myPos.direction=='N':
            myPos.y-=1
        elif myPos.direction=='S':
            myPos.y+=1
        elif myPos.direction=='E':
            myPos.x-=1
        elif myPos.direction=='W':
            myPos.x+=1
        elif myPos.direction=='Up':
            myPos.z-=1
        elif myPos.direction=='Down':
            myPos.z+=1

    def turn_left(myPos):
        if myPos.direction=='N':
            myPos.direction='W'
        elif myPos.direction=='S':
            myPos.direction="E"
        elif myPos.direction=='E':
            myPos.direction='N'
        elif myPos.direction=='W':
            myPos.direction='S'

    def turn_right(myPos):
        if myPos.direction=='N':
            myPos.direction='E'
        elif myPos.direction=='S':
            myPos.direction="W"
        elif myPos.direction=='E':
            myPos.direction='S'
        elif myPos.direction=='W':
            myPos.direction='N'

    def turn_up(myPos):
        if myPos.direction in ['N','E','W','S']:
            myPos.direction='Up'

    def turn_down(myPos):
        if(myPos.direction in ['N','E','W','S']):
            myPos.direction='Down'

    def execute_commands(myPos,commands):
        for command in commands:
            if command=='f':
                myPos.move_forward()
            elif command=='b':
                myPos.move_backward()
            elif command=='l':
                myPos.turn_left()
            elif command=='r':
                myPos.turn_right()
            elif command=='u':
                myPos.turn_up()
            elif command=='d':
                myPos.turn_down()