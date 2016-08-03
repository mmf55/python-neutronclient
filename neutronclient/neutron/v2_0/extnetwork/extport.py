import argparse

from neutronclient._i18n import _
from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.common import utils


class UpdatePortToExtPortMixin(object):
    """Define required variables for resource operations."""

    def add_arguments_extport(self, parser):
        parser.add_argument(
            '--extinterface-name',
            default=argparse.SUPPRESS,
            dest='extinterface_name',
            help=_('Used if is desired one specific external port on the requested node.'))

        parser.add_argument(
            '--extnode-name',
            default=argparse.SUPPRESS,
            dest='extnode_name',
            help=_('External node name of the node which the port will be placed'))

    def args2body_extport(self, parsed_args, body):
        neutronV20.update_dict(parsed_args, body, ['extinterface_name', 'extnode_name'])
