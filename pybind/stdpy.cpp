#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // Support for auto-conversion.

#include <vector>
#include <numeric>
#include <iterator>
#include <cmath>

// When I've tried to separate this function to another file,
// an error has occurred `expected in: flat namespace`.
double standardDeviation(std::vector<double> v) {
    double sum = std::accumulate(v.begin(), v.end(), 0.0);
    double mean = sum / v.size();

    double squareSum = std::inner_product(v.begin(), v.end(), v.begin(), 0.0);
    return sqrt(squareSum / v.size() - mean * mean);
}


PYBIND11_MODULE(stdpy, m) {
    m.def("standard_dev", &standardDeviation);
}
