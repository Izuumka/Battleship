import Player, Field
import os, sys


class Game:
    """
    
    """

    def __init__(self):
        self.__field = self.__create_fields()
        self.__players = self.__take_names()
        self.__curent_player = self.__game()

    def __take_names(self):
        """
        
        :return: 
        """
        self.name1 = input("Enter name of Player1 -> ")
        self.name2 = input("Enter name of Player2 -> ")

        player1 = Player.Player(self.name1)
        player2 = Player.Player(self.name2)

        return player1, player2

    def __create_fields(self):
        """
        
        :return: 
        """
        field1 = Field.Field()
        field2 = Field.Field()

        return field1, field2

    def __game(self):
        """
        
        :return: 
        """
        while True:

            while True:

                self.__field[0].field_with_ships()
                self.__field[1].field_without_ships()
                shoot = self.__field[1].shoot_at(self.__players[0].read_position())

                if shoot == False:
                    print("Nope...")
                    break

                elif shoot == None:
                    print("You shot in this plase twise, dont do that and try again!")
                    continue

                else:
                    print("Yes!!!")
                    continue

            while True:

                self.__field[1].field_with_ships()
                self.__field[0].field_without_ships()
                shoot = self.__field[0].shoot_at(self.__players[0].read_position())

                if shoot == False:
                    break

                elif shoot == None:
                    print("You shot in this plase twise, dont do that and try again!")
                    continue

                else:
                    print("Yes!!!")
                    continue
