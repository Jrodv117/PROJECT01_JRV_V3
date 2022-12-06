class Player:
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_AVG(self):
        if self.at_bats == 0:
            average = 0
        elif self.at_bats == 0 and self.hits == 0:
            average = 0
        else:
            average = self.hits / self.at_bats
        return round(average, 3)

    def __str__(self):
        return f"From str method of Test: a is {self.first_name}, b is {self.last_name},{self.position},{self.at_bats},{self.hits}"


class Lineup:
    def __init__(self):
        self.__starting_lineup = []

    def check_number(self, number):
        if 1 <= number <= len(self.__starting_lineup):
            return True
        return False

    def add(self, player):
        self.__starting_lineup.append(player)

    def remove(self, number):
        if self.check_number(number):
            print(self.__starting_lineup[number - 1].get_full_name(), "was deleted.")
            del self.__starting_lineup[number - 1]
            return True
        else:
            print("\nInvalid number")
            return False

    def move(self, number1, number2):
        if self.check_number(number1) and self.check_number(number2):
            player1 = self.__starting_lineup[number1 - 1]
            player2 = self.__starting_lineup[number2 - 1]
            print(player1.get_full_name(), "was selected")
            print(player1.get_full_name(), "was moved")
            self.__starting_lineup[number1 - 1], self.__starting_lineup[number2 - 1] = (
                self.__starting_lineup[number2 - 1],
                self.__starting_lineup[number1 - 1],
            )
            return True
        else:
            print("\nInvalid number")
            return False

    def edit_player_position(self, number, position):
        if self.check_number(number):
            player = self.__starting_lineup[number - 1]
            print(
                "You selected {0} POS = {1}".format(
                    player.get_full_name(), player.position
                )
            )
            player.position = position
            print(player.get_full_name(), "was updated.")

    def edit_player_stats(self, number, at_bats, hits):
        if self.check_number(number):
            player = self.__starting_lineup[number - 1]
            print(
                "You selected {0} At bats = {1}, Hits = {2}".format(
                    player.get_full_name(), player.at_bats, player.hits
                )
            )
            player.at_bats = at_bats
            player.hits = hits
            print("Edit stats")

    def display_lineup(self):
        print(
            " " * 3
            + f"{'Player'.ljust(31)}{'POS'.ljust(6)}{'AB'.ljust(6)}{'H'.ljust(6)}{'AVG'.ljust(6)}"
        )
        print("================================================================")
        for i, player in enumerate(self.__starting_lineup):
            print("{:<3d}".format(i + 1), end="")
            print("{:30s}".format(player.get_full_name()), end="")
            print("{:>3s}".format(player.position), end="")
            print("{:5d}".format(player.at_bats), end="")
            print("{:5d}".format(player.hits), end="")
            print("{:8.3f}".format(player.get_AVG()))

    def get_players_db(self):
        result = []
        for player in self.__starting_lineup:
            result.append(
                [
                    player.first_name,
                    player.last_name,
                    player.position,
                    player.at_bats,
                    player.hits,
                ]
            )
        return result
