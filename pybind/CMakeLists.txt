cmake_minimum_required(VERSION 3.7)
project(stdpy)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        stdpy.cpp
        std.h
        std.cpp
        )

include_directories(${PYTHON_INCLUDE_DIRS})

add_executable(stdpy ${SOURCE_FILES})
