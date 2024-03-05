from .die import Die
from .utils import i_just_throw_an_exception

"""
BUGFIX:
-corrected 'Y' with 'y' in the documentation for consistency
-correcting the method answer to count the dice value instead of the number of dices.
-removing method reset and track win/loses/rounds in the function separately due to resets at
 each calling of the class

"""

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)


    def answer(self):
        total = 0
        print()
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        wins = 0
        loses = 0 
        round = 0
        while True:
            runner = cls()
            print("Round {}\n".format(round))
            for die in runner.dice:
                dice_string = die.show()
                print(dice_string)
                print(die.value)

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                loses += 1
                c = 0
            print("Wins: {} Loses {}".format(wins, loses))
            round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                
                
                break

            prompt = input("Would you like to play again?[y/n]: ")

            if prompt == 'y' or prompt == '':
                runner = cls()
            elif prompt == 'n':
                return
            else:
                i_just_throw_an_exception()
