from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.neutron import v2_0 as neutronV20

from oslo_log import log as logging

LOG = logging.getLogger(__name__)


class ExtConnection(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extconnection'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_know_arguments(self, parser):
    parser.add_argument(
        '--extnodeint1-id', dest='extnodeint1_id',
        help=_('1st end of the connection'))

    parser.add_argument(
        '--extnodeint2-id', dest='extnodeint2_id',
        help=_('2nd end of the connection'))


def add_know_arguments_updatable(self, parser):
    parser.add_argument(
        '--types-supported', dest='types_supported',
        help=_('Types of overlay networks that this external connection supports.'))

    parser.add_argument(
        '--ids-pool', dest='ids_pool',
        help=_('Pool of IDs available to use in the segment. (xxxx:xxxx or xxxxx)'))


def args2body(self, parsed_args):
    body = {'extnodeint1_id': parsed_args.types_supported,
            'extnodeint2_id': parsed_args.ids_pool}
    return body


def updatable_args2body(self, body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['ids_pool', 'types_supported'])


class ExtConnectionCreate(extension.ClientExtensionCreate, ExtConnection):

    shell_command = 'extconnection-create'
    list_columns = ['id', 'types_supported', 'ids_pool', 'extnodeint1_id', 'extnodeint2_id']

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)
        add_know_arguments_updatable(self, parser)

    def args2body(self, parsed_args):
        body = args2body(self, parsed_args)
        updatable_args2body(self, body, parsed_args)
        return {'extconnection': body}


class ExtConnectionDelete(extension.ClientExtensionDelete, ExtConnection):

    shell_command = 'extconnection-delete'


class ExtConnectionUpdate(extension.ClientExtensionUpdate, ExtConnection):

    shell_command = 'extconnection-update'
    list_columns = ['id', 'types_supported', 'ids_pool', 'extnodeint1_id', 'extnodeint2_id']

    def add_known_arguments(self, parser):
        add_know_arguments_updatable(self, parser)

    def args2body(self, parsed_args):
        body = {}
        updatable_args2body(self, body, parsed_args)
        return {'extconnection': body}


class ExtConnectionList(extension.ClientExtensionList, ExtConnection):

    shell_command = 'extconnection-list'
    list_columns = ['id', 'types_supported', 'ids_pool', 'extnodeint1_id', 'extnodeint2_id']
    pagination_support = True
    sorting_support = True


class ExtConnectionShow(extension.ClientExtensionShow, ExtConnection):

    shell_command = 'extconnection-show'
