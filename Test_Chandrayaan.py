import unittest
from Chandrayaan import SpaceCraft

class TestSpacecraft(unittest.TestCase):

    def test_starting_position(myPos):
        spacecraft=SpaceCraft(0,0,0,'N')
        myPos.assertEqual(spacecraft.x,0)
        myPos.assertEqual(spacecraft.y,0)
        myPos.assertEqual(spacecraft.z,0)
        myPos.assertEqual(spacecraft.direction,'N')

    def test_forward_move(myPos):
        spacecraft = SpaceCraft(0,0,0,'N')
        spacecraft.move_forward()
        myPos.assertEqual(spacecraft.y,1)

    def test_backward_move(myPos):
        spacecraft = SpaceCraft(0,0,0,'N')
        spacecraft.move_backward()
        myPos.assertEqual(spacecraft.y,-1)

    def test_left_turn(myPos):
        spacecraft = SpaceCraft(0,0,0,'N')
        spacecraft.turn_left()
        myPos.assertEqual(spacecraft.direction,'W')
        
