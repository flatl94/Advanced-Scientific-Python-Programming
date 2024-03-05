# Just count the stupid dice
import random

"""
BUGFIX:
-removed useless functions
-modified random integer generator
-modified 6 dice string.


"""   

class Die:
    """
    This is always correct. Seriously, look away.
    """

    def __init__(self):
        self.roll()
        

    def roll(self):
        self.value = random.randint(1,6)
        

    def show(self):
        
        if self.value == 1:
            str_dice =  "---------\n|       |\n|   *   |\n|       |\n---------"
        elif self.value == 2:
            str_dice =  "---------\n|*      |\n|       |\n|      *|\n---------"
        elif self.value == 3:
            str_dice =  "---------\n|*      |\n|   *   |\n|      *|\n---------"
        elif self.value == 4:
            str_dice =  "---------\n|*     *|\n|       |\n|*     *|\n---------"
        elif self.value == 5:
            str_dice = "---------\n|*     *|\n|   *   |\n|*     *|\n---------"
        elif self.value == 6:
            str_dice = "---------\n|*     *|\n|*     *|\n|*     *|\n---------"
        else:
            raise ValueError('Error! This dice has only 6 faces.')
        return str_dice

    @classmethod
    def create_dice(cls, n):
        return [cls() for _ in range(n)]
