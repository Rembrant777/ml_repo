#!/bin/sh 

cd build/ 

if [ -f CMakeCache.txt ]; then 
    rm CMakeCache.txt && rm -r
fi 	

if [ -d ./CMakeFiles ]; then 
    rm -r ./CMakeFiles 

fi  

cmake ../ && make  
