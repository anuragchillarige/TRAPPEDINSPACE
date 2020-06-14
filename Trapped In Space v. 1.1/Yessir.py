import pygame
import random
import time

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((480,720))
pygame.display.set_caption("Trapped In Space v 1.0")

background = pygame.image.load("960x1440 background.jpg")

Standing = pygame.image.load('standing.png')

walkLeft = [pygame.image.load('Left1.png'), pygame.image.load('Left2.png'), pygame.image.load('Left3.png')]

walkRight = [pygame.image.load('Right1.png'), pygame.image.load('Right2.png'), pygame.image.load('Right3.png')]

asteriod = pygame.image.load('asteroid.png')

gameIcon = pygame.image.load('astronautfacehole.png')
pygame.display.set_icon(gameIcon)



class player():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 24	
		self.Standing = True
		self.left = False
		self.right = False
		self.walkCount = 0		
		self.hitbox = (self.x, self.y, self.width , self.height)
	def draw(self,win):
		if self.walkCount + 1 >= 10:
			self.walkCount = 0
		if not(self.standing):
			if self.left:
				win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
				self.walkCount += 1
			elif self.right:
				win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
				self.walkCount +=1
		else:
			if self.right:
				win.blit(walkRight[0], (self.x, self.y))
			else:
				win.blit(walkLeft[0], (self.x, self.y))

		self.hitbox = (self.x, self.y, self.width, self.height)
		#pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


def button(msg,x,y,w,h,ic,ac,action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
			pygame.draw.rect(win, ac, (x, y, w, h))
			if click[0] == 1 and action != None:
				if action == "play":
					mainLoop()
				elif action == "quit":
					pygame.quit()
					quit()
				elif action == "controls":
					howtoplay()
	else:
			pygame.draw.rect(win, ic, (x, y, w, h))
		
		
	font = pygame.font.SysFont('arial', 26)
	text = font.render(msg, 1, (0,0,0))
	win.blit(text, (100,365))


def startingScreen():
	start = True
	while start:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		win.fill((255,255,255))
		font = pygame.font.SysFont('mvboli', 55)
		smallfont = pygame.font.SysFont('mvboli', 13)
		text = font.render('Trapped In Space!', 1, (0,0,0))
		text2 = smallfont.render('Controls: Right arrow to move to the right, Left arrow to move to the left', 1, (0,0,0))
		win.blit(text, (0,160))
		win.blit(text2, (0, 250))
		
		button("Let's Start!", 100, 360, 100, 50, (0,255,0), (0,200,0), "play")
		button("Let's Start!", 280, 360, 100, 50, (255,0,0), (200,0,0), "quit")
		
		

		font = pygame.font.SysFont('arial', 26)
		text = font.render("Quit.", 1, (0,0,0))
		win.blit(text, (305,365))
		
		pygame.display.update()
		clock = pygame.time.Clock()
		clock.tick(40)


def howtoplay():
	win.fill((255,255,255))
	font = pygame.font.SysFont('mvboli', 50)
	text = font.render('Controls:Left Arrow: Move to the left Right Arrow: Move to the right', 1, (0,0,0))
	win.blit(text, (0,100))
	
	clock = pygame.time.Clock()
	clock.tick(40)
	pygame.display.update()



def spaceRocks(thingx, thingy, thingWidth, thingHeight, color):
	win.blit(asteriod, (thingx, thingy))
	asteroidHitbox = (thingx, thingy, thingWidth, thingHeight)
	#pygame.draw.rect(win, (255,0,0), asteroidHitbox, 2)


def died():
	
	while True:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		win.fill((1,1,1))
		font = pygame.font.SysFont('mvboli', 28)
		text = font.render('You Have Been Crushed By A Rock',1, (255,0,0))	
		text3 = font.render('ur bad lol', 1, (255,0,0))
		text2 = font.render('Your Score: ' + str(dodged), 1, (255,255,255))
		win.blit(text2, (0, 250))

		win.blit(text, (0, 100))
		
		
		button("Play Again", 100, 360, 100, 50, (0,255,0), (0,200,0), "play")
		button("", 280, 360, 100, 50, (255,0,0), (200,0,0), "quit")
	
		font = pygame.font.SysFont('arial', 26)
		text = font.render("Quit.", 1, (0,0,0))
		win.blit(text, (305,365))
		
		pygame.display.update()
		clock = pygame.time.Clock()
		clock.tick(40)

		



	
def things_dodged(count):
	font = pygame.font.SysFont('comicsansms', 17)
	text = font.render("Score : " + str(count), True, (255,255,255))
	win.blit(text, (0,0))





def mainLoop():
	
	global pause

	thing_startx = random.randrange(0,480)
	thing_starty = -10
	thing_speed = 25
	thing_width = 127
	thing_height = 95
	astroidHotbox = (thing_startx, thing_starty, thing_width, thing_height)

	global dodged
	dodged = 0

	
	


	astro = player(40, 550, 100, 200)

	

	run = True
	while run:
		clock = pygame.time.Clock()
		clock.tick(12)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT] and astro.x > astro.vel:
			astro.x -= astro.vel
			astro.left = True
			astro.right = False
			astro.standing = False


		elif keys[pygame.K_RIGHT] and astro.x < 480 - astro.width - astro.vel:
			astro.x += astro.vel
			astro.left = False
			astro.right = True
			astro.standing = False
		else:	
			astro.standing = True
			astro.walkCount = 0

		if keys[pygame.K_p]:
			pause = True
			paused()



		win.blit(background, (0,0))

		spaceRocks(thing_startx, thing_starty, thing_width, thing_height, (255,255,255))
		thing_starty += thing_speed

		
		things_dodged(dodged)
		
		rounds = 1

		if thing_starty > 720:
			
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,480)
			dodged += 1
			thing_speed += 1
		
				

			


		if astro.y < thing_starty + thing_height:
			

			if astro.x > thing_startx and astro.x < thing_startx + thing_width or astro.x + astro.width > thing_startx and astro.x + astro.width < thing_startx + thing_width:
				
				thingy = 0
				thingx = random.randrange(0,480)
				thing_speed = 20
				previousScores = open("ScoreLogs.txt", "a")
				previousScores.write("\nRound: " + str(dodged))
				
				rounds += 1
				print(rounds)
				


				died()

			
				



		astro.draw(win)

		pygame.display.update()


startingScreen()
mainLoop()
pygame.quit()
quit()
