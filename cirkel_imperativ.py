# [[file:Praesentation.org::*Cirklen][Cirklen:1]]
# Dette er et eksempel på en animation af en cirkel, som en vektorfunktion
# Animationen foregår vha biblioteket arcade
import arcade
import math

BREDDE = 800
HOEJDE = 600
SPORLAENGDE = 200
FARVE = arcade.csscolor.DARK_RED


def cirkel(tid, centrum, radius, vinkelhastighed, fase = 0):
    """Returnerer x- og y-koordinaterne til et punkt på periferien af en cirkel.
    Cirklen er defineret ud fra et centrum, en radius, en vinkelhastighed samt en fase.
    Er implementeret på helt samme måde, som i matematik."""
    x_c, y_c = centrum
    # De to næste linjer er som taget fra matematikbogen
    x = x_c + radius * math.cos(vinkelhastighed * tid + fase)
    y = y_c + radius * math.sin(vinkelhastighed * tid + fase)
    return x, y
    
# Denne funktion kaldes vha arcade.schedule i main. Bliver kaldt 60 gange i sekundet.
def tegn(delta_tid):
    arcade.start_render()
    # Beregner punkt på cirklens periferi
    x,y = cirkel(tegn.tid, (BREDDE/2, HOEJDE/2), 100, 1, 0)
    # Tegner punktet på cirklens periferi
    arcade.draw_circle_filled(x, y, 5, FARVE)
    # Fjerner det første punkt i sporet, hvis sporet er for langt
    if len(tegn.spor) > SPORLAENGDE:
        tegn.spor.pop(0)
    # Tegner sporet 
    for punkt in tegn.spor:
        arcade.draw_circle_filled(*punkt, 2, FARVE)
    # Opdaterer tiden
    tegn.tid += delta_tid 
    # Tilføjer det sidste nye punkt til sporet
    tegn.spor.append((x,y))
        

def main():
    arcade.open_window(BREDDE, HOEJDE, "En cirkel")

    arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    tegn.tid = 0.0
    tegn.spor = list()
    arcade.schedule(tegn, 1/60) # Funktionen tegn kaldes 60 gange i sekundet

    arcade.run()

main()
# Cirklen:1 ends here
