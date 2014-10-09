import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10

#### Put class definitions here ####
class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just aquired a gem! You have %d items!" %(len(player.inventory)))

class GreenGem(Gem):
    IMAGE = "GreenGem"
    SOLID = True



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

        if symbol in [key.UP, key.DOWN, key.LEFT, key.RIGHT]:
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
            if self.y - 1 < 0:
                self.board.draw_msg("You can't go any further in this direction!") 
                return (self.x, self.y)
            else:
                return (self.x, self.y - 1)
        elif direction == "down":
            if self.y + 1 > (GAME_HEIGHT - 1):
                self.board.draw_msg("You can't go any further in this direction!")
                return (self.x, self.y)
            else:
                return (self.x, self.y + 1)
        elif direction == "left":
            if self.x - 1 < 0:
                self.board.draw_msg("You can't go any further in this direction!") 
                return (self.x, self.y)
            else:
                return (self.x - 1, self.y)  
        elif direction == "right":
            if self.x + 1 > (GAME_WIDTH - 1):
                self.board.draw_msg("You can't go any further in this direction!")
                return (self.x, self.y)
            else:
                return (self.x + 1, self.y)
        return None

class Boy(Character):
    IMAGE = "Boy"

    def keyboard_handler(self, symbol, modifier):
        direction = None
        if symbol == key.W:
            direction = "up"
        elif symbol == key.S:
            direction = "down"
        elif symbol == key.A:
            direction = "left"
        elif symbol == key.D:
            direction = "right"

        if symbol in [key.W, key.S, key.A, key.D]:
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



    player2 = Boy()
    GAME_BOARD.register(player2)
    GAME_BOARD.set_el(5, 7, player2)
    print player2

    player1 = Character()
    GAME_BOARD.register(player1)
    GAME_BOARD.set_el(2, 2, player1)
    print player1

    GAME_BOARD.draw_msg("This game is wicked awesome.")
    #GAME_BOARD.erase_msg()

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(2, 1, gem)
    print gem

    greengem = GreenGem()
    GAME_BOARD.register(greengem)
    GAME_BOARD.set_el(4, 4, greengem)
    print greengem

