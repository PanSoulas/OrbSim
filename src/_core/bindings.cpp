#include "sgp4.hpp"
#include "coords.hpp"
#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

using namespace orbsim;
namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
    py::class_<TLEElements>(m, "TLEElements")
        .def(py::init<>())
        .def_readwrite("eccentricity", &TLEElements::eccentricity)
        .def_readwrite("mean_motion", &TLEElements::mean_motion)
        .def_readwrite("raan", &TLEElements::raan)
        .def_readwrite("arg_perigee", &TLEElements::arg_perigee)
        .def_readwrite("inclination", &TLEElements::inclination)
        .def_readwrite("mean_anomaly", &TLEElements::mean_anomaly)
        .def_readwrite("epoch_jd", &TLEElements::epoch_jd)
        .def_readwrite("bstar", &TLEElements::bstar);

    py::class_<StateVector>(m, "StateVector")
        .def(py::init<>())
        .def_readwrite("position_km", &StateVector::position_km)
        .def_readwrite("velocity_km_per_sec", &StateVector::velocity_km_per_sec);

    py::class_<ECEFVector>(m, "ECEFVector")
        .def(py::init<>())
        .def_readwrite("axis_x_km", &ECEFVector::axis_x_km)
        .def_readwrite("axis_y_km", &ECEFVector::axis_y_km)
        .def_readwrite("axis_z_km", &ECEFVector::axis_z_km);
    
    py::class_<Geographic>(m, "Geographic")
        .def(py::init<>())
        .def_readwrite("latitude_degrees", &Geographic::latitude_degrees)
        .def_readwrite("longitude_degrees", &Geographic::longitude_degrees)
        .def_readwrite("altitude_km", &Geographic::altitude_km);

    m.def("sgp4_propagate", &sgp4_propagate);
    m.def("eci_to_ecef", &eci_to_ecef);
    m.def("ecef_to_geographic", &ecef_to_geographic);
}
