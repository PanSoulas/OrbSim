#include "sgp4.hpp"
#include <cmath>

namespace orbsim{
    static constexpr double MU = 398600.4418 ; //Earth's gravitational parameter km^3/s^2
    static constexpr double RE = 6378.137 ;    //Earths's radius in km
    static constexpr double J2 = 1.082626e-3;  //J2 perturbation coefficient, dimensionless
    static constexpr double TWO_PI = 2.0 * 3.14159265358979323846;
    static constexpr double MIN_PER_DAY = 1440.0; //Minutes per day

    double mod2pi(double angle){
        double result = std::fmod(angle, TWO_PI);
        if (result < 0 )
        {
            result += TWO_PI;
        }
        return result;
    }

    double kepler(double mean_anomaly, double eccentricity){
        double eccentric_anomaly = mean_anomaly;
        for (int i = 0; i < 50; i++)
        {
            double delta = (eccentric_anomaly - eccentricity * std::sin(eccentric_anomaly) - mean_anomaly) / (1 - eccentricity * std::cos(eccentric_anomaly));
            eccentric_anomaly = eccentric_anomaly - delta;
            
            if (std::abs(delta) < 1e-12)
            {
                break;
            }        
        }
        return eccentric_anomaly;
    }
}