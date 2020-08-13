# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

from nvidia_clara.payloads_client import PayloadsClient
import nvidia_clara.payload_types as payload_types

# Client Creation with IP and Port of running instance of Clara

clara_ip_address = "10.0.0.1"
clara_port = "31851"

payload_client = PayloadsClient(target=clara_ip_address, port=clara_port)

# Create static re-usable Payload
payload_details = payload_client.create_payload()

# Delete Payload
payload_client.delete_payload(payload_id=payload_details.payload_id)

# Download from existing Payload ex. Payload with identifier '61a477bf-6bcc-4fdd-abad-ccb8886eb52f' with blob/file name ./input/I114.dcm
example_payload_identifier = '61a477bf-6bcc-4fdd-abad-ccb8886eb52f'

# Create BinaryIO stream object with write permissions and download from payload identifier: example_payload_identifier
with open('output.dcm', 'wb') as wb:
    payload_client.download_from(payload_id=payload_types.PayloadId(example_payload_identifier),
                                 blob_name='./input/I114.dcm',
                                 dest_obj=wb)

# Uploading BinaryIO stream to a new blob
# Create BinaryIO stream with read permissions (for sake of example: reading previous output stream)
with open('output.dcm', 'rb') as rb:
    payload_client.upload(payload_id=payload_types.PayloadId(example_payload_identifier),
                          blob_name='./test/new_blob.dcm', file_object=rb)

# Get Details of a Payload
confirming_details = payload_client.get_details(
    payload_id=payload_types.PayloadId(example_payload_identifier))
