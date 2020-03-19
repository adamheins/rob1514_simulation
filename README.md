# ROB 1514 Simulation

ROS package for the ROB 1514 project simulation environment. Provides a
practice [Gazebo](http://gazebosim.org/) world based on the portion of UTIAS
designated for the scavenger hunt project. Gazebo should already be installed
alongside ROS.

The simulated world used for the actual demo will use the same layout of walls
and doors, but objects may be moved around. QR codes will be different, and in
different locations, but will be placed at roughly the same height.

## Install
Clone the repository into your catkin workspace:
```
git clone https://github.com/adamheins/rob1514_simulation
```

You need to tell Gazebo where to find the QR code models. Add the following
line to your `.bashrc`:
```
export GAZEBO_MODEL_PATH=<path_to_catkin_ws>/src/rob1514_simulation/models:$GAZEBO_MODEL_PATH
```

Build and source the workspace as per usual ROS procedure.

## Run
Once the workspace has been built and sourced, just run
```
roslaunch rob1514_simulation simulation.launch
```

This should launch Gazebo and load the simulated UTIAS world. A turtlebot
should spawn at the map's origin, which you can control like a normal
turtlebot. The turtlebot is equipped with **two** cameras: the typical
front-facing Astra camera, and a side-facing (it points to the left) camera
meant to simulate a laptop's webcam. The side-facing camera renders as a simple
white box hovering above the turtlebot.

You can, of course, view all ROS topics using `rostopic list`. Topics for the
front-facing camera are prefixed with `/camera`, while the topics for the
side-facing camera are prefixed with `/head_camera`.


## QR Codes
There are seven QR codes distributed throughout the simulated world. QR codes
will be different and placed in different locations for the demo simulation.

If you wish, you can create your own QR code models to place in the Gazebo
environment using the provided Python script. Install dependencies using
```
pip install qrcode
```
Then, in a terminal, navigate to the folder `scripts` and run `python
make_qr_model.py <word>`, where `<word>` is replaced by the word you want the
QR code to encode. This will generate a folder called `qr_<word>` in the
current working directory. Move it to the `models` folder, and you should be
able to see it in Gazebo under the `Insert` tab.


## Notes
* Tested with Gazebo 7.0 with ROS Kinetic on Ubuntu 16.04.
