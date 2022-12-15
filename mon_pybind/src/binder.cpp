#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <shuffler.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)


namespace py = pybind11;

PYBIND11_MODULE(shufflerModule,m) {
    m.doc() = "allows to shuffle words in a word list";

    m.def("shuffle", &shuffle, "combines the words (strings) in the given array to get all the possible permutations with one word of each array constructiong a string of the size argument",
        py::arg("arrays"), py::arg("size"));

    m.def("hello", &hello, "says hello");

    m.def("mixedUpper", &mixedUpper, "generates a list of all the possible combinations of upper and lower character in a given word",
        py::arg("word"));
    
    m.attr("__version__") = "0.0.1";

}
