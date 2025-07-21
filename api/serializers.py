from rest_framework import serializers
from .models import BogieChecksheet, BmbcChecksheet, WheelAssembly, WheelSpecification

class BmbcChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmbcChecksheet
        fields = '__all__'

class WheelAssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelAssembly
        fields = '__all__'

class BogieChecksheetSerializer(serializers.ModelSerializer):
    bmbcChecksheet = BmbcChecksheetSerializer()
    wheelAssembly = WheelAssemblySerializer()

    class Meta:
        model = BogieChecksheet
        fields = '__all__'

    def create(self, validated_data):
        bmbc_data = validated_data.pop('bmbcChecksheet')
        wheel_data = validated_data.pop('wheelAssembly')

        bmbc = BmbcChecksheet.objects.create(**bmbc_data)
        wheel = WheelAssembly.objects.create(**wheel_data)

        bogie = BogieChecksheet.objects.create(
            bmbcChecksheet=bmbc,
            wheelAssembly=wheel,
            **validated_data
        )
        return bogie

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

