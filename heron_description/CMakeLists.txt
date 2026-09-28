cmake_minimum_required(VERSION 3.8)
project(heron_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY meshes launch urdf
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS scripts/env_run.sh
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
