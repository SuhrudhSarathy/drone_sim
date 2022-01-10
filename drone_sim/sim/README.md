# SIM
This folder contains python files for running the main math behind the actual Rigid Body Simulations. The files below are
1. `drone.py`: Simulates a Drone's Rigid Body Dynamics.
2. `parameters.py`: Contains all the parameters that are being used for simulation. These can be changed by the user, but the effect will be global. 
3. `sensors.py`: Simulate basic sensors such as GPS (`PositionTracker`) and IMU. Noise can be enabled to mimic real world sensor noise. All the sensors inherit the base `Sensor` class. A sensor needs to be `attached to` the drone:
```python
drone = Drone()

mysensor = Sensor() # Valid for other classes also (PositionTracker or IMU)
sensor.attach_to(drone)

data = sensor.sense() # This method can be called to get the data from the sensor

``` 

## References
1. https://andrew.gibiansky.com/downloads/pdf/Quadcopter%20Dynamics,%20Simulation,%20and%20Control.pdf
2. https://sal.aalto.fi/publications/pdf-files/eluu11_public.pdf

## Future Work
1. Simulate additional sensors (Altitude Sensors etc.)
2. Add obstacles and real time collision checking using Ray Casting (Simulate a 3D Lidar)
3. The simulation runs on simple Euler Integration and none of the ODE's are solved. Maybe solve the ODE's for more robust dynamics. (scipy.Integrate)
