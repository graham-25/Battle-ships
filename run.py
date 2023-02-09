# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def start_game():
    """
    This is where the board size is defined by the user, 
    it takes the user's input as the board size squaired. 
    We are going to initialise 2 boards so that one can 
    be hidden to hide the ships to be destroyed.
    """

    board_size =  int(input("Please enter the board size! "))
    size = board_size ** 2
    user_board = [(" ") for x in range(size)]
    com_board = [(" ") for x in range(size)]

    return user_board

def main():
    """
    
    """
    game = start_game()

print("Welcome to Battle Ships")
print("The aim of this game is to guess where the computers ships are to Destroy them. ")
main()