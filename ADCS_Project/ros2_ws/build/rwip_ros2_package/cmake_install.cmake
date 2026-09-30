# Install script for directory: /home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/src/rwip_ros2_package

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/install/rwip_ros2_package")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/rwip_ros2_package" TYPE PROGRAM FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/src/rwip_ros2_package/scripts/controller_node.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/rosidl_interfaces" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_index/share/ament_index/resource_index/rosidl_interfaces/rwip_ros2_package")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/msg" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_generator_type_description/rwip_ros2_package/msg/Controller.json")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/rwip_ros2_package/rwip_ros2_package" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_generator_c/rwip_ros2_package/" REGEX "/[^/]*\\.h$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/environment" TYPE FILE FILES "/opt/ros/jazzy/lib/python3.12/site-packages/ament_package/template/environment_hook/library_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/environment" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/library_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/librwip_ros2_package__rosidl_generator_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_c.so"
         OLD_RPATH "/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/rwip_ros2_package/rwip_ros2_package" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_typesupport_fastrtps_c/rwip_ros2_package/" REGEX "/[^/]*\\.cpp$" EXCLUDE)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/librwip_ros2_package__rosidl_typesupport_fastrtps_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_c.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/rwip_ros2_package/rwip_ros2_package" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_typesupport_introspection_c/rwip_ros2_package/" REGEX "/[^/]*\\.h$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/librwip_ros2_package__rosidl_typesupport_introspection_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_c.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/librwip_ros2_package__rosidl_typesupport_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_c.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/rwip_ros2_package/rwip_ros2_package" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_generator_cpp/rwip_ros2_package/" REGEX "/[^/]*\\.hpp$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/rwip_ros2_package/rwip_ros2_package" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_typesupport_fastrtps_cpp/rwip_ros2_package/" REGEX "/[^/]*\\.cpp$" EXCLUDE)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_cpp.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_cpp.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/librwip_ros2_package__rosidl_typesupport_fastrtps_cpp.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_cpp.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_cpp.so"
         OLD_RPATH "/opt/ros/jazzy/lib:/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_fastrtps_cpp.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/rwip_ros2_package/rwip_ros2_package" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_typesupport_introspection_cpp/rwip_ros2_package/" REGEX "/[^/]*\\.hpp$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_cpp.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_cpp.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/librwip_ros2_package__rosidl_typesupport_introspection_cpp.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_cpp.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_cpp.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_introspection_cpp.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_cpp.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_cpp.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/librwip_ros2_package__rosidl_typesupport_cpp.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_cpp.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_cpp.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_typesupport_cpp.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/environment" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/pythonpath.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/environment" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/pythonpath.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package-0.0.0-py3.12.egg-info" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_python/rwip_ros2_package/rwip_ros2_package.egg-info/")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_generator_py/rwip_ros2_package/" REGEX "/[^/]*\\.pyc$" EXCLUDE REGEX "/\\_\\_pycache\\_\\_$" EXCLUDE)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(
        COMMAND
        "/usr/bin/python3" "-m" "compileall"
        "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/install/rwip_ros2_package/lib/python3.12/site-packages/rwip_ros2_package"
      )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package" TYPE MODULE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_generator_py/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/rwip_ros2_package_s__rosidl_typesupport_fastrtps_c.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_introspection_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_introspection_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_introspection_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package" TYPE MODULE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_generator_py/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_introspection_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_introspection_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_introspection_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_introspection_c.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_introspection_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/rwip_ros2_package_s__rosidl_typesupport_introspection_c.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package" TYPE MODULE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_generator_py/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_c.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/rwip_ros2_package/rwip_ros2_package_s__rosidl_typesupport_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/rwip_ros2_package_s__rosidl_typesupport_c.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_py.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_py.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_py.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/librwip_ros2_package__rosidl_generator_py.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_py.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_py.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_py.so"
         OLD_RPATH "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package:/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librwip_ros2_package__rosidl_generator_py.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package" TYPE DIRECTORY FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_generator_rs/rwip_ros2_package/rust")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/msg" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_adapter/rwip_ros2_package/msg/Controller.idl")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/msg" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/src/rwip_ros2_package/msg/Controller.msg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/rwip_ros2_package")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/rwip_ros2_package")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/environment" TYPE FILE FILES "/opt/ros/jazzy/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/environment" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/environment" TYPE FILE FILES "/opt/ros/jazzy/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/environment" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_index/share/ament_index/resource_index/packages/rwip_ros2_package")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_cExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_cExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_generator_cExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_cExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_cExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_generator_cExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_generator_cExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_introspection_cExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_introspection_cExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_introspection_cExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_introspection_cExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_introspection_cExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_introspection_cExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_introspection_cExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_cExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_cExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_cExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_cExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_cExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_cExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_cExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_cppExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_cppExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_generator_cppExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_cppExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_cppExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_generator_cppExport.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cppExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cppExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cppExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cppExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cppExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cppExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_typesupport_fastrtps_cppExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_introspection_cppExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_introspection_cppExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_introspection_cppExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_introspection_cppExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_introspection_cppExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_introspection_cppExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_introspection_cppExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_cppExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_cppExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_cppExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_cppExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/rwip_ros2_package__rosidl_typesupport_cppExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_cppExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/rwip_ros2_package__rosidl_typesupport_cppExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_pyExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_pyExport.cmake"
         "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_generator_pyExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_pyExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake/export_rwip_ros2_package__rosidl_generator_pyExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_generator_pyExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/CMakeFiles/Export/42b2ddc9bb6b4e112819586ab2762170/export_rwip_ros2_package__rosidl_generator_pyExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_cmake/rosidl_cmake-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_export_dependencies/ament_cmake_export_dependencies-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_export_include_directories/ament_cmake_export_include_directories-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_export_libraries/ament_cmake_export_libraries-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_export_targets/ament_cmake_export_targets-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_cmake/rosidl_cmake_export_typesupport_targets-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_cmake/rosidl_cmake_export_typesupport_libraries-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rosidl_cmake/rosidl_cmake_aggregate_target-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package/cmake" TYPE FILE FILES
    "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_core/rwip_ros2_packageConfig.cmake"
    "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/ament_cmake_core/rwip_ros2_packageConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rwip_ros2_package" TYPE FILE FILES "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/src/rwip_ros2_package/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rwip_ros2_package__py/cmake_install.cmake")
  include("/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/rwip_ros2_package__rs/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/ros2_ws/build/rwip_ros2_package/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
