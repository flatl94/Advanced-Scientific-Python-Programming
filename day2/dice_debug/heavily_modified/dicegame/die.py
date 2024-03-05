# FINALLY WORKS
import random

class Die:
    """
    This should be correct, now. Should.
    
    """

    def __init__(self):
        self.__dice_values = []
        self.__dice_visual = []

    @property
    def roll_dice(self):
        dice_seed = random.randrange(1, 6)
        self.__dice_values.append(dice_seed)
        dice_pic = self.visual(dice_seed)
        self.__dice_visual.append(dice_pic)
        
    
    def visual(self, value):
        if isinstance(value, int):
            if value == 1:
                string_dice = "---------\n|       |\n|   *   |\n|       |\n---------"
            elif value == 2:
                string_dice = "---------\n|*      |\n|       |\n|      *|\n---------"
            elif value == 3:
                string_dice = "---------\n|*      |\n|   *   |\n|      *|\n---------"
            elif value == 4:
                string_dice = "---------\n|*     *|\n|       |\n|*     *|\n---------"
            elif value == 5:
                string_dice = "---------\n|*     *|\n|   *   |\n|*     *|\n---------"
            elif value == 6:
                string_dice = "---------\n|*     *|\n|*     *|\n|*     *|\n---------"
            else:
                raise ValueError('Error! We are playing with dices having 6 faces.')
        else:
            raise ValueError('Error! The method only accepts integers.')
        return string_dice

    @property
    def get_dices(self):
        return self.__dice_visual
    
    @property
    def get_values(self):
        return self.__dice_values
    
    @property
    def reset_dices(self):
        self.__dice_values = []
        self.__dice_visual = []
    

        
    
