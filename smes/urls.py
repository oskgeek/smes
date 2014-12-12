from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls import url, include
from service.models import Staff, PatientReport
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientReport
        
# ViewSets define the view behavior.
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientReport.objects.all()
    serializer_class = PatientSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'staff', StaffViewSet)
router.register(r'patient', PatientViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
