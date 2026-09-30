// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "rwip_ros2_package/msg/detail/controller__functions.h"
#include "rwip_ros2_package/msg/detail/controller__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace rwip_ros2_package
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Controller_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) rwip_ros2_package::msg::Controller(_init);
}

void Controller_fini_function(void * message_memory)
{
  auto typed_message = static_cast<rwip_ros2_package::msg::Controller *>(message_memory);
  typed_message->~Controller();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Controller_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rwip_ros2_package::msg::Controller, structure_needs_at_least_one_member),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Controller_message_members = {
  "rwip_ros2_package::msg",  // message namespace
  "Controller",  // message name
  1,  // number of fields
  sizeof(rwip_ros2_package::msg::Controller),
  false,  // has_any_key_member_
  Controller_message_member_array,  // message members
  Controller_init_function,  // function to initialize message memory (memory has to be allocated)
  Controller_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Controller_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Controller_message_members,
  get_message_typesupport_handle_function,
  &rwip_ros2_package__msg__Controller__get_type_hash,
  &rwip_ros2_package__msg__Controller__get_type_description,
  &rwip_ros2_package__msg__Controller__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace rwip_ros2_package


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<rwip_ros2_package::msg::Controller>()
{
  return &::rwip_ros2_package::msg::rosidl_typesupport_introspection_cpp::Controller_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, rwip_ros2_package, msg, Controller)() {
  return &::rwip_ros2_package::msg::rosidl_typesupport_introspection_cpp::Controller_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
