// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "rwip_ros2_package/msg/controller.h"


#ifndef RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__STRUCT_H_
#define RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Controller in the package rwip_ros2_package.
typedef struct rwip_ros2_package__msg__Controller
{
  uint8_t structure_needs_at_least_one_member;
} rwip_ros2_package__msg__Controller;

// Struct for a sequence of rwip_ros2_package__msg__Controller.
typedef struct rwip_ros2_package__msg__Controller__Sequence
{
  rwip_ros2_package__msg__Controller * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rwip_ros2_package__msg__Controller__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__STRUCT_H_
