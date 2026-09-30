// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice
#ifndef RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "rwip_ros2_package/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "rwip_ros2_package/msg/detail/controller__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rwip_ros2_package
bool cdr_serialize_rwip_ros2_package__msg__Controller(
  const rwip_ros2_package__msg__Controller * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rwip_ros2_package
bool cdr_deserialize_rwip_ros2_package__msg__Controller(
  eprosima::fastcdr::Cdr &,
  rwip_ros2_package__msg__Controller * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rwip_ros2_package
size_t get_serialized_size_rwip_ros2_package__msg__Controller(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rwip_ros2_package
size_t max_serialized_size_rwip_ros2_package__msg__Controller(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rwip_ros2_package
bool cdr_serialize_key_rwip_ros2_package__msg__Controller(
  const rwip_ros2_package__msg__Controller * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rwip_ros2_package
size_t get_serialized_size_key_rwip_ros2_package__msg__Controller(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rwip_ros2_package
size_t max_serialized_size_key_rwip_ros2_package__msg__Controller(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rwip_ros2_package
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rwip_ros2_package, msg, Controller)();

#ifdef __cplusplus
}
#endif

#endif  // RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
