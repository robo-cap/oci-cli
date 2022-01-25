# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('os.os_root_group.command_name', 'os'), cls=CommandGroupWithAlias, help=cli_util.override('os.os_root_group.help', """Common set of Object Storage and Archive Storage APIs for managing buckets, objects, and related resources.
For more information, see [Overview of Object Storage] and
[Overview of Archive Storage]."""), short_help=cli_util.override('os.os_root_group.short_help', """Object Storage Service API"""))
@cli_util.help_option_group
def os_root_group():
    pass


@click.command(cli_util.override('os.bucket_group.command_name', 'bucket'), cls=CommandGroupWithAlias, help="""A bucket is a container for storing objects in a compartment within a namespace. A bucket is associated with a single compartment. The compartment has policies that indicate what actions a user can perform on a bucket and all the objects in the bucket. For more information, see [Managing Buckets].

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def bucket_group():
    pass


@click.command(cli_util.override('os.object_lifecycle_policy_group.command_name', 'object-lifecycle-policy'), cls=CommandGroupWithAlias, help="""The collection of lifecycle policy rules that together form the object lifecycle policy of a given bucket.""")
@cli_util.help_option_group
def object_lifecycle_policy_group():
    pass


@click.command(cli_util.override('os.multipart_upload_group.command_name', 'multipart-upload'), cls=CommandGroupWithAlias, help="""Multipart uploads provide efficient and resilient uploads, especially for large objects. Multipart uploads also accommodate objects that are too large for a single upload operation. With multipart uploads, individual parts of an object can be uploaded in parallel to reduce the amount of time you spend uploading. Multipart uploads can also minimize the impact of network failures by letting you retry a failed part upload instead of requiring you to retry an entire object upload. See [Using Multipart Uploads].

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def multipart_upload_group():
    pass


@click.command(cli_util.override('os.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('os.retention_rule_group.command_name', 'retention-rule'), cls=CommandGroupWithAlias, help="""The details of a retention rule.""")
@cli_util.help_option_group
def retention_rule_group():
    pass


@click.command(cli_util.override('os.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('os.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workRequest status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('os.preauthenticated_request_group.command_name', 'preauthenticated-request'), cls=CommandGroupWithAlias, help="""Pre-authenticated requests provide a way to let users access a bucket or an object without having their own credentials. When you create a pre-authenticated request, a unique URL is generated. Users in your organization, partners, or third parties can use this URL to access the targets identified in the pre-authenticated request. See [Using Pre-Authenticated Requests].

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def preauthenticated_request_group():
    pass


@click.command(cli_util.override('os.replication_group.command_name', 'replication'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def replication_group():
    pass


@click.command(cli_util.override('os.namespace_group.command_name', 'namespace'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def namespace_group():
    pass


@click.command(cli_util.override('os.object_group.command_name', 'object'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def object_group():
    pass


os_root_group.add_command(bucket_group)
os_root_group.add_command(object_lifecycle_policy_group)
os_root_group.add_command(multipart_upload_group)
os_root_group.add_command(work_request_error_group)
os_root_group.add_command(retention_rule_group)
os_root_group.add_command(work_request_log_entry_group)
os_root_group.add_command(work_request_group)
os_root_group.add_command(preauthenticated_request_group)
os_root_group.add_command(replication_group)
os_root_group.add_command(namespace_group)
os_root_group.add_command(object_group)


@multipart_upload_group.command(name=cli_util.override('os.abort_multipart_upload.command_name', 'abort'), help=u"""Aborts an in-progress multipart upload and deletes all parts that have been uploaded. \n[Command Reference](abortMultipartUpload)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--upload-id', required=True, help=u"""The upload ID for a multipart upload.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def abort_multipart_upload(ctx, from_json, namespace_name, bucket_name, object_name, upload_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.abort_multipart_upload(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        upload_id=upload_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('os.cancel_work_request.command_name', 'cancel'), help=u"""Cancels a work request. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@multipart_upload_group.command(name=cli_util.override('os.commit_multipart_upload.command_name', 'commit'), help=u"""Commits a multipart upload, which involves checking part numbers and entity tags (ETags) of the parts, to create an aggregate object. \n[Command Reference](commitMultipartUpload)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--upload-id', required=True, help=u"""The upload ID for a multipart upload.""")
@cli_util.option('--parts-to-commit', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The part numbers and entity tags (ETags) for the parts to be committed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parts-to-exclude', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The part numbers for the parts to be excluded from the completed object. Each part created for this upload must be in either partsToExclude or partsToCommit, but cannot be in both.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.""")
@json_skeleton_utils.get_cli_json_input_option({'parts-to-commit': {'module': 'object_storage', 'class': 'list[CommitMultipartUploadPartDetails]'}, 'parts-to-exclude': {'module': 'object_storage', 'class': 'list[integer]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parts-to-commit': {'module': 'object_storage', 'class': 'list[CommitMultipartUploadPartDetails]'}, 'parts-to-exclude': {'module': 'object_storage', 'class': 'list[integer]'}})
@cli_util.wrap_exceptions
def commit_multipart_upload(ctx, from_json, namespace_name, bucket_name, object_name, upload_id, parts_to_commit, parts_to_exclude, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['partsToCommit'] = cli_util.parse_json_parameter("parts_to_commit", parts_to_commit)

    if parts_to_exclude is not None:
        _details['partsToExclude'] = cli_util.parse_json_parameter("parts_to_exclude", parts_to_exclude)

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.commit_multipart_upload(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        upload_id=upload_id,
        commit_multipart_upload_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.copy_object.command_name', 'copy'), help=u"""Creates a request to copy an object within a region or to another region.

See [Object Names] for object naming requirements. \n[Command Reference](copyObject)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--source-object-name', required=True, help=u"""The name of the object to be copied.""")
@cli_util.option('--destination-region', required=True, help=u"""The destination region the object will be copied to, for example \"us-ashburn-1\".""")
@cli_util.option('--destination-namespace', required=True, help=u"""The destination Object Storage namespace the object will be copied to.""")
@cli_util.option('--destination-bucket', required=True, help=u"""The destination bucket the object will be copied to.""")
@cli_util.option('--destination-object-name', required=True, help=u"""The name of the destination object resulting from the copy operation. Avoid entering confidential information.""")
@cli_util.option('--source-object-if-match-e-tag', help=u"""The entity tag (ETag) to match against that of the source object. Used to confirm that the source object with a given name is the version of that object storing a specified ETag.""")
@cli_util.option('--source-version-id', help=u"""VersionId of the object to copy. If not provided then current version is copied by default.""")
@cli_util.option('--destination-object-if-match-e-tag', help=u"""The entity tag (ETag) to match against that of the destination object (an object intended to be overwritten). Used to confirm that the destination object stored under a given name is the version of that object storing a specified entity tag.""")
@cli_util.option('--destination-object-if-none-match-e-tag', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists in the destination bucket.""")
@cli_util.option('--destination-object-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in \"opc-meta-*\" format. Avoid entering confidential information. Metadata key-value pairs entered in this field are assigned to the destination object. If you enter no metadata values, the destination object will inherit any existing metadata values associated with the source object.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--destination-object-storage-tier', type=custom_types.CliCaseInsensitiveChoice(["Standard", "InfrequentAccess", "Archive"]), help=u"""The storage tier that the object should be stored in. If not specified, the object will be stored in the same storage tier as the bucket.""")
@cli_util.option('--opc-sse-customer-algorithm', help=u"""The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key', help=u"""The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key-sha256', help=u"""The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-source-sse-customer-algorithm', help=u"""The optional header that specifies \"AES256\" as the encryption algorithm to use to decrypt the source object. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-source-sse-customer-key', help=u"""The optional header that specifies the base64-encoded 256-bit encryption key to use to decrypt the source object. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-source-sse-customer-key-sha256', help=u"""The optional header that specifies the base64-encoded SHA256 hash of the encryption key used to decrypt the source object. This value is used to check the integrity of the encryption key. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-kms-key-id', help=u"""The [OCID] of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "COMPLETED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'destination-object-metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'destination-object-metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def copy_object(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, bucket_name, source_object_name, destination_region, destination_namespace, destination_bucket, destination_object_name, source_object_if_match_e_tag, source_version_id, destination_object_if_match_e_tag, destination_object_if_none_match_e_tag, destination_object_metadata, destination_object_storage_tier, opc_sse_customer_algorithm, opc_sse_customer_key, opc_sse_customer_key_sha256, opc_source_sse_customer_algorithm, opc_source_sse_customer_key, opc_source_sse_customer_key_sha256, opc_sse_kms_key_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if opc_sse_customer_algorithm is not None:
        kwargs['opc_sse_customer_algorithm'] = opc_sse_customer_algorithm
    if opc_sse_customer_key is not None:
        kwargs['opc_sse_customer_key'] = opc_sse_customer_key
    if opc_sse_customer_key_sha256 is not None:
        kwargs['opc_sse_customer_key_sha256'] = opc_sse_customer_key_sha256
    if opc_source_sse_customer_algorithm is not None:
        kwargs['opc_source_sse_customer_algorithm'] = opc_source_sse_customer_algorithm
    if opc_source_sse_customer_key is not None:
        kwargs['opc_source_sse_customer_key'] = opc_source_sse_customer_key
    if opc_source_sse_customer_key_sha256 is not None:
        kwargs['opc_source_sse_customer_key_sha256'] = opc_source_sse_customer_key_sha256
    if opc_sse_kms_key_id is not None:
        kwargs['opc_sse_kms_key_id'] = opc_sse_kms_key_id
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceObjectName'] = source_object_name
    _details['destinationRegion'] = destination_region
    _details['destinationNamespace'] = destination_namespace
    _details['destinationBucket'] = destination_bucket
    _details['destinationObjectName'] = destination_object_name

    if source_object_if_match_e_tag is not None:
        _details['sourceObjectIfMatchETag'] = source_object_if_match_e_tag

    if source_version_id is not None:
        _details['sourceVersionId'] = source_version_id

    if destination_object_if_match_e_tag is not None:
        _details['destinationObjectIfMatchETag'] = destination_object_if_match_e_tag

    if destination_object_if_none_match_e_tag is not None:
        _details['destinationObjectIfNoneMatchETag'] = destination_object_if_none_match_e_tag

    if destination_object_metadata is not None:
        _details['destinationObjectMetadata'] = cli_util.parse_json_parameter("destination_object_metadata", destination_object_metadata)

    if destination_object_storage_tier is not None:
        _details['destinationObjectStorageTier'] = destination_object_storage_tier

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.copy_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        copy_object_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('os.create_bucket.command_name', 'create'), help=u"""Creates a bucket in the given namespace with a bucket name and optional user-defined metadata. Avoid entering confidential information in bucket names. \n[Command Reference](createBucket)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--name', required=True, help=u"""The name of the bucket. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods. Bucket names must be unique within an Object Storage namespace. Avoid entering confidential information. example: Example: my-new-bucket1""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to create the bucket.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Arbitrary string, up to 4KB, of keys and values for user-defined metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--public-access-type', type=custom_types.CliCaseInsensitiveChoice(["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"]), help=u"""The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.""")
@cli_util.option('--storage-tier', type=custom_types.CliCaseInsensitiveChoice(["Standard", "Archive"]), help=u"""The type of storage tier of this bucket. A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier. When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier' property is immutable after bucket is created.""")
@cli_util.option('--object-events-enabled', type=click.BOOL, help=u"""Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information about events, see [Overview of Events].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The [OCID] of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.""")
@cli_util.option('--versioning', type=custom_types.CliCaseInsensitiveChoice(["Enabled", "Disabled"]), help=u"""Set the versioning status on the bucket. By default, a bucket is created with versioning `Disabled`. Use this option to enable versioning during bucket creation. Objects in a version enabled bucket are protected from overwrites and deletions. Previous versions of the same object will be available in the bucket.""")
@cli_util.option('--auto-tiering', help=u"""Set the auto tiering status on the bucket. By default, a bucket is created with auto tiering `Disabled`. Use this option to enable auto tiering during bucket creation. Objects in a bucket with auto tiering set to `InfrequentAccess` are transitioned automatically between the 'Standard' and 'InfrequentAccess' tiers based on the access pattern of the objects.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'object_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'object_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def create_bucket(ctx, from_json, namespace_name, name, compartment_id, metadata, public_access_type, storage_tier, object_events_enabled, freeform_tags, defined_tags, kms_key_id, versioning, auto_tiering):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if public_access_type is not None:
        _details['publicAccessType'] = public_access_type

    if storage_tier is not None:
        _details['storageTier'] = storage_tier

    if object_events_enabled is not None:
        _details['objectEventsEnabled'] = object_events_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if versioning is not None:
        _details['versioning'] = versioning

    if auto_tiering is not None:
        _details['autoTiering'] = auto_tiering

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.create_bucket(
        namespace_name=namespace_name,
        create_bucket_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@multipart_upload_group.command(name=cli_util.override('os.create_multipart_upload.command_name', 'create'), help=u"""Starts a new multipart upload to a specific object in the given bucket in the given namespace.

See [Object Names] for object naming requirements. \n[Command Reference](createMultipartUpload)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object', required=True, help=u"""The name of the object to which this multi-part upload is targeted. Avoid entering confidential information. Example: test/object1.log""")
@cli_util.option('--content-type', help=u"""The optional Content-Type header that defines the standard MIME type format of the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and perform special operations on text only objects.""")
@cli_util.option('--content-language', help=u"""The optional Content-Language header that defines the content language of the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and differentiate objects based on a particular language.""")
@cli_util.option('--content-encoding', help=u"""The optional Content-Encoding header that defines the content encodings that were applied to the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to determine what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of the object.""")
@cli_util.option('--content-disposition', help=u"""The optional Content-Disposition header that defines presentational information for the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to let users download objects with custom filenames in a browser.""")
@cli_util.option('--cache-control', help=u"""The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions.""")
@cli_util.option('--storage-tier', type=custom_types.CliCaseInsensitiveChoice(["Standard", "InfrequentAccess", "Archive"]), help=u"""The storage tier that the object should be stored in. If not specified, the object will be stored in the same storage tier as the bucket.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in \"opc-meta-*\" format. Avoid entering confidential information.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.""")
@cli_util.option('--opc-sse-customer-algorithm', help=u"""The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key', help=u"""The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key-sha256', help=u"""The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-kms-key-id', help=u"""The [OCID] of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}}, output_type={'module': 'object_storage', 'class': 'MultipartUpload'})
@cli_util.wrap_exceptions
def create_multipart_upload(ctx, from_json, namespace_name, bucket_name, object, content_type, content_language, content_encoding, content_disposition, cache_control, storage_tier, metadata, if_match, if_none_match, opc_sse_customer_algorithm, opc_sse_customer_key, opc_sse_customer_key_sha256, opc_sse_kms_key_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if opc_sse_customer_algorithm is not None:
        kwargs['opc_sse_customer_algorithm'] = opc_sse_customer_algorithm
    if opc_sse_customer_key is not None:
        kwargs['opc_sse_customer_key'] = opc_sse_customer_key
    if opc_sse_customer_key_sha256 is not None:
        kwargs['opc_sse_customer_key_sha256'] = opc_sse_customer_key_sha256
    if opc_sse_kms_key_id is not None:
        kwargs['opc_sse_kms_key_id'] = opc_sse_kms_key_id
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['object'] = object

    if content_type is not None:
        _details['contentType'] = content_type

    if content_language is not None:
        _details['contentLanguage'] = content_language

    if content_encoding is not None:
        _details['contentEncoding'] = content_encoding

    if content_disposition is not None:
        _details['contentDisposition'] = content_disposition

    if cache_control is not None:
        _details['cacheControl'] = cache_control

    if storage_tier is not None:
        _details['storageTier'] = storage_tier

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.create_multipart_upload(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        create_multipart_upload_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('os.create_preauthenticated_request.command_name', 'create'), help=u"""Creates a pre-authenticated request specific to the bucket. \n[Command Reference](createPreauthenticatedRequest)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--name', required=True, help=u"""A user-specified name for the pre-authenticated request. Names can be helpful in managing pre-authenticated requests. Avoid entering confidential information.""")
@cli_util.option('--access-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite", "AnyObjectRead", "AnyObjectReadWrite"]), help=u"""The operation that can be performed on this resource.""")
@cli_util.option('--time-expires', required=True, type=custom_types.CLI_DATETIME, help=u"""The expiration date for the pre-authenticated request as per [RFC 3339]. After this date the pre-authenticated request will no longer be valid.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--bucket-listing-action', help=u"""Specifies whether a list operation is allowed on a PAR with accessType \"AnyObjectRead\" or \"AnyObjectReadWrite\". Deny: Prevents the user from performing a list operation. ListObjects: Authorizes the user to perform a list operation.""")
@cli_util.option('--object-name', help=u"""The name of the object that is being granted access to by the pre-authenticated request. Avoid entering confidential information. The object name can be null and if so, the pre-authenticated request grants access to the entire bucket if the access type allows that. The object name can be a prefix as well, in that case pre-authenticated request grants access to all the objects within the bucket starting with that prefix provided that we have the correct access type.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'PreauthenticatedRequest'})
@cli_util.wrap_exceptions
def create_preauthenticated_request(ctx, from_json, namespace_name, bucket_name, name, access_type, time_expires, bucket_listing_action, object_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['accessType'] = access_type
    _details['timeExpires'] = time_expires

    if bucket_listing_action is not None:
        _details['bucketListingAction'] = bucket_listing_action

    if object_name is not None:
        _details['objectName'] = object_name

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.create_preauthenticated_request(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        create_preauthenticated_request_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@replication_group.command(name=cli_util.override('os.create_replication_policy.command_name', 'create-replication-policy'), help=u"""Creates a replication policy for the specified bucket. \n[Command Reference](createReplicationPolicy)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--name', required=True, help=u"""The name of the policy. Avoid entering confidential information.""")
@cli_util.option('--destination-region-name', required=True, help=u"""The destination region to replicate to, for example \"us-ashburn-1\".""")
@cli_util.option('--destination-bucket-name', required=True, help=u"""The bucket to replicate to in the destination region. Replication policy creation does not automatically create a destination bucket. Create the destination bucket before creating the policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ReplicationPolicy'})
@cli_util.wrap_exceptions
def create_replication_policy(ctx, from_json, namespace_name, bucket_name, name, destination_region_name, destination_bucket_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['destinationRegionName'] = destination_region_name
    _details['destinationBucketName'] = destination_bucket_name

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.create_replication_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        create_replication_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@retention_rule_group.command(name=cli_util.override('os.create_retention_rule.command_name', 'create'), help=u"""Creates a new retention rule in the specified bucket. The new rule will take effect typically within 30 seconds. Note that a maximum of 100 rules are supported on a bucket. \n[Command Reference](createRetentionRule)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--display-name', help=u"""A user-specified name for the retention rule. Names can be helpful in identifying retention rules. Avoid entering confidential information.""")
@cli_util.option('--duration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-rule-locked', type=custom_types.CLI_DATETIME, help=u"""The date and time as per [RFC 3339] after which this rule is locked and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are allowed and no other properties can be changed. This property cannot be updated for rules that are in a locked state. Specifying it when a duration is not specified is considered an error.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({'duration': {'module': 'object_storage', 'class': 'Duration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'duration': {'module': 'object_storage', 'class': 'Duration'}}, output_type={'module': 'object_storage', 'class': 'RetentionRule'})
@cli_util.wrap_exceptions
def create_retention_rule(ctx, from_json, namespace_name, bucket_name, display_name, duration, time_rule_locked):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if duration is not None:
        _details['duration'] = cli_util.parse_json_parameter("duration", duration)

    if time_rule_locked is not None:
        _details['timeRuleLocked'] = time_rule_locked

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.create_retention_rule(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        create_retention_rule_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('os.delete_bucket.command_name', 'delete'), help=u"""Deletes a bucket if the bucket is already empty. If the bucket is not empty, use [DeleteObject] first. In addition, you cannot delete a bucket that has a multipart upload in progress or a pre-authenticated request associated with that bucket. \n[Command Reference](deleteBucket)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_bucket(ctx, from_json, namespace_name, bucket_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.delete_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.delete_object.command_name', 'delete'), help=u"""Deletes an object. \n[Command Reference](deleteObject)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--version-id', help=u"""VersionId used to identify a particular version of the object""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_object(ctx, from_json, namespace_name, bucket_name, object_name, if_match, version_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if version_id is not None:
        kwargs['version_id'] = version_id
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.delete_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_lifecycle_policy_group.command(name=cli_util.override('os.delete_object_lifecycle_policy.command_name', 'delete'), help=u"""Deletes the object lifecycle policy for the bucket. \n[Command Reference](deleteObjectLifecyclePolicy)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_object_lifecycle_policy(ctx, from_json, namespace_name, bucket_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.delete_object_lifecycle_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('os.delete_preauthenticated_request.command_name', 'delete'), help=u"""Deletes the pre-authenticated request for the bucket. \n[Command Reference](deletePreauthenticatedRequest)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--par-id', required=True, help=u"""The unique identifier for the pre-authenticated request. This can be used to manage operations against the pre-authenticated request, such as GET or DELETE.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_preauthenticated_request(ctx, from_json, namespace_name, bucket_name, par_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(par_id, six.string_types) and len(par_id.strip()) == 0:
        raise click.UsageError('Parameter --par-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.delete_preauthenticated_request(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        par_id=par_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@replication_group.command(name=cli_util.override('os.delete_replication_policy.command_name', 'delete-replication-policy'), help=u"""Deletes the replication policy associated with the source bucket. \n[Command Reference](deleteReplicationPolicy)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--replication-id', required=True, help=u"""The ID of the replication policy.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_replication_policy(ctx, from_json, namespace_name, bucket_name, replication_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(replication_id, six.string_types) and len(replication_id.strip()) == 0:
        raise click.UsageError('Parameter --replication-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.delete_replication_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        replication_id=replication_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@retention_rule_group.command(name=cli_util.override('os.delete_retention_rule.command_name', 'delete'), help=u"""Deletes the specified rule. The deletion takes effect typically within 30 seconds. \n[Command Reference](deleteRetentionRule)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--retention-rule-id', required=True, help=u"""The ID of the retention rule.""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_retention_rule(ctx, from_json, namespace_name, bucket_name, retention_rule_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(retention_rule_id, six.string_types) and len(retention_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --retention-rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.delete_retention_rule(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        retention_rule_id=retention_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('os.get_bucket.command_name', 'get'), help=u"""Gets the current representation of the given bucket in the given Object Storage namespace. \n[Command Reference](getBucket)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not match the ETag of the existing resource, the request returns the expected response. If the ETag matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["approximateCount", "approximateSize", "autoTiering"]), multiple=True, help=u"""Bucket summary includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated', and 'etag' fields. This parameter can also include 'approximateCount' (approximate number of objects), 'approximateSize' (total approximate size in bytes of all objects) and 'autoTiering' (state of auto tiering on the bucket). For example 'approximateCount,approximateSize,autoTiering'.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def get_bucket(ctx, from_json, namespace_name, bucket_name, if_match, if_none_match, fields):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('os.get_namespace.command_name', 'get'), help=u"""Each Oracle Cloud Infrastructure tenant is assigned one unique and uneditable Object Storage namespace. The namespace is a system-generated string assigned during account creation. For some older tenancies, the namespace string may be the tenancy name in all lower-case letters. You cannot edit a namespace.

GetNamespace returns the name of the Object Storage namespace for the user making the request. If an optional compartmentId query parameter is provided, GetNamespace returns the namespace name of the corresponding tenancy, provided the user has access to it. \n[Command Reference](getNamespace)""")
@cli_util.option('--compartment-id', help=u"""This is an optional field representing either the tenancy [OCID] or the compartment [OCID] within the tenancy whose Object Storage namespace is to be retrieved.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_namespace(ctx, from_json, compartment_id):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_namespace(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('os.get_namespace_metadata.command_name', 'get-namespace-metadata'), help=u"""Gets the metadata for the Object Storage namespace, which contains defaultS3CompartmentId and defaultSwiftCompartmentId.

Any user with the OBJECTSTORAGE_NAMESPACE_READ permission will be able to see the current metadata. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies]. \n[Command Reference](getNamespaceMetadata)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'NamespaceMetadata'})
@cli_util.wrap_exceptions
def get_namespace_metadata(ctx, from_json, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_namespace_metadata(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.get_object.command_name', 'get'), help=u"""Gets the metadata and body of an object. \n[Command Reference](getObject)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--version-id', help=u"""VersionId used to identify a particular version of the object""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not match the ETag of the existing resource, the request returns the expected response. If the ETag matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.""")
@cli_util.option('--range', help=u"""Optional byte range to fetch, as described in [RFC 7233]. Note that only a single range of bytes is supported.""")
@cli_util.option('--opc-sse-customer-algorithm', help=u"""The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key', help=u"""The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key-sha256', help=u"""The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--http-response-content-disposition', help=u"""Specify this query parameter to override the value of the Content-Disposition response header in the GetObject response.""")
@cli_util.option('--http-response-cache-control', help=u"""Specify this query parameter to override the Cache-Control response header in the GetObject response.""")
@cli_util.option('--http-response-content-type', help=u"""Specify this query parameter to override the Content-Type response header in the GetObject response.""")
@cli_util.option('--http-response-content-language', help=u"""Specify this query parameter to override the Content-Language response header in the GetObject response.""")
@cli_util.option('--http-response-content-encoding', help=u"""Specify this query parameter to override the Content-Encoding response header in the GetObject response.""")
@cli_util.option('--http-response-expires', help=u"""Specify this query parameter to override the Expires response header in the GetObject response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_object(ctx, from_json, file, namespace_name, bucket_name, object_name, version_id, if_match, if_none_match, range, opc_sse_customer_algorithm, opc_sse_customer_key, opc_sse_customer_key_sha256, http_response_content_disposition, http_response_cache_control, http_response_content_type, http_response_content_language, http_response_content_encoding, http_response_expires):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    if version_id is not None:
        kwargs['version_id'] = version_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if range is not None:
        kwargs['range'] = range
    if opc_sse_customer_algorithm is not None:
        kwargs['opc_sse_customer_algorithm'] = opc_sse_customer_algorithm
    if opc_sse_customer_key is not None:
        kwargs['opc_sse_customer_key'] = opc_sse_customer_key
    if opc_sse_customer_key_sha256 is not None:
        kwargs['opc_sse_customer_key_sha256'] = opc_sse_customer_key_sha256
    if http_response_content_disposition is not None:
        kwargs['http_response_content_disposition'] = http_response_content_disposition
    if http_response_cache_control is not None:
        kwargs['http_response_cache_control'] = http_response_cache_control
    if http_response_content_type is not None:
        kwargs['http_response_content_type'] = http_response_content_type
    if http_response_content_language is not None:
        kwargs['http_response_content_language'] = http_response_content_language
    if http_response_content_encoding is not None:
        kwargs['http_response_content_encoding'] = http_response_content_encoding
    if http_response_expires is not None:
        kwargs['http_response_expires'] = http_response_expires
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@object_lifecycle_policy_group.command(name=cli_util.override('os.get_object_lifecycle_policy.command_name', 'get'), help=u"""Gets the object lifecycle policy for the bucket. \n[Command Reference](getObjectLifecyclePolicy)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ObjectLifecyclePolicy'})
@cli_util.wrap_exceptions
def get_object_lifecycle_policy(ctx, from_json, namespace_name, bucket_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_object_lifecycle_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('os.get_preauthenticated_request.command_name', 'get'), help=u"""Gets the pre-authenticated request for the bucket. \n[Command Reference](getPreauthenticatedRequest)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--par-id', required=True, help=u"""The unique identifier for the pre-authenticated request. This can be used to manage operations against the pre-authenticated request, such as GET or DELETE.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'PreauthenticatedRequestSummary'})
@cli_util.wrap_exceptions
def get_preauthenticated_request(ctx, from_json, namespace_name, bucket_name, par_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(par_id, six.string_types) and len(par_id.strip()) == 0:
        raise click.UsageError('Parameter --par-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_preauthenticated_request(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        par_id=par_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@replication_group.command(name=cli_util.override('os.get_replication_policy.command_name', 'get-replication-policy'), help=u"""Get the replication policy. \n[Command Reference](getReplicationPolicy)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--replication-id', required=True, help=u"""The ID of the replication policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ReplicationPolicy'})
@cli_util.wrap_exceptions
def get_replication_policy(ctx, from_json, namespace_name, bucket_name, replication_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(replication_id, six.string_types) and len(replication_id.strip()) == 0:
        raise click.UsageError('Parameter --replication-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_replication_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        replication_id=replication_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@retention_rule_group.command(name=cli_util.override('os.get_retention_rule.command_name', 'get'), help=u"""Get the specified retention rule. \n[Command Reference](getRetentionRule)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--retention-rule-id', required=True, help=u"""The ID of the retention rule.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'RetentionRule'})
@cli_util.wrap_exceptions
def get_retention_rule(ctx, from_json, namespace_name, bucket_name, retention_rule_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(retention_rule_id, six.string_types) and len(retention_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --retention-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_retention_rule(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        retention_rule_id=retention_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('os.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request for the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('os.head_bucket.command_name', 'head'), help=u"""Efficiently checks to see if a bucket exists and gets the current entity tag (ETag) for the bucket. \n[Command Reference](headBucket)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not match the ETag of the existing resource, the request returns the expected response. If the ETag matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_bucket(ctx, from_json, namespace_name, bucket_name, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.head_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.head_object.command_name', 'head'), help=u"""Gets the user-defined metadata and entity tag (ETag) for an object. \n[Command Reference](headObject)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--version-id', help=u"""VersionId used to identify a particular version of the object""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not match the ETag of the existing resource, the request returns the expected response. If the ETag matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.""")
@cli_util.option('--opc-sse-customer-algorithm', help=u"""The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key', help=u"""The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key-sha256', help=u"""The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_object(ctx, from_json, namespace_name, bucket_name, object_name, version_id, if_match, if_none_match, opc_sse_customer_algorithm, opc_sse_customer_key, opc_sse_customer_key_sha256):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    if version_id is not None:
        kwargs['version_id'] = version_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if opc_sse_customer_algorithm is not None:
        kwargs['opc_sse_customer_algorithm'] = opc_sse_customer_algorithm
    if opc_sse_customer_key is not None:
        kwargs['opc_sse_customer_key'] = opc_sse_customer_key
    if opc_sse_customer_key_sha256 is not None:
        kwargs['opc_sse_customer_key_sha256'] = opc_sse_customer_key_sha256
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.head_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('os.list_buckets.command_name', 'list'), help=u"""Gets a list of all BucketSummary items in a compartment. A BucketSummary contains only summary fields for the bucket and does not contain fields like the user-defined metadata.

ListBuckets returns a BucketSummary containing at most 1000 buckets. To paginate through more buckets, use the returned `opc-next-page` value with the `page` request parameter.

To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies]. \n[Command Reference](listBuckets)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list buckets.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["tags"]), multiple=True, help=u"""Bucket summary in list of buckets includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated', and 'etag' fields. This parameter can also include 'tags' (freeformTags and definedTags). The only supported value of this parameter is 'tags' for now. Example 'tags'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[BucketSummary]'})
@cli_util.wrap_exceptions
def list_buckets(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, limit, page, fields):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_buckets,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_buckets,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_buckets(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@multipart_upload_group.command(name=cli_util.override('os.list_multipart_upload_parts.command_name', 'list-multipart-upload-parts'), help=u"""Lists the parts of an in-progress multipart upload. \n[Command Reference](listMultipartUploadParts)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--upload-id', required=True, help=u"""The upload ID for a multipart upload.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[MultipartUploadPartSummary]'})
@cli_util.wrap_exceptions
def list_multipart_upload_parts(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, object_name, upload_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_multipart_upload_parts,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            object_name=object_name,
            upload_id=upload_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_multipart_upload_parts,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            object_name=object_name,
            upload_id=upload_id,
            **kwargs
        )
    else:
        result = client.list_multipart_upload_parts(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            object_name=object_name,
            upload_id=upload_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@multipart_upload_group.command(name=cli_util.override('os.list_multipart_uploads.command_name', 'list'), help=u"""Lists all of the in-progress multipart uploads for the given bucket in the given Object Storage namespace. \n[Command Reference](listMultipartUploads)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[MultipartUpload]'})
@cli_util.wrap_exceptions
def list_multipart_uploads(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_multipart_uploads,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_multipart_uploads,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    else:
        result = client.list_multipart_uploads(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.list_object_versions.command_name', 'list-object-versions'), help=u"""Lists the object versions in a bucket.

ListObjectVersions returns an ObjectVersionCollection containing at most 1000 object versions. To paginate through more object versions, use the returned `opc-next-page` value with the `page` request parameter.

To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies]. \n[Command Reference](listObjectVersions)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--prefix', help=u"""The string to use for matching against the start of object names in a list query.""")
@cli_util.option('--start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--delimiter', help=u"""When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.""")
@cli_util.option('--fields', help=u"""Object summary by default includes only the 'name' field. Use this parameter to also include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time), 'timeModified' (object modification date and time), 'storageTier' and 'archivalState' fields. Specify the value of this parameter as a comma-separated, case-insensitive list of those field names. For example 'name,etag,timeCreated,md5,timeModified,storageTier,archivalState'. Allowed values are: name, size, etag, timeCreated, md5, timeModified, storageTier, archivalState""")
@cli_util.option('--start-after', help=u"""Object names returned by a list query must be greater than this parameter.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ObjectVersionCollection'})
@cli_util.wrap_exceptions
def list_object_versions(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, prefix, start, end, limit, delimiter, fields, start_after, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if prefix is not None:
        kwargs['prefix'] = prefix
    if start is not None:
        kwargs['start'] = start
    if end is not None:
        kwargs['end'] = end
    if limit is not None:
        kwargs['limit'] = limit
    if delimiter is not None:
        kwargs['delimiter'] = delimiter
    if fields is not None:
        kwargs['fields'] = fields
    if start_after is not None:
        kwargs['start_after'] = start_after
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_object_versions,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_object_versions,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    else:
        result = client.list_object_versions(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.list_objects.command_name', 'list'), help=u"""Lists the objects in a bucket. By default, ListObjects returns object names only. See the `fields` parameter for other fields that you can optionally include in ListObjects response.

ListObjects returns at most 1000 objects. To paginate through more objects, use the returned 'nextStartWith' value with the 'start' parameter. To filter which objects ListObjects returns, use the 'start' and 'end' parameters.

To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies]. \n[Command Reference](listObjects)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--prefix', help=u"""The string to use for matching against the start of object names in a list query.""")
@cli_util.option('--start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--delimiter', help=u"""When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.""")
@cli_util.option('--fields', help=u"""Object summary by default includes only the 'name' field. Use this parameter to also include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time), 'timeModified' (object modification date and time), 'storageTier' and 'archivalState' fields. Specify the value of this parameter as a comma-separated, case-insensitive list of those field names. For example 'name,etag,timeCreated,md5,timeModified,storageTier,archivalState'. Allowed values are: name, size, etag, timeCreated, md5, timeModified, storageTier, archivalState""")
@cli_util.option('--start-after', help=u"""Object names returned by a list query must be greater than this parameter.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ListObjects'})
@cli_util.wrap_exceptions
def list_objects(ctx, from_json, all_pages, namespace_name, bucket_name, prefix, start, end, limit, delimiter, fields, start_after):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if prefix is not None:
        kwargs['prefix'] = prefix
    if start is not None:
        kwargs['start'] = start
    if end is not None:
        kwargs['end'] = end
    if limit is not None:
        kwargs['limit'] = limit
    if delimiter is not None:
        kwargs['delimiter'] = delimiter
    if fields is not None:
        kwargs['fields'] = fields
    if start_after is not None:
        kwargs['start_after'] = start_after
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.list_objects(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('os.list_preauthenticated_requests.command_name', 'list'), help=u"""Lists pre-authenticated requests for the bucket. \n[Command Reference](listPreauthenticatedRequests)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name-prefix', help=u"""User-specified object name prefixes can be used to query and return a list of pre-authenticated requests.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[PreauthenticatedRequestSummary]'})
@cli_util.wrap_exceptions
def list_preauthenticated_requests(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, object_name_prefix, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if object_name_prefix is not None:
        kwargs['object_name_prefix'] = object_name_prefix
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_preauthenticated_requests,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_preauthenticated_requests,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    else:
        result = client.list_preauthenticated_requests(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@replication_group.command(name=cli_util.override('os.list_replication_policies.command_name', 'list-replication-policies'), help=u"""List the replication policies associated with a bucket. \n[Command Reference](listReplicationPolicies)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[ReplicationPolicySummary]'})
@cli_util.wrap_exceptions
def list_replication_policies(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_replication_policies,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_replication_policies,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    else:
        result = client.list_replication_policies(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@replication_group.command(name=cli_util.override('os.list_replication_sources.command_name', 'list-replication-sources'), help=u"""List the replication sources of a destination bucket. \n[Command Reference](listReplicationSources)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[ReplicationSource]'})
@cli_util.wrap_exceptions
def list_replication_sources(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_replication_sources,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_replication_sources,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    else:
        result = client.list_replication_sources(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@retention_rule_group.command(name=cli_util.override('os.list_retention_rules.command_name', 'list'), help=u"""List the retention rules for a bucket. The retention rules are sorted based on creation time, with the most recently created retention rule returned first. \n[Command Reference](listRetentionRules)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'RetentionRuleCollection'})
@cli_util.wrap_exceptions
def list_retention_rules(ctx, from_json, all_pages, namespace_name, bucket_name, page):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_retention_rules,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    else:
        result = client.list_retention_rules(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('os.list_work_request_errors.command_name', 'list'), help=u"""Lists the errors of the work request with the given ID. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('os.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Lists the logs of the work request with the given ID. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('os.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list buckets.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@replication_group.command(name=cli_util.override('os.make_bucket_writable.command_name', 'make-bucket-writable'), help=u"""Stops replication to the destination bucket and removes the replication policy. When the replication policy was created, this destination bucket became read-only except for new and changed objects replicated automatically from the source bucket. MakeBucketWritable removes the replication policy. This bucket is no longer the target for replication and is now writable, allowing users to make changes to bucket contents. \n[Command Reference](makeBucketWritable)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def make_bucket_writable(ctx, from_json, namespace_name, bucket_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.make_bucket_writable(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.put_object.command_name', 'put'), help=u"""Creates a new object or overwrites an existing object with the same name. The maximum object size allowed by PutObject is 50 GiB.

See [Object Names] for object naming requirements.

See [Special Instructions for Object Storage PUT] for request signature requirements. \n[Command Reference](putObject)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--put-object-body', required=True, help=u"""The object to upload to the object store.""")
@cli_util.option('--content-length', type=click.INT, help=u"""The content length of the body.""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.""")
@cli_util.option('--expect', help=u"""A value of `100-continue` requests preliminary verification of the request method, path, and headers before the request body is sent. If no error results from such verification, the server will send a 100 (Continue) interim response to indicate readiness for the request body. The only allowed value for this parameter is \"100-Continue\" (case-insensitive).""")
@cli_util.option('--content-md5', help=u"""The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error is returned with the message:

\"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)\"""")
@cli_util.option('--content-type', help=u"""The optional Content-Type header that defines the standard MIME type format of the object. Content type defaults to 'application/octet-stream' if not specified in the PutObject call. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and perform special operations on text only objects.""")
@cli_util.option('--content-language', help=u"""The optional Content-Language header that defines the content language of the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and differentiate objects based on a particular language.""")
@cli_util.option('--content-encoding', help=u"""The optional Content-Encoding header that defines the content encodings that were applied to the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to determine what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of the object.""")
@cli_util.option('--content-disposition', help=u"""The optional Content-Disposition header that defines presentational information for the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to let users download objects with custom filenames in a browser.""")
@cli_util.option('--cache-control', help=u"""The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions.""")
@cli_util.option('--opc-sse-customer-algorithm', help=u"""The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key', help=u"""The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key-sha256', help=u"""The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-kms-key-id', help=u"""The [OCID] of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.""")
@cli_util.option('--storage-tier', type=custom_types.CliCaseInsensitiveChoice(["Standard", "InfrequentAccess", "Archive"]), help=u"""The storage tier that the object should be stored in. If not specified, the object will be stored in the same storage tier as the bucket.""")
@cli_util.option('--opc-meta-', help=u"""Optional user-defined metadata key and value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def put_object(ctx, from_json, namespace_name, bucket_name, object_name, put_object_body, content_length, if_match, if_none_match, expect, content_md5, content_type, content_language, content_encoding, content_disposition, cache_control, opc_sse_customer_algorithm, opc_sse_customer_key, opc_sse_customer_key_sha256, opc_sse_kms_key_id, storage_tier, opc_meta_):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    if content_length is not None:
        kwargs['content_length'] = content_length
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if expect is not None:
        kwargs['expect'] = expect
    if content_md5 is not None:
        kwargs['content_md5'] = content_md5
    if content_type is not None:
        kwargs['content_type'] = content_type
    if content_language is not None:
        kwargs['content_language'] = content_language
    if content_encoding is not None:
        kwargs['content_encoding'] = content_encoding
    if content_disposition is not None:
        kwargs['content_disposition'] = content_disposition
    if cache_control is not None:
        kwargs['cache_control'] = cache_control
    if opc_sse_customer_algorithm is not None:
        kwargs['opc_sse_customer_algorithm'] = opc_sse_customer_algorithm
    if opc_sse_customer_key is not None:
        kwargs['opc_sse_customer_key'] = opc_sse_customer_key
    if opc_sse_customer_key_sha256 is not None:
        kwargs['opc_sse_customer_key_sha256'] = opc_sse_customer_key_sha256
    if opc_sse_kms_key_id is not None:
        kwargs['opc_sse_kms_key_id'] = opc_sse_kms_key_id
    if storage_tier is not None:
        kwargs['storage_tier'] = storage_tier
    if opc_meta_ is not None:
        kwargs['opc_meta_'] = opc_meta_
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.put_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        put_object_body=put_object_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_lifecycle_policy_group.command(name=cli_util.override('os.put_object_lifecycle_policy.command_name', 'put'), help=u"""Creates or replaces the object lifecycle policy for the bucket. \n[Command Reference](putObjectLifecyclePolicy)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The bucket's set of lifecycle policy rules.

This option is a JSON list with items of type ObjectLifecycleRule.  For documentation on ObjectLifecycleRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/objectstorage/20160918/datatypes/ObjectLifecycleRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'object_storage', 'class': 'list[ObjectLifecycleRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'object_storage', 'class': 'list[ObjectLifecycleRule]'}}, output_type={'module': 'object_storage', 'class': 'ObjectLifecyclePolicy'})
@cli_util.wrap_exceptions
def put_object_lifecycle_policy(ctx, from_json, force, namespace_name, bucket_name, items, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    if not force:
        if items:
            if not click.confirm("WARNING: Updates to items will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.put_object_lifecycle_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        put_object_lifecycle_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('os.reencrypt_bucket.command_name', 'reencrypt'), help=u"""Re-encrypts the unique data encryption key that encrypts each object written to the bucket by using the most recent version of the master encryption key assigned to the bucket. (All data encryption keys are encrypted by a master encryption key. Master encryption keys are assigned to buckets and managed by Oracle by default, but you can assign a key that you created and control through the Oracle Cloud Infrastructure Key Management service.) The kmsKeyId property of the bucket determines which master encryption key is assigned to the bucket. If you assigned a different Key Management master encryption key to the bucket, you can call this API to re-encrypt all data encryption keys with the newly assigned key. Similarly, you might want to re-encrypt all data encryption keys if the assigned key has been rotated to a new key version since objects were last added to the bucket. If you call this API and there is no kmsKeyId associated with the bucket, the call will fail.

Calling this API starts a work request task to re-encrypt the data encryption key of all objects in the bucket. Only objects created before the time of the API call will be re-encrypted. The call can take a long time, depending on how many objects are in the bucket and how big they are. This API returns a work request ID that you can use to retrieve the status of the work request task. All the versions of objects will be re-encrypted whether versioning is enabled or suspended at the bucket. \n[Command Reference](reencryptBucket)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "COMPLETED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def reencrypt_bucket(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, bucket_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.reencrypt_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.reencrypt_object.command_name', 'reencrypt'), help=u"""Re-encrypts the data encryption keys that encrypt the object and its chunks. By default, when you create a bucket, the Object Storage service manages the master encryption key used to encrypt each object's data encryption keys. The encryption mechanism that you specify for the bucket applies to the objects it contains.

You can alternatively employ one of these encryption strategies for an object:

- You can assign a key that you created and control through the Oracle Cloud Infrastructure Vault service.

- You can encrypt an object using your own encryption key. The key you supply is known as a customer-provided encryption key (SSE-C). \n[Command Reference](reencryptObject)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--kms-key-id', help=u"""The [OCID] of the master encryption key used to call the Vault service to re-encrypt the data encryption keys associated with the object and its chunks. If the kmsKeyId value is empty, whether null or an empty string, the API will perform re-encryption by using the kmsKeyId associated with the bucket or the master encryption key managed by Oracle, depending on the bucket encryption mechanism.""")
@cli_util.option('--sse-customer-key', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-sse-customer-key', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--version-id', help=u"""VersionId used to identify a particular version of the object""")
@json_skeleton_utils.get_cli_json_input_option({'sse-customer-key': {'module': 'object_storage', 'class': 'SSECustomerKeyDetails'}, 'source-sse-customer-key': {'module': 'object_storage', 'class': 'SSECustomerKeyDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sse-customer-key': {'module': 'object_storage', 'class': 'SSECustomerKeyDetails'}, 'source-sse-customer-key': {'module': 'object_storage', 'class': 'SSECustomerKeyDetails'}})
@cli_util.wrap_exceptions
def reencrypt_object(ctx, from_json, namespace_name, bucket_name, object_name, kms_key_id, sse_customer_key, source_sse_customer_key, version_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    if version_id is not None:
        kwargs['version_id'] = version_id
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if sse_customer_key is not None:
        _details['sseCustomerKey'] = cli_util.parse_json_parameter("sse_customer_key", sse_customer_key)

    if source_sse_customer_key is not None:
        _details['sourceSseCustomerKey'] = cli_util.parse_json_parameter("source_sse_customer_key", source_sse_customer_key)

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.reencrypt_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        reencrypt_object_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.rename_object.command_name', 'rename'), help=u"""Rename an object in the given Object Storage namespace.

See [Object Names] for object naming requirements. \n[Command Reference](renameObject)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--source-name', required=True, help=u"""The name of the source object to be renamed.""")
@cli_util.option('--new-name', required=True, help=u"""The new name of the source object. Avoid entering confidential information.""")
@cli_util.option('--src-obj-if-match-e-tag', help=u"""The if-match entity tag (ETag) of the source object.""")
@cli_util.option('--new-obj-if-match-e-tag', help=u"""The if-match entity tag (ETag) of the new object.""")
@cli_util.option('--new-obj-if-none-match-e-tag', help=u"""The if-none-match entity tag (ETag) of the new object. The only valid value is '*', which indicates request should fail if the new object already exists.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def rename_object(ctx, from_json, namespace_name, bucket_name, source_name, new_name, src_obj_if_match_e_tag, new_obj_if_match_e_tag, new_obj_if_none_match_e_tag):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceName'] = source_name
    _details['newName'] = new_name

    if src_obj_if_match_e_tag is not None:
        _details['srcObjIfMatchETag'] = src_obj_if_match_e_tag

    if new_obj_if_match_e_tag is not None:
        _details['newObjIfMatchETag'] = new_obj_if_match_e_tag

    if new_obj_if_none_match_e_tag is not None:
        _details['newObjIfNoneMatchETag'] = new_obj_if_none_match_e_tag

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.rename_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        rename_object_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.restore_objects.command_name', 'restore'), help=u"""Restores one or more objects specified by the objectName parameter. By default objects will be restored for 24 hours. Duration can be configured using the hours parameter. \n[Command Reference](restoreObjects)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""An object that is in an archive storage tier and needs to be restored.""")
@cli_util.option('--hours', type=click.INT, help=u"""The number of hours for which this object will be restored. By default objects will be restored for 24 hours. You can instead configure the duration using the hours parameter.""")
@cli_util.option('--version-id', help=u"""The versionId of the object to restore. Current object version is used by default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def restore_objects(ctx, from_json, namespace_name, bucket_name, object_name, hours, version_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['objectName'] = object_name

    if hours is not None:
        _details['hours'] = hours

    if version_id is not None:
        _details['versionId'] = version_id

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.restore_objects(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        restore_objects_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('os.update_bucket.command_name', 'update'), help=u"""Performs a partial or full update of a bucket's user-defined metadata.

Use UpdateBucket to move a bucket from one compartment to another within the same tenancy. Supply the compartmentID of the compartment that you want to move the bucket to. For more information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](updateBucket)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--compartment-id', help=u"""The compartmentId for the compartment to move the bucket to.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Arbitrary string, up to 4KB, of keys and values for user-defined metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--public-access-type', type=custom_types.CliCaseInsensitiveChoice(["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"]), help=u"""The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.""")
@cli_util.option('--object-events-enabled', type=click.BOOL, help=u"""Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information about events, see [Overview of Events].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The [OCID] of the Key Management master encryption key to associate with the specified bucket. If this value is empty, the Update operation will remove the associated key, if there is one, from the bucket. (The bucket will continue to be encrypted, but with an encryption key managed by Oracle.)""")
@cli_util.option('--versioning', type=custom_types.CliCaseInsensitiveChoice(["Enabled", "Suspended"]), help=u"""The versioning status on the bucket. If in state `Enabled`, multiple versions of the same object can be kept in the bucket. When the object is overwritten or deleted, previous versions will still be available. When versioning is `Suspended`, the previous versions will still remain but new versions will no longer be created when overwitten or deleted. Versioning cannot be disabled on a bucket once enabled.""")
@cli_util.option('--auto-tiering', help=u"""The auto tiering status on the bucket. If in state `InfrequentAccess`, objects are transitioned automatically between the 'Standard' and 'InfrequentAccess' tiers based on the access pattern of the objects. When auto tiering is `Disabled`, there will be no automatic transitions between storage tiers.""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'object_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'object_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def update_bucket(ctx, from_json, namespace_name, bucket_name, compartment_id, metadata, public_access_type, object_events_enabled, freeform_tags, defined_tags, kms_key_id, versioning, auto_tiering, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if bucket_name is not None:
        _details['name'] = bucket_name

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if public_access_type is not None:
        _details['publicAccessType'] = public_access_type

    if object_events_enabled is not None:
        _details['objectEventsEnabled'] = object_events_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if versioning is not None:
        _details['versioning'] = versioning

    if auto_tiering is not None:
        _details['autoTiering'] = auto_tiering

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.update_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        update_bucket_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('os.update_namespace_metadata.command_name', 'update-namespace-metadata'), help=u"""By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy.

You can change the default Swift/Amazon S3 compartmentId designation to a different compartmentId. All subsequent bucket creations will use the new default compartment, but no previously created buckets will be modified. A user must have OBJECTSTORAGE_NAMESPACE_UPDATE permission to make changes to the default compartments for Amazon S3 and Swift. \n[Command Reference](updateNamespaceMetadata)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--default-s3-compartment-id', help=u"""The updated compartment id for use by an S3 client, if this field is set.""")
@cli_util.option('--default-swift-compartment-id', help=u"""The updated compartment id for use by a Swift client, if this field is set.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'NamespaceMetadata'})
@cli_util.wrap_exceptions
def update_namespace_metadata(ctx, from_json, namespace_name, default_s3_compartment_id, default_swift_compartment_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if default_s3_compartment_id is not None:
        _details['defaultS3CompartmentId'] = default_s3_compartment_id

    if default_swift_compartment_id is not None:
        _details['defaultSwiftCompartmentId'] = default_swift_compartment_id

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.update_namespace_metadata(
        namespace_name=namespace_name,
        update_namespace_metadata_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('os.update_object_storage_tier.command_name', 'update-object-storage-tier'), help=u"""Changes the storage tier of the object specified by the objectName parameter. \n[Command Reference](updateObjectStorageTier)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""An object for which the storage tier needs to be changed.""")
@cli_util.option('--storage-tier', required=True, type=custom_types.CliCaseInsensitiveChoice(["Standard", "InfrequentAccess", "Archive"]), help=u"""The storage tier that the object should be moved to.""")
@cli_util.option('--version-id', help=u"""The versionId of the object. Current object version is used by default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_object_storage_tier(ctx, from_json, namespace_name, bucket_name, object_name, storage_tier, version_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['objectName'] = object_name
    _details['storageTier'] = storage_tier

    if version_id is not None:
        _details['versionId'] = version_id

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.update_object_storage_tier(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        update_object_storage_tier_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@retention_rule_group.command(name=cli_util.override('os.update_retention_rule.command_name', 'update'), help=u"""Updates the specified retention rule. Rule changes take effect typically within 30 seconds. \n[Command Reference](updateRetentionRule)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--retention-rule-id', required=True, help=u"""The ID of the retention rule.""")
@cli_util.option('--display-name', help=u"""A user-specified name for the retention rule. Names can be helpful in identifying retention rules. Avoid entering confidential information.""")
@cli_util.option('--duration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-rule-locked', type=custom_types.CLI_DATETIME, help=u"""The date and time as per [RFC 3339] after which this rule is locked and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are allowed and no other properties can be changed. This property cannot be updated for rules that are in a locked state. Specifying it when a duration is not specified is considered an error.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'duration': {'module': 'object_storage', 'class': 'Duration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'duration': {'module': 'object_storage', 'class': 'Duration'}}, output_type={'module': 'object_storage', 'class': 'RetentionRule'})
@cli_util.wrap_exceptions
def update_retention_rule(ctx, from_json, force, namespace_name, bucket_name, retention_rule_id, display_name, duration, time_rule_locked, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(retention_rule_id, six.string_types) and len(retention_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --retention-rule-id cannot be whitespace or empty string')
    if not force:
        if duration:
            if not click.confirm("WARNING: Updates to duration will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if duration is not None:
        _details['duration'] = cli_util.parse_json_parameter("duration", duration)

    if time_rule_locked is not None:
        _details['timeRuleLocked'] = time_rule_locked

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.update_retention_rule(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        retention_rule_id=retention_rule_id,
        update_retention_rule_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@multipart_upload_group.command(name=cli_util.override('os.upload_part.command_name', 'upload-part'), help=u"""Uploads a single part of a multipart upload. \n[Command Reference](uploadPart)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--upload-id', required=True, help=u"""The upload ID for a multipart upload.""")
@cli_util.option('--upload-part-num', required=True, type=click.INT, help=u"""The part number that identifies the object part currently being uploaded.""")
@cli_util.option('--upload-part-body', required=True, help=u"""The part being uploaded to the Object Storage service.""")
@cli_util.option('--content-length', type=click.INT, help=u"""The content length of the body.""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.""")
@cli_util.option('--expect', help=u"""A value of `100-continue` requests preliminary verification of the request method, path, and headers before the request body is sent. If no error results from such verification, the server will send a 100 (Continue) interim response to indicate readiness for the request body. The only allowed value for this parameter is \"100-Continue\" (case-insensitive).""")
@cli_util.option('--content-md5', help=u"""The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error is returned with the message:

\"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)\"""")
@cli_util.option('--opc-sse-customer-algorithm', help=u"""The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key', help=u"""The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-customer-key-sha256', help=u"""The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see [Using Your Own Keys for Server-Side Encryption].""")
@cli_util.option('--opc-sse-kms-key-id', help=u"""The [OCID] of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def upload_part(ctx, from_json, namespace_name, bucket_name, object_name, upload_id, upload_part_num, upload_part_body, content_length, if_match, if_none_match, expect, content_md5, opc_sse_customer_algorithm, opc_sse_customer_key, opc_sse_customer_key_sha256, opc_sse_kms_key_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')

    kwargs = {}
    if content_length is not None:
        kwargs['content_length'] = content_length
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if expect is not None:
        kwargs['expect'] = expect
    if content_md5 is not None:
        kwargs['content_md5'] = content_md5
    if opc_sse_customer_algorithm is not None:
        kwargs['opc_sse_customer_algorithm'] = opc_sse_customer_algorithm
    if opc_sse_customer_key is not None:
        kwargs['opc_sse_customer_key'] = opc_sse_customer_key
    if opc_sse_customer_key_sha256 is not None:
        kwargs['opc_sse_customer_key_sha256'] = opc_sse_customer_key_sha256
    if opc_sse_kms_key_id is not None:
        kwargs['opc_sse_kms_key_id'] = opc_sse_kms_key_id
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.upload_part(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        upload_id=upload_id,
        upload_part_num=upload_part_num,
        upload_part_body=upload_part_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)
