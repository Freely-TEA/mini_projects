import random as rand
from time import sleep as s

from prettytable import PrettyTable

class main_game:
    def __init__(self, count = 16):    
        self.box = []
        self.winning_box = []
        for i in range(1, count):
            self.box.append(str(i))
            self.winning_box.append(str(i))

        rand.shuffle(self.box)

        # add cursor
        self.winning_box.append("█")
        self.box.append("█")

        # cursor position
        self.cursor = 15

        self.count = count
    
    def painting(self):
        line = []
        table = PrettyTable()
        for i in range(0, self.count):
            element = "|" + self.box[i] + "|"
            line.append(element)
            if i == 3 or i == 7 or i == 11 or i == 15:
                table.add_row(line)
                line = []
        print(table)   

    def displacement(self, move):
        move = move.lower()
        warning_line = [[0, 1, 2, 3], [12, 13, 14, 15], [3, 7, 11, 15], [0, 4, 8, 12]]
        try:
            if move == "u":
                if self.cursor in warning_line[0]:
                    raise IndexError
                self.box[self.cursor - 4], self.box[self.cursor] = self.box[self.cursor], self.box[self.cursor - 4]
                self.cursor -= 4
                return True
            elif move =="d":
                if self.cursor in warning_line[1]:
                    raise IndexError
                self.box[self.cursor + 4], self.box[self.cursor] = self.box[self.cursor], self.box[self.cursor + 4]
                self.cursor += 4
                return True
            elif move == "r":
                if self.cursor in warning_line[2]:
                    raise IndexError
                self.box[self.cursor + 1], self.box[self.cursor] = self.box[self.cursor], self.box[self.cursor + 1]
                self.cursor += 1
                return True
            elif move == "l":
                if self.cursor in warning_line[3]:
                    raise IndexError
                self.box[self.cursor - 1], self.box[self.cursor] = self.box[self.cursor], self.box[self.cursor - 1]
                self.cursor -= 1
                return True
            else:
                print("Wrong direction")
                return False
        except IndexError:
            print("You can't move to this direction")
            return False

    def game(self):
        print('Game "Slice tile"')
        s(0.5)
        print("Your goal is to collect a tile of numbers from 1 to 16")
        s(0.5)
        print('You can only change the neighboring tiles located as "+"')
        s(0.5)
        print("Use this command:")
        s(0.5)
        print("R - move to right\nL - move to left\nU - move to up\nD - move to down")
        print("Start")

        while True:
            self.painting()
            self.displacement(input("Move to "))
            if self.box == self.winning_box:
                self.painting()
                print("YOU WIN!!!")
                s(3)
                quit()

game = main_game()
game.game()