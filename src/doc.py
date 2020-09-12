import operator
import math
def poll(lst):
	print lst
	p=[]
	l=[]
	for i in lst:
		l=filter(lambda x: ((abs(x[2]-i[2])<2) and(abs(x[3]-i[3])<2)and(abs(x[4]-i[4])<2)), lst)
		p.append((i[2],i[3],i[4],len(l)))
	p.sort(key=operator.itemgetter(-1))	
	return p[-1]
def yco_ord (a,b,n):
	i=0
	c=[]
	for x in a:
		if ((x[0]=='00')and(x[1]=='00')and(x[2]=='00')):
			c=b[i]
			c.append(n)
			b[i]=c
		i+=1
	
def continue1(b,a):
	print b,a
	n=len(b)
	m=len(a)	
	i=0
	j=0
	while i<m:
		while j<n:
			if ((abs(a[i][0]-b[j][0])<=5) and (abs(a[i][1]-b[j][1])<=5)):
				a.append(b[j])
				b.pop(j)
				j-=j
			j+=1
			n=len(b)
		j=0
		i+=1
		m=len(a)
	return a

def edge(a):
	i=0
	l=len(a)-2
	x=a[i]
	while i < l:
		y=a[i+1]
		z=a[i+2]
		if ((y-x),(z-y))==(1,1) :
			a.remove(y)
			l-=1
			i-=1
		x=y
		i+=1
	return a

def co_ord(lst):
	co=[]
	i=0
	for x in lst:
		if x[0]=='00':
			co.append(i)
		i+=1
	return co
 
dicty={}
dictx={}
with open('testimage10.ppm','r') as f:
	cn=f.readlines()
con=cn[3].encode('string-escape').split('\\x')
cont=[]

for x in con:
	cont.append(x.strip('('))
content=list(filter(None,cont))
dimention=cn[1].split(' ')
dimenx=dimention[0]
dimeny=dimention[1]
contents=[content[i:i+3] for i in range(0,len(content),3)]
final=[contents[i:i+int(dimenx)] for i in range(0,len(contents),int(dimenx))]
i=0
for x in final:
	c=co_ord(x)
	dictx[i]=(c)
	i+=1

for x in range (int(dimenx)):
	dicty[x]=[]
i=0	
for x in final:
	yco_ord(x,dicty,i)
	i+=1
def edging(d):
	j=0
	c=[]
	k=len(d)-1
	while j <= k:
		if (len(d[j])>1):
			c=edge(d[j])
			d[j]=c	
		j+=1
	return d
dictx=edging(dictx)

dicty=edging(dicty)
pict=[]
i=0

while  i< (len(dictx)-1):
	if len(dictx[i])>0:
		c=((j,i) for j in dictx[i])
		pict.extend(c)
	i+=1
i=0

while i< (len(dicty)-1):
	if len(dicty[i]):
		c=((i,j) for j in dicty[i])
		pict.extend(c)
	i+=1
pict =list(set(pict))
check=pict
figures=[]
while len(pict)>0:
	x=[pict[0]]
	print x
	pict.pop(0)
	print pict
	c=continue1(pict,x)
	print c
	figures.append(c)
	pict=[item for item in pict if item not in c]

print (len(figures))

