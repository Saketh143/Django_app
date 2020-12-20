# open a file
myfile = open("hello.txt", 'w')

# here myFile is object of class open
# hence , it has some methods and attributes
# lets use them

print("name :", myfile.name)  # using name attribute
print("opening mode:", myfile.mode)
print('is closed: ', myfile.closed)

"""write into file"""
myfile.write("i love python!")
myfile.close()

# append to a file
myfile = open("hello.txt", 'a')
myfile.write(' i also like C++')
myfile.close()

#read from a file
myfile=open('hello.txt','r+')
text=myfile.read(100)
print(text)