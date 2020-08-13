# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.


from enum import Enum
from nvidia_clara.grpc import common_pb2, jobs_pb2
import nvidia_clara.constants as constants


class BaseClient:

    @staticmethod
    def check_response_header(header):

        if not isinstance(header, common_pb2.ResponseHeader):
            raise TypeError("Header arguement must be of type ResponseHeader")

        if header.code < 0:

            if header.messages is not None:

                if len(header.messages) > 0:
                    message_string_list = [header.messages[i] for i in range(len(header.messages))]

                    raise Exception('\n'.join(message_string_list))

                else:
                    raise Exception("Internal Server Error " + str(header.code))

            else:
                raise Exception("Internal Server Error " + str(header.code))

    @staticmethod
    def get_request_header() -> common_pb2.RequestHeader:

        header = common_pb2.RequestHeader(api_version=common_pb2.Version(
            major=constants.ClaraVersionMajor,
            minor=constants.ClaraVersionMinor,
            patch=constants.ClaraVersionPatch),
            user_agent="Nvidia.Clara.Platform")

        return header


class RequestIterator(object):

    def __init__(self, requests):
        self._requests_iter = iter(requests)

    def __call__(self, handler=None):
        while True:
            try:
                request = next(self._requests_iter)
            except StopIteration:
                return
            yield request
