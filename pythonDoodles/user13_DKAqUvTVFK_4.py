import simplegui
# template for "Stopwatch: The Game"

# define global variables
t =0
a = 0
b = 0
c = 0
d = 0
x = 0
y = 0
interval = 100


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a
    global b
    global c
    global d
    a = t//600
    b = t//10%60//10
    c = t//10%10
    d = t%10
    return str(a) + ":" + str(b)+str(c) + ":" + str(d)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def b_reset():
    timer.stop()
    global x
    global y
    global t
    x = 0
    y = 0
    t = 0

def b_start():
    timer.start()

def b_stop():
    timer.stop()
    global x
    global y
    y = y +1    
    if d == 0:                
        x = x +1 
        
    


    
    
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t = t+ 1
#    print t
    

    
   
   
# define draw handler
def draw(canvas):
    canvas.draw_text(format(t),(100,110),30,"Red")
    canvas.draw_text(str(x)+"/"+str(y) ,(240,40),30,"Blue")
    
    
# create frame
f = simplegui.create_frame("Stopwatch: the game",300 , 200)


# register event handlers
b1 = f.add_button("Start",b_start,100)
b2 = f.add_button("Stop",b_stop,100)
b3 = f.add_button("Reset",b_reset,100)
timer = simplegui.create_timer(interval, tick)
f.set_draw_handler(draw)

# start frame
f.start()
# 0:00.0
# 0:01.1
# 0:32.1
# 1:01.3
#print format(0) 
#print format(11) 
#print format(321) 
#print format(613)  


# Please remember to review the grading rubric
