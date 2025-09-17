of=open("updated.txt","w")
inf=open("Repeated.txt","r")
lines_sofar=set()
for i in inf:
    if i not in lines_sofar:
        of.write(i)
        lines_sofar.add(i)
of.close()
inf.close()