cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(app)

#  export LD_LIBRARY_PATH=/opt/pytorch/pytorch/build/lib/
# export LIBRARY_PATH=/opt/pytorch/pytorch/build/lib/
# updated @2023/05/23 
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_C_FLAGS_DEBUG "-g")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")

# updated @2023/05/23 

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
add_executable(app app.cpp)
target_link_libraries(app 
	/opt/pytorch/pytorch/build/lib/libtorch.so  
	/opt/pytorch/pytorch/build/lib/libc10.so
	/opt/pytorch/pytorch/build/lib/libbackend_with_compiler.so
	/opt/pytorch/pytorch/build/lib/libtorch_cpu.so
	/opt/pytorch/pytorch/build/lib/libtorch_global_deps.so)


target_include_directories(app PRIVATE /opt/pytorch/pytorch/torch/include/torch/csrc/api/include)	
target_include_directories(app PRIVATE /opt/pytorch/pytorch/torch/include )	

set_property(TARGET app PROPERTY CXX_STANDARD 17)
