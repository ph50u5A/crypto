import collections, sys
from math import log
import operator
 
def filecharcount(openfile):
    return sorted(collections.Counter(c for l in openfile for c in l).items())
      
f = open('4pphfawsh.txt')
books = filecharcount(f)
f.close()

tot = sum([b for a,b in books])    #total number of characters

dic2 = {a:log(1000*b/tot) for a,b in books}
dic3 = {a:float(format(log(1000*b/tot),'.3f')) for a,b in books}
print(dic3)
print()
ltup=sorted(dic3.items(),key=operator.itemgetter(1),reverse=True)
slst = ''.join([a for a,b in ltup])
print(slst.replace('\n',''),'\n\nLength = ',len(slst),'\nTotal =  ',tot)
