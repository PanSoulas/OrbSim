#pragma once
#include <array>


namespace orbsim{ 
    struct TLEElements{
        double eccentricity;
        double mean_motion;                  
        double raan;           
        double arg_perigee;           
        double inclination;           
        double mean_anomaly;              
        double epoch_jd;     
        double bstar;          
    };
    
    struct StateVector{
        std::array<double, 3> position_km;
        std::array<double, 3> velocity_km_per_sec;
    };
}