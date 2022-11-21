# Julian Rodriguez-Vera
# Team Manager v2
# 11/10/2022
# This programn creates a simple program that allows user to manage his/her baseball team.

import FileIO
from datetime import datetime, date


def title():
    print("========================================================")
    print("\t\tBaseball Team Manager\n")
    today_date = date.today()
    print("CURRENT DATE :\t", today_date)
    game_date_str = input("GAME DATE :\t")

    if game_date_str != "" or len(game_date_str) != 0:
        game_date = datetime.strptime(game_date_str, "%Y-%m-%d")
        until_game_date = game_date - datetime(
            today_date.year, today_date.month, today_date.day
        )
        print("DAYS UNTIL GAME : ", until_game_date.days)
    menu()
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("========================================================")


def menu():
    print("\nMENU OPTIONS")
    print(
        "1 - Display lineup\n"
        + "2 - Add player\n"
        + "3 - Remove player\n"
        + "4 - Move player\n"
        + "5 - Edit player position\n"
        + "6 - Edit player stats \n"
        + "7 - Exit program\n"
    )


print()


def display_lineup(player_information):
    print(
        " " * 3
        + f"{'Player'.ljust(31)}{'POS'.ljust(6)}{'AB'.ljust(6)}{'H'.ljust(6)}{'AVG'.ljust(6)}"
    )
    print("=" * 60)
    for idx, player_information in enumerate(player_information, 1):
        number = str(idx)
        name = player_information["name"]
        position = player_information["position"]
        at_bats = player_information["at_bats"]
        hits = player_information["hits"]
        avg = int(hits) / int(at_bats)
        number = number.ljust(3)
        name = name.ljust(31)
        position = position.ljust(6)
        at_bats = at_bats.ljust(6)
        hits = hits.ljust(6)
        avg = "{0:.3f}".format(avg).ljust(6)
        print(number + name + position + at_bats + hits + avg)


def add_player(player_information, valid_positions):
    name = input("\nEnter player name: ").capitalize()
    position = input("Enter Player Position: ").upper()
    while position not in valid_positions:
        position = input("Enter a valid position: ").upper()
    at_bats = int(input("Enter player at_bats: "))
    while at_bats <= -1:
        at_bats = int(input("At bats cant be less than 0. Enter At bats: "))
    hits = int(input("Enter player hits: "))
    while hits > at_bats:
        hits = int(input("Hits can't be greater than At bats. Enter Hits: "))
    player_information.append(
        {"name": name, "position": position, "at_bats": str(at_bats), "hits": str(hits)}
    )
    FileIO.save_to_csv(player_information)
    print(f"{name} was added")


def remove_player(player_information):
    name = input("\nEnter player name to delete: ").capitalize()
    while not any(d["name"] == name for d in player_information):
        name = input("Enter a valid player to be edited : ").capitalize()
    for i in range(0, len(player_information)):
        if player_information[i]["name"].strip() == name.strip():
            player_information.pop(i)
            break
    print(f"{name} was removed.")
    FileIO.save_to_csv(player_information)


def move_player(player_information):
    player = input("\nEnter the name of player to be moved: ").capitalize()
    while not any(d["name"] == player for d in player_information):
        player = input("Enter a valid player to be edited : ").capitalize()
    position_in_list = int(input("Enter new list order for the player: "))
    for i in range(0, len(player_information)):
        if player_information[i]["name"].strip() == player.strip():
            deleted = player_information.pop(i)
            player_information.insert(position_in_list - 1, deleted)
            break
    print(f"{player} was moved.")
    FileIO.save_to_csv(player_information)


def edit_player_position(player_information, valid_positions):
    player = input("\nEnter the name of player to be edited : ").capitalize()
    while not any(d["name"] == player for d in player_information):
        player = input("Enter a valid player to be edited : ").capitalize()
    position = input("Enter a new position: ").upper()
    while position not in valid_positions:
        position = input("Enter a valid position: ").upper()
    for i in range(0, len(player_information)):
        if player_information[i]["name"].strip() == player.strip():
            player_information[i]["position"] = position
            print(
                player
                + "'s position was changed to "
                + player_information[i]["position"]
            )
            break
    FileIO.save_to_csv(player_information)


def get_at_bats(player_information, player):
    for i in range(0, len(player_information)):
        if player_information[i]["name"].strip() == player.strip():
            player_at_bats = player_information[i]["at_bats"]
    return player_at_bats


def edit_player_stats(player_information):
    player = input("\nEnter the name of player: ").capitalize()
    while not any(d["name"] == player for d in player_information):
        player = input("Enter a valid player to be edited: ").capitalize()
    print("You selected ", player)
    edit = input(f"Edit AB for {player}?(y/n): ").lower()
    while not edit == "y" and not edit == "n":
        edit = input(f"Edit AB for {player}?(y/n): ").lower()
    if edit == "y":
        at_bats = int(input("Enter new AB: "))
        while at_bats <= -1:
            at_bats = int(input("At bats cant be less than 0. Enter new AB: "))
        for i in range(0, len(player_information)):
            if player_information[i]["name"].strip() == player.strip():
                player_information[i]["at_bats"] = str(at_bats)
                break
        print(f"{player}'s AB were changed")
    elif edit == "n":
        pass
    edit = input(f"Edit H for {player}?(y/n): ").lower()
    while not edit == "y" and not edit == "n":
        edit = input(f"Edit H for {player}?(y/n): ").lower()
    if edit == "y":
        hits = int(input("enter new H: "))
        at_bats = get_at_bats(player_information, player)
        while hits > int(at_bats):
            hits = int(input("Hits can't be greater than AB. Enter new H: "))
        for i in range(0, len(player_information)):
            if player_information[i]["name"].strip() == player.strip():
                player_information[i]["hits"] = str(hits)
                break
        print(f"{player}'s hits were changed")
    elif edit == "n":
        pass
    FileIO.save_to_csv(player_information)


def main():
    title()

    player_information = FileIO.open_read_csv()

    valid_positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    while True:
        try:
            user_selection = int(input("\nMenu option: "))
            if user_selection == 1:
                display_lineup(player_information)
            elif user_selection == 2:
                add_player(player_information, valid_positions)
            elif user_selection == 3:
                remove_player(player_information)
            elif user_selection == 4:
                move_player(player_information)
            elif user_selection == 5:
                edit_player_position(player_information, valid_positions)
            elif user_selection == 6:
                edit_player_stats(player_information)
            elif user_selection == 7:
                print("Bye!")
                exit()
            else:
                print("Please input a valid menu selection\n")
                menu()
        except (ValueError, TypeError):
            print("Please input a valid menu selection\n")
            menu()


if __name__ == "__main__":
    main()
