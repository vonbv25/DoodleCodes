
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [WIDTH/60, HEIGHT/60]
score1 = 0
score2 = 0
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
right = random.choice([True, False])
countdown = 3


# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    random_vel= [random.randrange(120, 240)/60,random.randrange(60, 180)/60]
#    random_vel = [random.randrange(300,500) / 60,-random.randrange(60,180) / 60]
    if right == False:
        ball_vel[0] = -random_vel[0]
        
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [ random.choice( [-random_vel[0],random_vel[0]] ),random.choice([random_vel[1],-random_vel[1]]) ]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(right)
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    frame.set_draw_handler(draw)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    #for paddle 1
    if paddle1_pos-HALF_PAD_HEIGHT < 0:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos+HALF_PAD_HEIGHT > HEIGHT-1:
        paddle1_pos = (HEIGHT-1)- HALF_PAD_HEIGHT
    #for paddle 1   
    if paddle2_pos-HALF_PAD_HEIGHT < 0:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos+HALF_PAD_HEIGHT > HEIGHT-1:
        paddle2_pos = (HEIGHT-1)- HALF_PAD_HEIGHT
            
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 2, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 2, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 2, "White")
    
    # draw paddles
    #player 1 paddle
    c.draw_line([WIDTH-1, (paddle1_pos-HALF_PAD_HEIGHT)],[WIDTH-1, (paddle1_pos+HALF_PAD_HEIGHT)], PAD_WIDTH, "White")
    #player 2 paddle
    c.draw_line([0, (paddle2_pos-HALF_PAD_HEIGHT)],[0, (paddle2_pos+HALF_PAD_HEIGHT)], PAD_WIDTH, "White")

    # update ball
    global ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] =-ball_vel[1]
    elif ball_pos[1] >= ((HEIGHT-1) - BALL_RADIUS):
        ball_vel[1] =-ball_vel[1]
            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    c.draw_text(str(score2),(200,100),40,"WHITE","serif")
    c.draw_text(str(score1),(400,100),40,"WHITE","serif")
    #Updates the speed of the ball per bounce-back by 10%
    #collision for the player 1 paddle    
    if ball_pos[0] >= ((WIDTH- 1) - BALL_RADIUS):
        if ball_pos[1] >= (paddle1_pos-HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle1_pos+HALF_PAD_HEIGHT):
            #Updates the speed of the ball per bounce-back by 10%
            ball_vel[0] =-(ball_vel[0] + ball_vel[0]*0.10)
        else:
            ball_init(right)
            score2+=1
    #collision for the player 2 paddle 
    if ball_pos[0] <= 0 + BALL_RADIUS:
        if ball_pos[1] >= (paddle2_pos-HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos+HALF_PAD_HEIGHT):
            #Updates the speed of the ball per bounce-back by 10%
            ball_vel[0] =-(ball_vel[0] + ball_vel[0]*0.10)
        else:
            ball_init(right)
            score1+=1
        
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel += 15
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel -= 15
        
    if key==simplegui.KEY_MAP["S"]:
        paddle2_vel += 15
    elif key==simplegui.KEY_MAP["W"]:
        paddle2_vel -= 15
        


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel =0
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel =0
        
    if key==simplegui.KEY_MAP["S"]:
        paddle2_vel =0
    elif key==simplegui.KEY_MAP["W"]:
        paddle2_vel =0


    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button("New Game", new_game)

# start game
#new_game()
# start frame
frame.start()

