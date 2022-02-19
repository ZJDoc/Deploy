
# 条件编译

分两种情况：

1. 针对不同环境，在`CMakeLists.txt`中选择不同的配置选项；
2. 为`C++`程序预定义宏，在`C++`程序中执行不同程序。

*具体实现参考`cmakes/condition/`*

## CMake

在`CMakeLists.txt`文件中的基本语法如下：

```
if(<condition>)
  <commands>
elseif(<condition>) # optional block, can be repeated
  <commands>
else()              # optional block
  <commands>
endif()
```

可以预设变量（文件中或者外部设置）、使用条件表达式等等方式实现。

* 预设变量

```
set(CON1 OFF)

if (NOT CON1)
    MESSAGE(STATUS "con1 is ${CON1}")
endif ()
```

* 条件表达式

```
set(CON1 OFF)
set(CON2 "con2")

if (CON1)
    MESSAGE(STATUS "con1 is ${CON1}")
elseif (CON2 MATCHES "con2")
    MESSAGE(STATUS "con2 is ${CON2}")
endif ()
```

* 外部设置

在`CMakeLists.txt`中编写

```
if (CON3)
    MESSAGE(STATUS "con3 is ${CON3}")
endif ()
```

新建脚本`build.sh`，编写

```
#!/bin/bash

set -eux

BUILD_DIR=build/
if [[ ! -d "${BUILD_DIR}" ]]; then
  mkdir -p ${BUILD_DIR}
fi

cd ${BUILD_DIR}
cmake -DCON3=ON ../
make
./condition
```

执行

```
$ /bin/bash /home/zj/repos/Deploy/cmakes/condition/build.sh
+ BUILD_DIR=build/
+ [[ ! -d build/ ]]
+ cd build/
+ cmake -DCON3=ON ../
-- The C compiler identification is GNU 7.5.0
。。。
。。。
-- con3 is ON
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zj/repos/Deploy/cmakes/condition/build
+ make
Scanning dependencies of target condition
[ 50%] Building CXX object CMakeFiles/condition.dir/main.cpp.o
[100%] Linking CXX executable condition
[100%] Built target condition
+ ./condition
Hello, World!
```

## C++

`C++`也支持条件编译语法，可以在编译过程中设置宏常量，然后就可以在代码块中根据不同环境编译不同实现

```
#ifdef identifier 或者 #ifndef identifier
...
#elseif identifier
...
#else
...
#endif
```

`C++`代码如下：

```
// 条件一
#ifdef HAHA
    std::cout <<"Hello HAHA"<<std::endl;
#else
    std::cout << "Hello ..." << std::endl;
#endif
// 条件二
#ifdef AHAH
    std::cout << "Hello AHAH" << std::endl;
#endif
```

在`CMakeLists.txt`中使用语句`add_definition`进行宏定义

```
add_definitions(-DAHAH -DHAHA)
```

*上述命令类似于`g++ -DAHAH -DHAHA main.cpp`*

执行结果如下：

```
Hello HAHA
Hello AHAH
```

## 相关阅读

* [CMake if](https://cmake.org/cmake/help/latest/command/if.html)
* [#ifdef 和 #ifndef 指令 (C/c + +)](https://docs.microsoft.com/zh-cn/cpp/preprocessor/hash-ifdef-and-hash-ifndef-directives-c-cpp?view=msvc-170)
* [Microsoft C/C++ 编译器 预定义宏](https://docs.microsoft.com/zh-cn/cpp/preprocessor/predefined-macros?view=msvc-170)
* [add_definitions](https://cmake.org/cmake/help/v3.0/command/add_definitions.html)