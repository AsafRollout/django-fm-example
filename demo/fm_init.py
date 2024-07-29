# Import SDK
from rox.server.rox_server import Rox
from rox.server.flags.rox_flag import RoxFlag
from rox.core.entities.rox_string import RoxString
from rox.core.entities.rox_int import RoxInt
from rox.server.rox_options import RoxOptions, NetworkConfigurationsOptions

# Create Roxflags in the Flags container class
class Flags:
    def __init__(self):
        #Define the feature flags
        self.showMessage = RoxFlag(False)
        self.message = RoxString('This is the default message; try changing some flag values!')
        self.fontColor = RoxString('Black', ['Red', 'Green', 'Blue', 'Black'])
        self.fontSize = RoxInt(99, [10, 50, 99])
        
flags = Flags()

# Register the flags container
Rox.register(flags)

# OVERWRITING network configs to point to a customer environment
# VPC --> overwrite to point to different environment besides Multi-Tenant Production.
payload = data.get('payload')
options = payload.get('options')
configuration = options.get('configuration')
network_config = NetworkConfigurationsOptions(
    configuration['https://api.vpc-install-test.saas-tools.beescloud.com/device/get_configuration'],
    configuration['https://rox-conf.vpc-install-test.saas-tools.beescloud.com'],
    configuration['https://api.vpc-install-test.saas-tools.beescloud.com/device/update_state_store/'],
    configuration['https://rox-state.vpc-install-test.saas-tools.beescloud.com'],
    configuration['https://fm-analytics.vpc-install-test.saas-tools.beescloud.com'],
    configuration['https://sdk-notification-service.vpc-install-test.saas-tools.beescloud.com/sse'])

# last value is disbableSignatureVerification
options = RoxOptions(None, network_config, None, True)

# Setup the SDK key
sdk_key = '<YOUR-SDK-KEY>'
cancel_event = Rox.setup(sdk_key, options).result();

# Boolean flag example
print('showMessage is {}'.format(flags.showMessage.is_enabled()))

# String flag examples
print('font color is {}'.format(flags.fontColor.get_value()))
print('message is {}'.format(flags.message.get_value()))

# Double flag examples
print('fontSize is {}'.format(flags.fontSize.get_value()))

