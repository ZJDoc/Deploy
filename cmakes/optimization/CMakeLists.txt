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