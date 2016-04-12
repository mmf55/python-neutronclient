import argparse

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

    parser.add_argument(
        '--add-interface',
        metavar='name=name,type=type,segment=segment',
        action='append',
        default=argparse.SUPPRESS,
        dest='add_interfaces', type=utils.str2dict,
        help=_('Segments where this node has interfaces. '))


def args2body(self, parsed_args):
    body = {'name': parsed_args.name,
            'type': parsed_args.type}
    if 'add_interfaces' in parsed_args:
        body['add_interfaces'] = parsed_args.add_interfaces
    else:
        body['add_interfaces'] = None
    if 'rem_interfaces' in parsed_args:
        body['rem_interfaces'] = parsed_args.rem_interfaces
    else:
        body['rem_interfaces'] = None
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

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)

        parser.add_argument(
            '--remove-interface', metavar='id=id',
            action='append',
            default=argparse.SUPPRESS,
            dest='rem_interfaces', type=utils.str2dict,
            help=_('Remove interfaces from the Neutron External network management. '))

    def args2body(self, parsed_args):
        return args2body(self, parsed_args)


class ExtNodeList(extension.ClientExtensionList, ExtNode):

    shell_command = 'extnode-list'
    list_columns = ['id', 'name', 'type', 'interfaces']
    pagination_support = True
    sorting_support = True


class ExtNodeShow(extension.ClientExtensionShow, ExtNode):

    shell_command = 'extnode-show'

