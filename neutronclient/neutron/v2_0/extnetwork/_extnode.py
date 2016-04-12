
from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.common import utils


class ExtNode(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extnode'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_know_arguments(self, parser):
    parser.add_argument(
        '--name', dest='name',
        help=_('Name of this extnode.'))

    parser.add_argument(
        '--type', dest='type',
        help=_('External node type. E.g. router, switch, ap.'))

    # parser.add_argument(
    #     '--extsegments', dest='extsegments',
    #     help=_('Segments where this node has interfaces. '))


def args2body(self, parsed_args):
    body = {'name': parsed_args.name,
            'type': parsed_args.type}
    if 'extsegments' in parsed_args:
        body['extsegments'] = parsed_args.extsegments

    return {'extnode': body}


class ExtNodeCreate(extension.ClientExtensionCreate, ExtNode):

    shell_command = 'extnode-create'

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)

    def args2body(self, parsed_args):
        return args2body(self, parsed_args)


class ExtNodeDelete(extension.ClientExtensionDelete, ExtNode):

    shell_command = 'extnode-delete'


class ExtNodeUpdate(extension.ClientExtensionUpdate, ExtNode):

    shell_command = 'extnode-update'
    list_columns = ['id', 'name', 'ip_address']

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)

    def args2body(self, parsed_args):
        return args2body(self, parsed_args)


class ExtNodeList(extension.ClientExtensionList, ExtNode):

    shell_command = 'extnode-list'
    list_columns = ['id', 'name', 'type']
    pagination_support = True
    sorting_support = True


class ExtNodeShow(extension.ClientExtensionShow, ExtNode):

    shell_command = 'extnode-show'

