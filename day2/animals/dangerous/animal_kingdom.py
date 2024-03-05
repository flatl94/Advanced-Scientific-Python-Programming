class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Eagle', 'Duck', 'Seagull', 'Roaster']
    def printMembers(self):
        print('Printing members of the dangerous Birds class')
        for member in self.members:
            print('\t%s ' % member)

class Fishes:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Shark','Pirana','Barracuda']
    def printMembers(self):
        print('Printing members of the dangerous Fishes class.\n... sharks are not  fishes but does not matter')
        for member in self.members:
            print('\t%s ' % member)

class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Bull','Rat','Hippo']
    def printMembers(self):
        print('Printing members of the dangerous Mammals class')
        for member in self.members:
            print('\t%s ' % member)