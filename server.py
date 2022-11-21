import random
from socket import *
import numpy as np

#connection
serverPort = 45000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(( "", serverPort))
print ("The server is ready to receive")

#creating  grid
row = 10
column = 10
multi = row*column
grid = np.zeros(multi,dtype=int).reshape((row,column))

def printGrid():
  print(grid)
  print()
  print()

#create some ships
def createVerticalShip():
  x = random.randint(1,row-1)
  y = random.randint(1,column-1)
  grid[x,y] = 1
  grid[x+1,y]= 1
  grid[x-1,y] = 1

def createHorizantalShip():
  x = random.randint(1,row-2)
  y = random.randint(1,column-2)
  grid[x,y] = 1
  grid[x,y+1]= 1
  grid[x,y-1] = 1

createHorizantalShip()
createVerticalShip()
createVerticalShip()
createHorizantalShip()

print(grid)

message,address = serverSocket.recvfrom(2048)
print(f"message {message.decode()}, from {address}")

def Pick(address):
  message,address2 = serverSocket.recvfrom(2048)
  serverSocket.sendto(f"Pick an X smaller than 10".encode(),address)
  x,address = serverSocket.recvfrom(1024)
  print(f"Picked x = {x.decode()}")

  serverSocket.sendto("Pick a Y smaller than 10".encode(),address)
  y,address = serverSocket.recvfrom(1024)
  print(f"Picked y = {y.decode()}")
  row = int(x)
  col = int(y)

  if(row >= 10 or col >= 10):
      serverSocket.sendto("X or Y cannot be bigger than 9\nTo pick again pick any number".encode(),address)
      Pick(address)

  elif(grid[row,col] == 1):
      serverSocket.sendto("Hit! You Won".encode(),address)
      serverSocket.close()
  else:
      serverSocket.sendto("Missed...\nTo pick again pick any number ".encode(),address)
      grid[row,col] = -1
      printGrid()
      Pick(address)



Pick(address)

