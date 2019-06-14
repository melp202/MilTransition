from rest_framework import generics
from .serializers import StatesSerializer, OrganizationsSerializer
from .models import State, Organization


# from .forms import ArtistForm
# from .forms import SongForm

# create list view for API and create view
class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StatesSerializer

# create show, update, and delete routes for our API
class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StatesSerializer

# create list view for API and create view
class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationsSerializer

# create show, update, and delete routes for our API
class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationsSerializer

