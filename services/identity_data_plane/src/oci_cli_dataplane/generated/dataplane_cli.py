# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1

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


@cli.command(cli_util.override('identity_data_plane.identity_data_plane_root_group.command_name', 'identity-data-plane'), cls=CommandGroupWithAlias, help=cli_util.override('identity_data_plane.identity_data_plane_root_group.help', """APIs for managing identity data plane services. For example, use this API to create a scoped-access security token. To manage identity domains (for example, creating or deleting an identity domain) or to manage resources (for example, users and groups) within the default identity domain, see [IAM API]."""), short_help=cli_util.override('identity_data_plane.identity_data_plane_root_group.short_help', """Identity and Access Management Data Plane API"""))
@cli_util.help_option_group
def identity_data_plane_root_group():
    pass


@click.command(cli_util.override('identity_data_plane.security_token_group.command_name', 'security-token'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def security_token_group():
    pass


identity_data_plane_root_group.add_command(security_token_group)


@security_token_group.command(name=cli_util.override('identity_data_plane.generate_scoped_access_token.command_name', 'generate-scoped-access-token'), help=u"""Based on the calling Principal and the input payload, derive the claims, and generate a scoped-access token for specific resources. For example, set scope to urn:oracle:db::id::<compartment-id> for access to a database in a compartment. \n[Command Reference](generateScopedAccessToken)""")
@cli_util.option('--scope', required=True, help=u"""Scope definition for the scoped access token""")
@cli_util.option('--public-key', required=True, help=u"""A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will be put inside the security token by the auth service after successful validation of the certificate.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity_data_plane', 'class': 'SecurityToken'})
@cli_util.wrap_exceptions
def generate_scoped_access_token(ctx, from_json, scope, public_key):

    kwargs = {}

    _details = {}
    _details['scope'] = scope
    _details['publicKey'] = public_key

    client = cli_util.build_client('identity_data_plane', 'dataplane', ctx)
    result = client.generate_scoped_access_token(
        generate_scoped_access_token_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@security_token_group.command(name=cli_util.override('identity_data_plane.generate_user_security_token.command_name', 'generate-user'), help=u"""Exchanges a valid user token-based signature (API key and UPST) for a short-lived UPST of the authenticated user principal. When not specified, the user session duration is set to a default of 60 minutes in all realms. Resulting UPSTs are refreshable while the user session has not expired. \n[Command Reference](generateUserSecurityToken)""")
@cli_util.option('--public-key', required=True, help=u"""The user-owned public key in PEM format that corresponds to the RSA key pair used for signing requests. The user also owns the corresponding private key. This public key will be put inside the user security token by the auth service after successful validation of the request.""")
@cli_util.option('--session-expiration-in-minutes', type=click.INT, help=u"""User session expiration in minutes to which the requested user principal session token (UPST) is bounded. Valid values are from 5 to 60 for all realms.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity_data_plane', 'class': 'SecurityToken'})
@cli_util.wrap_exceptions
def generate_user_security_token(ctx, from_json, public_key, session_expiration_in_minutes):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['publicKey'] = public_key

    if session_expiration_in_minutes is not None:
        _details['sessionExpirationInMinutes'] = session_expiration_in_minutes

    client = cli_util.build_client('identity_data_plane', 'dataplane', ctx)
    result = client.generate_user_security_token(
        generate_user_security_token_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
