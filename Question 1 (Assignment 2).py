# Function to find teammates
def find_teammates(num_needed):
    print("Finding", num_needed, "teammates...")


# Function for battle royale mode
def battle_royale():
    players = int(input("Enter the number of players in your party: "))

    team_size = 3
    teammates_needed = team_size - players

    if teammates_needed > 0:
        find_teammates(teammates_needed)

    print("Match starting...")


# Function for practice mode
def practice():
    desired_map = input("Enter the desired map: ")
    print("Launching practice on", desired_map)


# Main program
mode = input("Enter game mode (br for Battle Royale): ")

if mode == "br":
    battle_royale()
else:
    practice()