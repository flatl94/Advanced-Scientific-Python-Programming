class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Songbird','Parrot']
    def printMembers(self):
        print('Printing members of the harmless Birds class')
        for member in self.members:
            print('\t%s ' % member)

class Fishes:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Goldfish','Whale']
    def printMembers(self):
        print('Printing members of the harmless Fishes class.\n... whales are not  fishes but does not matter')
        for member in self.members:
            print('\t%s ' % member)

class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Cow','Sheep','Doge']
    def printMembers(self):
        print('Printing members of the harmless Mammals class')
        for member in self.members:
            print('\t%s ' % member)