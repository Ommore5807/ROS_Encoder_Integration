import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ommore5807/Workspaces/ros2_py_ws/install/my_py_pkg'
