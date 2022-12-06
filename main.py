# Julian Rodriguez-Vera
# Team Manager v3
# 11/17/2022
# This programn creates an OPP approach to a baseball team manager using a Three-Tier-Architecture


import datetime
from db import *
from objects import *


class Baseball:
    def __init__(self):
        self.positions_list = ("C", "1B", "2B", "3B", "SS", "LF", "C", "RF", "P")

    def menu(self):
        print("\nMENU OPTIONS")
        print("1 - Display Lineup")
        print("2 - Add Player")
        print("3 - Remove Player")
        print("4 - Move Player")
        print("5 - Edit player position")
        print("6 - Edit Player stats")
        print("7 - Exit Program\n")
        print("POSITIONS")
        print(self.position_list())
        print("================================================================\n")

    def position_list(self):
        """
        Use tuple
        """
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(*self.positions_list)

    def get_name(self):
        first_name = str(input("Enter Name(First name): "))
        last_name = str(input("Enter Name(Last name): "))
        return first_name, last_name

    def get_position(self):
        while True:
            position = input("Position: ").strip().upper()
            if position not in self.positions_list:
                print("ERROR - Invalid position. Try again.")
                continue
            break
        return position

    def get_at_bats(self):
        at_bats = 0
        while True:
            try:
                at_bats = input("At bats: ")
                if at_bats == "zero":
                    at_bats = 0
                    print("Using At bats amount of 0")
                    break
                at_bats = int(at_bats)
                if at_bats < 0:
                    print("ERROR - Don't put negative number. Try Again")
                    continue
                break
            except ValueError:
                print("ERROR - Don't put string. Try again.")
        return at_bats

    def get_hits(self, at_bats):
        hits = 0
        while True:
            try:
                hits = int(input("Hits: "))
                if hits < 0:
                    print("ERROR - Don't put negative number. Try Again.")
                    continue
                if hits > at_bats:
                    print("ERROR - Player cannot have more hits than at bats.")
                    continue
                break
            except ValueError:
                print("ERROR - Don't put string. Try again.")
        return hits

    def add_player(self):
        first_name, last_name = self.get_name()
        position = self.get_position()
        at_bats = self.get_at_bats()
        hits = self.get_hits(at_bats)
        return Player(first_name, last_name, position, at_bats, hits)

    def get_number(self, prompt=""):
        number = 0
        while True:
            try:
                number = int(input(prompt))
                if number < 0:
                    print("ERROR - Don't put negative number. Try Again.")
                    continue
                break
            except ValueError:
                print("ERROR - Don't put string. Try again.")
        return number


def list_to_string(list):
    string = ""
    for element in list:
        string += element
    return string


def main():

    team = Baseball()
    data_driver = db()
    database = data_driver.load_from_file("players.txt")
    lineup = Lineup()
    for data in database:
        first_name = data[0].split()
        fname = list_to_string(first_name)
        last_name = data[1].split()
        lname = list_to_string(last_name)
        position = data[2]
        at_bats = int(data[3])
        hits = int(data[4])

        player = Player(fname, lname, position, at_bats, hits)
        lineup.add(player)
    print("================================================================")
    print("Baseball Team Manager\n")
    team.menu()
    while True:
        choice = 0
        try:
            choice = int(input("\nMenu option: "))
        except Exception:
            print("\nInvalid Choice")
            continue
        if choice == 1:
            lineup.display_lineup()
        elif choice == 2:
            lineup.add(team.add_player())
        elif choice == 3:
            lineup.remove(team.get_number("Number: "))
        elif choice == 4:
            number1 = team.get_number("Current lineup number: ")
            number2 = team.get_number("New lineup number: ")
            lineup.move(number1, number2)
        elif choice == 5:
            number = team.get_number("Lineup number: ")
            position = team.get_position()
            lineup.edit_player_position(number, position)
        elif choice == 6:
            number = team.get_number("Lineup number: ")
            at_bats = team.get_at_bats()
            hits = team.get_hits(at_bats)
            lineup.edit_player_stats(number, at_bats, hits)
        elif choice == 7:
            data_driver.save_to_file("players.txt", lineup.get_players_db())
            print("Bye!")
            break
        else:
            print()
            print("Invalid option. Try again!")


if __name__ == "__main__":
    main()
