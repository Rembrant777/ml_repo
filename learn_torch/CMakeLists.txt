cmake_minimum_required(VERSION 3.0)
# project name
project(debugfunc)

# define path to the libtorch extracted folder
set(CMAKE_PREFIX_PATH /usr/local/lib/)


# find torch library and all necessary files
find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

# executable to add that we want to compile and run
add_executable(debugfunc main.cpp)
# link torch libraries to our executable
target_link_libraries(debugfunc "${TORCH_LIBRARIES}")
set_property(TARGET debugfunc PROPERTY CXX_STANDARD 14)
