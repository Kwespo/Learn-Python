inp = input("")
f = open("Files\example.txt" , "r+") #opens the file (r+ allows us to write in it too)
print(f.read()) #reads and print out the entire file

f.write(f"\n" + inp) #makes a new line and adds whatever the input was.

f.close()

