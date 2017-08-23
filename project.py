def remove_delimiters(delimiters,s):
    new_s = s
    for i in delimiters:
        new_s = new_s.replace(i,' ')
        r = ' '.join(new_s.split())
    print(r, end = "\n")
    return r

delimiters = [",", ".", "!", "?", "/", "&", "-", ":", ";", "@", "'", "..."]
f1=open('file1.txt','r')
x =' '.join([line.rstrip('\n') for line in f1])
f1 = remove_delimiters(delimiters,x)
f2=open('file2.txt','r')
y =' '.join([line.rstrip('\n') for line in f2])
f2 = remove_delimiters(delimiters,y)


def frequency(f1,f2):
    a=[]
    b=[]
    a=f1.split()
    b=f2.split()
    d1={}
    d2={}
    for i in a:
        d1[i]=a.count(i)
    for j in b:
        d1[j]=a.count(j)
    for k in a:
        d2[k]=b.count(k)
    for h in b:
        d2[h]=b.count(h)
    return(d1,d2)
d1,d2=frequency(f1,f2)
print(d1)
print(d2)

l1=d1.values()
l2=d2.values()
u=[]
v=[]
u=list(l1)
v=list(l2)
print(u)
print(v)
def dotproduct(u,v):
    m=len(u)
    n=len(v)
    c=0
    for o in range(m):
        c=c+(u[o]*v[o])
    return(c)
c=dotproduct(u,v)
print(c)

def euclid(u):
    s=0
    for f in range(len(u)):
        s=s+(u[f]**2)
    return(s)
s1=euclid(u)
print(s1)
s2=euclid(v)
print(s2)

def cosfunc(c):
    cosfunction=c/((s1**0.5)*(s2**0.5))
    return(cosfunction)

r1=cosfunc(c)
print(r1)
r2=r1*100
print(r2)

