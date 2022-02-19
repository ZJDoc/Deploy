cmake_minimum_required(VERSION 3.16)
project(condition)

set(CMAKE_CXX_STANDARD 11)

set(CON1 OFF)
set(CON2 "con2")

if (NOT CON1)
    MESSAGE(STATUS "con1 is ${CON1}")
endif ()

if (CON1)
    MESSAGE(STATUS "con1 is ${CON1}")
elseif (CON2 MATCHES "con2")
    MESSAGE(STATUS "con2 is ${CON2}")
endif ()

if (CON3)
    MESSAGE(STATUS "con3 is ${CON3}")
endif ()

add_definitions(-DAHAH -DHAHA)

add_executable(condition main.cpp)
