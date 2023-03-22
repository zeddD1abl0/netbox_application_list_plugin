"""Top-level package for NetBox Application List Plugin."""

__author__ = """Jordan Keith"""
__email__ = 'zedd_D1abl0@gmail.com'
__version__ = '0.1.0'


from extras.plugins import PluginConfig


class ApplicationListConfig(PluginConfig):
    name = 'netbox_application_list_plugin'
    verbose_name = 'NetBox Application List Plugin'
    description = 'Application list plugin for NetBox'
    version = 'version'
    base_url = 'netbox_application_list_plugin'


config = ApplicationListConfig
