#pragma once
#include "sgp4.hpp"

namespace orbsim{ 

    struct ECEFVector{
        double axis_x_km;
        double axis_y_km;
        double axis_z_km;
    };
    
    struct Geographic{
        double latitude_degrees;
        double longitude_degrees;
        double altitude_km;
    };


    ECEFVector eci_to_ecef(const StateVector &state , double greenwich_sidereal_time);
    Geographic ecef_to_geographic(const ECEFVector &many_axis);
}
    