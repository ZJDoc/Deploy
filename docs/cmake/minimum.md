
# 最小实现

## 目标

创建可执行文件，打印`Hello World`

## 源文件

```
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

## CMakeList.txt

```
cmake_minimum_required(VERSION 3.16.0)
project(hello)

set(CMAKE_CXX_STANDARD 11)

add_executable(hello main.cpp)
```

## 目录结构

```
.
├── CMakeLists.txt
└── main.cpp
```

## 编译&运行

```
$ cmake .
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zj/CLionProjects/hello
$ make
Scanning dependencies of target hello
[ 50%] Building CXX object CMakeFiles/hello.dir/main.cpp.o
[100%] Linking CXX executable hello
[100%] Built target hello
$ ./hello 
Hello, World!
```