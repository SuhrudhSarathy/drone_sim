from drone_sim.sim import Drone
from drone_sim.control.base import BaseController
import numpy as np

class HoverController(BaseController):
    """Controller that brings the Drone to hovering mode"""
    def __init__(self, drone: Drone)->None:
        super(BaseController, self).__init__()
        self.drone = drone

    def cmd_vel(self) -> list[float, float, float, float]:
        return [0, 0, 0, 0]
