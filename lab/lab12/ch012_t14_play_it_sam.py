from random import randint
from typing import List

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board_in: List[List[str]]) -> None:
    for row in board_in:
        print(" ".join(row))


def random_row(board_in: List[List[str]]) -> int:
    return randint(0, len(board_in) - 1)


def random_col(board_in: List[List[str]]) -> int:
    return randint(0, len(board_in) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

# Write your code below!
Task1.	Getting Our Feet Wet

Background
In this project you will build a simplified, one-player version of the classic board game Battleship! In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.
To build this game we will use our knowledge of lists, conditionals and functions in Python. When you're ready to get started, click Next to continue.

The first thing we need to do is to set up the game board.



Instructions
1. Create a variable board and set it equal to an empty list.

Task2.	Make a List

Background
Good! Now we'll use a built-in Python function to generate our board, which we'll make into a 5 x 5 grid of all "O"s, for "ocean."
print(["O"] * 5)

will print out ['O', 'O', 'O', 'O', 'O'], which is the basis for a row of our board.
We'll do this five times to make five rows. (Since we have to do this five times, it sounds like a loop might be in order.)


Instructions
1. Create a 5 x 5 grid initialized to all 'O's and store it in board.
Use range() to loop 5 times.
Inside the loop, .append() a list containing 5 "O"s to board, just like in the example above.
Note that these are capital letter "O" and not zeros.

Task3.	Check it Twice

Background
Great job! Now that we've built our board, let's show it off.
Throughout our game, we'll want to print the game board so that the player can see which locations they have already guessed. Regularly printing the board will also help us debug our program.
The easiest way to print the board would be to have Python display it for us using the print command. Let's give that a try and see what the results look like—is this a useful way to print our board for Battleship?



Instructions
1. Use the print command to display the contents of the board list.

Task4.	Custom Print

Background
Now we can see the contents of our list, but clearly it would be easier to play the game if we could print the board out like a grid with each row on its own line.
We can use the fact that our board is a list of lists to help us do this. Let's set up a for loop to go through each of the elements in the outer list (each of which is a row of our board) and print them.



Instructions
1. First, delete your existing print statement.

Then, define a function named print_board with a single argument, board_in.
Inside the function, write a for loop to iterates through each row in board and print it to the screen.
Call your function with board to make sure it works.

Task5.	Printing Pretty

Background
We're getting pretty close to a playable board, but wouldn't it be nice to get rid of those quote marks and commas? We're storing our data as a list, but the player doesn't need to know that!
letters = ['a', 'b', 'c', 'd'] 
print(" ".join(letters))
print("---".join(letters))
In the example above, we create a list called letters.
Then, we print a b c d. The .join method uses the string to combine the items in the list.
Finally, we print a---b---c---d. We are calling the .join function on the "---" string.
We want to turn each row into "O O O O O".



Instructions
1. Inside your function, inside your for loop, use " " as the separator to .join the elements of each row.

Task6.	Hide...

Background
Excellent! Now, let's hide our battleship in a random location on the board.
Since we have a 2-dimensional list, we'll use two variables to store the ship's location, ship_row and ship_col.
from random import randint 
coin = randint(0, 1) 
dice = randint(1, 6)
In the above example, we first import the randint(low, high) function from the random module.
Then, we generate either zero or one and store it in coin.
Finally, we generate a number from one to six inclusive.
Let's generate a random_row and random_col from zero to four!



Instructions
1. Define two new functions, random_row and random_col, that each take board_in as input.

These functions should return a random row index and a random column index from your board, respectively. Use randint(0, len(board_in) - 1).
Call each function on board.

Task7.	...and Seek!

Background 
Good job! For now, let's store coordinates for the ship in the variables ship_row and ship_col. Now you have a hidden battleship in your ocean! Let's write the code to allow the player to guess where it is.
number = input("Enter a number: ") 
if int(number) == 0: 
  print("You entered 0")

input asks the user for input and returns it as a string. But we're going to want to use integers for our guesses! To do this, we'll wrap the inputs with int() to convert the string to an integer.



Instructions
1.In run method, Create a new variable called guess_row and set it to int(input("Guess Row: ")).

Create a new variable called guess_col and set it to int(input("Guess Col: ")).
Then, execute the file “ch012_t07_and_seek.py” and then answer the prompts by typing in a number and pressing Enter (or Return on some computers).

Task8.	It's Not Cheating—It's Debugging!

Background 
Awesome! Now we have a hidden battleship and a guess from our player. In the next few steps, we'll check the user's guess to see if they are correct.
While we're writing and debugging this part of the program, it will be helpful to know where that battleship is hidden. Let's add a print statement that displays the location of the hidden ship.
Of course, we'll remove this output when we're finished debugging since if we left it in, our game wouldn't be very challenging. :)




Instructions
1. Before the lines prompting the user for input:

Print the value of ship_row.
Print the value of ship_col.

Task9.	You win!

Background 
Okay—now for the fun! We have the actual location of the ship and the player's guess so we can check to see if the player guessed right.
For a guess to be right, guess_col should be equal to ship_col and guess_row should be equal to ship_row.
if guess_col == 0 and guess_row == 0: 
  print("Top-left corner.")

The example above is just a reminder about if statements.



Instructions
1. On line 33, add an if to check if guess_row equals ship_row and guess_col equals ship_col.

If that is the case, please print out "Congratulations! You sank my battleship!"
When you run this code, be sure to enter integer guesses in the panel where it asks for "Guess Row" and then "Guess Col".

Task10.	Danger, Will Robinson!!

Background 
Great! Of course, the player isn't going to guess right all the time, so we also need to handle the case where the guess is wrong.
print(board[2][3])

The example above prints out "O", the element in the 3rd row and 4th column.



Instructions
1. Add an else under the if we wrote in the previous step.

Print out "You missed my battleship!"
Set the list element at guess_row, guess_col to "X".
As the last line in your else statement, call print_board(board) again so you can see the "X".Make sure to enter a col and row that is on the board!

Task11.	Bad Aim

Background 
Great job! Now we can handle both correct and incorrect guesses from the user. But now let’s think a little bit more about the "miss" condition.
They can enter a guess that's off the board.
They can guess a spot they’ve already guessed.
They can just miss the ship.
We'll add these tests inside our else condition. Let's build the first case now!
if x not in range(8) or y not in range(3): 
  print("Outside the range")

The example above checks if either x or y are outside those ranges. The \ character just continues the if statement onto the next line.



Instructions
1. Add a new if statement that is nested under the else.

Like the example above, it should check if guess_row is not in range(5) or guess_col is not in range(5).
If that is the case, print out "Oops, that's not even in the ocean."
(When doing testing after you fulfill all the instructions, input a value for either row or column more than 5 (e.g. 10), you should be able to trigger the string "Oops, that's not even in the ocean.")
Task12.	Not Again!

Background 
Great! Now let's handle the second type of incorrect guess: the player guesses a location that was already guessed. How will we know that a location was previously guessed?
print(board[guess_row][guess_col])

The example above will print an 'X' if already guessed or an 'O' otherwise.



Instructions
1. Add an elif to see if the guessed location already has an 'X' in it.

If it has, print "You guessed that one already."

Task13.	Test Run

Background 
Congratulations! Now you should have a game of Battleship! that is fully functional for one guess.
Make sure you play it a couple of times and try different kinds of incorrect guesses. This is a great time to stop and do some serious debugging.
In the next task “”, we'll move on and look at how to give the user 4 guesses to find the battleship.



Instructions
1. Thoroughly test your game. Make sure you try a variety of different guesses and look for any errors in the syntax or logic of your program.

Task14.	Play It, Sam

Background 
You can successfully make one guess in Battleship! But we’d like our game to allow the player to make up to 4 guesses before they lose.
for turn in range(4): 
  # Make a guess 
  # Test that guess

We can use a for loop to iterate through a range. Each iteration will be a turn.



Instructions
1. Add a for loop that repeats the guessing and checking part of your game for 4 turns, like the example above.

At the beginning of each iteration, print "Turn", turn + 1 to let the player know what turn they are on.
Indent everything that should be repeated.

Task15.	Game Over

Background 
If someone runs out of guesses without winning right now, the game just exits. It would be nice to let them know why.
Since we only want this message to display if the user guesses wrong on their last turn, we need to think carefully about where to put it.
We’ll want to put it under the else that accounts for misses
We’ll want to print the message no matter what the cause of the miss
Since our turn variable starts at 0 and goes to 3, we will want to end the game when turn equals 3.



Instructions
1. Add an if statement that checks to see if the user is out of guesses.
Put it under the else that accounts for misses.
Put it after the if/elif/else statements that check for the reason the player missed. We want "Game Over" to print regardless of the reason.
If turn equals 3, print "Game Over".

Task16.	A Real Win

Background 
Almost there! We can play Battleship!, but you’ll notice that when you win, if you haven’t already guessed 4 times, the program asks you to enter another guess. What we’d rather have happen is for the program to end—it’s no fun guessing if you know you’ve already sunk the Battleship!
We can use the break command to get out of a for loop.




Instructions
1. Add a break under the win condition to end the loop after a win.

Task17.	To Your Battle Stations!

Background 
Congratulations! You have a fully functional Battleship game! Play it a couple of times and get your friends to try it out, too. (Don’t forget to go back and remove the debugging output that gives away the location of the battleship!)
You may want to take some time to clean up and document your code as well.




Instructions
1. Please remove the debugging output that gives away the location of the battleship, and execute the file “ch012_t17_to_battle_stations.py” to play the game for a few time.






