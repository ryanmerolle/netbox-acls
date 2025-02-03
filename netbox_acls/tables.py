"""
Define the object lists / table view for each of the plugin models.
"""

import django_tables2 as tables
from netbox.tables import ChoiceFieldColumn, NetBoxTable, columns

from .models import AccessList, ACLExtendedRule, ACLInterfaceAssignment, ACLStandardRule, ACLGroup

__all__ = (
    "AccessListTable",
    "ACLInterfaceAssignmentTable",
    "ACLStandardRuleTable",
    "ACLExtendedRuleTable",
    "ACLGroupTable",
)


COL_HOST_ASSIGNMENT = """
    {% if record.assigned_object.device %}
    <a href="{{ record.assigned_object.device.get_absolute_url }}">{{ record.assigned_object.device|placeholder }}</a>
    {% else %}
    <a href="{{ record.assigned_object.virtual_machine.get_absolute_url }}">{{ record.assigned_object.virtual_machine|placeholder }}</a>
    {% endif %}
 """


class AccessListTable(NetBoxTable):
    """
    Defines the table view for the AccessList model.
    """

    pk = columns.ToggleColumn()
    id = tables.Column(
        linkify=True,
    )
    assigned_object = tables.Column(
        linkify=True,
        orderable=False,
        verbose_name="Assigned Host",
    )
    name = tables.Column(
        linkify=True,
    )
    device = tables.Column(
        linkify=True,
    )
    type = ChoiceFieldColumn()
    default_action = ChoiceFieldColumn()
    rule_count = tables.Column(
        verbose_name="Rule Count",
    )
    acl_group = tables.Column(
        linkify=True,
        verbose_name="ACL Group",
    )
    tags = columns.TagColumn(
        url_name="plugins:netbox_acls:accesslist_list",
    )

    class Meta(NetBoxTable.Meta):
        model = AccessList
        fields = (
            "pk",
            "id",
            "name",
            "assigned_object",
            "type",
            "rule_count",
            "default_action",
            "comments",
            "action",
            "tags",
            "acl_group",
        )
        default_columns = (
            "name",
            "assigned_object",
            "type",
            "rule_count",
            "default_action",
            "tags",
            "acl_group",
        )


class ACLInterfaceAssignmentTable(NetBoxTable):
    """
    Defines the table view for the AccessList model.
    """

    pk = columns.ToggleColumn()
    id = tables.Column(
        linkify=True,
    )
    access_list = tables.Column(
        linkify=True,
    )
    direction = ChoiceFieldColumn()
    host = tables.TemplateColumn(
        template_code=COL_HOST_ASSIGNMENT,
    )
    assigned_object = tables.Column(
        linkify=True,
        orderable=False,
        verbose_name="Assigned Interface",
    )
    tags = columns.TagColumn(
        url_name="plugins:netbox_acls:aclinterfaceassignment_list",
    )

    class Meta(NetBoxTable.Meta):
        model = ACLInterfaceAssignment
        fields = (
            "pk",
            "id",
            "access_list",
            "direction",
            "host",
            "assigned_object",
            "tags",
        )
        default_columns = (
            "id",
            "access_list",
            "direction",
            "host",
            "assigned_object",
            "tags",
        )


class ACLStandardRuleTable(NetBoxTable):
    """
    Defines the table view for the ACLStandardRule model.
    """

    access_list = tables.Column(
        linkify=True,
    )
    index = tables.Column(
        linkify=True,
    )
    action = ChoiceFieldColumn()
    tags = columns.TagColumn(
        url_name="plugins:netbox_acls:aclstandardrule_list",
    )

    class Meta(NetBoxTable.Meta):
        model = ACLStandardRule
        fields = (
            "pk",
            "id",
            "access_list",
            "index",
            "action",
            "remark",
            "tags",
            "description",
            "source_prefix",
        )
        default_columns = (
            "access_list",
            "index",
            "action",
            "remark",
            "source_prefix",
            "tags",
        )


class ACLExtendedRuleTable(NetBoxTable):
    """
    Defines the table view for the ACLExtendedRule model.
    """

    access_list = tables.Column(
        linkify=True,
    )
    index = tables.Column(
        linkify=True,
    )
    action = ChoiceFieldColumn()
    tags = columns.TagColumn(
        url_name="plugins:netbox_acls:aclextendedrule_list",
    )
    protocol = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = ACLExtendedRule
        fields = (
            "pk",
            "id",
            "access_list",
            "index",
            "action",
            "remark",
            "tags",
            "description",
            "source_prefix",
            "source_ports",
            "destination_prefix",
            "destination_ports",
            "protocol",
        )
        default_columns = (
            "access_list",
            "index",
            "action",
            "remark",
            "tags",
            "source_prefix",
            "source_ports",
            "destination_prefix",
            "destination_ports",
            "protocol",
        )


class ACLGroupTable(NetBoxTable):
    """
    Defines the table view for the ACLGroup model.
    """

    pk = columns.ToggleColumn()
    id = tables.Column(
        linkify=True,
    )
    name = tables.Column(
        linkify=True,
    )
    devices = tables.ManyToManyColumn(
        linkify_item=True,
        verbose_name="Devices",
    )
    virtual_chassis = tables.ManyToManyColumn(
        linkify_item=True,
        verbose_name="Virtual Chassis",
    )
    virtual_machines = tables.ManyToManyColumn(
        linkify_item=True,
        verbose_name="Virtual Machines",
    )
    tags = columns.TagColumn(
        url_name="plugins:netbox_acls:aclgroup_list",
    )

    class Meta(NetBoxTable.Meta):
        model = ACLGroup
        fields = (
            "pk",
            "id",
            "name",
            "devices",
            "virtual_chassis",
            "virtual_machines",
            "tags",
        )
        default_columns = (
            "name",
            "devices",
            "virtual_chassis",
            "virtual_machines",
            "tags",
        )
