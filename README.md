# Drone_Sim [WIP]
A simple Drone dynamics simulation written in Python.

## Structure
The repository is divided into 3 main sub-modules:
1. `sim`: The files that simulate the Rigid Body Dynamics, Sensors etc. are here.
2. `viz`: The files that visualise the Drone Simulation are here.
3. `env`: A Simple GYM environment is implemented here.

## Installation Instructions
1. Clone the repository:
```bash
git clone git@github.com:SuhrudhSarathy/drone_sim.git 
```
2. Install using pip
```
cd drone_sim
pip install .
```
3. Alternatively, you can install it diretly using pip
```bash
python -m pip install git+<repository link>
```
- If the installation, doesn't work try updating the pip by running the following command
```bash
python -m pip install --upgrade pip
```
## Usage
A simple drone can be simulated using
```python
from drone_sim.sim import Drone
from drone_sim.sim.parameters import NULL_ROT
from drone_sim.viz import Body
from drone_sim.viz import Graphics
from drone_sim.sim import IMU

drone = Drone(x=0, y=0, z=2.5, enable_death=True)

body = Body()
imu = IMU()

body.attach_to(drone)
imu.attach_to(drone)

ui = Graphics()
ui.add_actor(drone)

omega = NULL_ROT

for t in range(1000):
   # Steps the simulation by setting Rotor Velocities
   drone.step([omega, omega, omega, omega])

   # Get the sensor data
   sensor_data = imu.sense()

   # Update the UI to display the simulation
   ui.update()
```
