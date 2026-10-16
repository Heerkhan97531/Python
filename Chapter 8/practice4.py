

file= open("report.txt", "a")
file.write(" \n i was perfect at my place and i a not claming that i was perfect " \
"\n just i am saying that i want to apolyjayze my mstakes from right to left of  my life  .")


# read entire fle
with open("new textfile.txt", "r") as f:
    line = f.read()
    print("read as a file: \n ",line)

# read line by line
with open("new textfile.txt", "r") as l:
    line1 = l.readline()
    line2 = l.readlines()  # using read all lines and show results in the form of list of string
    line3 = l.readline()  
    print("line1", line1)
    print("line2", line2) 
    print("line3", line3)