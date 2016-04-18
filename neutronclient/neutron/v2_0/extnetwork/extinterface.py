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
        '--tenant-id', dest='tenant_id',
        default=argparse.SUPPRESS,
        help=_('Tenant network ID for which the interface will be attached.'))

    parser.add_argument(
        '--extnodeint-id', dest='extnodeint_id',
        help=_('Interface of the extnode to be attached.'))

    parser.add_argument(
        '--network-id', dest='network_id',
        help=_('Network ID of the network in the datacenter to attach this interface.'))


def args2body(self, parsed_args):
    body = {'extnodeint_id': parsed_args.extnode_id,
            'network_id': parsed_args.network_id}
    if 'tenant_id' in parsed_args:
        body['tenant_id'] = parsed_args.tenant_id
    return {'extinterface': body}


class ExtInterfaceCreate(extension.ClientExtensionCreate, ExtInterface):
    shell_command = 'extinterface-create'

    list_columns = ['id', 'tenant_id', 'extnodeint_id', 'network_id']

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

    list_columns = ['id', 'type', 'extnode_id', 'network_id']

    pagination_support = True
    sorting_support = True


class ExtInterfaceShow(extension.ClientExtensionShow, ExtInterface):
    shell_command = 'extinterface-show'

    list_columns = ['id', 'tenant_id', 'extnodeint_id', 'network_id']
