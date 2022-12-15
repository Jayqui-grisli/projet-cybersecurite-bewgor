cmake_minimum_required(VERSION 3.4...3.18)
project(shuffler)

add_subdirectory(pybind11)
add_subdirectory(src/libshuffle)
pybind11_add_module(shufflerModule src/binder.cpp)    
target_link_libraries(shufflerModule PRIVATE myshuffler)

