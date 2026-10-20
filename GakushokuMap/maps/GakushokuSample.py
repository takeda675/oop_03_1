from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):

    def get_menu(self):
        return "鳥天丼"

    def get_summary(self):
        return "美味しい"

    def get_author(self):
        return "武田"