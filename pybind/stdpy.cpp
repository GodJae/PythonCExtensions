#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // Support for auto-conversion.

#include "std.h"

// If you don't include the std.cpp file in the build,
// an error occurs: `expected in: flat namespace`.
PYBIND11_MODULE(stdpy, m) {
    m.def("standard_dev", &standardDeviation);
}
