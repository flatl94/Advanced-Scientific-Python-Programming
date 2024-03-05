from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        
        self.__DICE = Die()
        self.__round = 1
        self.__wins = 0
        self.__losses = 0
        
    
    def roll_dices(self, n):
        for i in range(n):
            self.__DICE.roll_dice
        self.__visual_rolls = self.__DICE.get_dices
        self.__value_rolls = self.__DICE.get_values

    def check_answer(self, answer):
        correct_answer = sum(self.__value_rolls)
        print(type(correct_answer), type(answer))
        if answer == correct_answer:
            print("Congrats, you can add like a 6 year old...")
            self.__wins = self.__wins + 1
            
        else:
            print("(Perplexed - I am too old for all of this...) Your answer is  wrong.")
            self.__losses = self.__losses + 1
        self.__round = self.__round + 1
        self.__DICE.reset_dices
        

    @classmethod
    def run(_class):
        # Run the game as a whole.
        # Even greater variable name choise, 11/10.
        
        another_game = 'Y'
        while another_game in ['Y','y']:
            count_round = 0
            runner = _class()
            while count_round <= 6:
                runner.roll_dices(5)

                print("Round {}\n".format(runner.__round))

                for die in runner.__visual_rolls:
                    print(die)

                while True:
                    try:
                        guess = int(input("Give me your best guess. Remember you are dealing with integers...  "))
                    except ValueError:
                        print("What part of 'dealing with integers' you don't understand?")
                        continue
                    else:
                        break
                
                    
                runner.check_answer(guess)
                print("Wins: {} Loses {}".format(runner.__wins, runner.__losses))


                prompt = input("Would you like to continue playing?\nPress enter or Y/y to continue playing or press N/n to stop playing.")
                if prompt in ['Y','y','']:
                    count_round = count_round + 1
                    continue
                elif prompt in ['n','N']:
                    print("Let's gooooo! We got rid of this loser")
                    return
                else:
                    i_just_throw_an_exception()
            if runner.__wins > runner.__losses:
                print('yeah... you won')
            else:
                print('Congrats, your IQ cannot be measured with 3 digits.')
            another_game = input('Wonna play another game?\nPress Y/y for another game')