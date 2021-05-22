import redis
import sys
from itertools import izip_longest

masks = []
port = 6379
host = '127.0.0.1'


for i in range(1,len(sys.argv),2):
    if sys.argv[i] == '-db':
        num_1 = sys.argv[i + 1]

    if sys.argv[i] == '-db_rez':
        num_2 = sys.argv[i + 1]
    
    if sys.argv[i] == '-p':
        port = sys.argv[i + 1]

    if sys.argv[i] == '-h':
        host = sys.argv[i + 1]

    if sys.argv[i] == '-mask':
        masks.append(sys.argv[i + 1])
    


r = redis.Redis(
        db = 5,
        host = host,
        port = port,
        decode_responses=True
        )

r_dst = redis.Redis(
        db = 10,
        host = host,
        port = port,
        decode_responses=True
                )

def batcher(x,n):
    args = [iter(x)] * n
    return izip_longest(*args)




for key in batcher(r.scan_iter(), 10):
    key = str(key)

    is_special = 0

    mem = r.execute_command("MEMORY USAGE",key)

    for i in mask_list:
        if key[0:len(i)] ==  i:
            short_key = i
            is_special = 1

    if not is_special:
        if key[0].isdigit():
            short_key = str(key[0])

        else:
            short_key = ''
            for i in range(len(key) - 2):
                short_key += key[i]
                if key[i + 1] == ':' and key[i + 2].isdigit():
                    break


    if (isinstance(short_key, str)):
        r_dst.incrby(short_key,mem)
        r_dst.incrby('amount__of__' + short_key ,1)

print('analysis ended')