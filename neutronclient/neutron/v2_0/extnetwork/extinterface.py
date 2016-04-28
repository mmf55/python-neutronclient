import argparse

from neutronclient._i18n import _
from neutronclient.common import extension


class ExtInterface(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extinterface'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_known_arguments(self, parser):
    parser.add_argument(
        'name', metavar='<INT_NAME>',
        help=_('Name of the external interface.'))

    parser.add_argument(
        '--type', dest='type',
        help=_('Type of the access to the network that this interface implements.'))

    parser.add_argument(
        '--access-id', dest='access_id',
        default=argparse.SUPPRESS,
        help=_('Type of th access to the network that this interface implements.'))

    parser.add_argument(
        '--extnode-id', dest='extnode_id',
        help=_('Interface of the extnode to be attached.'))

    parser.add_argument(
        '--network-id', dest='network_id',
        help=_('Network ID of the network in the datacenter to attach this interface.'))


def args2body(self, parsed_args):
    body = {'name': parsed_args.name,
            'type': parsed_args.type,
            'extnode_id': parsed_args.extnode_id,
            'network_id': parsed_args.network_id}
    if 'access_id' in parsed_args:
        body['access_id'] = parsed_args.access_id
    else:
        body['access_id'] = None
    return {'extinterface': body}


class ExtInterfaceCreate(extension.ClientExtensionCreate, ExtInterface):
    shell_command = 'extinterface-create'

    list_columns = ['id', 'name', 'type', 'access_id', 'extnode_id', 'network_id', 'tenant_id']

    def add_known_arguments(self, parser):
        add_known_arguments(self, parser)

    def args2body(self, parsed_args):
        args2body(self, parsed_args)


class ExtInterfaceDelete(extension.ClientExtensionDelete, ExtInterface):
    shell_command = 'extinterface-delete'


class ExtInterfaceUpdate(extension.ClientExtensionUpdate, ExtInterface):
    shell_command = 'extinterface-update'

    list_columns = ['id', 'tenant_id', 'extnodeint_id', 'network_id']

    def add_known_arguments(self, parser):
        add_known_arguments(self, parser)

    def args2body(self, parsed_args):
        args2body(self, parsed_args)


class ExtInterfacesList(extension.ClientExtensionList, ExtInterface):
    """List of ExtInterfaces."""

    shell_command = 'extinterface-list'

    list_columns = ['id', 'name', 'type', 'access_id', 'extnode_id', 'network_id', 'tenant_id']

    pagination_support = True
    sorting_support = True


class ExtInterfaceShow(extension.ClientExtensionShow, ExtInterface):
    shell_command = 'extinterface-show'

    list_columns = ['id', 'name', 'type', 'access_id', 'extnode_id', 'network_id', 'tenant_id']
