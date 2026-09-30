// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "rwip_ros2_package/msg/detail/controller__rosidl_typesupport_introspection_c.h"
#include "rwip_ros2_package/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "rwip_ros2_package/msg/detail/controller__functions.h"
#include "rwip_ros2_package/msg/detail/controller__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rwip_ros2_package__msg__Controller__init(message_memory);
}

void rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_fini_function(void * message_memory)
{
  rwip_ros2_package__msg__Controller__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rwip_ros2_package__msg__Controller, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_message_members = {
  "rwip_ros2_package__msg",  // message namespace
  "Controller",  // message name
  1,  // number of fields
  sizeof(rwip_ros2_package__msg__Controller),
  false,  // has_any_key_member_
  rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_message_member_array,  // message members
  rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_init_function,  // function to initialize message memory (memory has to be allocated)
  rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_message_type_support_handle = {
  0,
  &rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_message_members,
  get_message_typesupport_handle_function,
  &rwip_ros2_package__msg__Controller__get_type_hash,
  &rwip_ros2_package__msg__Controller__get_type_description,
  &rwip_ros2_package__msg__Controller__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rwip_ros2_package
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rwip_ros2_package, msg, Controller)() {
  if (!rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_message_type_support_handle.typesupport_identifier) {
    rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &rwip_ros2_package__msg__Controller__rosidl_typesupport_introspection_c__Controller_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
