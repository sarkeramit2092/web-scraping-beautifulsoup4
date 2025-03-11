# f = open("D:\\Documents\\python\\test.txt")

#if file exist then "w" is for write mode.
#if file doesn't exist then use "x" for once.

#f = open("test.txt", "w")
#f.write("Amit become python developer in 2025.")

#if we want to append some lines insted of overwrite then use "a".

#f = open("test.txt", "a")
#f.write("\nI am a django expert!!")
#f.close()

# for only read use "r" mode.

#f = open("test.txt", "r")
#print(f.read())
#f.close()

f = open("test.txt", "r")
f_out = open("test2.txt","w")

for i in f:
  token = i.split(" ")
  #print(token)
  f_out.write("worldcount: "+ str(len(token)) + i)
  #print(len(token))

f.close()