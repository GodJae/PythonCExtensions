cmake_minimum_required(VERSION 3.7)
project(std)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        std-wrapper.cpp
        std.cpp
        std.h)

include_directories(${PYTHON_INCLUDE_DIRS})

add_executable(std ${SOURCE_FILES})
