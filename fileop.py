with open("JKV.txt","w") as f:
 f.write("Hi my name is khyati.\n")
 f.write("i am 10 years old\n")
 f.write("JKV is my family name\n")
with open("JKV.txt","r") as f:
 data=f.readlines()
 for i in data:
  word=i.split()
  print(word)