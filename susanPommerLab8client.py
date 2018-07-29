##################################################################
# C21B Intermediate Python Programming: Assignment Lab 8 Client
# Name:   Susan Pommer
# Network Programming
#
# Description:  This program:
# Creates a connection-oriented client-server program
# Also see:  susanPommerLab8server.py
# Uses Python's socket module to create client/server socket objects
# Establish a network connection between a server and client
# Syncs run computer's hostname and port between client/server programs
# Sends a simple message from client to server
# Server replies to client message across the connection channel

# Server program shall print statement verifying connection to client
# Client program shall print statement echoing back message sent

# Date:  03/13/2018
##################################################################

# Import socket
import socket

# Get hostname of computer the program is running on
server = socket.gethostname()
# print(server) ## FOR TESTING
port = 80   # Connect via this port; need same for server

# Create a socket with TCP connection
# See Week 8 notes 28 - 29
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make request of server on socket
request = "Susan Pommer request sent from Host "+server+"\n\n"

# Try to connect to the server
s.connect((server, port))

# Send request -- need to encode as Python 3 uses bytestrings
s.send(request.encode())

# Buffer how much data downloaded at a time on response
data = s.recv(1024)

# Must decode bytestring response
data_decoded = data.decode()

# Print response from server
print('RESPONSE RECEIVED: ' + data_decoded)

# Close connection
s.close()

######################## OUTPUT ##################################

#"C:\Users\Susan Dog\venv\Scripts\python.exe" "C:/Pommer Files/CLASSES/FHC CS21B/susanPommerLab8client.py"
#RESPONSE RECEIVED: server's echo response to: Susan Pommer request sent from Host SusanDog-PC

#Process finished with exit code 0

#--------------------------------------------------------------------
