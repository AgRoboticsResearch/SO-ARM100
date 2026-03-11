#!/usr/bin/env python3
"""
Visualize SO101 robot with new gripper - ALL MESHES
"""

import placo
import numpy as np
import pinocchio
from ischedule import schedule, run_loop
from placo_utils.visualization import robot_viz, robot_frame_viz

URDF_PATH = "/home/hls/SO-ARM100/Simulation/SO101/so101_new_gripper_test.urdf"

print("=" * 50)
print("SO101 with New Gripper - Full Visualization")
print("=" * 50)

# Load robot
robot = placo.RobotWrapper(URDF_PATH, placo.Flags.ignore_collisions)
robot.update_kinematics()

print(f"Loaded: {URDF_PATH}")
print(f"Joints: {robot.model.njoints}")
print(f"Frames: {len(robot.model.frames)}")

# Create visualization
viz = robot_viz(robot)

# Set all joints to zero
q = np.zeros(robot.model.nq)
robot.state.q = q
robot.update_kinematics()

# Display robot
viz.display(q)

# Show all body frames
print("\nShowing frames:")
for frame in robot.model.frames:
    if frame.type == pinocchio.FrameType.BODY and frame.name != "universe":
        print(f"  - {frame.name}")
        robot_frame_viz(robot, frame.name)

print("\n" + "=" * 50)
print("Visualization ready!")
print("=" * 50)

@schedule(interval=0.1)
def loop():
    pass

if __name__ == "__main__":
    run_loop()
