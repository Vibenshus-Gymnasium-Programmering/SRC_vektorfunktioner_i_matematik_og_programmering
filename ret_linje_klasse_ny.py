# [[file:Praesentation.org::*Den rette linje][Den rette linje:1]]
import arcade
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
        self.spor.append(self.punkt)
        if len(self.spor) >= self.sporlaengde:
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

class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    def setup(self):
        self.ret_linje = Ret_Linje((100, 50), (100, 50), arcade.csscolor.RED, 100)

    def update(self, delta_tid):
        self.ret_linje.opdater(delta_tid)

    def on_draw(self):
        self.clear()
        self.ret_linje.tegn()

def main():
    vindue = Vindue(BREDDE, HOEJDE, "Ret linje som klasse")
    vindue.setup()

    arcade.run()

main()
# Den rette linje:1 ends here
