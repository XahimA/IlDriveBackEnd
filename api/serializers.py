from rest_framework import serializers
from .models import CarDetail, UserDetail,TripDetail, DriverDetail, truck,NewTripDetails, Data,OwnerDetail


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetail
        # fields = ['time', 'ax', 'ay', 'az', 'speed', 'trip', 'geoloacation']
        fields = '__all__'

class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

class UserdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        # fields = ['time', 'ax', 'ay', 'az', 'speed', 'trip', 'geoloacation']
        fields = ['id','Trip']

class TripDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripDetail
        # fields = ['time', 'ax', 'ay', 'az', 'speed', 'trip', 'geoloacation']
        # fields = ['Trip_No', 'Risk_Instance', 'Average_speed', 'Trip_time', 'Distance_Travelled', 'Score']
        fields = '__all__'

class TripDetailsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripDetail
        # fields = ['time', 'ax', 'ay', 'az', 'speed', 'trip', 'geoloacation']
        fields = ['Trip_No', 'Risk_Instance', 'Average_speed', 'Trip_time', 'Distance_Travelled', 'Score', 'C1', 'C2', 'C4']
        # fields = '__all__'

class DriverDetailsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model =  DriverDetail
        # fields = ['time', 'ax', 'ay', 'az', 'speed', 'trip', 'geoloacation']
        # fields = ['Name', 'Sirname', 'PhoneNo']
        fields = '__all__'

class truckdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = truck
        fields = '__all__'
        # depth = 1

class NewTripdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTripDetails
        fields = '__all__'

class DataDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class OwnerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerDetail
        fields = '__all__'
