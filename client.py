from socket import *

port = 45000
host = '127.0.0.1'

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect((host,port))
message = "Connect"
sock.sendto(message.encode(),(host,port))
sock.sendto(message.encode(),(host,port))

while True:
  modifiedMessage,address = sock.recvfrom(2048)
  if(modifiedMessage.decode() == "Hit! You Won"):
      print(f"From server: {modifiedMessage.decode()}")
      print("Game Won")
      break

  print(f"From server: {modifiedMessage.decode()}")
  message = input("Pick: \n")
  sock.sendto(message.encode(),(host,port))

sock.close()
