// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice

#ifndef RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include <cstddef>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "rwip_ros2_package/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "rwip_ros2_package/msg/detail/controller__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace rwip_ros2_package
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rwip_ros2_package
cdr_serialize(
  const rwip_ros2_package::msg::Controller & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rwip_ros2_package
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  rwip_ros2_package::msg::Controller & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rwip_ros2_package
get_serialized_size(
  const rwip_ros2_package::msg::Controller & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rwip_ros2_package
max_serialized_size_Controller(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rwip_ros2_package
cdr_serialize_key(
  const rwip_ros2_package::msg::Controller & ros_message,
  eprosima::fastcdr::Cdr &);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rwip_ros2_package
get_serialized_size_key(
  const rwip_ros2_package::msg::Controller & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rwip_ros2_package
max_serialized_size_key_Controller(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace rwip_ros2_package

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rwip_ros2_package
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, rwip_ros2_package, msg, Controller)();

#ifdef __cplusplus
}
#endif

#endif  // RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
