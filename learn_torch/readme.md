# torch 

[link](https://pytorch.org/cppdocs/installing.html)

## how to execute torch script on your mac 
* install pytorch 
```
brew install pytorch 
``` 

* install gdb, clang, cmake 
```
brew install gdb, clang, cmake 
```

* create a cpp file that invokes torch 
```
#include <torch/torch.h>
#include <iostream>

int main() {
  torch::Tensor tensor = torch::rand({2, 3});
  std::cout << tensor << std::endl;
  return 0; 
}
```

* create CMakeLists.txt file 
```
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
```
