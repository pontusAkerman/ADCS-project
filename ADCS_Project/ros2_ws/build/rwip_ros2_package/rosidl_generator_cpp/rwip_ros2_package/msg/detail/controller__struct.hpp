// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from rwip_ros2_package:msg/Controller.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "rwip_ros2_package/msg/controller.hpp"


#ifndef RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__STRUCT_HPP_
#define RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__rwip_ros2_package__msg__Controller __attribute__((deprecated))
#else
# define DEPRECATED__rwip_ros2_package__msg__Controller __declspec(deprecated)
#endif

namespace rwip_ros2_package
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Controller_
{
  using Type = Controller_<ContainerAllocator>;

  explicit Controller_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit Controller_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    rwip_ros2_package::msg::Controller_<ContainerAllocator> *;
  using ConstRawPtr =
    const rwip_ros2_package::msg::Controller_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<rwip_ros2_package::msg::Controller_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<rwip_ros2_package::msg::Controller_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      rwip_ros2_package::msg::Controller_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<rwip_ros2_package::msg::Controller_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      rwip_ros2_package::msg::Controller_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<rwip_ros2_package::msg::Controller_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<rwip_ros2_package::msg::Controller_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<rwip_ros2_package::msg::Controller_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__rwip_ros2_package__msg__Controller
    std::shared_ptr<rwip_ros2_package::msg::Controller_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__rwip_ros2_package__msg__Controller
    std::shared_ptr<rwip_ros2_package::msg::Controller_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Controller_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const Controller_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Controller_

// alias to use template instance with default allocator
using Controller =
  rwip_ros2_package::msg::Controller_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace rwip_ros2_package

#endif  // RWIP_ROS2_PACKAGE__MSG__DETAIL__CONTROLLER__STRUCT_HPP_
