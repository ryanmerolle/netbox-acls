"""
Define the NetBox Plugin
"""

from netbox.plugins import PluginConfig

from .version import version_semver


class NetBoxACLsConfig(PluginConfig):
    """
    Plugin specifc configuration
    """

    name = "netbox_acls"
    verbose_name = "Access Lists"
    version = version_semver()
    description = "Manage simple ACLs in NetBox"
    base_url = "access-lists"
    min_version = "4.1.0"
    max_version = "4.1.99"


config = NetBoxACLsConfig
