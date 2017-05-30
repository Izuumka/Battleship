class Player:
    def __init__(self, name):
        self.__name = name

    def read_position(self):
        """
        
        :return: 
        """
        while 1:
            coordinates = input("Enter coordinate of shoot. Example: J 3 -> ")

            coordinates = coordinates.split()

            low = coordinates[0].lower()
            abetka = 'abcdefghij'
            try:
                if 0 < int(coordinates[-1]) <= 10 and low in abetka:
                    return int(coordinates[1]), abetka.find(low) + 1
                else:
                    print("Try again!")
                    continue
            except Exception:
                print("Try again!")
                continue
