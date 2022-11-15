import arcade

WIDTH = 800
HEIGHT = 600

def straight_line(time, a, b):
    x = time
    y = a*time + b
    return x, y

def on_draw(delta_time):
    arcade.start_render()
    x,y = straight_line(on_draw.time, 2, 3)
    arcade.draw_circle_filled(x, y, 5, arcade.csscolor.RED)
    # if len(on_draw.trace) > 200:
    #     on_draw.trace.pop(0)
    for point in on_draw.trace:
        arcade.draw_circle_filled(point[0], point[1], 3, arcade.csscolor.PINK)
    if (x >= 0 and x <WIDTH) and (y >= 0 and y <= HEIGHT):
        on_draw.time += 60*delta_time
        on_draw.trace.append((x,y))
    else:
        on_draw.time = on_draw.time
        

def main():
    arcade.open_window(WIDTH, HEIGHT, "En ret linje")

    arcade.set_background_color(arcade.csscolor.BEIGE)

    on_draw.time = 0
    on_draw.trace = list()
    arcade.schedule(on_draw, 1/60)

    arcade.run()

main()
