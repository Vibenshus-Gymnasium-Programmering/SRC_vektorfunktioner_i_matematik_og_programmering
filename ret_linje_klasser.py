import arcade
import math

WIDTH = 800
HEIGHT = 600

class RetLinje:
    def __init__(self,kendt_punkt,retningsvektor, starttid = 0, punktradius = 4, farve = arcade.csscolor.BLUE, sportykkelse = 2, antal_punkter_i_spor = 100):
        self.kendt_punkt_x, self.kendt_punkt_y = kendt_punkt
        self.rx, self.ry = retningsvektor
        self.x = self.kendt_punkt_x + self.rx*starttid
        self.y = self.kendt_punkt_y + self.ry*starttid
        self.tid = starttid
        self.punktradius = punktradius
        self.farve = farve
        self.sportykkelse = sportykkelse
        self.antal_punkter_i_spor = antal_punkter_i_spor
        self.spor = list()
        self.grafpunkter = list()

    def opdater(self, delta_tid):
        self.spor.append((self.x, self.y))
        if len(self.spor) >= self.antal_punkter_i_spor:
            self.spor.pop(0)
        self.x = self.kendt_punkt_x+self.rx*self.tid
        self.y = self.kendt_punkt_y + self.ry*self.tid
        self.tid += delta_tid
    def tegn(self):
        arcade.draw_circle_filled(self.x, self.y, self.punktradius,self.farve)
        for punkt in self.spor:
            x, y = punkt
            # arcade.draw_circle_filled(x, y, self.sportykkelse,self.farve)
            arcade.draw_circle_filled(*punkt, self.sportykkelse,self.farve)

class Cirkel:
    def __init__(self, centrum, radius, vinkelhastighed, fase = 0,
                 starttid = 0.0,
                 punktradius = 4, farve = arcade.csscolor.BLUE,
                 sportykkelse = 2, antal_punkter_i_spor = 100):
        self.centrum_x, self.centrum_y = centrum
        self.x = self.centrum_x + radius*math.cos(vinkelhastighed*starttid+fase)
        self.y = self.centrum_y + radius*math.sin(vinkelhastighed*starttid+fase)
        self.radius = radius
        self.vinkelhastighed = vinkelhastighed
        self.fase = fase
        self.tid = starttid
        self.punktradius = punktradius
        self.farve = farve
        self.sportykkelse = sportykkelse
        self.antal_punkter_i_spor = antal_punkter_i_spor
        self.spor = list()
        self.grafpunkter = list()

    def opdater(self, delta_tid):
        self.spor.append((self.x, self.y))
        if len(self.spor) >= self.antal_punkter_i_spor:
            self.spor.pop(0)
        self.x = self.centrum_x + self.radius*math.cos(self.vinkelhastighed*self.tid+self.fase)
        self.y = self.centrum_y + self.radius*math.sin(self.vinkelhastighed*self.tid+self.fase)
        self.tid += delta_tid

    def tegn(self):
        arcade.draw_circle_filled(self.x, self.y, self.punktradius,self.farve)
        for punkt in self.spor:
            x, y = punkt
            # arcade.draw_circle_filled(x, y, self.sportykkelse, self.farve)
            arcade.draw_circle_filled(*punkt, self.sportykkelse, self.farve)

class RetLinjeVindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.BEIGE)

    def setup(self):
        self.linje = RetLinje((0,100),(100,10))
        self.tid = 0.0
        # self.cirkel = Cirkel((500, 400), 150,6)
        self.cirkel = Cirkel((self.linje.x, self.linje.y), 150,-6)

    def update(self, delta_tid):
        # self.tid += delta_tid
        self.linje.opdater(delta_tid)
        self.cirkel.centrum_x = self.linje.x
        self.cirkel.centrum_y = self.linje.y
        self.cirkel.opdater(delta_tid)

        # self.cirkel.opdater(delta_tid)
        # self.linje.kendt_punkt_x = self.cirkel.x
        # self.linje.kendt_punkt_y = self.cirkel.y
        # self.linje.opdater(delta_tid)

    def on_draw(self):
        self.clear()
        self.linje.tegn()
        self.cirkel.tegn()
        
def main():
    vindue = RetLinjeVindue(WIDTH, HEIGHT, "En ret linje med klasser")
    vindue.setup()

    arcade.run()

main()
