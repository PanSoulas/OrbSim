pybind11_add_module(_core
    sgp4.cpp
    coords.cpp
    bindings.cpp
)

target_compile_options(_core PRIVATE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-O3 -march=native -ffast-math>
    $<$<CXX_COMPILER_ID:MSVC>:/O2>
)

install(TARGETS _core DESTINATION orbsim)
