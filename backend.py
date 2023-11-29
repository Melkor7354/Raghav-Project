import pickle
import os

player_base = [['Lionel Messi', 'RW', 93, 'Inter Miami', 'Argentina'], []]
user_path = os.path.expanduser('~')
path1 = user_path+'/players'
path2 = user_path+'/squad'


def convert_images_to_binary(image_file_paths):
    binary_cards = []
    for i in image_file_paths:
        f = open(i, 'rb')
        binary_cards.append(f.read())
        f.close()
    return binary_cards


def check_player_in_squad(players):



def initialize():
    if os.path.exists(user_path+'/football_game'):
        pass
    else:
        mode = 0o666
        os.mkdir(path1, mode=mode)
        os.mkdir(path2, mode=mode)



class Player:
    def __init__(self, name, position, ovr, club, country, image):
        self.name = name
        self.position = position
        self.ovr = ovr
        self.club = club
        self.country = country
        self.image = image

    def player_info(self):
        return [self.name, self.position, self.ovr, self.club, self.country, self.image]

    def save(self):
        with open(path1+'{}'.format(self.name), 'wb') as file:
            pickle.dump(self, file)


def Squad(list):
    def __init__(self):
        list.__init__(self)






