##################################################################
# C21B Intermediate Python Programming: Assignment Lab 8 Server
# Name:   Susan Pommer
# Topic:  Network Programming
# Description:  This program:
# Creates a connection-oriented client-server program
# Also see:  susanPommerLab8client.py
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

# Define server to connect to and port to connect through
# Must be same as client since not pinging a website
# Use arbitrary non-privileged port
# See Week 8 Notes, slide X for port options
server = socket.gethostname()
port = 80

# Create / spec a socket with TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to that socket
s.bind((server, port))

# Listen for requests
s.listen(1)

# Connect to request
conn, addr = s.accept()

# Print info when connected to confirm connection
print ('Connected by', addr)

# Loop to receive and reply to request data
while True:
    # Data is what we receive through the connection
    data = conn.recv(1024)
    # print(data)   ## FOR TESTING

    # Need to decode the data sent from the client into string
    # Add to the string to confirm that it is a response
    reply = ("server's echo response to: " + data.decode())

    if not data:
        break

    # Send response -- need to encode to send back
    conn.sendall(str.encode(reply))

    # Confirmation that message sent
    # print("Reply sent")  ## FOR TESTING

# Close connection to client
conn.close()

######################## OUTPUT ##################################

#"C:\Users\Susan Dog\venv\Scripts\python.exe" "C:/Pommer Files/CLASSES/FHC CS21B/susanPommerLab8server.py"
#Connected by ('192.168.1.82', 50190)

#Process finished with exit code 0

#-----------------------------------------------------------------



