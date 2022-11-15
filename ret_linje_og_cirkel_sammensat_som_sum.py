# [[file:Praesentation.org::*2. metode][2. metode:1]]
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
        # Tidligere tegnede vi også sporet her. Nu er det flyttet til Vinduesklassen

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
        # Tidligere tegnede vi også sporet her. Nu er det flyttet til Vinduesklassen
        for punkt in self.spor:
            x, y = punkt
            arcade.draw_circle_filled(x, y, 2, self.farve)

class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    def setup(self):
        self.ret_linje = Ret_Linje((50, 500), (20,-10), arcade.csscolor.YELLOW)
        # Cirklen skal bare bevæge sig rundt om origo
        self.cirkel = Cirkel((0, 0), 20, -5, 0, arcade.csscolor.GREEN)
        self.samlet_spor = list()
        self.samlet_punkt = None
        self.samlet_sporlaengde = 100

    def update(self, delta_tid):
        # Opdaterer linje og cirkel hver for sig
        x_samlet = self.ret_linje.punkt[0] + self.cirkel.punkt[0]
        y_samlet = self.ret_linje.punkt[1] + self.cirkel.punkt[1]
        self.samlet_punkt = (x_samlet, y_samlet)
        self.samlet_spor.append(self.samlet_punkt)
        if len(self.samlet_spor) >= self.samlet_sporlaengde:
            self.samlet_spor.pop(0)
        self.ret_linje.opdater(delta_tid)
        self.cirkel.opdater(delta_tid)

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(*self.samlet_punkt, 5, arcade.csscolor.TOMATO)
        for punkt in self.samlet_spor:
            arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.TOMATO)

        
def main():
    vindue = Vindue(BREDDE, HOEJDE, "Sammensat bevægelse af ret linje og cirkel")
    vindue.setup()

    arcade.run()

main()
# 2. metode:1 ends here
