#!/bin/sh 

if [ -d ./build ]; then
        rm -r ./build 	
	mkdir ./build 
fi

cd ./build && cmake ../ && make 
