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
        '--extinterface1-id', dest='extinterface1_id',
        help=_('First endpoint of the \'extlink\'.'))

    parser.add_argument(
        '--extinterface2-id', dest='extinterface2_id',
        help=_('Second endpoint of the \'extlink\'.'))

    parser.add_argument(
        '--network-id', dest='network_id',
        help=_('Network ID that is to be associated with this link.'))


def add_know_arguments_updatable(parser):
    parser.add_argument(
        'name', metavar='<LINK_NAME>',
        help=_('Name of this external link.'))


def args2body(body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['extinterface1_id',
                                               'extinterface2_id',
                                               'network_id'])


def args2body_updatable(body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['name'])


class ExtLinkCreate(extension.ClientExtensionCreate, ExtLink):
    shell_command = 'extlink-create'

    list_columns = ['id',
                    'name',
                    'segmentation_id',
                    'extinterface1_id',
                    'extinterface2_id',
                    'network_id']

    def add_known_arguments(self, parser):
        add_known_arguments(parser)
        add_know_arguments_updatable(parser)

    def args2body(self, parsed_args):
        body = {}
        args2body(body, parsed_args)
        args2body_updatable(body, parsed_args)
        return {'extlink': body}


class ExtLinkDelete(extension.ClientExtensionDelete, ExtLink):
    shell_command = 'extlink-delete'


class ExtLinkUpdate(extension.ClientExtensionUpdate, ExtLink):
    shell_command = 'extlink-update'

    list_columns = ['id',
                    'name',
                    'segmentation_id',
                    'extinterface1_id',
                    'extinterface2_id',
                    'network_id']

    def add_known_arguments(self, parser):
        add_know_arguments_updatable(parser)

    def args2body(self, parsed_args):
        body = {}
        args2body_updatable(body, parsed_args)
        return {'extlink': body}


class ExtLinkList(extension.ClientExtensionList, ExtLink):
    shell_command = 'extlink-list'
    list_columns = ['id',
                    'name',
                    'segmentation_id',
                    'extinterface1_id',
                    'extinterface2_id',
                    'network_id']
    pagination_support = True
    sorting_support = True


class ExtLinkShow(extension.ClientExtensionShow, ExtLink):
    shell_command = 'extlink-show'
