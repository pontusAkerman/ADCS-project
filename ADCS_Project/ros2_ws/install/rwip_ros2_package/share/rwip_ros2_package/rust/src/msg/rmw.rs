#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "rwip_ros2_package__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__rwip_ros2_package__msg__Controller() -> *const std::ffi::c_void;
}

#[link(name = "rwip_ros2_package__rosidl_generator_c")]
extern "C" {
    fn rwip_ros2_package__msg__Controller__init(msg: *mut Controller) -> bool;
    fn rwip_ros2_package__msg__Controller__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Controller>, size: usize) -> bool;
    fn rwip_ros2_package__msg__Controller__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Controller>);
    fn rwip_ros2_package__msg__Controller__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Controller>, out_seq: *mut rosidl_runtime_rs::Sequence<Controller>) -> bool;
}

// Corresponds to rwip_ros2_package__msg__Controller
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Controller {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for Controller {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !rwip_ros2_package__msg__Controller__init(&mut msg as *mut _) {
        panic!("Call to rwip_ros2_package__msg__Controller__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Controller {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { rwip_ros2_package__msg__Controller__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { rwip_ros2_package__msg__Controller__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { rwip_ros2_package__msg__Controller__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Controller {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Controller where Self: Sized {
  const TYPE_NAME: &'static str = "rwip_ros2_package/msg/Controller";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__rwip_ros2_package__msg__Controller() }
  }
}


