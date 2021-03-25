import arcade

arcade.open_window(800,800, "Cool Window that Does Stuff")
arcade.start_render()
arcade.set_background_color(arcade.csscolor.ORCHID)
# drawing ground
arcade.draw_lrtb_rectangle_filled(0, 800, 250, 0, arcade.csscolor.PURPLE)

arcade.finish_render()
arcade.run()
