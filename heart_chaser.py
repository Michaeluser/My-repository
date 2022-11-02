import random
import time
import pygame
import ptext
from pygame.locals import *
import multiprocessing
global posx_list, entities, score, f_c_x, f_c_y, fallen_cat
pygame.init()


clock = pygame.time.Clock()

score = 0

move_right = [ 
pygame.image.load("Images/R1.png"),
pygame.image.load("Images/R2.png"),
pygame.image.load("Images/R3.png"),
pygame.image.load("Images/R4.png"),
pygame.image.load("Images/R5.png"),
pygame.image.load("Images/R6.png"),
pygame.image.load("Images/R7.png"),
pygame.image.load("Images/R8.png"),
pygame.image.load("Images/R9.png")
]

move_left = [
pygame.image.load("Images/L1.png"), 
pygame.image.load("Images/L2.png"), 
pygame.image.load("Images/L3.png"),
pygame.image.load("Images/L4.png"),
pygame.image.load("Images/L5.png"),
pygame.image.load("Images/L6.png"),
pygame.image.load("Images/L7.png"),
pygame.image.load("Images/L8.png"),
pygame.image.load("Images/L9.png")
]

basket_anim = [
pygame.image.load("Images/Sprites/basket1.png"),
pygame.image.load("Images/Sprites/basket2.png"),
pygame.image.load("Images/Sprites/basket3.png"),
pygame.image.load("Images/Sprites/basket4.png"),
pygame.image.load("Images/Sprites/basket5.png"),
pygame.image.load("Images/Sprites/basket6.png"),
pygame.image.load("Images/Sprites/basket7.png"),
pygame.image.load("Images/Sprites/basket8.png"),
pygame.image.load("Images/Sprites/basket9.png")
]

menu_anim = [
pygame.image.load("Images/Backgrounds/menu1.png"),
pygame.image.load("Images/Backgrounds/menu2.png"),
pygame.image.load("Images/Backgrounds/menu3.png"),
pygame.image.load("Images/Backgrounds/menu4.png"),
pygame.image.load("Images/Backgrounds/menu5.png"),
pygame.image.load("Images/Backgrounds/menu6.png"),
pygame.image.load("Images/Backgrounds/menu7.png"),
pygame.image.load("Images/Backgrounds/menu8.png"),
pygame.image.load("Images/Backgrounds/menu9.png")
]
button_play = [
pygame.image.load("Images/Backgrounds/bp_def.png"), 
pygame.image.load("Images/Backgrounds/bp_hov.png"), 
pygame.image.load("Images/Backgrounds/bp_pres.png")
]

basket_stand = pygame.image.load("Images/Sprites/basket.png")
bg = pygame.image.load("Images/Backgrounds/bg1.png")
standing = pygame.image.load("Images/standing.png")
# rock = pygame.image.load("Images/rock.jpg")
class Window():
	def __init__(self, width, height):
		self.width = width
		self.height = height

class cat_catcher(object):
	def __init__(self, x, y, width, height, mc_width, mc_height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.left = False
		self.right = False
		self.walk_count = 0
		self.mc_width = mc_width
		self.mc_height = mc_height
		self.radius = 5
		self.hitbox = (self.x + 15, self.y + 10, 34, 60)
	def draw(self, screen):
		if self.walk_count + 1 >= 27:
			self.walk_count = 0
		if self.left:
			screen.blit(move_left[self.walk_count//3], (self.x, self.y))
			self.walk_count += 1
			self.hitbox = (self.x, self.y + 10, 64, 60)
		elif self.right:
			screen.blit(move_right[self.walk_count//3], (self.x, self.y))
			self.walk_count += 1
			self.hitbox = (self.x, self.y + 10, 64, 60)
		else:
			screen.blit(standing, (self.x, self.y))
			self.hitbox = (self.x + 15, self.y + 10, 34, 60)
		pygame.draw.circle(screen, (255, 0, 0), ((self.x + 32), (self.y + 10)), self.radius)
		pygame.draw.rect(screen, (255, 20, 10), self.hitbox, 2)
class fall_cat():
	def __init__(self, x, y, ent_width, ent_height):
		self.x = x
		self.y = y
		self.vel = 5
		self.ent_width = ent_width
		self.ent_height = ent_height
		self.hitbox = (self.x + 15, self.y + 10, 34, 60)

	def gen_ent(self, screen):
		screen.blit(basket_stand, (self.x, self.y))
		self.hitbox = (self.x + 15, self.y + 10, 34, 60)
		pygame.draw.rect(screen, (255, 20, 10), self.hitbox, 2)

	def gen_rock(self, screen):
		screen.blit(rock, (self.x, self.y))
		self.hitbox = (self.x + 15, self.y + 10, 34, 60)

	def catch(self):
		print("Caught times")
class Button():
	def __init__(self, x, y, image_def, image_hov):
		self.x = x
		self.y = y
		self.image_def = image_def
		self.image_hov = image_hov
		self.width = image_def.get_size()[0]
		self.height = image_def.get_size()[1]
	def init_button(self, mouse_pos):
		self.mouse_pos = mouse_pos
		self.events = pygame.event.get()
		if self.x < mouse_pos[0] < self.x + self.width:
			if self.y < mouse_pos[1] < self.y + self.height:
				for event in self.events:
					if event.type == pygame.MOUSEBUTTONDOWN:
						screen.blit(self.image_hov, (self.x, self.y))
		else:
			screen.blit(self.image_def, (self.x, self.y))
		pygame.display.update()




win = Window(640, 480)
main_cat = cat_catcher(250, 396, 640, 480, 64, 64)
button_start = Button(win.width/3 - 20, win.height* 0.2, button_play[0], button_play[1])
button_opt = Button(win.width/3 - 20, win.height* 0.2 + 50, button_play[0], button_play[1])
screen = pygame.display.set_mode((win.width, win.height))
pygame.display.set_caption("Cat catcher")
font = pygame.font.SysFont("Calibri", 60)
font_h = pygame.font.SysFont("Arial", 37)
font_t = pygame.font.SysFont("Arial", 20)
color = (255, 255, 255)
text_about = font_h.render("Authors", 1, color)
authors = """
Dana
Insta: @_danon_cheh_
Telegram: +380 97 442 13 72

Mike
Insta: @michael_chepara
Telegram: +380 68 183 41 14
"""
author_01 = font_h.render(authors[1:5], 1, color)
author_02 = font_t.render(authors[6:26], 1, color)
author_03 = font_t.render(authors[27:54], 1, color)
author_11 = font_h.render(authors[56:60], 1, color)
author_12 = font_t.render(authors[61:84], 1, color)
author_13 = font_t.render(authors[85:112], 1, color)
#fallen_cat = fall_cat(f_c_x, f_c_y, 64, 64)


# def shift(right, left):
# 	global x, y
# 	z = 0
# 	if right == True and left == False:
# 		while z < 20:	x
# 			z += 1
# 			x += 1
# 			screen.blit(move_right[0], (x, y))
# 	if right == False and left == True:
# 		while z < 20:
# 			z += 1
# 			x -= 1
# 			screen.blit(move_left[0], (x, y)) 
# 	pygame.display.update()

def drawScreen():
	screen.blit(bg, (0, 0))
	text = font.render(f"Score: {str(score)}", 1, (0,0,0))
	screen.blit(text, (20, 0))
	main_cat.draw(screen)
	for entity in entities:
		entity.gen_ent(screen)
	pygame.display.update()

entities = []

def play(entities):
	t_list = []
	posx_list = []
	[t_list.append(i) for i in range(0, round(win.width/32))]
	[posx_list.append(k*32) for k in t_list]

	run = 1
	#	fallen_cat = fall_cat(f_c_x, f_c_y, 64, 64)
	while run:
		clock.tick(27)
		f_c_x = random.choice(posx_list)
		f_c_y = random.randint(0, round((win.height)/5))

		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.QUIT()


		for entity in entities:
			if entity.y < win.height:
				entity.y += entity.vel
			else:
				entities.pop(entities.index(entity))

			# if main_cat.hitbox[1] < fallen_cat.hitbox[1] +  fallen_cat.hitbox[3] and main_cat.hitbox[1] + main_cat.hitbox[3] > fallen_cat.hitbox[1]:
			# 	if main_cat.hitbox[0] + main_cat.hitbox[3] > fallen_cat.hitbox[0] and main_cat.hit_box[0] < fallen_cat.hitbox[0] + fallen_cat.hitbox[3]:
			# 		score += 1
			# 		fallen_cat.catch(score)
		keys = pygame.key.get_pressed()

		if True:
			if len(entities) < 5:
				if f_c_x + 64 < win.width:
					entities.append(fall_cat(f_c_x, f_c_y, 64, 64))


		if keys[pygame.K_RIGHT] and main_cat.x + 64 < win.width:
			main_cat.x += main_cat.vel
			main_cat.right = True
			main_cat.left = False
			# if keys[pygame.K_SPACE]:
			# shift(right, left)

		elif keys[pygame.K_LEFT] and main_cat.x >= 0:
			main_cat.x -= main_cat.vel
			main_cat.right = False
			main_cat.left = True
			# shift(right, left)
		else:
			main_cat.right = False
			main_cat.left = False
			main_cat.walk_count = 0
		drawScreen()
	pygame.quit()
def change_background():
	b_i = 0
	while 1:
		b_i += 1
		if b_i == 9:
			b_i = 0
		screen.blit(menu_anim[b_i], (0,0))

		pygame.display.update()
def menu_mainloop():
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.QUIT()

anim_back = multiprocessing.Process(target = change_background)
process_menu_mainloop = multiprocessing.Process(target = menu_mainloop)
def menu(screen):
	anim_back.start()
	process_menu_mainloop.start()


def about(author_01, author_02, author_03, author_11, author_12, author_13, screen, text_about):
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.QUIT()
		screen.blit(text_about, ((win.width/2 - text_about.get_width()/2), win.height - 480))
		screen.blit(author_01, ((win.width/2 - author_01.get_width()/2), win.height - 410))
		screen.blit(author_02, ((win.width/2 - author_02.get_width()/2), win.height - 350))
		screen.blit(author_03, ((win.width/2 - author_03.get_width()/2), win.height - 310))
		screen.blit(author_11, ((win.width/2 - author_11.get_width()/2), win.height - 250))
		screen.blit(author_12, ((win.width/2 - author_12.get_width()/2), win.height - 210))
		screen.blit(author_13, ((win.width/2 - author_13.get_width()/2), win.height - 170))
		pygame.display.update()

play(entities)
# menu(screen)
# about(author_01, author_02, author_03, author_11, author_12, author_13, screen, text_about)
