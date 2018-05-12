cmake_minimum_required(VERSION 3.7)
project(std)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        cpp-native/std-wrapper.cpp
        cpp-native/std.cpp
        cpp-native/std.h)

include_directories(${PYTHON_INCLUDE_DIRS})

add_executable(std ${SOURCE_FILES})
