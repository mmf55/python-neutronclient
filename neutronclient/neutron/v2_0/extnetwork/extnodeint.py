import argparse

from neutronclient._i18n import _
from neutronclient.common import extension
from neutronclient.neutron import v2_0 as neutronV20


class ExtNodeInt(extension.NeutronClientExtension):
    """Define required variables for resource operations."""

    resource = 'extnodeint'
    resource_plural = '%ss' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


def add_know_arguments(self, parser):

    parser.add_argument(
        '--type', dest='type',
        help=_('External node interface type. E.g. port, SSID.'))

    parser.add_argument(
        '--extnodename', dest='extnodename',
        help=_('External node name.'))


def add_know_arguments_updatable(self, parser):
    parser.add_argument(
        'name', metavar='<NODE_NAME>',
        help=_('Name of this external node interface.'))


def args2body(self, body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['type', 'extnodename'])


def args2body_updatable(self, body, parsed_args):
    neutronV20.update_dict(parsed_args, body, ['name'])


class ExtNodeIntCreate(extension.ClientExtensionCreate, ExtNodeInt):
    shell_command = 'extnodeint-create'

    list_columns = ['id', 'name', 'type', 'interfaces']

    def add_known_arguments(self, parser):
        add_know_arguments(self, parser)
        add_know_arguments_updatable(self, parser)

    def args2body(self, parsed_args):
        body = {}
        args2body(self, body, parsed_args)
        args2body_updatable(self, body, parsed_args)
        return {'extnodeint': body}


class ExtNodeDelete(extension.ClientExtensionDelete, ExtNodeInt):

    shell_command = 'extnodeint-delete'


class ExtNodeUpdate(extension.ClientExtensionUpdate, ExtNodeInt):
    shell_command = 'extnodeint-update'

    list_columns = ['id', 'name', 'type', 'extnodename']

    def add_known_arguments(self, parser):
        add_know_arguments_updatable(self, parser)

    def args2body(self, parsed_args):
        body = {}
        args2body_updatable(self, body, parsed_args)
        return {'extnodeint': body}


class ExtNodeList(extension.ClientExtensionList, ExtNodeInt):

    shell_command = 'extnodeint-list'
    list_columns = ['id', 'name', 'type', 'extnodename']
    pagination_support = True
    sorting_support = True


class ExtNodeShow(extension.ClientExtensionShow, ExtNodeInt):

    shell_command = 'extnodeint-show'


