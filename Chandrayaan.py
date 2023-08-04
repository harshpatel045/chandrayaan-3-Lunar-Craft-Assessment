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

         