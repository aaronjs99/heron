cmake_minimum_required(VERSION 2.8.3)
project(heron_control)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY config launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS scripts/vel_cov
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

