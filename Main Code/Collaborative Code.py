import arcade

arcade.open_window(800,800, "Cool Window that Does Stuff")
arcade.start_render()
arcade.set_background_color(arcade.csscolor.ORCHID)
def dog_body():
   #draw the dogs legs
  arcade.draw_polygon_filled(x y x y super cool xy arcade.csscolor.BEIGE)
  arcade.draw_polygon_filled(x y x y super cool xy arcade.csscolor.BEIGE)
  arcade.draw_polygon_filled(x y x y super cool xy arcade.csscolor.BEIGE)
  arcade.draw_polygon_filled(x y x y super cool xy arcade.csscolor.BEIGE)
  #draw dog tail
  arcade.draw_polygon_filled(x y x y super cool xy arcade.csscolor.BROWN)
  #draw the dog's body
  arcade.draw_rectangle_filled(x,y, blah blah arcade.csscolor.BEIGE)
  
def draw_eyes():
    arcade.draw_circle_filled(x y z arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x y z arcade.csscolor.BLACK)
def draw_eye_bags():
      # under eyes
    arcade.draw_circle_filled(x y z arcade.csscolor.LIGHTBROWN)
    arcade.draw_circle_filled(x y z arcade.csscolor.LIGHTBROWN)
def draw_ears():
    arcade.draw_triangle_filled(a b c d e f arcade.csscolor.BEIGE)
    arcade.draw_triangle_filled(a b c d e f  arcade.csscolor.BEIGE)
 

# drawing ground
arcade.draw_lrtb_rectangle_filled(0, 800, 225, 0, arcade.csscolor.PURPLE)

arcade.finish_render()
arcade.run()
