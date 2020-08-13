# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia/clara/platform/common.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia/clara/platform/common.proto',
  package='nvidia.clara.platform',
  syntax='proto3',
  serialized_options=b'\n\031com.nvidia.clara.platformZ\004apis\252\002\032Nvidia.Clara.Platform.Grpc',
  serialized_pb=b'\n\"nvidia/clara/platform/common.proto\x12\x15nvidia.clara.platform\"\x1b\n\nIdentifier\x12\r\n\x05value\x18\x01 \x01(\t\"E\n\x07Version\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\x12\r\n\x05patch\x18\x03 \x01(\x05\x12\r\n\x05label\x18\x04 \x01(\t\"X\n\rRequestHeader\x12\x33\n\x0b\x61pi_version\x18\x01 \x01(\x0b\x32\x1e.nvidia.clara.platform.Version\x12\x12\n\nuser_agent\x18\x02 \x01(\t\"0\n\x0eResponseHeader\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x10\n\x08messages\x18\x02 \x03(\t\"\x1a\n\tTimestamp\x12\r\n\x05value\x18\x01 \x01(\x12\x42>\n\x19\x63om.nvidia.clara.platformZ\x04\x61pis\xaa\x02\x1aNvidia.Clara.Platform.Grpcb\x06proto3'
)




_IDENTIFIER = _descriptor.Descriptor(
  name='Identifier',
  full_name='nvidia.clara.platform.Identifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='nvidia.clara.platform.Identifier.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=88,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='nvidia.clara.platform.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='nvidia.clara.platform.Version.major', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor', full_name='nvidia.clara.platform.Version.minor', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patch', full_name='nvidia.clara.platform.Version.patch', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='nvidia.clara.platform.Version.label', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=159,
)


_REQUESTHEADER = _descriptor.Descriptor(
  name='RequestHeader',
  full_name='nvidia.clara.platform.RequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_version', full_name='nvidia.clara.platform.RequestHeader.api_version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_agent', full_name='nvidia.clara.platform.RequestHeader.user_agent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=249,
)


_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='nvidia.clara.platform.ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='nvidia.clara.platform.ResponseHeader.code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages', full_name='nvidia.clara.platform.ResponseHeader.messages', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=299,
)


_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='nvidia.clara.platform.Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='nvidia.clara.platform.Timestamp.value', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=327,
)

_REQUESTHEADER.fields_by_name['api_version'].message_type = _VERSION
DESCRIPTOR.message_types_by_name['Identifier'] = _IDENTIFIER
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['RequestHeader'] = _REQUESTHEADER
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['Timestamp'] = _TIMESTAMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Identifier = _reflection.GeneratedProtocolMessageType('Identifier', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIER,
  '__module__' : 'nvidia.clara.platform.common_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.Identifier)
  })
_sym_db.RegisterMessage(Identifier)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'nvidia.clara.platform.common_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.Version)
  })
_sym_db.RegisterMessage(Version)

RequestHeader = _reflection.GeneratedProtocolMessageType('RequestHeader', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTHEADER,
  '__module__' : 'nvidia.clara.platform.common_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.RequestHeader)
  })
_sym_db.RegisterMessage(RequestHeader)

ResponseHeader = _reflection.GeneratedProtocolMessageType('ResponseHeader', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEHEADER,
  '__module__' : 'nvidia.clara.platform.common_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.ResponseHeader)
  })
_sym_db.RegisterMessage(ResponseHeader)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'nvidia.clara.platform.common_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.Timestamp)
  })
_sym_db.RegisterMessage(Timestamp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
