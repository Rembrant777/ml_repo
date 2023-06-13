## docker common commands 
### docker-compose up 

* setup all container that are describe in yaml file 
```
docker-compose up 
```

* backend setup all cntainers that are described in yaml file 
```
docker-compose up -d 
```

* not create new but setup all stoped containers 
```
docker-compose up --no-recreate -d
```

* only create single container that with name of test1
```
docker-compose -d test1
```

* stop all containers 
```
docker-compose stop
```

* start all container(not backend)
```
docker-compose start
```

* stop all containers and remove corresponding containers 
```
docker-compose down 
```
