# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia/clara/platform/clara.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nvidia_clara.grpc import common_pb2 as nvidia_dot_clara_dot_platform_dot_common__pb2

from nvidia_clara.grpc.common_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia/clara/platform/clara.proto',
  package='nvidia.clara.platform',
  syntax='proto3',
  serialized_options=b'\n\031com.nvidia.clara.platformZ\004apis\252\002\032Nvidia.Clara.Platform.Grpc',
  serialized_pb=b'\n!nvidia/clara/platform/clara.proto\x12\x15nvidia.clara.platform\x1a\"nvidia/clara/platform/common.proto\"H\n\x10\x43laraStopRequest\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.nvidia.clara.platform.RequestHeader\"J\n\x11\x43laraStopResponse\x12\x35\n\x06header\x18\x01 \x01(\x0b\x32%.nvidia.clara.platform.ResponseHeader\"K\n\x13\x43laraVersionRequest\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.nvidia.clara.platform.RequestHeader\"~\n\x14\x43laraVersionResponse\x12\x35\n\x06header\x18\x01 \x01(\x0b\x32%.nvidia.clara.platform.ResponseHeader\x12/\n\x07version\x18\x02 \x01(\x0b\x32\x1e.nvidia.clara.platform.Version2\xc6\x01\n\x05\x43lara\x12Y\n\x04Stop\x12\'.nvidia.clara.platform.ClaraStopRequest\x1a(.nvidia.clara.platform.ClaraStopResponse\x12\x62\n\x07Version\x12*.nvidia.clara.platform.ClaraVersionRequest\x1a+.nvidia.clara.platform.ClaraVersionResponseB>\n\x19\x63om.nvidia.clara.platformZ\x04\x61pis\xaa\x02\x1aNvidia.Clara.Platform.GrpcP\x00\x62\x06proto3'
  ,
  dependencies=[nvidia_dot_clara_dot_platform_dot_common__pb2.DESCRIPTOR,],
  public_dependencies=[nvidia_dot_clara_dot_platform_dot_common__pb2.DESCRIPTOR,])




_CLARASTOPREQUEST = _descriptor.Descriptor(
  name='ClaraStopRequest',
  full_name='nvidia.clara.platform.ClaraStopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nvidia.clara.platform.ClaraStopRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=96,
  serialized_end=168,
)


_CLARASTOPRESPONSE = _descriptor.Descriptor(
  name='ClaraStopResponse',
  full_name='nvidia.clara.platform.ClaraStopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nvidia.clara.platform.ClaraStopResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=170,
  serialized_end=244,
)


_CLARAVERSIONREQUEST = _descriptor.Descriptor(
  name='ClaraVersionRequest',
  full_name='nvidia.clara.platform.ClaraVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nvidia.clara.platform.ClaraVersionRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=246,
  serialized_end=321,
)


_CLARAVERSIONRESPONSE = _descriptor.Descriptor(
  name='ClaraVersionResponse',
  full_name='nvidia.clara.platform.ClaraVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nvidia.clara.platform.ClaraVersionResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='nvidia.clara.platform.ClaraVersionResponse.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=323,
  serialized_end=449,
)

_CLARASTOPREQUEST.fields_by_name['header'].message_type = nvidia_dot_clara_dot_platform_dot_common__pb2._REQUESTHEADER
_CLARASTOPRESPONSE.fields_by_name['header'].message_type = nvidia_dot_clara_dot_platform_dot_common__pb2._RESPONSEHEADER
_CLARAVERSIONREQUEST.fields_by_name['header'].message_type = nvidia_dot_clara_dot_platform_dot_common__pb2._REQUESTHEADER
_CLARAVERSIONRESPONSE.fields_by_name['header'].message_type = nvidia_dot_clara_dot_platform_dot_common__pb2._RESPONSEHEADER
_CLARAVERSIONRESPONSE.fields_by_name['version'].message_type = nvidia_dot_clara_dot_platform_dot_common__pb2._VERSION
DESCRIPTOR.message_types_by_name['ClaraStopRequest'] = _CLARASTOPREQUEST
DESCRIPTOR.message_types_by_name['ClaraStopResponse'] = _CLARASTOPRESPONSE
DESCRIPTOR.message_types_by_name['ClaraVersionRequest'] = _CLARAVERSIONREQUEST
DESCRIPTOR.message_types_by_name['ClaraVersionResponse'] = _CLARAVERSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClaraStopRequest = _reflection.GeneratedProtocolMessageType('ClaraStopRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLARASTOPREQUEST,
  '__module__' : 'nvidia.clara.platform.clara_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.ClaraStopRequest)
  })
_sym_db.RegisterMessage(ClaraStopRequest)

ClaraStopResponse = _reflection.GeneratedProtocolMessageType('ClaraStopResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLARASTOPRESPONSE,
  '__module__' : 'nvidia.clara.platform.clara_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.ClaraStopResponse)
  })
_sym_db.RegisterMessage(ClaraStopResponse)

ClaraVersionRequest = _reflection.GeneratedProtocolMessageType('ClaraVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLARAVERSIONREQUEST,
  '__module__' : 'nvidia.clara.platform.clara_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.ClaraVersionRequest)
  })
_sym_db.RegisterMessage(ClaraVersionRequest)

ClaraVersionResponse = _reflection.GeneratedProtocolMessageType('ClaraVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLARAVERSIONRESPONSE,
  '__module__' : 'nvidia.clara.platform.clara_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.ClaraVersionResponse)
  })
_sym_db.RegisterMessage(ClaraVersionResponse)


DESCRIPTOR._options = None

_CLARA = _descriptor.ServiceDescriptor(
  name='Clara',
  full_name='nvidia.clara.platform.Clara',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=452,
  serialized_end=650,
  methods=[
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='nvidia.clara.platform.Clara.Stop',
    index=0,
    containing_service=None,
    input_type=_CLARASTOPREQUEST,
    output_type=_CLARASTOPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Version',
    full_name='nvidia.clara.platform.Clara.Version',
    index=1,
    containing_service=None,
    input_type=_CLARAVERSIONREQUEST,
    output_type=_CLARAVERSIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLARA)

DESCRIPTOR.services_by_name['Clara'] = _CLARA

# @@protoc_insertion_point(module_scope)
