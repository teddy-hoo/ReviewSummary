# a wrapper for stanford nlp part of speech tagger software

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import config
from comments import Comments

class Poser:

    def __init__(self):
        
        command = config.STANFORD_PATH + config.POS
        self.poser = pexpect.spawn(command)


    def pos(self, sentence):
        
        if len(sentence) == 0:
            return False

        self.poser.sendline(senetnce)


def poser():
    pass
    # read data from db and tag the pos