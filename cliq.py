import simplegui

class shapeAttributes:

class Circle:
    
        def __init__(self):
            self.radius = 50
            self.center_point = (100, 100)
            
class Character:
    
    def __init__(self):     
        self.circle_shape = Circle()
        self.shape_attributes = shapeAttributes()
         
    def draw_me(self, canvas):


        canvas.draw_circle(
            self.circle_shape.center_point,
            self.circle_shape.raius,
            self.shape_attributes.line_width,
            self.shape_attributes.line_color,
            self.shape_attributes.fill_color
            )
        

cliq = Character()



   

# Handler to draw on canvas
def draw(canvas):
    cliq.draw_me(canvas)
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
