# psuedocode:
# import data from constants.py
# create clean_data function:
#   create new list of dictionaries
#   copy data from argument while converting height to an integer and experience to a boolean
#   split guardians into a list of strings making 2 separate entries in the dictionary
#   return cleaned list of dictionaries
# 
# create balance_teams function:
#   increment through the list of experienced players, assigning them to one of the 3 teams
#   increment through inexperienced players, assigning them to one of the 3 teams
#   store the players data in 3 new lists of dictionaries for each team
#
# inside dunder main statement:
# run clean_data on constants.py
# run balance_teams on constants.py
# loop until user chooses to quit the program:
#   display menu and give user an option to select:
#       display team stats:
#           display list of teams and give user option to select which team:
#           display length of list of players for the team
#           display number of experienced players on the team
#           display number of inexperienced players on the team
#           display average height of the players on the team
#           increment through the players and print their names
#           increment through the players and print the names of their guardians
#       quit:
#           end program
import constants


def clean_data(data):
    cleaned_data = []
    for player in data:
        cleaned = {}
        cleaned['name'] = player['name']
        cleaned['guardians'] = player['guardians'].split(" and ")
        if player['experience'] == 'YES':
            cleaned['experience'] = True
        else:
            cleaned['experience'] = False
        cleaned['height'] = int(player['height'].split()[0])
        cleaned_data.append(cleaned)
    return cleaned_data


def balance_teams(data):
    experienced = []
    inexperienced = []
    team_1 = []
    team_2 = []
    team_3 = []
    
    for player in data:
        if player['experience']:
            experienced.append(player)
        else: 
            inexperienced.append(player)
            
    while experienced:
        team_1.append(experienced.pop())
        team_2.append(experienced.pop())
        team_3.append(experienced.pop())
        
    while inexperienced:
        team_1.append(inexperienced.pop())
        team_2.append(inexperienced.pop())
        team_3.append(inexperienced.pop())
    
    return team_1, team_2, team_3


def display_stats(team):
    total_players = len(team)
    total_experienced = 0
    total_height = 0
    names = []
    guardians = []
    for player in team:
        total_height += player['height']
        names.append(player['name'])
        guardians.append(', '.join(player['guardians']))
        if player['experience']:
            total_experienced += 1
    average_height = total_height / total_players
    total_inexperienced = total_players - total_experienced
    print("Total Players: {}".format(total_players))
    print("Total Experienced: {}".format(total_experienced))
    print("Total Inexperienced: {}".format(total_inexperienced))
    print("Average Height: {:.1f} inches".format(average_height))
    print("Players:\n" + ', '.join(names))
    print("Guardians:\n" + ', '.join(guardians))
    input("\nPress ENTER to return to menu.\n")
    


if __name__ == "__main__":
    cleaned_teams = clean_data(constants.PLAYERS)
    
    team_A, team_B, team_C = balance_teams(cleaned_teams)
    print("Welcome to the Basketball Team Stats Tool.\n\n")
    loop = True
    while loop == True:
        print("MENU:\nA) Display Team Stats\nB) Quit Program")
        menu_choice = input("Choose an option: ").lower()
        if menu_choice == 'b':
            loop = False
        elif menu_choice == 'a':
            team_choice = input("\nSelect a team:\nA) {}\nB) {}\nC) {}\nChoose an option: "
                                .format(constants.TEAMS[0],constants.TEAMS[1],constants.TEAMS[2])).lower()
            print()
            if team_choice == 'a':
                print(constants.TEAMS[0] + " Stats:\n")
                display_stats(team_A)
            elif team_choice == 'b':
                print(constants.TEAMS[1] + " Stats:\n")
                display_stats(team_B)
            elif team_choice == 'c':
                print(constants.TEAMS[2] + " Stats:\n")
                display_stats(team_C)
            else:
                print("Oops! That isn't a valid team.\n")
        else:
            print("\nOops! That isn't a valid menu option. Please try again.\n")
        
        

    
    