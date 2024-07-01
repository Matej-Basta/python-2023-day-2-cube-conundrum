RED = 12
GREEN = 13
BLUE = 14

try:
    with open("input_file.txt", "r") as input_file:
        with open("output_file.txt", "w") as output_file:
            sum = 0
            for line in input_file.readlines():
                new_list = line.split(":")
                game_number = new_list[0].split(" ")[-1]
                tries = new_list[1].split(";")
                valid_game = True
                for individual_try in tries:
                    for value in individual_try.split(","):
                        amount, color = value.strip().split(" ")
                        match color:
                            case "red":
                                if int(amount) > RED:
                                    valid_game = False
                            case "green":
                                if int(amount) > GREEN:
                                    valid_game = False
                            case "blue":
                                if int(amount) > BLUE:
                                    valid_game = False
                if valid_game:
                    sum += int(game_number)
            print(sum)
            output_file.write(str(sum))
except FileNotFoundError:
    print("The file has not been found.")
except:
    print("An error occurred.")