// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice

#include "rwip_ros2_package/msg/detail/controller__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_rwip_ros2_package
const rosidl_type_hash_t *
rwip_ros2_package__msg__Controller__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xa0, 0xe6, 0xc5, 0x73, 0x20, 0x6e, 0x7e, 0xc1,
      0x9c, 0xdb, 0xee, 0x14, 0x8e, 0x6c, 0x8b, 0x77,
      0x92, 0x1a, 0xea, 0x1e, 0x3a, 0x20, 0x57, 0x92,
      0x01, 0x37, 0x1e, 0xe8, 0x6a, 0xf3, 0x07, 0x14,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char rwip_ros2_package__msg__Controller__TYPE_NAME[] = "rwip_ros2_package/msg/Controller";

// Define type names, field names, and default values
static char rwip_ros2_package__msg__Controller__FIELD_NAME__structure_needs_at_least_one_member[] = "structure_needs_at_least_one_member";

static rosidl_runtime_c__type_description__Field rwip_ros2_package__msg__Controller__FIELDS[] = {
  {
    {rwip_ros2_package__msg__Controller__FIELD_NAME__structure_needs_at_least_one_member, 35, 35},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
rwip_ros2_package__msg__Controller__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {rwip_ros2_package__msg__Controller__TYPE_NAME, 32, 32},
      {rwip_ros2_package__msg__Controller__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}


static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
rwip_ros2_package__msg__Controller__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {rwip_ros2_package__msg__Controller__TYPE_NAME, 32, 32},
    {msg_encoding, 3, 3},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
rwip_ros2_package__msg__Controller__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *rwip_ros2_package__msg__Controller__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
