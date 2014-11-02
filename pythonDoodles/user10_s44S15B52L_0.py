# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0
# Define "helper" functions
def increment():
    global counter
    counter = counter+1
    
# Define event handler functions
def reset():
    global counter
    counter = 0
    
def tick():
    increment()
    print counter
# Create a frame
frame = simplegui.create_frame("haha",200,200)
# Register event handlers
timer = simplegui.create_timer(1000,tick)
button1= frame.add_button("Click me!",reset )
# Start frame and timers
frame.start()
timer.start()