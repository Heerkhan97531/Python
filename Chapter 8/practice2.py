# write a program to read a text from a given file certificate.txt and find wheteher it contan the world live.
try:
    file = open("certificate567.txt")
    print(file.read())
    fileofdata = file. lower()
    if "live" in fileofdata:
     print("yes, the words live is present in to it" , fileofdata)
    else:
        print("No")
except :
  print("file not exist.") 