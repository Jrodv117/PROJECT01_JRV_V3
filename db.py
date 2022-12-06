class db:
    def __init__(files):
        files.positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

    def valid_Names(files, names):
        if names in files.names:
            return True
        else:
            return False

    def valid_POS(files, pos):
        if pos in files.positions:
            return True
        else:
            return False

    def valid_at_bats(files, at_bats):
        try:
            at_bats = int(at_bats)
            return True
        except Exception:
            return False

    def valid_H(files, hits):
        try:
            hits = int(hits)
            return True
        except Exception:
            return False

    def valid_AVG(files, average):
        try:
            average = float(average)
            return True
        except Exception:
            return False

    def load_from_file(files, FILE_NAME):
        try:
            database = []
            inp = open(FILE_NAME, "r")
            line = inp.readline()
        except FileNotFoundError:
            print("ERROR - Unable to open {}".format(FILE_NAME))
            quit()
        while line:
            player = line.strip().split(",")
            if len(player) == 5:
                valid = files.valid_POS(player[2])
                allow = True
                if not valid:
                    if allow:
                        print("Error(s) Occured in Player with details:", line)
                    print("Position is Invalid")
                    allow = False
                valid = files.valid_at_bats(player[3])
                if not valid:
                    if allow:
                        print("Error(s) Occured in Player with details:", line)
                    print("At bat is Invalid")
                    allow = False
                valid = files.valid_H(player[4])
                if not valid:
                    if allow:
                        print("Error(s) Occured in Player with details:", line)
                    print("Invalid Hits")
                    allow = False
            database.append(player)
            line = inp.readline()
        inp.close()
        return database

    def save_to_file(files, FILE_NAME, database):
        try:
            output = open(FILE_NAME, "w", encoding="utf-8")
        except FileNotFoundError:
            print("ERROR - Unable to open {}".format(FILE_NAME))
            quit()
        for data in database:
            data = ",".join(list(map(str, data)))
            print(data, file=output)
        output.close()
