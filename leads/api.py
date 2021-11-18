from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


#Lead Viewset
#It is a class-based View, that does not provide and method handlers such as .get() or .post(). 
#Instead it provides actions such as .lead() and .create()
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permissions_classes= [ 
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer