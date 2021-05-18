import sys
import redis
import collections


unints = ['b','Kb','Mb','Gb']

#counter = collections.Counter()
#mem_counter = collections.Counter()

def main(mask_list, n1,n2):
    r = redis.Redis(db = n1)    

    for key in r.scan_iter():

        r = redis.Redis(db = n1)

        is_special = 0

        mem = r.execute_command("MEMORY USAGE",key)

        for i in mask_list:
            if key[0:len(i)] ==  i:
                short_key = i
                is_special = 1

        if not is_special:
            if key[0].isdigit():
                short_key = key[0]

            else:
                short_key = ''
                for i in range(len(key)):
                    short_key += key[i]
                    if key[i + 1] == ':' and key[i + 2].isdigit():
                        break

        r = redis.Redis(db = n2)

        r.incr(short_key,mem)
        r.incr('amount__of__' + short_key ,1)

        #counter[short_key] += 1
        #mem_counter[short_key] += r.execute_command("MEMORY USAGE",key)
    print('analysis ended')

masks = []

r = redis.Redis(db = 0)

num_1 = 0
num_2 = 1

while 1:
    print('1 - Enter analyzed db number, default number = 0')
    print('2 - Enter db number, to wich the information will be written, default number = 1')
    print('3 - Enter new special mask')
    print('4 - start analysis')
    print('5 - output db')
    print('6 - exit')
    choose = input()
    if (choose == 1):
        num_1 = input()
        r = redis.Redis(db = num_1)

    if (choose == 2):
        num_2 = input()
        

    if (choose == 3):
        mask = raw_input()
        masks.append(mask)
        print('Mask added')
        print('Current special masks list: ')
        print(masks)
            
    if (choose == 4):
        main(masks,num_1,num_2)
    
    if(choose == 5):
        print('Enter db number to output')
        x = input()
        print('Enter Units')
        print('1 - baits')
        print('2 - Kbaits')
        print('3 - Mbaits')
        print('4 - Gbaits')
        m = input()
        m-= 1

        r = redis.Redis(db = x)
        key_list = sorted(r.scan_iter())
        print('===================')
        print('amount of every key ')
        for key in key_list:   
            if key[0:12] == 'amount__of__':
                print(key[12:len(key)] + '  :  ' + r.get(key))

        print('memory usage of keys ')
        for key in key_list:   
            if not key[0:12] == 'amount__of__':
                print(key +  '  :  ' + str(float(r.get(key)) / (1024 ** m)) + ' ' + unints[m])
        
        print('===================')

    if (choose == 6):
        break



#print(counter)
#print(mem_counter)