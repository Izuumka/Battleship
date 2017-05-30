import random


def read_field():
    """

    :return: 
    """
    file = open('field.txt', 'r')
    content = file.readlines()
    content[-1] += "\n"
    data = []

    for num in range(len(content)):
        content[num] = content[num][:-1]

        if len(content[num]) < 10:
            content[num] += ' ' * (10 - len(content[num]))

        time_place = []

        for element in content[num]:
            if element == ' ':
                time_place.append(0)
            elif element == "*":
                time_place.append(1)
            else:
                time_place.append(2)

        data.append(time_place)

    return data


def konvert(tuple):
    """

    :param tuple: 
    :return: 
    """
    if type(tuple[0]) == str:

        low = tuple[0].lower()
        abetka = 'abcdefghij'

        if 0 < tuple[1] <= 10 and low in abetka:
            return abetka.find(low) + 1, tuple[1]
        else:
            return None

    else:
        return tuple


def has_ship(data, tuple):
    """

    :param data: 
    :param tuple: 
    :return: 
    """
    tuple = konvert(tuple)

    if 10 >= tuple[0] >= 1 and 10 >= tuple[1] >= 1:
        if data[tuple[1] - 1][tuple[0] - 1] == 1 or \
                        data[tuple[1] - 1][tuple[0] - 1] == 2:
            return True
        else:
            return False
    else:
        return False


def ship_size(data, tuple):
    """

    :param data: 
    :param tuple: 
    :return: 
    """
    if has_ship(data, tuple):

        ship_size = 1

        for num in range(1, 4):
            if has_ship(data, (tuple[0] + num, tuple[1])):
                ship_size += 1
            else:
                break

        for num in range(1, 4):
            if has_ship(data, (tuple[0] - num, tuple[1])):
                ship_size += 1
            else:
                break

        for num in range(1, 4):
            if has_ship(data, (tuple[0], tuple[1] + num)):
                ship_size += 1
            else:
                break

        for num in range(1, 4):
            if has_ship(data, (tuple[0], tuple[1] - num)):
                ship_size += 1
            else:
                break

        return ship_size

    else:
        return 0


def is_valid(data):
    """

    :param data: 
    :return: 
    """
    lenght_list = [ship_size(data, (num + 1, n_num + 1)) for num in range(len(data))
                   for n_num in range(len(data[num])) if has_ship(data, (num + 1, n_num + 1))]

    if lenght_list.count(4) == lenght_list.count(1) == 4 \
            and lenght_list.count(2) == lenght_list.count(3) == 6:
        pass
    else:
        return False

    all_ships_part = [(num + 1, n_num + 1) for num in range(len(data))
                      for n_num in range(len(data[num])) if has_ship(data, (num + 1, n_num + 1))]

    all_ships = []

    for tuple in all_ships_part:
        parts = [tuple]
        for num in range(1, 4):
            if has_ship(data, (tuple[0] + num, tuple[1])):
                parts.append((tuple[0] + num, tuple[1]))
            else:
                break

        for num in range(1, 4):
            if has_ship(data, (tuple[0] - num, tuple[1])):
                parts.append((tuple[0] - num, tuple[1]))
            else:
                break

        for num in range(1, 4):
            if has_ship(data, (tuple[0], tuple[1] + num)):
                parts.append((tuple[0], tuple[1] + num))
            else:
                break

        for num in range(1, 4):
            if has_ship(data, (tuple[0], tuple[1] - num)):
                parts.append((tuple[0], tuple[1] - num))
            else:
                break
        all_ships.append(parts)

    for ship in all_ships:
        ships_area = []
        for part in ship:
            ships_area.append((part[0] - 1, part[1] - 1))
            ships_area.append((part[0] - 1, part[1] + 1))
            ships_area.append((part[0] + 1, part[1] + 1))
            ships_area.append((part[0] + 1, part[1] - 1))
        for area in ships_area:
            if has_ship(data, area):
                return False
    return True


def field_to_str(data):
    """

    :param data: 
    :return: 
    """
    field = ""

    for line in data:
        field += "\n"

        for element in line:
            if element == 0:
                field += ' '
            elif element == 1:
                field += '*'
            else:
                field += 'x'

    print(field)


def generate_field():
    """

    :return: 
    """
    field = [(i, r) for i in range(1, 11) for r in range(1, 11)]
    dict_field = {}

    while 1:

        for i in field:
            dict_field[i] = 0

        ships_area = []

        for lenght in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:

            ship = []
            count = 0

            while len(ship) != lenght:
                count += 1

                if count > 100:
                    ship = []

                dot = random.choice(field)
                row = random.choice([0, 1])

                for part in range(lenght):

                    if row == 0 and dot[row] + lenght <= 10 \
                            and (dot[row] + part, dot[1]) not in ships_area:

                        ship.append((dot[row] + part, dot[1]))

                    elif row == 1 and dot[row] + lenght <= 10 \
                            and (dot[0], dot[row] + part) not in ships_area:

                        ship.append((dot[0], dot[row] + part))

                    else:
                        break

            for part in ship:
                dict_field[part] = 1

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

        data = []

        for i in range(1, 11):
            line = []
            for r in range(1, 11):
                if dict_field[(i, r)] == 0:
                    line.append(0)
                else:
                    line.append(1)
            data.append(line)
        if is_valid(data):
            continue
        else:
            break

    field_str = "  |A|B|C|D|E|F|G|H|I|J|\n  ---------------------"

    for i in range(1, 11):

        if i == 10:
            field_str += '\n%s|' % str(i)
        else:
            field_str += '\n%s |' % str(i)

        for r in range(1, 11):

            if dict_field[(i, r)] == 0:
                field_str += ' |'

            else:
                field_str += '*|'

    print(field_str)
