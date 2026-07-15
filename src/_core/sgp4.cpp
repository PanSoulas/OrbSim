#include "sgp4.hpp"
#include <cmath>
#include <stdexcept>


namespace orbsim{
    static constexpr double MU = 398600.4418 ; //Earth's gravitational parameter km^3/s^2
    static constexpr double RE = 6378.137 ;    //Earths's radius in km
    static constexpr double J2 = 1.082626e-3;  //J2 perturbation coefficient, dimensionless
    static constexpr double TWO_PI = 2.0 * 3.14159265358979323846;
    static constexpr double MIN_PER_DAY = 1440.0; //Minutes per day
    static constexpr double KE = 7.436685316e-2;
    static constexpr double K2 = 0.5 * J2 * RE * RE; 

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

        StateVector sgp4_propagate(const TLEElements &element , double time_offset){
            if (element.eccentricity >= 1 || element.eccentricity < 0)
            {
                throw std::runtime_error("Eccentricity is out of bounds. It must belong to the domain [0,1) ! \n");
            }
            
            double semi_major_axis_a;
            double n = element.mean_motion;

            semi_major_axis_a = std::pow(KE/n , 2.0/3.0) * RE;

            double semi_latus_rectum_p; // The width of the orbit
            semi_latus_rectum_p = semi_major_axis_a * (1 - std::pow(element.eccentricity, 2));

            double cos_i = std::cos(element.inclination);

            double eta = std::sqrt(1 - std::pow(element.eccentricity, 2)); // how far the orbit is from circular

            double n_dot = n + (3.0 * K2 * n / (semi_latus_rectum_p * semi_latus_rectum_p)) * (1.5 * std::pow(cos_i, 2) - 0.5) * eta; // J2's effect on how fast a satellite moves

            double M = mod2pi(element.mean_anomaly + n_dot * time_offset); // mean anomaly at time
            double RAAN = mod2pi(element.raan);                            // RAAN at time
            double arguments_of_perigee = mod2pi(element.arg_perigee);     // Perigee at time


            double eccentric_anomaly = kepler(M, element.eccentricity);

            double cos_E = std::cos(eccentric_anomaly);
            double sin_E = std::sin(eccentric_anomaly);
            
            double nu = std::atan2(std::sqrt(1 - std::pow(element.eccentricity, 2)) * sin_E, cos_E - element.eccentricity); // true anomaly

            double radius_Earth = semi_major_axis_a * (1 - element.eccentricity * cos_E);

            // 2D coordinate system alligned with the orbit
            double x_pqw = radius_Earth * std::cos(nu);
            double y_pqw = radius_Earth * std::sin(nu);

            double h = std::sqrt(MU * semi_major_axis_a * (1 - std::pow(element.eccentricity, 2)) ); // angular momentum
            
            // velocity in perifocal frame
            double vx_pqw = -(MU / h) * std::sin(nu) / 60.0;
            double vy_pqw = (MU / h) * (element.eccentricity + std::cos(nu)) / 60.0;


            //ROTATING FROM THE PERIFOCAL FRAME INTO THE *ECI* FRAME
            
            double cos_o = std::cos(arguments_of_perigee);
            double sin_o = std::sin(arguments_of_perigee);

            double cos_R = std::cos(element.raan);
            double sin_R = std::sin(element.raan);

            double cos_I = std::cos(element.inclination);
            double sin_I = std::sin(element.inclination);

            double x = (cos_o * cos_R - sin_o * sin_R * cos_I) * x_pqw + (-sin_o * cos_R - cos_o * sin_R * cos_I) * y_pqw;
            double y = (cos_o * sin_R + sin_o * cos_R * cos_I) * x_pqw + (-sin_o * sin_R + cos_o * cos_R * cos_I) * y_pqw;
            double z = (sin_o * sin_I) * x_pqw + (cos_o * sin_I) * y_pqw;
            
            double vx = (cos_o * cos_R - sin_o * sin_R * cos_I) * vx_pqw + (-sin_o * cos_R - cos_o * sin_R * cos_I) * vy_pqw;
            double vy = (cos_o * sin_R + sin_o * cos_R * cos_I) * vx_pqw + (-sin_o * sin_R + cos_o * cos_R * cos_I) * vy_pqw;
            double vz = (sin_o * sin_I) * vx_pqw + (cos_o * sin_I) * vy_pqw;

            StateVector result;
            result.position_km = {x, y, z};
            result.velocity_km_per_sec = {vx, vy, vz};
            return result;
        }
}