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
  arcade.draw_triangle_filled(250,400,250,430,180,450, arcade.csscolor.BEIGE)

 #draw the dog's body
  arcade.draw_rectangle_filled(400, 400, 300, 150, arcade.csscolor.SIENNA)
  
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
 def draw_mouth():
   arcade.draw_arc_filled(400, 380, 50, -75, arcade.csscolor.MEDIUM_VIOLET_RED, 0, 180)
# drawing ground
arcade.draw_lrtb_rectangle_filled(0, 800, 225, 0, arcade.csscolor.PURPLE)

arcade.finish_render()
arcade.run()
