import argparse

from neutronclient._i18n import _
from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.common import utils


class UpdatePortToExtPortMixin(object):
    """Define required variables for resource operations."""

    def add_arguments_extport(self, parser):
        parser.add_argument(
            '--external-port',
            metavar='access_id=access_id,extnodeint_id=extnodeint_id',
            action='append',
            default=argparse.SUPPRESS,
            dest='external_port', type=utils.str2dict,
            help=_('Set this port to be an external port.'))

    def args2body_extport(self, parsed_args, body):
        neutronV20.update_dict(parsed_args, body, ['external_port'])

