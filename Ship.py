import random


class Ships():
    """

    """

    def __init__(self, bow, length):
        """

        :param bow:
        :param length:
        """
        self.horizontal = random.choice([True, False])
        self.__hit = [True] * length[1]
        self.bow = bow
        self.length = length

    def list_coo(self):
        """

        :return:
        """
        list_coo = []

        if self.horizontal:
            for num in range(self.length[1]):
                list_coo.append([(self.bow[0], self.bow[1] + num)])

        else:
            for num in range(self.length[1]):
                list_coo.append([(self.bow[0] + num, self.bow[1])])

        return list_coo

    def shoot_at(self, tuple_):
        """

        :param tuple_:
        :return:
        """
        num = 0
        self.shoot_list = self.list_coo()

        for part in self.__hit:
            self.shoot_list[num].append(part)
            num += 1

        count = 0

        if [(tuple_)] in self.list_coo():
            for part in self.shoot_list:
                count += 1
                if part[0] == tuple_:
                    part[1] = False
                    break

            self.__hit[count - 1] = False

        else:
            return False
