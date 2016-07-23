from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.neutron import v2_0 as neutronV20

from oslo_log import log as logging

LOG = logging.getLogger(__name__)


class ExtSegment(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extsegment'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_know_arguments(self, parser):
    parser.add_argument(
        'name', metavar='<SEGMENT_NAME>',
        help=_('Name of this external segment.'))

    parser.add_argument(
        '--type-supported', dest='type_supported',
        help=_('Types of overlay networks that this external connection supports.'))

    parser.add_argument(
        '--ids-available', dest='ids_available',
        help=_('Pool of VLAN IDs available to use in the segment. (xxxx:xxxx or xxxxx)'))


def args2body(parsed_args):
    body = {'name': parsed_args.name,
            'type_supported': parsed_args.type_supported,
            'ids_available': parsed_args.ids_available,
            }
    return body


class ExtConnectionCreate(extension.ClientExtensionCreate, ExtSegment):

    shell_command = 'extsegment-create'

    list_columns = ['id',
                    'name',
                    'type_supported',
                    'ids_available',
                    ]

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)

    def args2body(self, parsed_args):
        body = args2body(parsed_args)
        return {'extsegment': body}


class ExtConnectionDelete(extension.ClientExtensionDelete, ExtSegment):

    shell_command = 'extsegment-delete'


class ExtConnectionUpdate(extension.ClientExtensionUpdate, ExtSegment):

    shell_command = 'extsegment-update'
    list_columns = ['id', 'name', 'type_supported', 'ids_available']

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)

    def args2body(self, parsed_args):
        body = args2body(parsed_args)
        return {'extsegment': body}


class ExtConnectionList(extension.ClientExtensionList, ExtSegment):

    shell_command = 'extsegment-list'
    list_columns = ['id', 'name', 'type_supported', 'ids_available']
    pagination_support = True
    sorting_support = True


class ExtConnectionShow(extension.ClientExtensionShow, ExtSegment):

    shell_command = 'extsegment-show'
