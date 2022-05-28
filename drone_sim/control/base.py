"""File for base Controller
"""
from drone_sim.sim import Drone
class BaseController:
    """Base Controller Class"""
    def __init__(self, drone: Drone):
        self.drone = drone

    def cmd_vel(self)->list[float, float, float, float]:
        """
        Returns the instructed rotor velocities that can then
        used to step the drone.
        Returns: list[float, float, float, float]
        """
        raise NotImplementedError
    