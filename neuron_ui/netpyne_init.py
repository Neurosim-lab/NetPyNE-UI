import logging
from netpyne import specs
from netpyne import sim
from netpyne import analysis
from netpyne.tests import tests
from netpyne.metadata import metadata
from netpyne.metadata import api
import json
from neuron_ui import neuron_utils
from jupyter_geppetto.geppetto_comm import GeppettoJupyterModelSync

netParams = specs.NetParams()
simConfig = specs.SimConfig()

neuron_utils.createProject(name='SampleProject')

GeppettoJupyterModelSync.current_model.original_model = json.dumps({'netParams': netParams.__dict__,
                                                                    'simConfig': simConfig.__dict__,
                                                                    'metadata': metadata.metadata,
                                                                    'requirement': 'from neuron_ui.netpyne_init import *'})

logging.debug(GeppettoJupyterModelSync.current_model.original_model)