class Ship:
    def __init__(self, bow, horizontal, lenght):
        self.bow = bow
        self.horizontal = horizontal
        self.__lenght = lenght
        self.__hit = self.create_ship()

    def create_ship(self):
        """
        
        :return: 
        """
        ship = {}

        if self.horizontal:

            for i in [(self.bow[0] + i, self.bow[1]) for i in range(self.__lenght)]:
                ship[i] = False

        else:

            for i in [(self.bow[0], self.bow[1] + i) for i in range(self.__lenght)]:
                ship[i] = False

        return ship

    def shoot_at(self, tuple):

        if tuple in self.__hit:

            self.__hit[tuple] = True
            return True
        else:
            return False

    def is_dead(self):
        """
        
        :return: 
        """
        for i in self.__hit:

            if self.__hit[i] == True:
                return False

        return True
