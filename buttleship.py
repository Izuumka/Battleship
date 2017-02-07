import random


def read_field(name_file):
    """
    read from file field and return new format of field
    :param name_file: name of file with field
    :return: data
    """
    file = open(name_file, 'r')
    conten = file.readlines()

    new_content = []

    for element in [element.replace('\n', '') for element in conten]:
        if len(element) < 10:
            element = element + (' ' * (10 - len(element)))
        elif len(element) > 10:
            element = element[: 10]

        new_content.append(element)

    data = {"A": [], "B": [], "C": [], "D": [], "E": [],
            "F": [], "G": [], "H": [], "I": [], "J": []}

    for num in range(len(new_content)):
        new_format = []
        for element in new_content[num]:
            if element == ' ':
                new_format.append('0')
            elif element == '*':
                new_format.append('1')
            elif element == 'X' or element == 'x':
                new_format.append('2')
            data[num + 1] = new_format

    for num in range(1, 11):
        data["A"].append(data[num][0])
        data["B"].append(data[num][1])
        data["C"].append(data[num][2])
        data["D"].append(data[num][3])
        data["E"].append(data[num][4])
        data["F"].append(data[num][5])
        data["G"].append(data[num][6])
        data["H"].append(data[num][7])
        data["I"].append(data[num][8])
        data["J"].append(data[num][9])

    return data


def has_ship(data, coordinate):
    """
    Check if in dots are ship and return True or False
    :param data: format of field
    :param coordinate: (tuple) -  dots ("D", 3)
    :return:(bool)
    """
    try:
        if int(data[coordinate[0]][coordinate[1] - 1]) == 1:
            return True
        else:
            return False
    except Exception:
        return None


def ship_size(data, coordinate):
    """
    Count the ship size
    :param data: (data)
    :param coordinate: (tuple)
    :return: integer number
    """
    try:
        if has_ship(data, coordinate):

            str_coordinate = "/ABCDEFGHIJ/"

            count = 1

            regeest = str_coordinate.find(coordinate[0])

            num = 1
            while has_ship(data, (coordinate[0], coordinate[1] - num)):
                count += 1
                num += 1

            num = 1
            while has_ship(data, (coordinate[0], coordinate[1] + num)):
                count += 1
                num += 1

            num = 1
            while has_ship(data, (str_coordinate[regeest - num], coordinate[1])):
                count += 1
                num += 1

            num = 1
            while has_ship(data, (str_coordinate[regeest + num], coordinate[1])):
                count += 1
                num += 1

            return count
        else:
            return 0
    except Exception:
        return None


def check_alone(data, coordinate):
    """

    :param data:
    :param coordinate:
    :return:
    """
    listuk = []
    listuk2 = []
    try:
        if has_ship(data, coordinate):
            listuk.append(coordinate)

            str_coordinate = "/ABCDEFGHIJ/"

            count = 1

            regeest = str_coordinate.find(coordinate[0])

            num = 1
            while has_ship(data, (coordinate[0], coordinate[1] - num)):
                listuk.append((coordinate[0], coordinate[1] - num))
                num += 1

            num = 1
            while has_ship(data, (coordinate[0], coordinate[1] + num)):
                listuk.append((coordinate[0], coordinate[1] + num))
                num += 1

            num = 1
            while has_ship(data, (str_coordinate[regeest - num], coordinate[1])):
                listuk.append((str_coordinate[regeest - num], coordinate[1]))
                num += 1

            num = 1
            while has_ship(data, (str_coordinate[regeest + num], coordinate[1])):
                listuk.append((str_coordinate[regeest + num], coordinate[1]))
                num += 1

            noun = 1
            counter = 1

            for element in listuk:
                while noun != 3:
                    if (element[0], element[1] + counter)
                        listuk2.append((element[0], element[1] + counter))
                        counter *= -1
                        noun += 1
                noun -= 2
            return listuk2
        else:
            return None
    except Exception:
        return None

print(check_alone(read_field('field.txt'), ('A', 3)))


def is_valid(data):
    """

    :param data:
    :return:
    """
    pass

# print(read_field('field.txt'))
# print(has_ship(read_field('field.txt'), ('A', 1)))
# print(ship_size(read_field('field.txt'), ('A', 7)))
