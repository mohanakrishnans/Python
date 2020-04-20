# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:16:12 2020

@author: mohan
"""

#people_file = open("people.txt","x")

#people_file = open("people.txt","a")

# first write
#-------------
people_file = open("people.txt","w")
people_file.write('Bob\n')
people_file.write("Mary\n")
people_file.write("Sarah\n")
people_file.close()

# appending more data
# keeping the existing data
#---------------------------
people_file = open("people.txt","a")
people_file.write("\nBob_1\n")
people_file.write("Mary_1\n")
people_file.write("Sarah_1\n")
people_file.close()


people_file = open("people.txt","r")
print(people_file.read())


people_file = open("people.txt","r")
print(people_file.readline())
print(people_file.readline())
print(people_file.readline())


people_file = open("people.txt","r")
for person in people_file:
    print(person)
    
    
# to delete a file 
#---------------------    
import os 

f = open("file.txt","a")
f.close()

if os.path.exists('file.txt'):
    os.remove('file.txt')
    print("File Removed!!")
else:
    print('Thereis no such file')


# copy a file
#------------
from shutil import copyfile
copyfile('people.txt','another_file.txt')

# rename and move file 
#--------------------
from shutil import move
move('people.txt','another-file.txt')