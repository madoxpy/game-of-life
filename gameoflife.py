import random
from pygame import                                                                                                    *

X = 50
Y = 30
size = 15
N = 200
colors = [(0,0,0),(255,0,0),(0,128,255),(255,128,0),(255,0,128),(128,255,0),(128,0,255),(0,255,0),(0,0,255)]

	
lifesurvive=[2,3] # 23/3 #12345/3 #2345/45678
deadres=[3]

init()
window=display.set_mode((size*X,size*Y+30))
clock=time.Clock()
Font=font.SysFont("arial",26)





def num_neigh(x,y,board):
	return board[(x-1+X)%X][y]+board[(x+1+X)%X][y]+board[(x-1+X)%X][(y-1+Y)%Y]+board[(x-1+X)%X][(y+1+Y)%Y]+board[(x+1+X)%X][(y-1+Y)%Y]+board[(x+1+X)%X][(y+1+Y)%Y]+board[x][(y-1+Y)%Y]+board[x][(y+1+Y)%Y]


def game(board):
	newboard=[]
	for i in range(X):
		tmp =[]
		for j in range(Y):
			tmp.append(board[i][j])
		newboard.append(tmp)

	for j in range(Y):
		for i in range(X):
			if newboard[i][j]==0:
				if num_neigh(i,j,newboard) in deadres:
					board[i][j]=1
			elif newboard[i][j]==1:
				if not num_neigh(i,j,newboard) in lifesurvive:
					board[i][j]=0

					
def newgame(board):				
	board = []
	for i in range(X):
		tmp =[]
		for j in range(Y):
			tmp.append(0)
		board.append(tmp)

	i=0
	while i<N:
		x = random.randint(0,X-1)
		y = random.randint(0,Y-1)
		if board[x][y]==0:
			board[x][y]=1
			i=i+1
	return board
		

def save(board):
	file=open("save.dat","w")
	for i in range(Y):
		line=""
		for j in range(X):
			line=line+str(board[j][i])
		file.write(line+"\n")
	
board = []		
board=newgame(board)		
end=False
pause=False

while not end:
	for z in event.get():
		if z.type==QUIT:
			end=True
		#if z.type == MOUSEBUTTONUP:
			
			
	keys = key.get_pressed()
	if keys[K_n]:
		board = newgame(board)
	if keys[K_a]:
		N= N+10
		board = newgame(board)
	if keys[K_z]:
		N = N-10
		board = newgame(board)
	if keys[K_p]:
		pause=not pause
	#if mouse.get_pressed()[0] == 1:
	if keys[K_SPACE]:
		x=mouse.get_pos()[0]/size
		y=mouse.get_pos()[1]/size
		board[x][y]=1
	if keys[K_r]:
		x=mouse.get_pos()[0]/size
		y=mouse.get_pos()[1]/size
		board[x][y]=0
	if keys[K_s]:
		save(board)
	if keys[K_i]:
		tosave = Surface( (size*X,size*Y) )
		tosave.blit(window,(0,0),(0,0,size*X,size*Y))
		image.save(tosave,"image.png")
		
		
	window.fill((0,0,0))
	
	for x in range(X):
		for y in range(Y):
			if board[x][y]==1:
				draw.rect(window,colors[num_neigh(x,y,board)],Rect(x*size,y*size,size-1,size-1))
				draw.rect(window,colors[0],Rect(x*size+1,y*size+1,size-3,size-3))
	text = Font.render("Board "+str(X)+"x"+str(Y)+", N = "+str(N),True,(255,255,255))
	window.blit(text,(20,Y*size+3))
	if not pause:
		game(board)

	clock.tick(20)
	display.flip()