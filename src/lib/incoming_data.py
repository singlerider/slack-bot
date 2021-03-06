import time
from threading import Thread


def initialize(irc, config):
    channel = config
    IncomingData(irc, channel).start()


class IncomingData(Thread):

    def __init__(self, irc, channel):
        Thread.__init__(self)
        self.daemon = True
        self.irc = irc
        self.channel = channel

    def run(self):
        while True:
            # print(self.callback, self.channel)
            data = self.irc.nextMessage()
            self.irc.check_for_ping(data)
