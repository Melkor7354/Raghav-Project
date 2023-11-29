import pickle
import os
import random

player_base = [['Messi', 'RW', 93]]
user_path = os.path.expanduser('~')
path_main = user_path+'\\football_game'
path1 = path_main+'\\players'
path2 = path_main+'\\squad'


def convert_images_to_binary(image_file_path):
    f = open(image_file_path, 'rb')
    binary_card = f.read()
    f.close()
    return binary_card


def initialize():
    if os.path.exists(path_main):
        pass
    else:
        mode = 0o666
        os.mkdir(path_main, mode=mode)
        os.mkdir(path1, mode=mode)
        os.mkdir(path2, mode=mode)
        players = []
        forwards = []
        defenders = []
        midfielders = []
        gk = []
        for player in player_base:
            image = convert_images_to_binary(user_path+'\\cards\\{}.png'.format(player[0]))
            a = Player(player[0], player[1], player[2], image)
            print(a)
            a.save()
            players.append(a)
            if a.position in ('GK'):
                gk.append(a)
            elif a.position in ('LB', 'CB', ' RB'):
                defenders.append(a)
            if a.position in ('LM', 'RM', 'CM', 'CAM', 'CDM'):
                midfielders.append(a)
            else:
                forwards.append(a)

    def random_initial_squad(forw, mid, defe, goal):
        s = Squad()
        f = random.sample(forw, 3)
        m = random.sample(mid, 3)
        d = random.sample(defe, 4)
        g = random.sample(goal, 1)
        for i in [f, m, d, g]:
            for j in i:
                s.append(j)
        s.save()

        random_initial_squad(forwards, defenders, midfielders, gk)


class Player:
    def __init__(self, name, position, ovr, image):
        self.name = name
        self.position = position
        self.ovr = ovr
        self.image = image

    def player_info(self):
        return [self.name, self.position, self.ovr, self.image]

    def save(self):
        with open(path1+'\\{}'.format(self.name), 'wb') as file:
            pickle.dump(self, file)


class Squad(list):
    def __init__(self):
        list.__init__(self)

    def replace_player(self, old, new):
        self.remove(old)
        self.append(new)
        self.save()

    def check_player_in_squad(self):
        forwards = 0
        midfield = 0
        defense = 0
        gk = 0
        for player in self:
            if player.position in ('RW', 'LW', 'ST', 'CF'):
                forwards += 1
            elif player.position in ('CM', 'CAM', 'CDM', 'RM', 'LM'):
                midfield += 1
            elif player.position in ('LB', 'CB', 'RB', 'LWB', 'RWB'):
                defense += 1
            else:
                gk += 1
        if (forwards > 3) or (forwards < 1) or (midfield > 5) or (midfield < 3) or (defense > 5) or (defense < 3) or \
                (gk != 1):
            return False
        else:
            return True

    def save(self):
        with open(path2+'squad', 'wb') as file:
            pickle.dump(self, file)

initialize()






