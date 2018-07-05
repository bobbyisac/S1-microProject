# Implementation of classic arcade game Pong
#import simplegui
import simpleguitk as simplegui
import signal,subprocess,os
#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random,os
import pygame,time
music=1
pygame.init()
pygame.mixer.music.load('3.mp3')
pygame.mixer.music.play(-1, 0.0)
#snd2 = pygame.mixer.Sound('2.mp3')
#snd2.play(-1, 0)

def playm():
	global music
	if music==1:
		pygame.init()
		pygame.mixer.music.load("3.mp3")
		#snd1 = pygame.mixer.Sound('1.mp3')
		#snd1.play()
		pygame.mixer.music.play(-1, 0.0)
		#time.sleep(0.1)
		
color="blue"
# initialize globals - pos and vel encode vertical info for paddles
global ball_pos, ball_vel
WIDTH = 1000
HEIGHT = 350
BALL_RADIUS = 8
PAD_WIDTH = 8
PAD_HEIGHT = 70
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
iterate = 0
score1 = "0"
score2 = "0"

os.system("clear")
p1=raw_input("Enter Player 1 Name:")
p2=raw_input("Enter Player 2 Name:")
score5 =raw_input("Winning Score? : ")

def stop():
	pid=os.getpid()
	os.kill(pid, signal.SIGINT)


# helper function that spawns a ball, returns a position vector and a velocity vector
def ball_init():
    global acc1, ball_pos, ball_vel, iterate
    ball_pos = [WIDTH/2, HEIGHT/2]
    if (iterate == 2):
        ball_vel = [random.randrange(1,7), random.randrange(1,7)]
    else:
        ball_vel = [-(random.randrange(1,6)), -(random.randrange(1,6))]
    acc1 = 1

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos,PAD_HEIGHT # these are floats
    global score1, score2,music# these are ints
    paddle1_pos = [0, HEIGHT/2]
    paddle2_pos = [WIDTH, HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    ball_pos = [WIDTH/2, HEIGHT/2]
    score1 = int(score1)
    score1 = 0
    score1 = str(score1)
    score2 = int(score2)
    score2 = 0
    score2 = str(score2)
    score5 = 5
    score5 = str(score5)
    PAD_HEIGHT = 70
    music=1
    

def draw(c):
    flag=0
    global acc1, score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, iterate, paddle2_vel, paddle1_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if (paddle2_pos[1] >= PAD_HEIGHT/80 and paddle2_pos[1] <= (HEIGHT - PAD_HEIGHT)):
        paddle2_pos[1] = paddle2_pos[1] - paddle2_vel
    elif (paddle2_pos[1] < PAD_HEIGHT/80):
        paddle2_pos[1] = paddle2_pos[1] + 1
    elif (paddle2_pos[1] > (HEIGHT - PAD_HEIGHT)):
        paddle2_pos[1] = paddle2_pos[1] - 1
        
    if (paddle1_pos[1] >= PAD_HEIGHT/80 and paddle1_pos[1] <= (HEIGHT - PAD_HEIGHT)):
        paddle1_pos[1] = paddle1_pos[1] - paddle1_vel
    elif (paddle1_pos[1] < PAD_HEIGHT/80):
        paddle1_pos[1] = paddle1_pos[1] + 1
    elif (paddle1_pos[1] > (HEIGHT - PAD_HEIGHT)):
        paddle1_pos[1] = paddle1_pos[1] - 1
        
    # draw mid line and gutters
    if flag!=1:
        c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
        c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
        c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line(paddle1_pos, ((paddle1_pos[0] + PAD_WIDTH), paddle1_pos[1]), 1, "White")
    c.draw_line(((paddle1_pos[0] + PAD_WIDTH/2), paddle1_pos[1]), ((paddle1_pos[0] + PAD_WIDTH/2), (paddle1_pos[1] + PAD_HEIGHT)), PAD_WIDTH, "White")
    c.draw_line(((paddle1_pos[0] + PAD_WIDTH), (paddle1_pos[1] + PAD_HEIGHT)), ((paddle1_pos[0] - PAD_WIDTH), (paddle1_pos[1] + PAD_HEIGHT)), 1, "White")
    c.draw_line(paddle2_pos, ((paddle2_pos[0] - PAD_WIDTH), paddle2_pos[1]), 1, "White")
    c.draw_line(((paddle2_pos[0] - PAD_WIDTH/2), paddle2_pos[1]), ((paddle2_pos[0] - PAD_WIDTH/2), (paddle2_pos[1] + PAD_HEIGHT)), PAD_WIDTH, "White")
    c.draw_line(((paddle2_pos[0] - PAD_WIDTH), (paddle2_pos[1] + PAD_HEIGHT)), (paddle2_pos[0], (paddle2_pos[1] + PAD_HEIGHT)), 1, "White")
    c.draw_line((paddle2_pos[0], (paddle2_pos[1] + PAD_HEIGHT)), paddle2_pos, 1, "White")
    
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    if ((ball_pos[0] + (2 * BALL_RADIUS)) >= WIDTH):
        score1 = int(score1)
        score1 += 1
        pygame.init()
        pygame.mixer.music.load("chomp.wav")
	#snd3 =  pygame.mixer.Sound('chomp.wav')
	#snd3.play()
        pygame.mixer.music.play()
        time.sleep(0.1)
        score1 = str(score1)
        iterate = 1
        ball_init()
    elif ((ball_pos[0] - (2 * BALL_RADIUS)) <= 0):
        score2 = int(score2)
        score2 += 1
        pygame.init()
        pygame.mixer.music.load("chomp.wav")
	#snd3 =  pygame.mixer.Sound('chomp.wav')
	#snd3.play()
        pygame.mixer.music.play()
        time.sleep(0.1)
        score2 = str(score2)
        iterate = 2
        ball_init()
    elif ((ball_pos[1] >= (paddle2_pos[1] - 5)) and (ball_pos[1] <= (paddle2_pos[1] + PAD_HEIGHT + 5)) and ((ball_pos[0] + (2 * BALL_RADIUS)) >= (WIDTH - PAD_WIDTH - 2))):
        ball_vel[0] += acc1
        ball_vel[0] = -(ball_vel[0])
    elif ((ball_pos[1] >= (paddle1_pos[1] - 5)) and (ball_pos[1] <= (paddle1_pos[1] + PAD_HEIGHT + 5)) and ((ball_pos[0] - (2 * BALL_RADIUS)) <= (PAD_WIDTH + 2))):
        ball_vel[0] -= acc1
        ball_vel[0] = -(ball_vel[0])

            
    if ((ball_pos[1] + (2 * BALL_RADIUS)) >= HEIGHT):
        ball_vel[1] = -(ball_vel[1])
    elif ((ball_pos[1] - (2 * BALL_RADIUS)) <= 0):
        ball_vel[1] = -(ball_vel[1])
    
    flag=0
    global music
    global p1,p2
    while int(score1)>=int(score5) or int(score2)>=int(score5):
        if (int(score1)>=int(score5)):
                c.draw_text(p1+" wins",((WIDTH/2)-150, HEIGHT/2), 24, "purple")
                #pygame.init()
                #pygame.mixer.music.load("WilhelmScream.wav")
                #pygame.mixer.music.play()
                #time.sleep(0.1)
                playm()
                music=0
                flag=1
                score1,score2=str(int(score5)+1),"0"                	
                break
        elif (int(score2)>=int(score5)):
                c.draw_text(p2+" wins",((WIDTH/2)-150, HEIGHT/2), 24, "orange")
                #pygame.init()
                #pygame.mixer.music.load("WilhelmScream.wav")
                #pygame.mixer.music.play()
                #time.sleep(0.1)
                playm()
                music=0
                flag=1	
                score1,score2="0",str(int(score5)+1)  	
                break
   


    if flag==1:
        global PAD_HEIGHT, HEIGHT
        PAD_HEIGHT = HEIGHT
        #c.draw_circle(ball_pos, BALL_RADIUS, 20,"Black")
        c.draw_text(score1,(250, 50), 24, "Black")
        c.draw_text(score2,(750, 50), 24, "Black")

        c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "Black")
        c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Black")
        c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Black")

    global color
    if score1==score2 and flag==0:
        color=random.choice(["green","red","blue"])
        #color="green"
    elif score1>score2 and flag==0:
        #color=random.choice(["red","yellow"])
        color="red" 
    elif score2>score1 and flag==0:
        #color=random.choice(["blue","green"]) 
        color="blue"
    
   
   
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 20,color)
    if flag!=1:
    		
    	c.draw_text(score1,(250, 50), 24, "Red")
    	c.draw_text(score2,(750, 50), 24, "Blue")
    
def keydown(key):
 
    acc = 10
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP["up"]):
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= acc
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= acc
 
def keyup(key):
    acc = 10
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
   
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)
#frame.add_button("Exit", stop, 100)

# start frame
while (score1<score5) or (score2<score5):
 init()
 ball_init()
 frame.start()
