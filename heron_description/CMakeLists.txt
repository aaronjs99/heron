cmake_minimum_required(VERSION 3.8)
project(heron_description)

find_package(ament_cmake REQUIRED)

# NOTE: roslaunch_add_file_check(launch/description.launch) had no direct ament_cmake equivalent
# The block below (ament_lint_auto) is NOT a one-to-one replacement
# It only checks Python syntax/style, it does not validate that the launch file actually parses or runs correctly

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(DIRECTORY meshes launch urdf
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS scripts/env_run.sh
  DESTINATION share/${PROJECT_NAME}
)

ament_package()