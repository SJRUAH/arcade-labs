import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Open the window. Set the window title and dimensions

# Set the background color

# Clear screen and start render process

# --- Drawing Commands Will Go Here ---

def circunferencia(x, y, radius, grosor):
    arcade.draw_circle_outline(x, y, radius, arcade.color.BLACK, grosor)



def poly_negro():
    arcade.draw_polygon_filled([[400, 750],  # Vertice superior
                                [475, 450],
                                [750, 400],  # Vertice derecho
                                [475, 350],
                                [400, 50],  # Vertice inferior
                                [325, 350],
                                [50, 400],  # Vertice izquierdo
                                [325, 450]],
                               arcade.color.BLACK)
def poly_blanco(x,y):
    arcade.draw_polygon_filled([[x-470, y],
                                [x-235, y-185],
                                [x, y],
                                [x-185, y-235],
                                [x, y-470],
                                [x-235, y-285],
                                [x-470, y-470],
                                [x-285, y-235]],
                               arcade.color.WHITE)
def on_draw(delta_time):
    arcade.start_render()

    circunferencia(400, 400, 330, 8)
    circunferencia(400, 400, 280, 18)
    poly_blanco(on_draw.poly_blanco1, 635) #revisar esta linea y la siguiente
    poly_blanco(635, on_draw.poly_blanco2)
    on_draw.poly_blanco1 += 8
    on_draw.poly_blanco2 += 8
    poly_negro()

on_draw.poly_blanco1=635
on_draw.poly_blanco2=635

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Wind Rose")
    arcade.set_background_color(arcade.color.BRONZE)
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

main()


# Finish drawing and display the result


# Keep the window open until the user hits the 'close' button
