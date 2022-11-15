# [[file:Praesentation.org::*Den rette linje][Den rette linje:1]]
# Dette er et eksempel på en animation af en ret linje, som en vektorfunktion
# Animationen foregår vha biblioteket arcade
import arcade

BREDDE = 800
HOEJDE = 600
SPORLAENGDE = 200
FARVE = arcade.csscolor.DARK_RED


def ret_linje(tid, stationaert_punkt, retningsvektor):
    """Returnerer x- og y-koordinaterne til et punkt på en ret linje.
    Er implementeret på helt samme måde, som i matematik."""
    x_0, y_0 = stationaert_punkt
    r_x, r_y = retningsvektor
    # De to næste linjer er som taget fra matematikbogen
    x = x_0 + r_x * tid
    y = y_0 + r_y * tid
    return x, y

# Denne funktion kaldes vha arcade.schedule i main. Bliver kaldt 60 gange i sekundet.
def tegn(delta_tid):
    arcade.start_render()
    # Beregner punkt på linjen
    x,y = ret_linje(tegn.tid, (0,500),(1,-0.5))
    # Tegner punktet på linjen
    arcade.draw_circle_filled(x, y, 5, FARVE)
    # Fjerner det første punkt i sporet, hvis sporet er for langt
    if len(tegn.spor) > SPORLAENGDE:
        tegn.spor.pop(0)
    # Tegner sporet 
    for punkt in tegn.spor:
        arcade.draw_circle_filled(*punkt, 2, FARVE)
    # Opdaterer tiden, hvis punktet er inden for vinduet
    if (x >= 0 and x <BREDDE) and (y >= 0 and y <= HOEJDE):
        # Tiden opdateres med 1 
        tegn.tid += delta_tid * 60
        # Tilføjer det sidste nye punkt til sporet
        tegn.spor.append((x,y))
    # Stopper animationen, hvis punktet på linjen er uden for vinduet
    else:
        # Tiden holdes konstant, så animationen stopper
        tegn.tid = tegn.tid
        

def main():
    arcade.open_window(BREDDE, HOEJDE, "En ret linje")

    arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    tegn.tid = 0
    tegn.spor = list()
    arcade.schedule(tegn, 1/60) # Funktionen tegn kaldes 60 gange i sekundet

    arcade.run()

main()
# Den rette linje:1 ends here
