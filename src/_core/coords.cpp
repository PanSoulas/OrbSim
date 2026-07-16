#include "coords.hpp"
#include <cmath>

namespace orbsim{
    static constexpr double RE = 6378.137 ;    //Earths's radius in km
    static constexpr double TWO_PI = 2.0 * 3.14159265358979323846;

    ECEFVector eci_to_ecef(const StateVector &state , double greenwich_sidereal_time){
        double x_eci = state.position_km[0];
        double y_eci = state.position_km[1];
        double z_eci = state.position_km[2];

        double x_ecef = x_eci * std::cos(greenwich_sidereal_time) + y_eci * std::sin(greenwich_sidereal_time);
        double y_ecef = -x_eci *std::sin(greenwich_sidereal_time) + y_eci * std::cos(greenwich_sidereal_time);
        double z_ecef = z_eci;

        return {x_ecef, y_ecef, z_ecef};
    }
    
    Geographic ecef_to_geographic(const ECEFVector &many_axis){
        double longitude = std::atan2(many_axis.axis_y_km, many_axis.axis_x_km);                           //angle around the equator
        double distance = std::sqrt(std::pow(many_axis.axis_x_km, 2) + std::pow(many_axis.axis_y_km, 2));   //distance from Earth's rotation axis
        double latitude = std::atan2(many_axis.axis_z_km, distance);                                        //angle above equator
        double altitude = std::sqrt(std::pow(many_axis.axis_x_km, 2) + std::pow(many_axis.axis_y_km, 2) + std::pow(many_axis.axis_z_km, 2)) - RE; // distance above Earth's surface
        
        double longitude_to_degrees = (longitude * 180) / (TWO_PI / 2.0);
        double latitude_to_degrees = (latitude * 180) / (TWO_PI / 2.0);

        return {latitude_to_degrees, longitude_to_degrees, altitude};
    }
}