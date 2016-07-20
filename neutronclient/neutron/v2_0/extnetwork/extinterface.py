import argparse

from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.neutron import v2_0 as neutronV20


class ExtInterface(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extinterface'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_know_arguments(parser):
    parser.add_argument(
        '--type', dest='type',
        help=_('External node interface type. E.g. l2 or l3.'))

    parser.add_argument(
        '--ip-address', dest='ip_address',
        help=_('The ip address already attributed to this interface'))

    parser.add_argument(
        '--extnode-id', dest='extnode_id',
        help=_('External node ID.'))


def add_know_arguments_updatable(parser):

    parser.add_argument(
        '--extsegment-id', dest='extsegment_id',
        help=_('Segment \'extsegment\' for which this interface belongs.'))


def args2body(body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['type',
                                               'ip_address',
                                               'extsegment_id',
                                               'extnode_id'])


def args2body_updatable(body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['name'])


class ExtInterfaceCreate(extension.ClientExtensionCreate, ExtInterface):
    shell_command = 'extinterface-create'

    list_columns = ['id', 'name', 'type', 'ip_address', 'extsegment_id', 'extnode_id']

    def add_known_arguments(self, parser):
        add_know_arguments(parser)
        add_know_arguments_updatable(parser)

    def args2body(self, parsed_args):
        body = {}
        args2body(body, parsed_args)
        args2body_updatable(body, parsed_args)
        return {'extinterface': body}


class ExtInterfaceDelete(extension.ClientExtensionDelete, ExtInterface):

    shell_command = 'extinterface-delete'


class ExtInterfaceUpdate(extension.ClientExtensionUpdate, ExtInterface):
    shell_command = 'extinterface-update'

    list_columns = ['id', 'name', 'type', 'ip_address', 'extsegment_id', 'extnode_id']

    def add_known_arguments(self, parser):
        add_know_arguments_updatable(parser)

    def args2body(self, parsed_args):
        body = {}
        args2body_updatable(body, parsed_args)
        return {'extinterface': body}


class ExtInterfaceList(extension.ClientExtensionList, ExtInterface):
    shell_command = 'extinterface-list'

    list_columns = ['id', 'name', 'type', 'ip_address', 'extsegment_id', 'extnode_id']
    pagination_support = True
    sorting_support = True


class ExtInterfaceShow(extension.ClientExtensionShow, ExtInterface):

    shell_command = 'extinterface-show'


