# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logging.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import vector_pb2 as vector__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='logging.proto',
  package='robotics.reinforcement_learning.robotable.envs',
  syntax='proto3',
  serialized_pb=_b('\n\rlogging.proto\x12.robotics.reinforcement_learning.robotable.envs\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0cvector.proto\"n\n\x10RobotableEpisode\x12Z\n\x0cstate_action\x18\x01 \x03(\x0b\x32\x44.robotics.reinforcement_learning.robotable.envs.RobotableStateAction\"V\n\x13RobotableMotorState\x12\r\n\x05\x61ngle\x18\x01 \x01(\x01\x12\x10\n\x08velocity\x18\x02 \x01(\x01\x12\x0e\n\x06torque\x18\x03 \x01(\x01\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\x01\"\xd1\x02\n\x14RobotableStateAction\x12\x12\n\ninfo_valid\x18\x06 \x01(\x08\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\rbase_position\x18\x02 \x01(\x0b\x32\x1b.robotics.messages.Vector3d\x12\x35\n\x10\x62\x61se_orientation\x18\x03 \x01(\x0b\x32\x1b.robotics.messages.Vector3d\x12\x35\n\x10\x62\x61se_angular_vel\x18\x04 \x01(\x0b\x32\x1b.robotics.messages.Vector3d\x12Y\n\x0cmotor_states\x18\x05 \x03(\x0b\x32\x43.robotics.reinforcement_learning.robotable.envs.RobotableMotorStateb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,vector__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ROBOTABLEEPISODE = _descriptor.Descriptor(
  name='RobotableEpisode',
  full_name='robotics.reinforcement_learning.robotable.envs.RobotableEpisode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_action', full_name='robotics.reinforcement_learning.robotable.envs.RobotableEpisode.state_action', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=222,
)


_ROBOTABLEMOTORSTATE = _descriptor.Descriptor(
  name='RobotableMotorState',
  full_name='robotics.reinforcement_learning.robotable.envs.RobotableMotorState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='angle', full_name='robotics.reinforcement_learning.robotable.envs.RobotableMotorState.angle', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='robotics.reinforcement_learning.robotable.envs.RobotableMotorState.velocity', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='torque', full_name='robotics.reinforcement_learning.robotable.envs.RobotableMotorState.torque', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='robotics.reinforcement_learning.robotable.envs.RobotableMotorState.action', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=310,
)


_ROBOTABLESTATEACTION = _descriptor.Descriptor(
  name='RobotableStateAction',
  full_name='robotics.reinforcement_learning.robotable.envs.RobotableStateAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_valid', full_name='robotics.reinforcement_learning.robotable.envs.RobotableStateAction.info_valid', index=0,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='robotics.reinforcement_learning.robotable.envs.RobotableStateAction.time', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_position', full_name='robotics.reinforcement_learning.robotable.envs.RobotableStateAction.base_position', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_orientation', full_name='robotics.reinforcement_learning.robotable.envs.RobotableStateAction.base_orientation', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_angular_vel', full_name='robotics.reinforcement_learning.robotable.envs.RobotableStateAction.base_angular_vel', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='motor_states', full_name='robotics.reinforcement_learning.robotable.envs.RobotableStateAction.motor_states', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=650,
)

_ROBOTABLEEPISODE.fields_by_name['state_action'].message_type = _ROBOTABLESTATEACTION
_ROBOTABLESTATEACTION.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ROBOTABLESTATEACTION.fields_by_name['base_position'].message_type = vector__pb2._VECTOR3D
_ROBOTABLESTATEACTION.fields_by_name['base_orientation'].message_type = vector__pb2._VECTOR3D
_ROBOTABLESTATEACTION.fields_by_name['base_angular_vel'].message_type = vector__pb2._VECTOR3D
_ROBOTABLESTATEACTION.fields_by_name['motor_states'].message_type = _ROBOTABLEMOTORSTATE
DESCRIPTOR.message_types_by_name['RobotableEpisode'] = _ROBOTABLEEPISODE
DESCRIPTOR.message_types_by_name['RobotableMotorState'] = _ROBOTABLEMOTORSTATE
DESCRIPTOR.message_types_by_name['RobotableStateAction'] = _ROBOTABLESTATEACTION

RobotableEpisode = _reflection.GeneratedProtocolMessageType('RobotableEpisode', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTABLEEPISODE,
  __module__ = 'logging_pb2'
  # @@protoc_insertion_point(class_scope:robotics.reinforcement_learning.robotable.envs.RobotableEpisode)
  ))
_sym_db.RegisterMessage(RobotableEpisode)

RobotableMotorState = _reflection.GeneratedProtocolMessageType('RobotableMotorState', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTABLEMOTORSTATE,
  __module__ = 'logging_pb2'
  # @@protoc_insertion_point(class_scope:robotics.reinforcement_learning.robotable.envs.RobotableMotorState)
  ))
_sym_db.RegisterMessage(RobotableMotorState)

RobotableStateAction = _reflection.GeneratedProtocolMessageType('RobotableStateAction', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTABLESTATEACTION,
  __module__ = 'logging_pb2'
  # @@protoc_insertion_point(class_scope:robotics.reinforcement_learning.robotable.envs.RobotableStateAction)
  ))
_sym_db.RegisterMessage(RobotableStateAction)


# @@protoc_insertion_point(module_scope)