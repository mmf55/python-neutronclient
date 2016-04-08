
from neutronclient._i18n import _
from neutronclient.common import extension


class ExtInterface(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extinterface'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def args2body(parsed_args):
    body = {'type': parsed_args.type,
            'extnode_id': parsed_args.extnode_id,
            'tenant_id': parsed_args.tenant_id,
            'tenant_network': parsed_args.tenant_network}
    return {'extinterface': body}


class CPortCreate(extension.ClientExtensionCreate, ExtInterface):

    shell_command = 'extinterface-create'

    def add_known_arguments(self, parser):

        parser.add_argument(
            '--type', dest='type',
            help=_('Type of extinterface (eg.: SSID, physical port.)'))

        parser.add_argument(
            '--extnode-id', dest='extnode_id',
            help=_('CSegment for this CLink to be attached.'))

        parser.add_argument(
            '--tenant-id', dest='tenant_id',
            help=_('Tenant ID for which the port will belong.'))

        parser.add_argument(
            '--tenant-network', dest='tenant_network',
            help=_('Tenant network ID for which the port will be attached.'))

    def args2body(self, parsed_args):
        args2body(parsed_args)


class CPortDelete(extension.ClientExtensionDelete, ExtInterface):

    shell_command = 'extinterface-delete'


class CPortUpdate(extension.ClientExtensionUpdate, ExtInterface):

    shell_command = 'extinterface-update'

    def add_known_arguments(self, parser):

        parser.add_argument(
            '--type',
            help=_('Type of CPort (eg.: SSID, physical port.)'))

        parser.add_argument(
            '--cnode-id',
            help=_('CSegment for this CLink to be attached.'))

        parser.add_argument(
            '--tenant-id',
            help=_('Tenant ID for which the port will belong.'))

        parser.add_argument(
            '--tenant-network',
            help=_('Tenant network ID for which the port will be attached.'))

    def args2body(self, parsed_args):
        args2body(parsed_args)


class ExtInterfacesList(extension.ClientExtensionList, ExtInterface):
    """List of ExtInterfaces."""

    shell_command = 'extinterface-list'
    list_columns = ['id', 'type', 'extnode_id', 'network_id']
    pagination_support = True
    sorting_support = True


class ExtInterfaceShow(extension.ClientExtensionShow, ExtInterface):

    shell_command = 'extinterface-show'

