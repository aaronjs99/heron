cmake_minimum_required(VERSION 3.0.2)
project(heron_control)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY config launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS scripts/vel_cov.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
