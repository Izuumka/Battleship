import random
import Ship


class Field():
    """

    """

    def __init__(self):
        """

        """

    def field_generate(self):

        field = []

        for num in range(1, 11):
            for number in range(1, 11):
                field.append((num, number))

        return field

    def create_ships(self, size):
        """

        :return:
        """

        self.all = []

        while 1:
            bow = random.choice(self.field_generate())
            if bow[1] + size <= 10 or bow[0] + size <= 10:
                while 1:
                    ship = Ship.Ships(bow, (1, size))
                    for element in ship.list_coo():
                        if element in self.all:
                            continue
                        else:
                            self.all.append(element)
                            print(element)
                            break


            else:
                continue

        return ship.shoot_list()

    def shoot_at(self, tuple):
        """

        :param tuple:
        :return:
        """
        pass

    def field_without_ships(self):
        """

        :return:
        """
        pass

    def field_with_ships(self):
        """

        :return:
        """
        pass

    def field_check(self):
        pass


field = Field()
print(field.create_ships(4))
