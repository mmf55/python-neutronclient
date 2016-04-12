from neutronclient._i18n import _
from neutronclient.common import extension

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
        '--name', dest='name',
        help=_('Name of the segment.'))

    parser.add_argument(
        '--types-supported', dest='types_supported',
        help=_('Types of overlay networks that this extsegment supports.'))

    parser.add_argument(
        '--ids-pool', dest='ids_pool',
        help=_('Pool of IDs available to use in the segment. (xxxx:xxxx or xxxxx)'))


def args2body(self, parsed_args):
    body = {'name': parsed_args.name,
            'types_supported': parsed_args.types_supported,
            'ids_pool': parsed_args.ids_pool}
    return {'extsegment': body}


class ExtSegmentCreate(extension.ClientExtensionCreate, ExtSegment):

    shell_command = 'extsegment-create'
    list_columns = ['id', 'types_supported', 'ids_pool']

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)

    def args2body(self, parsed_args):
        return args2body(self, parsed_args)


class ExtSegmentDelete(extension.ClientExtensionDelete, ExtSegment):

    shell_command = 'csegment-delete'


class ExtSegmentUpdate(extension.ClientExtensionUpdate, ExtSegment):

    shell_command = 'csegment-update'
    list_columns = ['id', 'types_supported', 'nodes_connected']

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)

    def args2body(self, parsed_args):
        return args2body(parsed_args)


class ExtSegmentList(extension.ClientExtensionList, ExtSegment):

    shell_command = 'extsegment-list'
    list_columns = ['id', 'types_supported', 'ids_pool']
    pagination_support = True
    sorting_support = True


class ExtSegmentShow(extension.ClientExtensionShow, ExtSegment):

    shell_command = 'extsegment-show'
