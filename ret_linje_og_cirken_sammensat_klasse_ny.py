# [[file:Praesentation.org::*1. metode][1. metode:1]]
import arcade
import math
BREDDE = 800
HOEJDE = 600
SPORLAENGDE = 200

class Ret_Linje:
    def __init__(self, fast_punkt, retningsvektor, farve, sporlaengde = None):
        self.fast_punkt = fast_punkt
        self.retningsvektor = retningsvektor
        self.punkt = self.fast_punkt
        self.farve = farve
        self.sporlaengde = sporlaengde
        if self.sporlaengde:
            self.spor = list()

    def opdater(self, delta_tid):
        if self.sporlaengde:
            self.spor.append(self.punkt)
        if self.sporlaengde and len(self.spor) >= self.sporlaengde:
            self.spor.pop(0)
        
        x, y = self.punkt
        vx, vy = self.retningsvektor
        x += vx * delta_tid
        y += vy * delta_tid
        self.punkt = (x, y)

    def tegn(self):
        x, y = self.punkt
        arcade.draw_circle_filled(x, y, 5, self.farve)
        for punkt in self.spor:
            x, y = punkt
            arcade.draw_circle_filled(x, y, 2, self.farve)

class Cirkel:
    def __init__(self, centrum, radius, vinkelhastighed, vinkel, farve, sporlaengde = None):
        self.centrum = centrum
        self.radius = radius
        self.vinkelhastighed = vinkelhastighed
        self.vinkel = vinkel
        self.punkt = centrum[0] + self.radius * math.cos(self.vinkel), centrum[1] + self.radius * math.sin(self.vinkel)
        self.farve = farve
        self.sporlaengde = sporlaengde
        if self.sporlaengde:
            self.spor = list()

    def opdater(self, delta_tid):
        if self.sporlaengde:
            self.spor.append(self.punkt)
        if self.sporlaengde and len(self.spor) >= self.sporlaengde:
            self.spor.pop(0)
        
        self.vinkel += self.vinkelhastighed * delta_tid
        self.punkt = self.centrum[0] + self.radius * math.cos(self.vinkel), self.centrum[1] + self.radius * math.sin(self.vinkel)

    def tegn(self):
        x, y = self.punkt
        arcade.draw_circle_filled(x, y, 5, self.farve)
        for punkt in self.spor:
            x, y = punkt
            arcade.draw_circle_filled(x, y, 2, self.farve)

class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    def setup(self):
        self.ret_linje = Ret_Linje((50, 500), (20,-10), arcade.csscolor.YELLOW, 100)
        self.cirkel = Cirkel(self.ret_linje.punkt, 20, -5, 0, arcade.csscolor.GREEN, 100)

    def update(self, delta_tid):
        # Opdaterer cirklens centrum til at være linjens punkt
        self.cirkel.centrum = self.ret_linje.punkt
        self.ret_linje.opdater(delta_tid)
        self.cirkel.opdater(delta_tid)

    def on_draw(self):
        self.clear()
        self.cirkel.tegn()
        self.ret_linje.tegn()
def main():
    vindue = Vindue(BREDDE, HOEJDE, "Sammensat bevægelse af ret linje og cirkel")
    vindue.setup()

    arcade.run()

main()
# 1. metode:1 ends here
