"""
Create views to handle the API logic.
A view set is a single class that can handle the view, add, change,
and delete operations which each require dedicated views under the UI.
"""

from django.db.models import Count
from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import (
    AccessListSerializer,
    ACLExtendedRuleSerializer,
    ACLInterfaceAssignmentSerializer,
    ACLStandardRuleSerializer,
    ACLGroupSerializer,
    ACLGroupInterfaceAssignmentSerializer,
)

__all__ = [
    "AccessListViewSet",
    "ACLStandardRuleViewSet",
    "ACLInterfaceAssignmentViewSet",
    "ACLExtendedRuleViewSet",
    "ACLGroupViewSet",
    "ACLGroupInterfaceAssignmentViewSet",
]


class AccessListViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django AccessList model & associates it to a view.
    """

    queryset = (
        models.AccessList.objects.prefetch_related("tags")
        .annotate(
            rule_count=Count("aclextendedrules") + Count("aclstandardrules"),
        )
        .prefetch_related("tags")
    )
    serializer_class = AccessListSerializer
    filterset_class = filtersets.AccessListFilterSet


class ACLInterfaceAssignmentViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ACLInterfaceAssignment model & associates it to a view.
    """

    queryset = models.ACLInterfaceAssignment.objects.prefetch_related(
        "access_list",
        "tags",
    )
    serializer_class = ACLInterfaceAssignmentSerializer
    filterset_class = filtersets.ACLInterfaceAssignmentFilterSet


class ACLStandardRuleViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ACLStandardRule model & associates it to a view.
    """

    queryset = models.ACLStandardRule.objects.prefetch_related(
        "access_list",
        "tags",
        "source_prefix",
    )
    serializer_class = ACLStandardRuleSerializer
    filterset_class = filtersets.ACLStandardRuleFilterSet


class ACLExtendedRuleViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ACLExtendedRule model & associates it to a view.
    """

    queryset = models.ACLExtendedRule.objects.prefetch_related(
        "access_list",
        "tags",
        "source_prefix",
        "destination_prefix",
    )
    serializer_class = ACLExtendedRuleSerializer
    filterset_class = filtersets.ACLExtendedRuleFilterSet


class ACLGroupViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ACLGroup model & associates it to a view.
    """

    queryset = models.ACLGroup.objects.prefetch_related("tags")
    serializer_class = ACLGroupSerializer
    filterset_class = filtersets.ACLGroupFilterSet


class ACLGroupInterfaceAssignmentViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ACLGroupInterfaceAssignment model & associates it to a view.
    """

    queryset = models.ACLGroupInterfaceAssignment.objects.prefetch_related(
        "acl_group",
        "interface",
        "tags",
    )
    serializer_class = ACLGroupInterfaceAssignmentSerializer
    filterset_class = filtersets.ACLGroupInterfaceAssignmentFilterSet
