file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'w')
file.write("Hi I am Penguin and I am one yr. old")
file.close()

file = open('Codingal.txt', 'a')
file.write("Hi I am Penguin and I am one yr. old")
file.close()