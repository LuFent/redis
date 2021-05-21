## main


***$ python main.py -db <db number> -db_rez <db to write rezult number> -h <host default - 127.0.0.1 > -p <port default - 6379> -mask <add special mask>
keys in any order***  

    
*for example, running:*

    
    
***$ python main.py -db 1 -db_rez 10 -h 127.0.0.1 -p 6379 -mask eml -mask qwe.zxc***    

Will connect to Redis with params (db1,host = 127.0.0.1, port = 6379),write into db 10
Amount and memory usage of keys of every type (from db 1), keys with masks "eml" and "qwe.zxc" will be written as seporated types


## output

$ python output.py -db <db number, = db_rez from main.py!!!> -units <units of information: b, Kb, Mb, Gb, default - Kb> -h <host, default - 127.0.0.1 > -p <port, default - 6379>
keys in any order

    for example 

running(after running main.py, db = db_rez from main.py!!!):
$ python output.py -db 10 -units Mb -h 127.0.0.1 -p 6379

Will connect to Redis with params (db10,host = 127.0.0.1, port = 6379) and output 
Amount and memory usage(in Mb) of keys of every type from db1
