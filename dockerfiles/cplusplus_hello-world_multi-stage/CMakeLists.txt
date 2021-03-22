cmake_minimum_required(VERSION 3.1)
project(multi)

set(CMAKE_CXX_FLAGS "-static ${CMAKE_CXX_FLAGS}")
set(CMAKE_CXX_STANDARD 11)

add_executable(app main.cpp test.cpp test.h)