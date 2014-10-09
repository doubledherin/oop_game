import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just aquired a gem! You have %d items!" %(len(player.inventory)))



class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Horns"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def keyboard_handler(self, symbol, modifier):
        direction = None
        if symbol == key.UP:
            direction = "up"
        elif symbol == key.DOWN:
            direction = "down"
        elif symbol == key.LEFT:
            direction = "left"
        elif symbol == key.RIGHT:
            direction = "right"

        self.board.draw_msg("%s moves %s" % (self.IMAGE, direction))

        if direction:
            next_location = self.next_pos(direction)

            if next_location:
                next_x = next_location[0]
                next_y = next_location[1]

                existing_el = self.board.get_el(next_x, next_y)

                if existing_el:
                    existing_el.interact(self)

                if existing_el and existing_el.SOLID:
                    self.board.draw_msg("There's something in my way!")
                elif existing_el is None or not existing_el.SOLID:
                    self.board.del_el(self.x, self.y)
                    self.board.set_el(next_x, next_y, self)

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y - 1)
        elif direction == "down":
            return (self.x, self.y + 1)
        elif direction == "left":
            return (self.x - 1, self.y)
        elif direction == "right":
            return (self.x + 1, self.y)
        return None

####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    rock_positions = [
            (2,1),
            (1,2),
            (3,2),
            (2,3)
        ]
    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock

    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 2, player)
    print player

    GAME_BOARD.draw_msg("This game is wicked awesome.")
    #GAME_BOARD.erase_msg()

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(2, 1, gem)
    print gem





        #     self.board.draw_msg('%s says: "You pressed up!"' % self.IMAGE)
        #     next_y = self.y - 1
        #     self.board.del_el(self.x, self.y)
        #     self.board.set_el(self.x, next_y, self)
        # elif symbol == key.DOWN:
        #     self.board.draw_msg('%s says: "You pressed down!"' % self.IMAGE)
        #     next_y = self.y + 1
        #     self.board.del_el(self.x, self.y)
        #     self.board.set_el(self.x, next_y, self)
        # elif symbol == key.LEFT:
        #     self.board.draw_msg('%s says: "You pressed left!"' % self.IMAGE)
        #     next_x = self.x - 1
        #     self.board.del_el(self.x, self.y)
        #     self.board.set_el(next_x, self.y, self)
        # elif symbol == key.RIGHT:
        #     self.board.draw_msg('%s says: "You pressed right!"' % self.IMAGE)
        #     next_x = self.x + 1
        #     self.board.del_el(self.x, self.y)
        #     self.board.set_el(next_x, self.y, self)
        # elif symbol == key.SPACE:
        #     self.board.erase_msg()