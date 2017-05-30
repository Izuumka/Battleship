import random
import Ship


class Field:
    """
    
    """

    def __init__(self):
        self.__ships = self.field_generation()

    def field_generation(self):
        """
        
        :return: 
        """

        field = [(i, r) for i in range(1, 11) for r in range(1, 11)]
        dict_field = {}

        for i in field:
            dict_field[i] = None

        ships_area = []

        for lenght in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:

            ship = []
            count = 0

            while len(ship) != lenght:
                count += 1

                if count > 100:
                    ship = []

                dot = random.choice(field)
                row = random.choice([True, False])

                for part in range(lenght):

                    if row and dot[0] + lenght <= 10 \
                            and (dot[0] + part, dot[1]) not in ships_area:

                        ship.append((dot[0] + part, dot[1]))

                    elif not row and dot[1] + lenght <= 10 \
                            and (dot[0], dot[1] + part) not in ships_area:

                        ship.append((dot[0], dot[1] + part))

                    else:
                        break

            cl_ship = Ship.Ship(ship[0], row, lenght)
            for part in ship:
                dict_field[part] = cl_ship

            for part in ship:
                ships_area.append((part[0], part[1]))
                ships_area.append((part[0], part[1] + 1))
                ships_area.append((part[0], part[1] - 1))
                ships_area.append((part[0] - 1, part[1]))
                ships_area.append((part[0] + 1, part[1]))
                ships_area.append((part[0] - 1, part[1] - 1))
                ships_area.append((part[0] - 1, part[1] + 1))
                ships_area.append((part[0] + 1, part[1] + 1))
                ships_area.append((part[0] + 1, part[1] - 1))

        return dict_field

    def shoot_at(self, tuple):
        """
        
        :param tuple: 
        :return: 
        """
        if self.__ships[tuple] == None:
            self.__ships[tuple] = 0
            return False

        elif self.__ships[tuple] == 1 or self.__ships[tuple] == 0:
            return None

        else:
            if self.__ships[tuple].shoot_at(tuple):
                self.__ships[tuple] = 1
                return True
            else:
                return False

    def field_without_ships(self):
        """
        
        :return: 
        """
        field_str = "  -Field of your enemy-\
            \n  |A|B|C|D|E|F|G|H|I|J|\
            \n  ---------------------"

        for i in range(1, 11):

            if i == 10:
                field_str += '\n%s|' % str(i)
            else:
                field_str += '\n%s |' % str(i)

            for r in range(1, 11):

                if self.__ships[(i, r)] == 0:
                    field_str += '+|'
                elif self.__ships[(i, r)] == 1:
                    field_str += '#|'
                else:
                    field_str += ' |'
        print(field_str)

    def field_with_ships(self):
        """
        
        :return: 
        """
        field_str = "  -----Your  field-----\
                \n  |A|B|C|D|E|F|G|H|I|J|\n  ---------------------"

        for i in range(1, 11):

            if i == 10:
                field_str += '\n%s|' % str(i)
            else:
                field_str += '\n%s |' % str(i)

            for r in range(1, 11):

                if self.__ships[(i, r)] == 0:
                    field_str += '+|'
                elif self.__ships[(i, r)] == 1:
                    field_str += '#|'
                elif self.__ships[(i, r)] == None:
                    field_str += ' |'
                else:
                    field_str += '*|'

        print(field_str)

    def end_of_game(self):
        """
        
        :return: 
        """
        for dot in self.__ships:
            if self.__ships[dot] != None:
                if self.__ships[dot].is_dead() == False:
                    return False
        return True