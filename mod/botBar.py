from mod.Bar import Bar

class BotBar(Bar):


    def autoplay(self):
        return self.cards.pop()