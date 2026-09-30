// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "rwip_ros2_package/msg/controller.hpp"


#ifndef RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__TRAITS_HPP_
#define RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "rwip_ros2_package/msg/detail/controller__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace rwip_ros2_package
{

namespace msg
{

inline void to_flow_style_yaml(
  const Controller & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Controller & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Controller & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace rwip_ros2_package

namespace rosidl_generator_traits
{

[[deprecated("use rwip_ros2_package::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const rwip_ros2_package::msg::Controller & msg,
  std::ostream & out, size_t indentation = 0)
{
  rwip_ros2_package::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use rwip_ros2_package::msg::to_yaml() instead")]]
inline std::string to_yaml(const rwip_ros2_package::msg::Controller & msg)
{
  return rwip_ros2_package::msg::to_yaml(msg);
}

template<>
inline const char * data_type<rwip_ros2_package::msg::Controller>()
{
  return "rwip_ros2_package::msg::Controller";
}

template<>
inline const char * name<rwip_ros2_package::msg::Controller>()
{
  return "rwip_ros2_package/msg/Controller";
}

template<>
struct has_fixed_size<rwip_ros2_package::msg::Controller>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<rwip_ros2_package::msg::Controller>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<rwip_ros2_package::msg::Controller>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__TRAITS_HPP_
