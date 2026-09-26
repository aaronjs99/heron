cmake_minimum_required(VERSION 3.8)
project(heron_control)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS scripts/vel_cov.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()