# VIZ
This folder contains all the code required for visualising the Drone Simulation. The files in the folder are:
1. `body.py`: This implements the visualisation of the body of the drone. The body uses the Rotation matrix from the drone to visualise the attitude of the drone. The body has to be `attached_to` a Drone object in order to visualise it.

```python
# This is the drone Object
drone = Drone()

# This is the body object which is attached to the Drone to plot it
body = Body()
body.attach_to(drone)
```

2. `visualiser.py`: This implements the `Graphics` or the plot for visualising the drone. The Graphics object plot all the actors added to it.
```python
graphics = Graphics()

# This is the drone Object
drone = Drone()

graphics.add_actor(drone)
```
Multi Drone visualiser is also supported. All the drones that are to be visualised should be added to the Graphics object as actors
