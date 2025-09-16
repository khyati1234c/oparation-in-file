f=open("sample.txt","w")
f.write("Hi.My name is Khyati Verma.\n" )
f.write("I am 10 years old\n")
f.write("I study in class 5\n")
f.close()

f=open("sample.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f=open("sample.txt","r")
l=f.readlines()
print(l)
for i in l:
    print(i.strip())
f.close()

f=open("sample.txt","r")
print(f.read(10))
f.close()

f=open("sample.txt","r")
text=f.read()
l=text.split()
print(l)
print("number of words in the file is",len(l))
f.close()