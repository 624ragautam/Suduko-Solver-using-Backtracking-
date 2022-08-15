# import pygame library 
import pygame
import copy 

# initialise the pygame font 
pygame.font.init()

# Total window 
screen = pygame.display.set_mode((500, 600)) 

# Title  
pygame.display.set_caption("SUDOKU USING BACKTRACKING")  

x = 0
y = 0
dif = 500 /9
choice=0

# Default Sudoku Board. 
default_grid =[ 
		[7, 8, 0, 4, 0, 0, 1, 2, 0], 
		[6, 0, 0, 0, 7, 5, 0, 0, 9], 
		[0, 0, 0, 6, 0, 1, 0, 7, 8], 
		[0, 0, 7, 0, 4, 0, 2, 6, 0], 
		[0, 0, 1, 0, 5, 0, 9, 3, 0], 
		[9, 0, 4, 0, 6, 0, 0, 0, 5], 
		[0, 7, 0, 3, 0, 0, 0, 1, 2], 
		[1, 2, 0, 0, 0, 7, 4, 0, 0], 
		[0, 4, 9, 2, 0, 6, 0, 0, 7] 
	] 
grid=copy.deepcopy(default_grid)


# Load test fonts for future use 
font1 = pygame.font.SysFont("comicsans", 40) 
font2 = pygame.font.SysFont("comicsans", 20) 
def get_cord(pos): 
	global x 
	x = pos[0]//dif 
	global y 
	y = pos[1]//dif 

# Highlight the cell selected 
def draw_box():
	pygame.draw.line(screen, (250, 0, 0), (x * dif - 3, y * dif), (x * dif + (dif + 3) * (9 - x), y * dif), 5)
	pygame.draw.line(screen, (250, 0, 0), (0, y * dif), (x * dif - 3, y * dif), 5)
	pygame.draw.line(screen, (250, 0, 0), (x * dif - 3, (y + 1) * dif), (x * dif + (dif + 3) * (9 - x), (y + 1) * dif),
					 5)
	pygame.draw.line(screen, (250, 0, 0), (0, (y + 1) * dif), (x * dif - 3, (y + 1) * dif), 5)
	pygame.draw.line(screen, (250, 0, 0), (x * dif - 3, 9 * dif), (x * dif + dif + 3, 9 * dif), 5)
	pygame.draw.line(screen, (250, 0, 0), (x * dif - 3, 0), (x * dif + dif + 3, 0), 10)
	pygame.draw.line(screen, (250, 0, 0), (x * dif, y * dif), (x * dif, y * dif + (dif) * (9 - y)), 5)
	pygame.draw.line(screen, (250, 0, 0), (x * dif, 0), (x * dif, y * dif), 5)
	pygame.draw.line(screen, (250, 0, 0), ((x + 1) * dif, y * dif), ((x + 1) * dif, y * dif + (dif) * (9 - y)), 5)
	pygame.draw.line(screen, (250, 0, 0), ((x + 1) * dif, 0), ((x + 1) * dif, y * dif), 5)
	pygame.draw.line(screen, (250, 0, 0), (9 * dif, y * dif), (9 * dif, y * dif + dif), 10)
	pygame.draw.line(screen, (250, 0, 0), (0, y * dif), (0, y * dif + dif), 10)

	if ((x < 3) and (x >= 0)) and ((y < 3) and (y >= 0)):
		pygame.draw.line(screen, (250, 0, 0), (0, 0), (3 * dif, 0), 10)
		pygame.draw.line(screen, (250, 0, 0), (0, 3 * dif), (3 * dif, 3 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (0, 0), (0, 3 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 0), (3 * dif, 3 * dif), 5)
	if ((x < 3) and (x >= 0)) and ((y < 6) and (y >= 3)):
		pygame.draw.line(screen, (250, 0, 0), (0, 3 * dif), (3 * dif, 3 * dif), 10)
		pygame.draw.line(screen, (250, 0, 0), (0, 6 * dif), (3 * dif, 6 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (0, 3 * dif), (0, 6 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 3 * dif), (3 * dif, 6 * dif), 5)
	if ((x < 3) and (x >= 0)) and ((y < 9) and (y >= 6)):
		pygame.draw.line(screen, (250, 0, 0), (0, 6 * dif), (3 * dif, 6 * dif), 10)
		pygame.draw.line(screen, (250, 0, 0), (0, 9 * dif), (3 * dif, 9 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (0, 6 * dif), (0, 9 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 6 * dif), (3 * dif, 9 * dif), 5)
	if ((x < 6) and (x >= 3)) and ((y < 3) and (y >= 0)):
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 0), (6 * dif, 0), 10)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 3 * dif), (6 * dif, 3 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 0), (3 * dif, 3 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 0), (6 * dif, 3 * dif), 5)
	if ((x < 6) and (x >= 3)) and ((y < 6) and (y >= 3)):
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 3 * dif), (6 * dif, 3 * dif), 10)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 6 * dif), (6 * dif, 6 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 3 * dif), (3 * dif, 6 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 3 * dif), (6 * dif, 6 * dif), 5)

	if ((x < 6) and (x >= 3)) and ((y < 9) and (y >= 6)):
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 6 * dif), (6 * dif, 6 * dif), 10)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 9 * dif), (6 * dif, 9 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (3 * dif, 6 * dif), (3 * dif, 9 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 6 * dif), (6 * dif, 9 * dif), 5)
	if ((x < 9) and (x >= 6)) and ((y < 3) and (y >= 0)):
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 0), (9 * dif, 0), 10)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 3 * dif), (9 * dif, 3 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 0), (6 * dif, 3 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (9 * dif, 0), (9 * dif, 3 * dif), 5)
	if ((x < 9) and (x >= 6)) and ((y < 6) and (y >= 3)):
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 3 * dif), (9 * dif, 3 * dif), 10)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 6 * dif), (9 * dif, 6 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 3 * dif), (6 * dif, 6 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (9 * dif, 3 * dif), (9 * dif, 6 * dif), 5)
	if ((x < 9) and (x >= 6)) and ((y < 9) and (y >= 6)):
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 6 * dif), (9 * dif, 6 * dif), 10)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 9 * dif), (9 * dif, 9 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (6 * dif, 6 * dif), (6 * dif, 9 * dif), 5)
		pygame.draw.line(screen, (250, 0, 0), (9 * dif, 6 * dif), (9 * dif, 9 * dif), 5)


# Function to draw required lines for making Sudoku grid		 
def draw(): 
	# Draw the lines 
		
	for i in range (9): 
		for j in range (9): 
			if grid[i][j]!= 0:
				# Fill color in numbers of the default grid
				if grid[i][j]==default_grid[i][j]:
					pygame.draw.rect(screen, (127,127,127), (i * dif, j * dif, dif+1 , dif+1))
				
			
				# Fill grid with default numbers specified 
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif+20 , j * dif+15))
 
	# Draw lines horizontally and vertically to form grid		 
	for i in range(10): 
		if i % 3 == 0 : 
			thick = 7
		else: 
			thick = 2
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


# Fill value entered in cell	 
def draw_val(choice): 
	
		text2 = font1.render(str(choice), 1, (0, 0, 0)) 
		screen.blit(text2, (x * dif + 20, y * dif + 15))
			  
   
def raise_error1(): 
	text1 = font2.render("WRONG!!", 1, (0, 0, 0)) 
	screen.blit(text1, (20, 580))	

def correct_choice(): 
	text1 = font1.render("Right choice! Continue!", 1, (0, 0, 0)) 
	screen.blit(text1, (20, 570)) 	

# Check if the value entered in board is valid 
def valid(m, i, j, val): 
    for it in range(9): 
        if m[i][it]== val: 
            return False
        if m[it][j]== val: 
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3): 
        for j in range (jt * 3, jt * 3 + 3): 
            if m[i][j]== val: 
                return False
    return True

# Solves the sudoku board using Backtracking Algorithm 
def solve(grid, i, j): 
      
    while grid[i][j]!= 0: 
        if i<8: 
            i+= 1
        elif i == 8 and j<8: 
            i = 0
            j+= 1

        elif i == 8 and j == 8: 
            return True
    pygame.event.pump()     
    for it in range(1, 10): 
        if valid(grid, i, j, it)== True: 
            grid[i][j]= it 
            global x, y 
            x = i 
            y = j 
            # white color background 
            screen.fill((255, 255, 255)) 
            draw() 
            draw_box() 
            pygame.display.update() 
            pygame.time.delay(2)
            if solve(grid, i, j)== 1: 
                return True
            else: 
                grid[i][j]= 0
            # white color background 
            screen.fill((255, 255, 255))
 
            draw() 
            draw_box() 
            pygame.display.update() 
            pygame.time.delay(2)
    return False  

# Display instruction for the game 
def instruction():
	text1 = font2.render("Enter values", 1, (0, 0, 0)) 
	screen.blit(text1, (15, 520))
	text2=	font2.render("Click 'Enter' to visualise,'D' to set to default grid,'A' to see the Answer grid",1,(0,0,0))
	screen.blit(text2, (15, 540))

def raise_error2(): 
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (255, 0, 0)) 
    screen.blit(text1, (20, 570))
   
def solution():
	text1 = font2.render("ANSWER GRID", 1, (0, 0, 0)) 
	screen.blit(text1, (200, 580))

run = True
flag1=0
flag2=0
error=0
rs=0
flag3=0
sl=0

# The loop thats keep the window running 
while run: 
	
	# White color background 
	screen.fill((255,255, 255))
	# Loop through the events stored in event.get() 
	for event in pygame.event.get(): 
		# Quit the game window 
		if event.type == pygame.QUIT: 
			run = False
		# Get the mouse postion to insert number	 
		if event.type == pygame.MOUSEBUTTONDOWN: 
			flag1 = 1
			pos = pygame.mouse.get_pos() 
			get_cord(pos) 
		# Get the number to be inserted if key pressed	 
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_LEFT: 
				x-= 1
				flag1 = 1
			if event.key == pygame.K_RIGHT: 
				x+= 1
				flag1 = 1
			if event.key == pygame.K_UP: 
				y-= 1
				flag1 = 1
			if event.key == pygame.K_DOWN: 
				y+= 1
				flag1 = 1
			if event.key == pygame.K_1:
				choice = 1
			if event.key == pygame.K_2: 
				choice = 2	
			if event.key == pygame.K_3: 
				choice = 3
			if event.key == pygame.K_4: 
				choice = 4
			if event.key == pygame.K_5:
				choice = 5
			if event.key == pygame.K_6: 
				choice = 6
			if event.key == pygame.K_7: 
				choice = 7
			if event.key == pygame.K_8: 
				choice = 8
			if event.key == pygame.K_9:
				choice = 9
			if event.key == pygame.K_RETURN:
				flag2=1
			if event.key == pygame.K_a:
				flag3=1	
			if event.key == pygame.K_DELETE:
				if grid[int(x)][int(y)]==default_grid[int(x)][int(y)]:
					choice=0
				else:
					choice=10
 	
			# If D is pressed reset the board to default 
			if event.key == pygame.K_d: 
				rs = 0
				error = 0
				flag2 = 0
				grid=[ 
				[7, 8, 0, 4, 0, 0, 1, 2, 0], 
				[6, 0, 0, 0, 7, 5, 0, 0, 9], 
				[0, 0, 0, 6, 0, 1, 0, 7, 8], 
				[0, 0, 7, 0, 4, 0, 2, 6, 0], 
				[0, 0, 1, 0, 5, 0, 9, 3, 0], 
				[9, 0, 4, 0, 6, 0, 0, 0, 5], 
				[0, 7, 0, 3, 0, 0, 0, 1, 2], 
				[1, 2, 0, 0, 0, 7, 4, 0, 0], 
				[0, 4, 9, 2, 0, 6, 0, 0, 7] 
			] 
	
	if flag2 == 1: 
		if solve(grid,0,0)==False:
			error=1
			rs=0
		else:
			grid=[ 
				[7, 8, 0, 4, 0, 0, 1, 2, 0], 


			[6, 0, 0, 0, 7, 5, 0, 0, 9],
				[0, 0, 0, 6, 0, 1, 0, 7, 8], 
				[0, 0, 7, 0, 4, 0, 2, 6, 0], 
				[0, 0, 1, 0, 5, 0, 9, 3, 0], 
				[9, 0, 4, 0, 6, 0, 0, 0, 5], 
				[0, 7, 0, 3, 0, 0, 0, 1, 2], 
				[1, 2, 0, 0, 0, 7, 4, 0, 0], 
				[0, 4, 9, 2, 0, 6, 0, 0, 7] 
			      ]
			rs = 1
			error=0
			
		flag2=0
		

	if flag3==1:
		grid=[ 
				[7, 8, 0, 4, 0, 0, 1, 2, 0], 
				[6, 0, 0, 0, 7, 5, 0, 0, 9], 
				[0, 0, 0, 6, 0, 1, 0, 7, 8], 
				[0, 0, 7, 0, 4, 0, 2, 6, 0], 
				[0, 0, 1, 0, 5, 0, 9, 3, 0], 
				[9, 0, 4, 0, 6, 0, 0, 0, 5], 
				[0, 7, 0, 3, 0, 0, 0, 1, 2], 
				[1, 2, 0, 0, 0, 7, 4, 0, 0], 
				[0, 4, 9, 2, 0, 6, 0, 0, 7] 
			      ]
		if solve(grid,0,0)==True:
			sl=1
			rs=0
			error=0
			flag3=0
			

	if choice!= 0: 
		draw_val(choice) 
		if choice in [1,2,3,4,5,6,7,8,9]: 
			grid[int(x)][int(y)]= choice
			flag1=0

		else:
			grid[int(x)][int(y)]= 0
			raise_error2()	
		choice=0

	if  error== 1: 
		raise_error1()

	if rs == 1: 
		correct_choice()
		
	if sl==1:
		solution()	  
	draw()
	if flag1 == 1: 
		draw_box()	 	 
	instruction() 
	# Update window 
	pygame.display.update() 

# Quit pygame window	 
pygame.quit()	 
	
