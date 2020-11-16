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
# source: nvidia/clara/platform/clara.proto

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from nvidia_clara.grpc import jobs_pb2 as nvidia_dot_clara_dot_platform_dot_jobs__pb2


class JobsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddMetadata = channel.unary_unary(
        '/nvidia.clara.platform.Jobs/AddMetadata',
        request_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsAddMetadataRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsAddMetadataResponse.FromString,
        )
    self.Cancel = channel.unary_unary(
        '/nvidia.clara.platform.Jobs/Cancel',
        request_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsCancelRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsCancelResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/nvidia.clara.platform.Jobs/Create',
        request_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsCreateRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsCreateResponse.FromString,
        )
    self.List = channel.unary_stream(
        '/nvidia.clara.platform.Jobs/List',
        request_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsListRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsListResponse.FromString,
        )
    self.ReadLogs = channel.unary_stream(
        '/nvidia.clara.platform.Jobs/ReadLogs',
        request_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsReadLogsRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsReadLogsResponse.FromString,
        )
    self.RemoveMetadata = channel.unary_unary(
        '/nvidia.clara.platform.Jobs/RemoveMetadata',
        request_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsRemoveMetadataRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsRemoveMetadataResponse.FromString,
        )
    self.Start = channel.unary_unary(
        '/nvidia.clara.platform.Jobs/Start',
        request_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsStartRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsStartResponse.FromString,
        )
    self.Status = channel.unary_unary(
        '/nvidia.clara.platform.Jobs/Status',
        request_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsStatusRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsStatusResponse.FromString,
        )


class JobsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddMetadata(self, request, context):
    """Requests the addition of metadata to a job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Cancel(self, request, context):
    """Request cancellation of a running job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Requests creation of a new job based on a known pipeline.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Requests a filtered list of all known jobs, or a list of all running jobs if no filter is provided.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadLogs(self, request, context):
    """Requests the download of logs for an operator of a job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveMetadata(self, request, context):
    """Requests the removal of metadata from a job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Start(self, request, context):
    """Request starting of a job created by the Create RPC.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Status(self, request, context):
    """Requests the status of a known job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JobsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.AddMetadata,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsAddMetadataRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsAddMetadataResponse.SerializeToString,
      ),
      'Cancel': grpc.unary_unary_rpc_method_handler(
          servicer.Cancel,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsCancelRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsCancelResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsCreateRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsCreateResponse.SerializeToString,
      ),
      'List': grpc.unary_stream_rpc_method_handler(
          servicer.List,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsListRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsListResponse.SerializeToString,
      ),
      'ReadLogs': grpc.unary_stream_rpc_method_handler(
          servicer.ReadLogs,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsReadLogsRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsReadLogsResponse.SerializeToString,
      ),
      'RemoveMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveMetadata,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsRemoveMetadataRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsRemoveMetadataResponse.SerializeToString,
      ),
      'Start': grpc.unary_unary_rpc_method_handler(
          servicer.Start,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsStartRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsStartResponse.SerializeToString,
      ),
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsStatusRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_jobs__pb2.JobsStatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nvidia.clara.platform.Jobs', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
