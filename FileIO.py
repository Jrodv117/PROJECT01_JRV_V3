import csv

FILE_NAME = "BaseballPlayers.csv"

        
def open_read_csv():
    try:
        with open(FILE_NAME, mode='r', newline="", encoding='utf-8-sig') as data_file:
            DATA = csv.reader(data_file)
            player_stats = []
            for row in DATA:
                dictionary = {"name": row[0],
                "position": row[1],
                "at_bats": row[2],
                "hits": row[3]}
                player_stats.append(dictionary)
            return player_stats
    except:
        print("CSV FILE NOT FOUND OR COULDN'T BE READ PLAYER DATA MUST BE ENTERED MANUALLY")



def save_to_csv(player_information):
    with open(FILE_NAME, 'w', newline="", encoding='utf-8-sig') as data_file:
        writer = csv.writer(data_file)
        for row in player_information:
            writer.writerow(row.values())
