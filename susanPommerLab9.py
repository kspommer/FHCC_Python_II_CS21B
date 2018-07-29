
##################################################################
# C21B Assignment #9
# Name:   Susan Pommer
# Topic:  Network Programming -- ftblib
#
# If possible, I would like to use the extra assignment as
# some extra credit points to use against final exam score
# I have a busy work week coming and weekend conference/hackathon
# and will not have many cycles to study for the final
#
# Description: This program uses the ftplib module to:
#   Connect to a remote server: mozilla.org
#   Displays the server's welcome message
#   Print the current working directory
#   List the directory files of working directory
#   Selects and downloads a file to local drive

# Note:  https://www.ibiblio.org/
#   ibiblio.org is one of the
#   largest free information databases online.

# Date:  03/18/2018
##################################################################
# Import the Python ftplib module
from ftplib import FTP

# Main program
def main():
    # Create an ftplib.FTP class object
    ftp = FTP('ftp.ibiblio.org')

    # Login to the server; no authentication required
    ftp.login()

    # Client established a connection
    # Get and print the server welcome message
    print("Welcome:", ftp.getwelcome())

    # Print current working directory
    # pwd() command gets current working directory
    print("\nCurrent working directory:", ftp.pwd())

    # Obtain directory listing of the login directory
    directoryList = ftp.nlst()

    # Print each file
    # Assign last file as selected file to save to local files
    # Could also save file list into an array; select file by index
    # My program assumes there is at least one file
    # Could add try / except statement to catch when no files found
    print("\nDirectory Listing: ")
    for entry in directoryList:
        print(entry)
        selectedFile = entry

    # Call the method which saves the local file
    saveFile(ftp, selectedFile)

    # Close the connection and quit
    ftp.quit()

    # Print statement
    print("\n" + selectedFile + " has been saved to local files.")


#---------------- Method to save selected file to local drive ----------

def saveFile(ftp, selectedFile):
    # Assign selected file
    remoteFile = selectedFile

    # Open remote file for writing of remote file in binary mode
    localFile = open(remoteFile, 'wb')

    # Retrieve the remote file and save to local file
    # For other file types, need to use retrlines
    ftp.retrbinary('RETR ' + remoteFile, localFile.write)

    # Close the local file
    localFile.close()

#---------------- Run the program -----------------------------
main()



#----------------- Program Output -----------------------------

#"C:\Users\Susan Dog\venv\Scripts\python.exe" "C:/Pommer Files/CLASSES/FHC CS21B/susanPommerLab9.py"
#Welcome: 220 ProFTPD Server

#Current working directory: /

#Directory Listing:
#HEADER.images
#incoming
#HEADER.html
#pub
#unc
#README

#README has been saved to local files.

#Process finished with exit code 0