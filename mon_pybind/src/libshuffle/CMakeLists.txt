cmake_minimum_required(VERSION 3.4...3.18)

project(libshuffle)

set(SRCS
	shuffler.cpp
	)
	
set(HEADERS
	shuffler.h
	)

add_library(myshuffler ${SRCS} ${HEADERS})
target_include_directories(myshuffler PUBLIC .)
set_target_properties(myshuffler PROPERTIES POSITION_INDEPENDENT_CODE ON)
