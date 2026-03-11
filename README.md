# SO-ARM100 Simulation - New Gripper Test

This repository contains simulation files for testing a new custom gripper (Gripper_SROI) on the SO101 robot arm.

## Files

| File | Description |
|------|-------------|
| `Simulation/SO101/assets/Gripper_SROI.stl` | Custom gripper 3D model (STL format) |
| `Simulation/SO101/so101_new_gripper_test.urdf` | URDF robot description with the new gripper attached |
| `Simulation/SO101/visualize_all.py` | Python script to visualize the robot in 3D |

## Requirements

Install the required Python packages:

```bash
pip install placo pinocchio ischedule
```

## Usage

### 1. Visualize the Robot with New Gripper

Run the visualization script:

```bash
cd Simulation/SO101
python visualize_all.py
```

This will open a 3D visualization window showing the SO101 robot with the new Gripper_SROI attached. The script:

- Loads the URDF file (`so101_new_gripper_test.urdf`)
- Displays all robot meshes including the new gripper
- Shows coordinate frames for each body link

### 2. Using the URDF in Your Own Code

The URDF file can be used with:

- **Pinocchio** - rigid body dynamics library
- **Placo** - robot visualization and control
- **ROS/ROS2** - robot operating system
- **MuJoCo/PyBullet** - physics simulators

Example with Pinocchio:

```python
import pinocchio

urdf_path = "Simulation/SO101/so101_new_gripper_test.urdf"
model = pinocchio.buildModelFromUrdf(urdf_path)
```

### 3. Gripper STL File

The `Gripper_SROI.stl` is referenced by the URDF and located at:

```
Simulation/SO101/assets/Gripper_SROI.stl
```

If you move the URDF file, update the mesh path inside it to point to the correct STL location.

## File Structure

```
Simulation/SO101/
├── assets/
│   ├── Gripper_SROI.stl          # New custom gripper
│   ├── base_so101_v2.stl         # Base parts
│   ├── sts3215_03a_v1.stl        # Servo motors
│   └── ...                       # Other SO101 parts
├── so101_new_gripper_test.urdf   # Robot URDF with new gripper
└── visualize_all.py              # Visualization script
```

## Notes

- The URDF uses absolute file paths. Adjust paths if your repository is in a different location.
- The gripper is attached via the `wrist_roll` joint to the wrist link.
- A `camera_mount_link` frame is included for mounting cameras.
