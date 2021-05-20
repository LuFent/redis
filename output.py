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
            port = port,
        decode_responses=True
            )

key_list = sorted(r.scan_iter())
total_count = 0
print('===================')
print('amount of every key ')
for key in key_list:   
    if key[0:12] == 'amount__of__':
        print(key[12:len(key)] + ':  ' + r.get(key))
        total_count+=int(r.get(key))
print('===================')
print('Totla count: ' + str(total_count))
print('===================')


print()
print('memory usage of keys ')
total_size = 0
for key in key_list:   
    if not key[0:12] == 'amount__of__':
        key_str = str(key)
        val = float(r.get(key))
        print(key_str +  ':  ' + str(round(val / (1024 ** m), 1)) + ' ' + units[m])
        total_size+=int(r.get(key))

print('===================')
print('Totla size: ' + str(round(total_size / (1024 ** m), 1)) + ' ' + units[m])
print('===================')

