from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.neutron import v2_0 as neutronV20


class ExtNode(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extnode'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_know_arguments(parser):
    parser.add_argument(
        'name', metavar='<NODE_NAME>',
        help=_('External node name (Maps directly to the real device hostname).'))

    parser.add_argument(
        '--ip-address', dest='ip_address',
        help=_('The ip address of the management interface.'))

    parser.add_argument(
        '--topology-discover', dest='topology_discover',
        help=_('Run the topology discover.'))


def args2body(body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['name',
                                               'ip_address',
                                               'topology_discover',
                                               ])


class ExtNodeCreate(extension.ClientExtensionCreate, ExtNode):
    shell_command = 'extnode-create'

    list_columns = ['id', 'name', 'ip_address']

    def add_known_arguments(self, parser):
        add_know_arguments(parser)

    def args2body(self, parsed_args):
        body = {}
        args2body(body, parsed_args)
        return {'extnode': body}


class ExtNodeDelete(extension.ClientExtensionDelete, ExtNode):

    shell_command = 'extnode-delete'


class ExtNodeUpdate(extension.ClientExtensionUpdate, ExtNode):
    shell_command = 'extnode-update'

    list_columns = ['id', 'name', 'ip_address']

    def add_known_arguments(self, parser):
        add_know_arguments(parser)

    def args2body(self, parsed_args):
        body = {}
        args2body(body, parsed_args)
        return {'extnode': body}


class ExtNodeList(extension.ClientExtensionList, ExtNode):
    shell_command = 'extnode-list'

    list_columns = ['id', 'name', 'ip_address']
    pagination_support = True
    sorting_support = True
