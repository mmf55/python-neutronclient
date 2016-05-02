import argparse

from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.neutron import v2_0 as neutronV20


class ExtLink(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extlink'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_known_arguments(parser):
    parser.add_argument(
        '--type', dest='type',
        help=_('Type of overlay network that this clink implements.'))

    parser.add_argument(
        '--extconnection-id', dest='extconnection_id',
        help=_('Connection \'extconnection\' for this extlink to be attached.'))


def add_know_arguments_updatable(parser):
    parser.add_argument(
        '--extport-id', dest='extport_id',
        help=_('Port ID for which this \'extlink\' will be associated.'))

    parser.add_argument(
        '--overlay-id', dest='overlay_id',
        help=_('Physical network ID that this link will use.'))


def args2body(self, body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['type', 'extconnection_id'])


def args2body_updatable(self, body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['extport_id', 'overlay_id'])


class ExtLinkCreate(extension.ClientExtensionCreate, ExtLink):
    shell_command = 'extlink-create'

    list_columns = ['id', 'type', 'extconnection_id', 'extport_id', 'overlay_id']

    def add_known_arguments(self, parser):
        add_known_arguments(parser)
        add_know_arguments_updatable(parser)

    def args2body(self, parsed_args):
        body = {}
        args2body(self, body, parsed_args)
        args2body_updatable(self, body, parsed_args)
        return {'extlink': body}


class ExtLinkDelete(extension.ClientExtensionDelete, ExtLink):
    shell_command = 'extlink-delete'


class ExtLinkUpdate(extension.ClientExtensionUpdate, ExtLink):
    shell_command = 'extlink-update'

    list_columns = ['id', 'type', 'extconnection_id', 'extport_id', 'overlay_id']

    def add_known_arguments(self, parser):
        add_know_arguments_updatable(parser)

    def args2body(self, parsed_args):
        body = {}
        args2body_updatable(self, body, parsed_args)
        return {'extlink': body}


class ExtLinkList(extension.ClientExtensionList, ExtLink):
    shell_command = 'extlink-list'
    list_columns = ['id', 'type', 'extconnection_id', 'extport_id', 'overlay_id']
    pagination_support = True
    sorting_support = True


class ExtLinkShow(extension.ClientExtensionShow, ExtLink):
    shell_command = 'extlink-show'
