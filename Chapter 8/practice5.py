#read only the first line of the bio.txt/ new textfile.txt file
file= open ("new textfile.txt", "r")
line1= file.readline()
print(line1)
file.close()

with open("new textfile.txt", "r") as f:
    print("line 1:",f.readline())


# to remove file 
import os
os.remove("report.txt")
file.close()

   