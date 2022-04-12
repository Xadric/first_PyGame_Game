import pygame


pygame.init()
win = pygame.display.set_mode((500, 500))
walkRight = [pygame.image.load('sprites/pygame_right_1.png'), pygame.image.load('sprites/pygame_right_2.png'), pygame.image.load('sprites/pygame_right_3.png'), pygame.image.load('sprites/pygame_right_4.png'), pygame.image.load('sprites/pygame_right_5.png'), pygame.image.load('sprites/pygame_right_6.png')]

walkLeft = [pygame.image.load('sprites/pygame_left_1.png'), pygame.image.load('sprites/pygame_left_2.png'), pygame.image.load('sprites/pygame_left_3.png'), pygame.image.load('sprites/pygame_left_4.png'), pygame.image.load('sprites/pygame_left_5.png'), pygame.image.load('sprites/pygame_left_6.png')]

bg = pygame.image.load('sprites/pygame_bg.jpg')
playerStand = pygame.image.load('sprites/pygame_idle.png')
pygame.display.set_caption("CUBE")


clock = pygame.time.Clock()

x =50
y=400
widht = 60
height = 71
speed = 5

isJump=False
jumpCount=10

left=False
right=False
animCount=0

lastMove="right"

class snaryad():
    def __init__(self,x,y,radius,color,fasing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.fasing=fasing
        self.vel=8*fasing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)




def drawWindow():
    global animCount
    win.blit(bg,(0,0))
    if left:
        win.blit(walkLeft[animCount//5],(x,y))
        animCount+=1
    elif right:
        win.blit(walkRight[animCount//5],(x,y))
        animCount+=1
    else:
        win.blit(playerStand,(x,y))

    for bullet in bullets:
        bullet.draw(win)


    if animCount + 1>=30:
        animCount=0
    pygame.display.update()

run = True
bullets=[]
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    for bullet in  bullets:
        if bullet.x < 500 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys=pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove=="left":
            fasing=1
        else:
            fasing=-1
        if len(bullets)<=5:
            bullets.append(snaryad(round(x+widht//2),round(y+height//2),5,(255,0,0),fasing))

    if keys[pygame.K_a] and x>5:
        x-=speed
        left= True
        right=False
        lastMove='right'
    elif keys[pygame.K_d] and x<455:
        x+=speed
        left=False
        right=True
        lastMove='left'
    else:
        left=False
        right=False
        animCount=0
    if not(isJump):
        # if keys[pygame.K_w] and y>5:
        #     y-=speed
        # if keys[pygame.K_s]and y<435:
        #     y+=speed
        if keys[pygame.K_SPACE]:
            isJump=True

    else:
        if jumpCount>= -10:
            if jumpCount<0:
                y+=(jumpCount**2)/2
            else:
                y-=(jumpCount**2)/2
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10
    drawWindow()



pygame.quit()