# [[file:Praesentation.org::*Sammesatte bevægelser][Sammesatte bevægelser:1]]
# Dette er et eksempel på en sammensat animation af en cirkel på en ret linje som en vektorfunktion
# Animationen foregår vha biblioteket arcade
import arcade
import math

BREDDE = 800
HOEJDE = 600
SPORLAENGDE_LINJE = 200
SPORLAENGDE_CIRKEL = 200
FARVE_LINJE = arcade.csscolor.DARK_RED
FARVE_CIRKEL = arcade.csscolor.BLUE

# Genbrugt fra eksemplet med den rette linje
def ret_linje(tid, stationaert_punkt, retningsvektor):
    """Returnerer x- og y-koordinaterne til et punkt på en ret linje.
    Er implementeret på helt samme måde, som i matematik."""
    x_0, y_0 = stationaert_punkt
    r_x, r_y = retningsvektor
    # De to næste linjer er som taget fra matematikbogen
    x = x_0 + r_x * tid
    y = y_0 + r_y * tid
    return x, y

# Genbrugt fra eksemplet med cirklen
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
    # Først punkt for linjen
    x_linje,y_linje = ret_linje(tegn.tid, (0,500),(1,-0.5))
    # Tegner punktet på linjen
    arcade.draw_circle_filled(x_linje, y_linje, 5, FARVE_LINJE)
    # Fjerner det første punkt i sporet, hvis sporet er for langt
    if len(tegn.spor_linje) > SPORLAENGDE_LINJE:
        tegn.spor_linje.pop(0)
    # Tegner sporet  for linjen
    for punkt in tegn.spor_linje:
        arcade.draw_circle_filled(*punkt, 2, FARVE_LINJE)

    # Beregner punkt på cirklens periferi
    # Linjens punkt sættes til at være cirklens centrum
    x_cirkel,y_cirkel = cirkel(tegn.tid, (x_linje, y_linje), 100, 0.1, 0)
    # Tegner punktet på cirklens periferi
    arcade.draw_circle_filled(x_cirkel, y_cirkel, 5, FARVE_CIRKEL)
    # Fjerner det første punkt i sporet, hvis sporet er for langt
    if len(tegn.spor_cirkel) > SPORLAENGDE_CIRKEL:
        tegn.spor_cirkel.pop(0)
    # Tegner sporet 
    for punkt in tegn.spor_cirkel:
        arcade.draw_circle_filled(*punkt, 2, FARVE_CIRKEL)
    # Opdaterer tiden, hvis punktet for linjen er inden for vinduet
    if (x_linje >= 0 and x_linje <BREDDE) and (y_linje >= 0 and y_linje <= HOEJDE):
        # Tiden opdateres med 1 
        tegn.tid += delta_tid * 60 # Der er ganget med 60 for at få animationen til gå hurtigere.
        # Tilføjer det sidste nye punkt til sporet for linjen
        tegn.spor_linje.append((x_linje,y_linje))
        # Tilføjer det sidste nye punkt til sporet for cirklen
        tegn.spor_cirkel.append((x_cirkel, y_cirkel))
    # Stopper animationen, hvis punktet på linjen er uden for vinduet
    else:
        # Tiden holdes konstant, så animationen stopper
        tegn.tid = tegn.tid
        

def main():
    arcade.open_window(BREDDE, HOEJDE, "En cirkel")

    arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    tegn.tid = 0.0
    tegn.spor_linje = list()
    tegn.spor_cirkel = list()
    arcade.schedule(tegn, 1/60) # Funktionen tegn kaldes 60 gange i sekundet

    arcade.run()

main()
# Sammesatte bevægelser:1 ends here
