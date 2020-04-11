
import sys          #This module contains the sys.exit() function
choices = []        #Creating a list 'choices'


def printBoard() :
    '''
    This function prints the 3*3 board.
    The intial value consist of position number stored in choices list.
    As user gives input the 'X' or "O' is appended at that position.
    '''
    print( '\n ----------')
    print( '|' ,choices[0] , '|' , choices[1] , '|' , choices[2] , '|')
    print( ' ----------')
    print( '|' , choices[3] , '|' , choices[4] , '|' , choices[5] , '|')
    print( ' ----------')
    print( '|' , choices[6] , '|' , choices[7] , '|' , choices[8] , '|')
    print( ' ----------\n')


print("\n\t\t\tWELCOME TO TIC TAC TOE GAME.\n\n\n PLAYER 1 = 'X' \t\t PLAYER 2 = '0'")
for x in range (0, 9) :
    choices.append(x + 1)   #This appends index value +1 to the list

playerOneTurn = True    #as set to true game starts with platerOne
winner = False      #intializing winner as false so that loop will start
count=0     #intializing count to zero .If count > 9 game finishes.

while not winner :      #if winner value is false condition is true loop starts

    printBoard()        #the printboard function is called with intial values.
    if(count>=9):   
        '''if count >= 9 it means maximum moves done .
        Its a draw because no one wins and maximum moves are achieved.
        So the game exits and its a draw.
        '''
        print("Draw")
        sys.exit()  
       

    
    if playerOneTurn :  #if player one value is true its player one turn else player two's turn
        print( "Player 1:")
    else :
        print( "Player 2:") #if player1 value is false. Player1 value changes further using 'not keyword'.

    try:
        choice = int(input(">> "))  #input of player stored in choice variable
    except:
        # it executes if user enter anything other than integer value
        print("Please enter a valid input")
        continue
        '''
        Python continue statement. It returns the control to the beginning of the while loop.. 
        The continue statement rejects all the remaining statements in the current iteration 
        of the loop and moves the control back to the top of the loop.
         The continue statement can be used in both while and for loops.
        '''
    if(choice>9):
        '''
        If user enter value > 9 then control goes to the beginning of while loop.
        The user needs to enter the input again
        '''
        print("Invalid Input.Please Enter a valid choice")
        continue
        
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("Illegal move, The place is already filled. Please try again")
        continue

    if playerOneTurn :
        '''
        If player1 gave input increment count value.
        Place 'X' in choices list for player1 at the index value 'choice -1'.
        Variable choice contains input given by players
        '''
        count+=1
        choices[choice - 1] = 'X'
    else :
        '''
        If player2 gave input increment count value.
        Place '0' in choices list for player1 at the index value 'choice -1'.
        Variable choice contains input given by players
        '''
        count+=1
        choices[choice - 1] = '0'

    playerOneTurn = not playerOneTurn
    '''
    After player1 turns its value change alternatively from TRUE to FALSE and vice versa.
    Due to this the input toggles between plaayer1 and player2.
    The not keyword is a logical operator.
    The return value will be True if the statement(s) are not True, otherwise it will return False.
    '''

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            '''
            Checks row condition of tic tac toe game.
            If values at the index for a row in the list is same then winner is updated as true.
            e.g
                choices[0]==choices[1]==choices[2] then a player wins
            After it we call printboard function.
            But as the value of winner is true the while loop is not executed and the winner is declared.
            '''
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            '''
            Checks column condition of tic tac toe game.
            If values at the index for a column  in the list is same then winner is updated as true.
            e.g
                choices[0]==choices[3]==choices[6] then a player wins.
            After it we call printboard function.
            But as the value of winner is true the while loop is not executed and the winner is declared.
            '''
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        '''
        Checks the diagonal winning condition of tic tac toe game.
        The value of winner is updated to True
        '''
        printBoard()

print ("Player " ,playerOneTurn + 1 , " wins!\n")
'''
If playerOneTurn is False then player1 wins.
Because playerOne value is false then the game ended as player1 won.
Else player2 wins

'''

'''
OUTPUT :


			WELCOME TO TIC TAC TOE GAME.


 PLAYER 1 = 'X' 		 PLAYER 2 = '0'

 ----------
| 1 | 2 | 3 |
 ----------
| 4 | 5 | 6 |
 ----------
| 7 | 8 | 9 |
 ----------

Player 1:
>> 1

 ----------
| X | 2 | 3 |
 ----------
| 4 | 5 | 6 |
 ----------
| 7 | 8 | 9 |
 ----------

Player 2:
>> 5

 ----------
| X | 2 | 3 |
 ----------
| 4 | 0 | 6 |
 ----------
| 7 | 8 | 9 |
 ----------

Player 1:
>> 9

 ----------
| X | 2 | 3 |
 ----------
| 4 | 0 | 6 |
 ----------
| 7 | 8 | X |
 ----------

Player 2:
>> 8

 ----------
| X | 2 | 3 |
 ----------
| 4 | 0 | 6 |
 ----------
| 7 | 0 | X |
 ----------

Player 1:
>> 6

 ----------
| X | 2 | 3 |
 ----------
| 4 | 0 | X |
 ----------
| 7 | 0 | X |
 ----------

Player 2:
>> 2

 ----------
| X | 0 | 3 |
 ----------
| 4 | 0 | X |
 ----------
| 7 | 0 | X |
 ----------

Player  2  wins!



'''
