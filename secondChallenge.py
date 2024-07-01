try:
    with open("input_file.txt", "r") as input_file:
        with open("output_file.txt", "w") as output_file:
            sum = 0
            for line in input_file.readlines():
                red, green, blue = 0, 0, 0
                tries = line.split(":")[-1].split(";")
                for individual_try in tries:
                    for value in individual_try.split(","):
                        amount, color = value.strip().split(" ")
                        match color:
                            case "red":
                                red = int(amount) if int(amount) > red else red
                            case "blue":
                                blue = int(amount) if int(amount) > blue else blue
                            case "green":
                                green = int(amount) if int(amount) > green else green
                power_set = red * green * blue
                sum += power_set
            print(sum)
except FileNotFoundError:
    print("File does not exist!")