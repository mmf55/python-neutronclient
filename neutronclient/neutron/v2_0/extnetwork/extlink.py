import argparse

from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.common import utils


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
        '--network-id', dest='network_id',
        help=_('Network ID for which this \'extlink\' will be associated.'))

    parser.add_argument(
        '--overlay-id', dest='overlay_id',
        help=_('Physical network ID that this link will use.'))

    parser.add_argument(
        '--extsegment-id', dest='extsegment_id',
        help=_('Segment \'extsegment\' for this extink to be attached.'))

    parser.add_argument(
        '--add-connection',
        metavar='type=type,extnodeint1=extnodeint1,extnodeint2=extnodeint2,extlink=extlink',
        action='append',
        default=argparse.SUPPRESS,
        dest='add_connections', type=utils.str2dict,
        help=_('Segments where this node has interfaces. '))


def args2body(self, parsed_args):
    body = {'type': parsed_args.type,
            'network_id': parsed_args.network_id,
            'overlay_id': parsed_args.overlay_id,
            'extsegment_id': parsed_args.extsegment_id}
    if 'add_connections' in parsed_args:
        body['add_connections'] = parsed_args.add_connections
    else:
        body['add_connections'] = None
    if 'rem_connections' in parsed_args:
        body['rem_connections'] = parsed_args.rem_connections
    else:
        body['rem_connections'] = None
    return {'extlink': body}


class ExtLinkCreate(extension.ClientExtensionCreate, ExtLink):
    shell_command = 'extlink-create'

    list_columns = ['id', 'type', 'network_id', 'overlay_id', 'extsegment_id', 'connections']

    def add_known_arguments(self, parser):
        add_known_arguments(parser)

    def args2body(self, parsed_args):
        return args2body(self, parsed_args)


class ExtLinkDelete(extension.ClientExtensionDelete, ExtLink):
    shell_command = 'extlink-delete'


class ExtLinkUpdate(extension.ClientExtensionUpdate, ExtLink):
    shell_command = 'extlink-update'

    list_columns = ['id', 'type', 'network_id', 'overlay_id', 'extsegment_id', 'connections']

    def add_known_arguments(self, parser):
        add_known_arguments(parser)

        parser.add_argument(
            '--remove-connection', metavar='id=id',
            action='append',
            default=argparse.SUPPRESS,
            dest='rem_connections', type=utils.str2dict,
            help=_('Remove interfaces from the Neutron External network management. '))

    def args2body(self, parsed_args):
        args2body(self, parsed_args)


class ExtLinkList(extension.ClientExtensionList, ExtLink):
    shell_command = 'extlink-list'
    list_columns = ['id', 'type', 'network_id', 'overlay_id', 'extsegment_id', 'connections']
    pagination_support = True
    sorting_support = True


class ExtLinkShow(extension.ClientExtensionShow, ExtLink):
    shell_command = 'extlink-show'
