# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from nvidia_clara.grpc import payloads_pb2 as nvidia_dot_clara_dot_platform_dot_payloads__pb2


class PayloadsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/nvidia.clara.platform.Payloads/Create',
        request_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsCreateRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsCreateResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/nvidia.clara.platform.Payloads/Delete',
        request_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDeleteRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDeleteResponse.FromString,
        )
    self.Details = channel.unary_stream(
        '/nvidia.clara.platform.Payloads/Details',
        request_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDetailsRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDetailsResponse.FromString,
        )
    self.Download = channel.unary_stream(
        '/nvidia.clara.platform.Payloads/Download',
        request_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDownloadRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDownloadResponse.FromString,
        )
    self.Remove = channel.unary_unary(
        '/nvidia.clara.platform.Payloads/Remove',
        request_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsRemoveRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsRemoveResponse.FromString,
        )
    self.Upload = channel.stream_unary(
        '/nvidia.clara.platform.Payloads/Upload',
        request_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsUploadRequest.SerializeToString,
        response_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsUploadResponse.FromString,
        )


class PayloadsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    """Requests the creation of a new payload.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Requests the deletion of a known payload.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Details(self, request, context):
    """Requests the details (file listing) of a known payload.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Download(self, request, context):
    """Requests the download of a blob (file) from a known payload.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Remove(self, request, context):
    """Requests the removal, or deltition, of a blob from a known payload.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Upload(self, request_iterator, context):
    """Requests the upload of a blob (file) to a known payload.
    When payload type is PAYLOAD_TYPE_PIPELINE, uploads are written to the ~/input/ folder of the payload.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PayloadsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsCreateRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsCreateResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDeleteRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDeleteResponse.SerializeToString,
      ),
      'Details': grpc.unary_stream_rpc_method_handler(
          servicer.Details,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDetailsRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDetailsResponse.SerializeToString,
      ),
      'Download': grpc.unary_stream_rpc_method_handler(
          servicer.Download,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDownloadRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsDownloadResponse.SerializeToString,
      ),
      'Remove': grpc.unary_unary_rpc_method_handler(
          servicer.Remove,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsRemoveRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsRemoveResponse.SerializeToString,
      ),
      'Upload': grpc.stream_unary_rpc_method_handler(
          servicer.Upload,
          request_deserializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsUploadRequest.FromString,
          response_serializer=nvidia_dot_clara_dot_platform_dot_payloads__pb2.PayloadsUploadResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nvidia.clara.platform.Payloads', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
