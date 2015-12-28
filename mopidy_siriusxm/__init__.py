from __future__ import absolute_import, unicode_literals

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
        schema['base_url'] = config.String()
        schema['auth_url'] = config.String()
        schema['device_make'] = config.String()
        schema['oem'] = config.String()
        schema['os_version'] = config.String()
        schema['platform'] = config.String()
        schema['device_id'] = config.String()
        schema['sxm_app_version'] = config.String()
        schema['carrier'] = config.String()
        schema['app_region'] = config.String()
        schema['device_model'] = config.String()
        schema['result_template'] = config.String()
        schema['allow_network'] = config.Boolean()
        schema['allow_cache'] = config.Boolean()
        return schema

    def setup(self, registry):
        from .siriusXMBackend import SiriusXM
        registry.add('backend', SiriusXM)
