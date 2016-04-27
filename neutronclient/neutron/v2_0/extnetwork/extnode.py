import argparse

from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.common import utils
from oslo_serialization import jsonutils


def _format_interfaces(extnode):
    try:
        return '\n'.join([jsonutils.dumps(extnode) for extnode in
                          extnode['interfaces']])
    except (TypeError, KeyError):
        return ''


class ExtNode(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extnode'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_know_arguments_base(self, parser):
    parser.add_argument(
        'name', metavar='<NODE_NAME>',
        help=_('Name of this extnode.'))

    parser.add_argument(
        '--type', dest='type',
        help=_('External node type. E.g. router, switch, ap.'))


def add_know_arguments_add(self, parser):
    parser.add_argument(
        '--add-interface',
        metavar='name=name,segment_id=segment_id',
        action='append',
        default=argparse.SUPPRESS,
        dest='add_interfaces', type=utils.str2dict,
        help=_('Segments where this node has interfaces. '))


def add_know_arguments_remove(self, parser):
    parser.add_argument(
        '--remove-interface', metavar='id=id',
        action='append',
        default=argparse.SUPPRESS,
        dest='rem_interfaces', type=utils.str2dict,
        help=_('Remove interfaces from the Neutron External network management. '))


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

    list_columns = ['id', 'name', 'type', 'interfaces']

    def add_known_arguments(self, parser):
        add_know_arguments_base(self, parser)
        add_know_arguments_add(self, parser)

    def args2body(self, parsed_args):
        return args2body(self, parsed_args)


class ExtNodeDelete(extension.ClientExtensionDelete, ExtNode):

    shell_command = 'extnode-delete'


class ExtNodeUpdate(extension.ClientExtensionUpdate, ExtNode):
    shell_command = 'extnode-update'

    list_columns = ['id', 'name', 'type', 'interfaces']

    def add_known_arguments(self, parser):
        add_know_arguments_remove(self, parser)

    def args2body(self, parsed_args):
        return args2body(self, parsed_args)


class ExtNodeList(extension.ClientExtensionList, ExtNode):

    shell_command = 'extnode-list'
    _formatters = {'interfaces': _format_interfaces, }
    list_columns = ['id', 'name', 'type', 'interfaces']
    pagination_support = True
    sorting_support = True


class ExtNodeShow(extension.ClientExtensionShow, ExtNode):

    shell_command = 'extnode-show'


