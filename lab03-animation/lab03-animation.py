import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Compass Rose"
# Open the window. Set the window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
# Set the background color
arcade.set_background_color(arcade.color.BRONZE)
# Clear screen and start render process

# --- Drawing Commands Will Go Here ---

def circunferencia(x, y, radius, grosor):
    arcade.draw_circle_outline(x, y, radius, arcade.color.BLACK, grosor)

circunferencia(400, 400, 330, 8)
circunferencia(400,400,280, 18)

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
def poly_blanco():
    arcade.draw_polygon_filled([[165, 635],
                                [400, 450],
                                [635, 635],
                                [450, 400],
                                [635, 165],
                                [400, 350],
                                [165, 165],
                                [350, 400]],
                               arcade.color.WHITE)
def on_draw(delta_time):
    arcade.start_render()

    circunferencia()




# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.schedule(on_draw, 1/60)
arcade.run()