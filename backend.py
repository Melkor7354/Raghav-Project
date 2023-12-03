import pickle
import os
import random
import tkinter as tk
player_base = [['LIONEL MESSI', 'RW', 90], ['CRISTIANO RONALDO', 'ST', 86],
               ['TONI KROOS', 'CM', 86], ['GARNACHO', 'LW', 75], ['HARRY KANE', 'ST', 90],
               ['SON', 'LW', 87], ['COLE PALMER', 'CAM', 66], ['STERLING', 'LW', 83],
               ['ENZO', 'CM', 83], ['JAMAL MUSIALA', 'CAM', 86], ['JUDE BELLINGHAM', 'CM', 86],
               ['JEREMY DOKU', 'RW', 77], ['MARCUS RAHSFORD', 'LW', 85], ['SOFYAN AMRABAT', 'CM', 80],
               ['RASMUS HOJLUND', 'ST', 76], ['PEDRI', 'CM', 86], ['PABLO GAVI', 'CB', 83],
               ['WILLIAM SALIBA', 'CB', 83], ['DAYOT UPAMECANO', 'CB', 82], ['KEVIN DE BRUYNE', 'CAM', 91],
               ['KARIM BENZEMA', 'ST', 90], ['JOSHUA KIMMICH', 'CDM', 88], ['JAN OBLAK', 'GK', 88],
               ['ANDREAS CHRISTENSEN', 'CB', 83], ['ANDREAS PEREIRA', 'CAM', 77], ['KVARATSKHELIA', 'LW', 86],
               ['BASTONI', 'CB', 85], ['REECE JAMES', 'RB', 84], ['FERLAND MENDY', 'LB', 82],
               ['MIKE MAIGNAN', 'GK', 87], ['NICHOLAS JACKSON', 'ST', 78], ['FRED', 'CDM', 81],
               ['MALACIA', 'LB', 78], ['RICO LEWIS', 'RB', 73]]
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
            image = user_path+'\\cards\\{}.png'.format(player[0])
            a = Player(player[0], player[1], player[2], image)
            a.save()
            players.append(a)
            if a.position == 'GK':
                gk.append(a)
            elif a.position in ('LB', 'CB', ' RB'):
                defenders.append(a)
            elif a.position in ('LM', 'RM', 'CM', 'CAM', 'CDM'):
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
        self.price = self.ovr*6*9

    def player_info(self):
        return [self.name, self.position, self.ovr, self.image]

    def save(self):
        with open(path1+'\\{}'.format(self.name), 'wb') as file:
            pickle.dump(self, file)


class Squad(list):
    def __init__(self, crest=None, name=None):
        list.__init__(self)

        self.crest = crest
        self.name = name

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
        with open(path2+'\\main', 'wb') as file:
            pickle.dump(self, file)


def read_squad():
    with open(path2 + '\\main', 'rb') as file:
        squad = pickle.load(file)
        players = []
        for i in squad:
            players.append((i.name, i.position, i.ovr, i.ovr*6*9, i.image))
        return players

def random_player_image(player):
    squad = read_squad()
    not_in_squad = []
    for player in player_base:
        for starter in squad:
            if player[0] != starter[0]:
                not_in_squad += player
            else:
                pass
    transfers = random.sample(not_in_squad, 2)
    ret = []
    for player in transfers:
        ret.append(player)
    return ret

def squad_name():
    if os.path.exists(path_main):
        pass
    else:
        window = tk.Tk()
        window.geometry('200x200')
        entry = tk.Entry(window)
        name = ''
        def get_name():
            global name
            name = entry.get()
            window.destroy()
        submit = tk.Button(window, text='SUBMIT', command=get_name)
        entry.pack()
        submit.pack()
        window.mainloop()
        return name
        
