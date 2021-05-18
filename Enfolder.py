import sys
import redis
from random import randint
import collections

r = redis.Redis(db = 0)

abc = [
'A','B','C'
]

#       **** Enfolding Database with random keys & values
for i in range(10):
    key = abc[randint(0,2)] + ':' + abc[randint(0,2)] + ':' + str(randint(0,1000)) 
    value = randint(0,100)
    r.set(key,value)
    
for i in range(5):
    key = str(randint(0,100)) + ':' +  str(randint(0,100))
    value = randint(0,100)
    r.set(key,value)

for i in range(5):
    key = 'email' + ':' + abc[randint(0,2)] + abc[randint(0,2)] + '@gmail.com'
    value = randint(0,100)
    r.set(key,value)

