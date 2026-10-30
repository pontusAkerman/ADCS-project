#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to rwip_ros2_package__msg__ControlInput

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ControlInput {

    // This member is not documented.
    #[allow(missing_docs)]
    pub motor_torque: f64,

}



impl Default for ControlInput {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::ControlInput::default())
  }
}

impl rosidl_runtime_rs::Message for ControlInput {
  type RmwMsg = super::msg::rmw::ControlInput;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        motor_torque: msg.motor_torque,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      motor_torque: msg.motor_torque,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      motor_torque: msg.motor_torque,
    }
  }
}


// Corresponds to rwip_ros2_package__msg__States

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct States {

    // This member is not documented.
    #[allow(missing_docs)]
    pub phi: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub phi_dot: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub theta: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub theta_dot: f64,

}



impl Default for States {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::States::default())
  }
}

impl rosidl_runtime_rs::Message for States {
  type RmwMsg = super::msg::rmw::States;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        phi: msg.phi,
        phi_dot: msg.phi_dot,
        theta: msg.theta,
        theta_dot: msg.theta_dot,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      phi: msg.phi,
      phi_dot: msg.phi_dot,
      theta: msg.theta,
      theta_dot: msg.theta_dot,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      phi: msg.phi,
      phi_dot: msg.phi_dot,
      theta: msg.theta,
      theta_dot: msg.theta_dot,
    }
  }
}


