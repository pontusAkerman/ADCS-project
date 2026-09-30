# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target rwip_ros2_package::rwip_ros2_package
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${rwip_ros2_package_TARGETS}.
if(rwip_ros2_package_TARGETS AND NOT TARGET rwip_ros2_package::rwip_ros2_package)
  add_library(rwip_ros2_package::rwip_ros2_package INTERFACE IMPORTED)
  set_target_properties(rwip_ros2_package::rwip_ros2_package PROPERTIES
    INTERFACE_LINK_LIBRARIES "${rwip_ros2_package_TARGETS}")
endif()
