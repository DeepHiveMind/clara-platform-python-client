# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia/clara/platform/node-monitor/metrics.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nvidia_clara.grpc import common_pb2 as nvidia_dot_clara_dot_platform_dot_common__pb2

from nvidia_clara.grpc.common_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia/clara/platform/node-monitor/metrics.proto',
  package='nvidia.clara.platform.node_monitor',
  syntax='proto3',
  serialized_options=b'\n%com.nvidia.clara.platform.nodemonitorZ\004apis\252\002&Nvidia.Clara.Platform.NodeMonitor.Grpc',
  serialized_pb=b'\n0nvidia/clara/platform/node-monitor/metrics.proto\x12\"nvidia.clara.platform.node_monitor\x1a\"nvidia/clara/platform/common.proto\"\xbb\x02\n\nGpuDetails\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\x12G\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x39.nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics\x12\x33\n\ttimestamp\x18\x03 \x01(\x0b\x32 .nvidia.clara.platform.Timestamp\x1a\x9b\x01\n\nGpuMetrics\x12\x1a\n\x12memory_utilization\x18\x01 \x01(\x02\x12\x17\n\x0fgpu_utilization\x18\x02 \x01(\x02\x12\x12\n\nfree_bar_1\x18\x03 \x01(\x03\x12\x12\n\nused_bar_1\x18\x04 \x01(\x03\x12\x17\n\x0f\x66ree_gpu_memory\x18\x05 \x01(\x03\x12\x17\n\x0fused_gpu_memory\x18\x06 \x01(\x03\"P\n\x18MonitorGpuMetricsRequest\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.nvidia.clara.platform.RequestHeader\"\x97\x01\n\x19MonitorGpuMetricsResponse\x12\x35\n\x06header\x18\x01 \x01(\x0b\x32%.nvidia.clara.platform.ResponseHeader\x12\x43\n\x0bgpu_details\x18\x02 \x03(\x0b\x32..nvidia.clara.platform.node_monitor.GpuDetails2\x97\x01\n\x07Monitor\x12\x8b\x01\n\nGpuMetrics\x12<.nvidia.clara.platform.node_monitor.MonitorGpuMetricsRequest\x1a=.nvidia.clara.platform.node_monitor.MonitorGpuMetricsResponse0\x01\x42V\n%com.nvidia.clara.platform.nodemonitorZ\x04\x61pis\xaa\x02&Nvidia.Clara.Platform.NodeMonitor.GrpcP\x00\x62\x06proto3'
  ,
  dependencies=[nvidia_dot_clara_dot_platform_dot_common__pb2.DESCRIPTOR,],
  public_dependencies=[nvidia_dot_clara_dot_platform_dot_common__pb2.DESCRIPTOR,])




_GPUDETAILS_GPUMETRICS = _descriptor.Descriptor(
  name='GpuMetrics',
  full_name='nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='memory_utilization', full_name='nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics.memory_utilization', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_utilization', full_name='nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics.gpu_utilization', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_bar_1', full_name='nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics.free_bar_1', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used_bar_1', full_name='nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics.used_bar_1', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_gpu_memory', full_name='nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics.free_gpu_memory', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used_gpu_memory', full_name='nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics.used_gpu_memory', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=285,
  serialized_end=440,
)

_GPUDETAILS = _descriptor.Descriptor(
  name='GpuDetails',
  full_name='nvidia.clara.platform.node_monitor.GpuDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='nvidia.clara.platform.node_monitor.GpuDetails.device_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='nvidia.clara.platform.node_monitor.GpuDetails.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='nvidia.clara.platform.node_monitor.GpuDetails.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GPUDETAILS_GPUMETRICS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=440,
)


_MONITORGPUMETRICSREQUEST = _descriptor.Descriptor(
  name='MonitorGpuMetricsRequest',
  full_name='nvidia.clara.platform.node_monitor.MonitorGpuMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nvidia.clara.platform.node_monitor.MonitorGpuMetricsRequest.header', index=0,
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
  serialized_start=442,
  serialized_end=522,
)


_MONITORGPUMETRICSRESPONSE = _descriptor.Descriptor(
  name='MonitorGpuMetricsResponse',
  full_name='nvidia.clara.platform.node_monitor.MonitorGpuMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nvidia.clara.platform.node_monitor.MonitorGpuMetricsResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_details', full_name='nvidia.clara.platform.node_monitor.MonitorGpuMetricsResponse.gpu_details', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=525,
  serialized_end=676,
)

_GPUDETAILS_GPUMETRICS.containing_type = _GPUDETAILS
_GPUDETAILS.fields_by_name['data'].message_type = _GPUDETAILS_GPUMETRICS
_GPUDETAILS.fields_by_name['timestamp'].message_type = nvidia_dot_clara_dot_platform_dot_common__pb2._TIMESTAMP
_MONITORGPUMETRICSREQUEST.fields_by_name['header'].message_type = nvidia_dot_clara_dot_platform_dot_common__pb2._REQUESTHEADER
_MONITORGPUMETRICSRESPONSE.fields_by_name['header'].message_type = nvidia_dot_clara_dot_platform_dot_common__pb2._RESPONSEHEADER
_MONITORGPUMETRICSRESPONSE.fields_by_name['gpu_details'].message_type = _GPUDETAILS
DESCRIPTOR.message_types_by_name['GpuDetails'] = _GPUDETAILS
DESCRIPTOR.message_types_by_name['MonitorGpuMetricsRequest'] = _MONITORGPUMETRICSREQUEST
DESCRIPTOR.message_types_by_name['MonitorGpuMetricsResponse'] = _MONITORGPUMETRICSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GpuDetails = _reflection.GeneratedProtocolMessageType('GpuDetails', (_message.Message,), {

  'GpuMetrics' : _reflection.GeneratedProtocolMessageType('GpuMetrics', (_message.Message,), {
    'DESCRIPTOR' : _GPUDETAILS_GPUMETRICS,
    '__module__' : 'nvidia.clara.platform.node_monitor.metrics_pb2'
    # @@protoc_insertion_point(class_scope:nvidia.clara.platform.node_monitor.GpuDetails.GpuMetrics)
    })
  ,
  'DESCRIPTOR' : _GPUDETAILS,
  '__module__' : 'nvidia.clara.platform.node_monitor.metrics_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.node_monitor.GpuDetails)
  })
_sym_db.RegisterMessage(GpuDetails)
_sym_db.RegisterMessage(GpuDetails.GpuMetrics)

MonitorGpuMetricsRequest = _reflection.GeneratedProtocolMessageType('MonitorGpuMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MONITORGPUMETRICSREQUEST,
  '__module__' : 'nvidia.clara.platform.node_monitor.metrics_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.node_monitor.MonitorGpuMetricsRequest)
  })
_sym_db.RegisterMessage(MonitorGpuMetricsRequest)

MonitorGpuMetricsResponse = _reflection.GeneratedProtocolMessageType('MonitorGpuMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MONITORGPUMETRICSRESPONSE,
  '__module__' : 'nvidia.clara.platform.node_monitor.metrics_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.clara.platform.node_monitor.MonitorGpuMetricsResponse)
  })
_sym_db.RegisterMessage(MonitorGpuMetricsResponse)


DESCRIPTOR._options = None

_MONITOR = _descriptor.ServiceDescriptor(
  name='Monitor',
  full_name='nvidia.clara.platform.node_monitor.Monitor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=679,
  serialized_end=830,
  methods=[
  _descriptor.MethodDescriptor(
    name='GpuMetrics',
    full_name='nvidia.clara.platform.node_monitor.Monitor.GpuMetrics',
    index=0,
    containing_service=None,
    input_type=_MONITORGPUMETRICSREQUEST,
    output_type=_MONITORGPUMETRICSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MONITOR)

DESCRIPTOR.services_by_name['Monitor'] = _MONITOR

# @@protoc_insertion_point(module_scope)
