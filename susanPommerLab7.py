###########################################################
# Course:  CS21B Python Programming: Lab #7
# Name:  Susan Pommer
#
# Description:  This program creates a database using
# SQLite3.  Data is inserted and a series of data
# manipulations executed.

# File name:  susanPommerLab7.py
# Date:  March 6, 2018
###########################################################

# Import SQLite3
import sqlite3

## ----------------- MAIN PROGRAM -------------------------#
# Create a database
con = sqlite3.connect('pommer.db')

# Create cursor object responsible for executing SQL statements
cur = con.cursor()

# Create a table with 2 columns called PopByRegion
# Column one: Region contains names of regions (text)
# Column two: Population contains the region's population (integer)
cur.execute('CREATE TABLE PopByRegion(Region text,Population int)')

# Make three entries into the PopByRegion table
# Cursor class method execute takes SQL statement as string and executes
cur.execute('INSERT INTO PopByRegion VALUES ("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 110562)')

# Commit changes
con.commit()

# Close Connection
con.close()

## -------------------- STATEMENT SESSION  --------------------------- ##

# Execute the following statements against the database
# Copied from Assignment 7

#>>> import sqlite3

# NOTE -- I NEEDED TO EDIT THE FOLLOWING COMMAND FOR CORRECT FILE PATH
#>>> con = sqlite3.connect('C:\Pommer Files\CLASSES\FHC CS21B\pommer.db')

#>>> cur = con.cursor()
#>>> cur.execute('SELECT Region, Population FROM PopByRegion')
#>>> cur.fetchall()

#>>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER by Region')
#>>> cur.fetchall()

#>>> cur.execute('SELECT Region FROM PopByRegion')
#>>> cur.fetchall()

#>>> cur.execute ('SELECT Region FROM PopbyRegion WHERE Population > 400000')
#>>> cur.fetchall()

#>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
#>>> cur.fetchone()

#>>> cur.execute('''UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"''')
#>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
#>>> cur.fetchone()

#>>> cur.execute('DELETE FROM PopByRegion WHERE Region < "S"')
#>>> cur.execute('SELECT * FROM PopByRegion')
#>>> cur.fetchall()

#>>> cur.close()
#>>> con.close()

## ------------------ SAMPLE RUN -----------------------------------##

#Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)]
# on win32
#Type "help", "copyright", "credits" or "license" for more information.

#>>> import sqlite3
#>>> con=sqlite3.connect('C:\Pommer Files\CLASSES\FHC CS21B\pommer.db')
#>>> cur=con.cursor()
#>>>
#>>> cur.execute('SELECT Region, Population FROM PopByRegion')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.fetchall()
#[('Central Africa', 330993), ('Southeastern Africa', 743112), ('Japan', 110562)]
#>>>
#>>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER by Region')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.fetchall()
#('Central Africa', 330993), ('Japan', 110562), ('Southeastern Africa', 743112)]
#>>>
#>>> cur.execute('SELECT Region FROM PopByRegion')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.fetchall()
#[('Central Africa',), ('Southeastern Africa',), ('Japan',)]
#>>>
#>>> cur.execute('SELECT Region from PopByRegion WHERE Population >400000')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.fetchall()
#[('Southeastern Africa',)]
#>>>
# NOTE:  I ACCIDENTALLY TYPED cur.fetchall() FIRST
#>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.fetchall()
#[('Japan', 110562)]
#>>>
# NOTE:  HERE I TRIED AGAIN WITH cur.fetchone()
#>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.fetchone()
#('Japan', 110562)
#>>>
#>>> cur.execute('''UPDATE PopByRegion SET Population =100600 WHERE Region = "Jap
#an"''')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.fetchone()
#('Japan', 100600)
#>>>
#>>> cur.execute('DELETE FROM PopByRegion WHERE Region < "S"')
#<sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.execute('SELECT * FROM PopByRegion')
#sqlite3.Cursor object at 0x0000000002783EA0>
#>>> cur.fetchall()
#[('Southeastern Africa', 743112)]
#>>>
#>>> cur.close()
#>>> con.close()
#>>>

# --------------------------------------------------------------------------------#