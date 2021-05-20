import sys
import redis
unit = 'Kb'

port = 6379
host = '127.0.0.1'

for i in range(1,len(sys.argv),2):
    if sys.argv[i] == '-db':
        x = sys.argv[i + 1]

    if sys.argv[i] == '-units':
        unit = sys.argv[i + 1]
    
    if sys.argv[i] == '-p':
        port = sys.argv[i + 1]

    if sys.argv[i] == '-h':
        host = sys.argv[i + 1]


units = ['b','Kb','Mb','Gb']

m = units.index(unit)

r = redis.Redis(
            db = x,
            host = host,
            port = port
            )

key_list = sorted(r.scan_iter())
print('===================')
print('amount of every key ')
for key in key_list:   
    if key[0:12] == b'amount__of__':
        print(key[12:len(key)] + b'  :  ' + r.get(key))

print()
print(b'memory usage of keys ')
for key in key_list:   
    if not key[0:12] == b'amount__of__':
        print(key +  b'  :  ' + str(float(r.get(key)) / (1024 ** m)) + ' ' + units[m])

print('===================')

