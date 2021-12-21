from rest_framework.routers import APIRootView

from messaging.api.serializers import (
    ContactAssignmentSerializer,
    ContactRoleSerializer,
    ContactSerializer,
)
from messaging.filters import (
    ContactAssignmentFilterSet,
    ContactFilterSet,
    ContactRoleFilterSet,
)
from messaging.models import Contact, ContactAssignment, ContactRole
from peering_manager.api.views import ModelViewSet


class MessagingRootView(APIRootView):
    def get_view_name(self):
        return "Messaging"


class ContactRoleViewSet(ModelViewSet):
    queryset = ContactRole.objects.all()
    serializer_class = ContactRoleSerializer
    filterset_class = ContactRoleFilterSet


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filterset_class = ContactFilterSet


class ContactAssignmentViewSet(ModelViewSet):
    queryset = ContactAssignment.objects.prefetch_related("object", "contact", "role")
    serializer_class = ContactAssignmentSerializer
    filterset_class = ContactAssignmentFilterSet