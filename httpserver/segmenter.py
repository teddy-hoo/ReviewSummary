# a wrapper for stanford nlp segment software

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import config
from comments import Comments

class Segmenter:

    def __init__(self):
        
        command = config.STANFORD_PATH + config.SEGMENT
        self.segmenter = pexpect.spawn(command)


    def segment(self, sentence):

        if len(sentence) == 0:
            return False

        self.segmenter.sendline(sentence)


def segmenter():

    seg = Segmenter()

    base.db.connect()

    for c in Comments:
        try:
            c.segmented = seg.segment(c.raw)
            c.save()
        except:
            print c.raw, "segment error!"

    base.db.close()
