
from neutronclient._i18n import _
from neutronclient.common import extension


class ExtSegment(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extsegment'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def args2body(parsed_args):
    body = {'types-supported': parsed_args.types_supported,
            'nodes-connected': parsed_args.nodes_connected}
    return {'extsegment': body}


class ExtSegmentCreate(extension.ClientExtensionCreate, ExtSegment):

    shell_command = 'extsegment-create'
    list_columns = ['id', 'types_supported', 'ids_pool']

    def add_known_arguments(self, parser):

        parser.add_argument(
            '--types-supported', dest='types_supported',
            help=_('Types of overlay networks that this extsegment supports.'))

        parser.add_argument(
            '--ids-pool', dest='ids-pool',
            help=_('Pool of IDs available to use in the segment.'))

    def args2body(self, parsed_args):
        return self.args2body(parsed_args)


class ExtSegmentDelete(extension.ClientExtensionDelete, ExtSegment):

    shell_command = 'csegment-delete'


class ExtSegmentUpdate(extension.ClientExtensionUpdate, ExtSegment):

    shell_command = 'csegment-update'
    list_columns = ['id', 'types_supported', 'nodes_connected']

    def add_known_arguments(self, parser):

        parser.add_argument(
            '--types-supported', dest='types_supported',
            help=_('Types of overlay networks that this extsegment supports.'))

        parser.add_argument(
            '--ids-pool', dest='ids-pool',
            help=_('Pool of IDs available to use in the segment.'))

    def args2body(self, parsed_args):
        return args2body(parsed_args)


class ExtSegmentList(extension.ClientExtensionList, ExtSegment):

    shell_command = 'extsegment-list'
    list_columns = ['id', 'types_supported', 'ids_pool']
    pagination_support = True
    sorting_support = True


class ExtSegmentShow(extension.ClientExtensionShow, ExtSegment):

    shell_command = 'extsegment-show'
