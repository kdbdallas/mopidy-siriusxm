from __future__ import unicode_literals

import logging
import os

from mopidy import config, ext

__version__ = '0.1.0'

logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-SiriusXM'
    ext_name = 'siriusxm'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['username'] = config.String()
        schema['password'] = config.Secret()
        schema['remember_me'] = config.Boolean()
        schema['baseURL'] = config.String()
        schema['authURL'] = config.String()
        schema['deviceMake'] = config.String()
        schema['oem'] = config.String()
        schema['osVersion'] = config.String()
        schema['platform'] = config.String()
        schema['deviceID'] = config.String()
        schema['sxmAppVersion'] = config.String()
        schema['carrier'] = config.String()
        schema['appRegion'] = config.String()
        schema['deviceModel'] = config.String()
        schema['resultTemplate'] = config.String()
        schema['allow_network'] = config.Boolean()
        schema['allow_cache'] = config.Boolean()
        return schema

    def setup(self, registry):
        from .siriusXMBackend import SiriusXM
        registry.add('backend', SiriusXM)
