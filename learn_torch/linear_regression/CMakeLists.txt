cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(lr_app)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
add_executable(lr_app lr_app.cpp)
target_link_libraries(lr_app 
	/opt/pytorch/pytorch/build/lib/libtorch.so  
	/opt/pytorch/pytorch/build/lib/libc10.so
	/opt/pytorch/pytorch/build/lib/libbackend_with_compiler.so
	/opt/pytorch/pytorch/build/lib/libtorch_cpu.so
	/opt/pytorch/pytorch/build/lib/libtorch_global_deps.so)


target_include_directories(lr_app PRIVATE /opt/pytorch/pytorch/torch/include/torch/csrc/api/include)	
target_include_directories(lr_app PRIVATE /opt/pytorch/pytorch/torch/include )	

set_property(TARGET lr_app PROPERTY CXX_STANDARD 17)
