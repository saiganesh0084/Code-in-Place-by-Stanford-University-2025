



def main():
    num = 20 # Total num of stones
    player_turn = 1 # Start with plaayer one

            # Run a while loop to check whether there are any stones left
    while num > 0: 
        print(f"There are {num} stones left.")

            # Ask the current player for input
        user_input = int(input(f"Player {player_turn} would you like to remove 1 or 2 stones?"))

            # Check for correct input by player
        while user_input !=1 and user_input !=2:
            user_input = int(input("Please enter 1 or 2: "))

            # Check whether number of stones left for given input
        while num == 1 and user_input !=1:
            user_input = int(input("Please enter 1: "))
        num = num - user_input
   
            # Switch players turn
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn  = 1
            
            #Spacing
        print("")

    print(f"Player {player_turn} wins!")

if __name__ == '__main__':
    main()