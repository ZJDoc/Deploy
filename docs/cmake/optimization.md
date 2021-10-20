
# 结构优化

## 目标

分离源文件、中间编译文件和最后可执行文件

## CMakeLists.txt

指定安装路径和待安装的文件

```
cmake_minimum_required(VERSION 3.16)
project(hello)

set(CMAKE_CXX_STANDARD 11)

add_executable(hello main.cpp)

IF (NOT DEFINED ENV{CMAKE_INSTALL_PREFIX})
    MESSAGE(STATUS "CMAKE_INSTALL_PREFIX not defined")
    set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/install)
ENDIF()
MESSAGE(STATUS "output: ${CMAKE_INSTALL_PREFIX}")
install(TARGETS hello RUNTIME DESTINATION bin)
```

* 如果未设置环境变量`CMAKE_INSTALL_PREFIX`，那么设置安装文件夹为`install`；
* 编译完成后，将可执行文件`hello`放置到安装路径下的`bin`目录

## 脚本

编写`shell`脚本，完成所有编译操作

```
$ cat run.sh 
#!/bin/bash

set -eux

mkdir build

cd build/

cmake -DCMAKE_INSTALL_PREFIX=../install ..

make

make install

cd ..
```

## 目录结构

```
.
├── CMakeLists.txt
├── main.cpp
└── run.sh
```

## 编译&运行

```
$ bash run.sh 
+ mkdir build
+ cd build/
+ cmake -DCMAKE_INSTALL_PREFIX=../install ..
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
-- CMAKE_INSTALL_PREFIX not defined
-- output: /home/zj/CLionProjects/hello/install
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zj/CLionProjects/hello/build
+ make
Scanning dependencies of target hello
[ 50%] Building CXX object CMakeFiles/hello.dir/main.cpp.o
[100%] Linking CXX executable hello
[100%] Built target hello
+ make install
[100%] Built target hello
Install the project...
-- Install configuration: ""
-- Installing: /home/zj/CLionProjects/hello/install/bin/hello
+ cd ..
$ ./install/bin/hello 
Hello, World!
```