from rest_framework import serializers
from ONW.models import hosts,groups,network_events,backend_settings

class hostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = hosts
        fields = '__all__'

class groupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = groups
        fields = '__all__'

class network_eventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = network_events
        fields = '__all__'

class backend_settingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = backend_settings
        fields = '__all__'