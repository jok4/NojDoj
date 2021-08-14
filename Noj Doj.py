import pygame, time, sys

from random import randrange
import random 

pygame.init()

WIDTH= 700
HEIGHT= 400


show= pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('NOJ DOJ ( by Nnaemeka O.J)')


clock= pygame.time.Clock()

show.fill((255,255,255))

black= (0,0,0)
white= (255,255,255)

red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)

global score
score = 0

global continuegame
continuegame= True

global highscore
highscore = 28

global up_pressed
up_pressed = False


class board1:
    def __init__(self,x,y,dx= 0, dy= 0):
        self.x= x
        self.y= y
        self.dx= dx
        self.dy= dy
        self.sizex= 20
        self.sizey= 100

    def draw(self):
        pygame.draw.rect(show, blue, (self.x,self.y,self.sizex,self.sizey))
       

    #def glide_up(self):
     #   self.y-= self.dy

    #def glide_down(self):
    #    self.y+= self.dy
       
    def move(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        pressed = pygame.key.get_pressed()
        speed = 6
        if pressed[pygame.K_UP]: self.y -= speed
        if pressed[pygame.K_DOWN]: self.y += speed
        if pressed[pygame.K_w]: self.y -= speed
        if pressed[pygame.K_s]: self.y += speed
     
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT - self.sizey:
            self.y = HEIGHT - self.sizey    
            
           
            
    def getcenter(self):
        a= self.x + self.sizex/2
        b= self.y + self.sizey/2
        return a,b

    #def bounce(self, x, y):
     #   cx,cy = self.getcenter()
      #  if (((x-(cx))**2 + (y-(cy))**2)**0.5) < (self.sizex):
       #     return True
        #return False
       
    #def bounce1(self):
     #   x,y= ball.getcenter()
      #  if ball.bounce(x,y):
       #     ball.collide()

       
class board2:
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.sizex= 20
        self.sizey= 100

    def draw(self):
        pygame.draw.rect(show, blue, (self.x,self.y,self.sizex,self.sizey))
       
       
    def move(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('w'):
                    self.y -= 15
                elif event.key == pygame.K_LEFT or event.key == ord('s'):
                    self.y += 15

    def move2(self, ball):
        speedu= randrange(6,9)
        speedd= randrange(5,8)
        if ball.x > WIDTH/3:
            if ball.y > self.y :
                self.y+= speedd
            if ball.y < self.y + self.sizey/2:
                self.y-= speedu


        
        #if ball.x > WIDTH/3:
            #self.y = ball.y - randrange(1,7)


            
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT - self.sizey:
            self.y = HEIGHT - self.sizey
        #pygame.time.wait(1000)
        #self.y-= 1

    def getcenter(self):
        a= self.x + self.sizex/2
        b= self.y + self.sizey/2
        return a,b
 

       
 
class ball:
    def __init__(self, x,y,dx= -10, dy= random.choice((-5, 5))):
        self.x= x
        self.y= y
        self.dx= dx
        self.dy= dy
        self.size= 10
        self.color= green
        self.score= 0

    def move(self):
        self.x+=self.dx
        self.y+=self.dy

    def draw(self):
        p= (self.x,self.y)
        pygame.draw.circle(show, self.color, p, self.size)
   
    def collide(self):
       
        if self.y-self.size-5< 0 or self.y+self.size+5> HEIGHT:
            self.dy= -1*self.dy


    def getcenter(self):
        a= self.x + self.size/2
        b= self.y + self.size/2
        return a,b

           
    def bounce1(self, board1):
        if self.x +- self.size == board1.x + board1.sizex and self.y >= board1.y and self.y <= board1.y + board1.sizey:
            self.dx *= -1

    def bounce2(self, board2):
        if self.x + self.size == board2.x and self.y >= board2.y and self.y <= board2.y + board2.sizey:
            self.dx *= -1
       
    def isoutside(self):
        global score
        if self.x > WIDTH+100:
            self.x -= 200
            self.y = int(HEIGHT/2)
            pygame.time.wait(1000)
            self.dx *= -1
            self.dy *= -1
            score += 1

    def gameover(self):
        global continuegame
        if self.x < -10:  
            continuegame= False
         
    #def goal(self):


def drawscore():
        font= pygame.font.SysFont(None, 25)
        text= font.render("Score:" + str(score), True, black)
        show.blit(text, (0,10))











def rungame():
    global score
    score= 0
    global continuegame
    continuegame= True

    b= ball(WIDTH-200,randrange(10,HEIGHT-10))
    b1= board1(20,140)
    b2= board1(WIDTH-40,140)
   

    while continuegame:
        show.fill((255,255,200)) #pitch

        ball.draw(b)
        ball.move(b)
        ball.collide(b)
        ball.bounce1(b,b1)
        ball.bounce2(b,b2)
        ball.isoutside(b)
       

        board1.draw(b1)
        board1.move(b1)
       
        board2.draw(b2)
        #board2.move(b2) GET THIS TO WORK
        board2.move2(b2,b)


        drawscore()
       
        pygame.draw.line(show, green, (0,0), (WIDTH,0),8)

        pygame.draw.line(show, green, (0,HEIGHT-2), (WIDTH,HEIGHT-2),8)

        ball.gameover(b)





        pygame.display.update()
        clock.tick(55)



def gameover_display():
    global highscore
    f = open('Highscore.txt',  'a')
    f.truncate(0)
    if score > highscore:
        highscore = score
        font= pygame.font.SysFont(None, 75)
        text= font.render("Yeah! New Highscore!", True, black)
        show.blit(text, (int(WIDTH/14),int(HEIGHT/1.5)))
        pygame.display.update()
    pygame.time.wait(2000)

    f.write(str(highscore))
    f = open('Highscore.txt',  'r')
    hg= f.read()
   
    font= pygame.font.SysFont(None, 75)
    text= font.render("Game Over Fam", True, black)
    show.blit(text, (int(WIDTH/5),int(HEIGHT/3)))
    pygame.display.update()
    pygame.time.wait(2000)
           
    font= pygame.font.SysFont(None, 75)
    text= font.render("Highscore: "  + hg, True, black)
    show.blit(text, (int(WIDTH/4.5),int(HEIGHT/2)))
    pygame.display.update()
    pygame.time.wait(2000)


def main():
    while True:
        rungame()
        gameover_display()
       


main()

#Add sounds
#Let the game continue after some time
