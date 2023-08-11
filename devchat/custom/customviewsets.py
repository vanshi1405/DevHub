from rest_framework import viewsets


class CustomProfileViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        pass