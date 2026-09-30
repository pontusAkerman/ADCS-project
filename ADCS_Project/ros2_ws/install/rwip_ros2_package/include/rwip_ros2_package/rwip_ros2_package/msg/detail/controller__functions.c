// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice
#include "rwip_ros2_package/msg/detail/controller__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
rwip_ros2_package__msg__Controller__init(rwip_ros2_package__msg__Controller * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
rwip_ros2_package__msg__Controller__fini(rwip_ros2_package__msg__Controller * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
rwip_ros2_package__msg__Controller__are_equal(const rwip_ros2_package__msg__Controller * lhs, const rwip_ros2_package__msg__Controller * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
rwip_ros2_package__msg__Controller__copy(
  const rwip_ros2_package__msg__Controller * input,
  rwip_ros2_package__msg__Controller * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

rwip_ros2_package__msg__Controller *
rwip_ros2_package__msg__Controller__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rwip_ros2_package__msg__Controller * msg = (rwip_ros2_package__msg__Controller *)allocator.allocate(sizeof(rwip_ros2_package__msg__Controller), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rwip_ros2_package__msg__Controller));
  bool success = rwip_ros2_package__msg__Controller__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
rwip_ros2_package__msg__Controller__destroy(rwip_ros2_package__msg__Controller * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    rwip_ros2_package__msg__Controller__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
rwip_ros2_package__msg__Controller__Sequence__init(rwip_ros2_package__msg__Controller__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rwip_ros2_package__msg__Controller * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(rwip_ros2_package__msg__Controller)) {
      return false;
    }
    data = (rwip_ros2_package__msg__Controller *)allocator.zero_allocate(size, sizeof(rwip_ros2_package__msg__Controller), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rwip_ros2_package__msg__Controller__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rwip_ros2_package__msg__Controller__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
rwip_ros2_package__msg__Controller__Sequence__fini(rwip_ros2_package__msg__Controller__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rwip_ros2_package__msg__Controller__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

rwip_ros2_package__msg__Controller__Sequence *
rwip_ros2_package__msg__Controller__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rwip_ros2_package__msg__Controller__Sequence * array = (rwip_ros2_package__msg__Controller__Sequence *)allocator.allocate(sizeof(rwip_ros2_package__msg__Controller__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = rwip_ros2_package__msg__Controller__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
rwip_ros2_package__msg__Controller__Sequence__destroy(rwip_ros2_package__msg__Controller__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    rwip_ros2_package__msg__Controller__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
rwip_ros2_package__msg__Controller__Sequence__are_equal(const rwip_ros2_package__msg__Controller__Sequence * lhs, const rwip_ros2_package__msg__Controller__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!rwip_ros2_package__msg__Controller__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
rwip_ros2_package__msg__Controller__Sequence__copy(
  const rwip_ros2_package__msg__Controller__Sequence * input,
  rwip_ros2_package__msg__Controller__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(rwip_ros2_package__msg__Controller)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(rwip_ros2_package__msg__Controller);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    rwip_ros2_package__msg__Controller * data =
      (rwip_ros2_package__msg__Controller *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!rwip_ros2_package__msg__Controller__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          rwip_ros2_package__msg__Controller__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!rwip_ros2_package__msg__Controller__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
