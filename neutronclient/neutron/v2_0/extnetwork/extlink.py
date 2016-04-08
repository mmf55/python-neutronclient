from neutronclient._i18n import _
from neutronclient.common import extension


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
        '--extsegment', dest='extsegment',
        help=_('Segment \'extsegment\' for this extink to be attached.'))


def args2body(self, parsed_args):
    body = {'type': parsed_args.type,
            'extsegment': parsed_args.csegment}
    return {'extlink': body}


class ExtLinkCreate(extension.ClientExtensionCreate, ExtLink):
    shell_command = 'extlink-create'

    def add_known_arguments(self, parser):
        self.add_known_arguments(parser)

    def args2body(self, parsed_args):
        return args2body(self, parsed_args)


class ExtLinkDelete(extension.ClientExtensionDelete, ExtLink):
    shell_command = 'extlink-delete'


class ExtLinkUpdate(extension.ClientExtensionUpdate, ExtLink):
    shell_command = 'extlink-update'

    def add_known_arguments(self, parser):
        self.add_known_arguments(parser)

    def args2body(self, parsed_args):
        args2body(self, parsed_args)


class CLinkList(extension.ClientExtensionList, ExtLink):
    shell_command = 'extlink-list'
    list_columns = ['id', 'network_id', 'overlay_id', 'extsegment']
    pagination_support = True
    sorting_support = True


class ExtLinkShow(extension.ClientExtensionShow, ExtLink):
    shell_command = 'extlink-show'
