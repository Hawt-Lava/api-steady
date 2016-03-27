from rest_framework import mixins
from rest_framework import generics


class BaseView(mixins.RetrieveModelMixin, mixins.ListModelMixin,
               mixins.UpdateModelMixin, mixins.DestroyModelMixin,
               generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
