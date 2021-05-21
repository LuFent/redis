### Redis database analysator

## main.py

```
$ python main.py -db <db number> -db_rez <db to write rezult number> -h <host default - 127.0.0.1 > -p <port default - 6379> -mask <add special mask>
```  
Keys in any order

*For example, running:*


```    
$ python main.py -db 1 -db_rez 10 -h 127.0.0.1 -p 6379 -mask eml -mask qwe.zxc
````  


&nbsp; Will connect to Redis with params (db1,host = 127.0.0.1, port = 6379),write into db 10 amount and memory usage of keys of every type (from db 1), keys with masks "eml" and "qwe.zxc" will be written as separated types

&nbsp;

## output.py


```
$ python output.py -db <db number, = db_rez from main.py!!!> -units <units of information: b, Kb, Mb, Gb, default - Kb> -h <host, default - 127.0.0.1 > -p <port, default - 6379>
```
Keys in any order


For example running(after running main.py, db = db_rez from main.py!!!):

```  
$ python output.py -db 10 -units Mb -h 127.0.0.1 -p 6379
```

&nbsp; Will connect to Redis with params (db10,host = 127.0.0.1, port = 6379) and output 
Amount and memory usage(in Mb) of keys of every type from db1
