import argparse

from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.common import utils
from oslo_serialization import jsonutils


def _format_interfaces(extlink):
    try:
        return '\n'.join([jsonutils.dumps(extlink) for extlink in
                          extlink['connections']])
    except (TypeError, KeyError):
        return ''


class ExtLink(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extlink'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_known_arguments_create(parser):
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


def add_know_arguments_add(parser):
    parser.add_argument(
        '--add-connection',
        metavar='type=type,extnodeint1=extnodeint1,extnodeint2=extnodeint2',
        action='append',
        default=argparse.SUPPRESS,
        dest='add_connections', type=utils.str2dict,
        help=_('Segments where this node has interfaces. '))


def add_know_arguments_remove(parser):
    parser.add_argument(
        '--remove-connection', metavar='id=id',
        action='append',
        default=argparse.SUPPRESS,
        dest='rem_connections', type=utils.str2dict,
        help=_('Remove interfaces from the Neutron External network management. '))


def args2body_base(self, body, parsed_args):
    body = {'type': parsed_args.type,
            'network_id': parsed_args.network_id,
            'overlay_id': parsed_args.overlay_id,
            'extsegment_id': parsed_args.extsegment_id}
    return body


def args2body_add(self, body, parsed_args):
    if 'add_connections' in parsed_args:
        body['add_connections'] = parsed_args.add_connections
    else:
        body['add_connections'] = None
    return body


def args2body_remove(self, body, parsed_args):
    if 'rem_connections' in parsed_args:
        body['rem_connections'] = parsed_args.rem_connections
    else:
        body['rem_connections'] = None
    return body


class ExtLinkCreate(extension.ClientExtensionCreate, ExtLink):
    shell_command = 'extlink-create'

    list_columns = ['id', 'type', 'network_id', 'overlay_id', 'extsegment_id', 'connections']

    def add_known_arguments(self, parser):
        add_known_arguments_create(parser)
        add_know_arguments_add(parser)

    def args2body(self, parsed_args):
        body = {}
        body = args2body_base(self, body, parsed_args)
        body = args2body_add(self, body, parsed_args)
        return {'extlink': body}


class ExtLinkDelete(extension.ClientExtensionDelete, ExtLink):
    shell_command = 'extlink-delete'


class ExtLinkUpdate(extension.ClientExtensionUpdate, ExtLink):
    shell_command = 'extlink-update'

    list_columns = ['id', 'type', 'network_id', 'overlay_id', 'extsegment_id', 'connections']

    def add_known_arguments(self, parser):
        add_know_arguments_add(parser)
        add_know_arguments_remove(parser)

    def args2body(self, parsed_args):
        body = {}
        body = args2body_add(self, body, parsed_args)
        body = args2body_remove(self, body, parsed_args)
        return {'extlink': body}


class ExtLinkList(extension.ClientExtensionList, ExtLink):
    shell_command = 'extlink-list'
    _formatters = {'connections': _format_interfaces, }
    list_columns = ['id', 'type', 'network_id', 'overlay_id', 'extsegment_id', 'connections']
    pagination_support = True
    sorting_support = True


class ExtLinkShow(extension.ClientExtensionShow, ExtLink):
    shell_command = 'extlink-show'
