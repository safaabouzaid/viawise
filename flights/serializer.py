from rest_framework import serializers
from .models import Flight,Review,SeatType,Offer
'''
class FlightSerializer(serializers.ModelSerializer) :
    
    reviws=serializers.SerializerMethodField(method_name='get_reviews',read_only=True)
    class Meta:
        model=Flight
        fields="all"

    def get_reviews(self,obj):
        reviews=obj.reviews.all()
        serializer=ReviewSerializer(reviews,many=True)
        return serializer.data
'''    
class ReviewSerializer(serializers.ModelSerializer) : 
    class Meta:
       
        model=Review
        fields='__all__'

class FlightSerializer(serializers.ModelSerializer) :
    
    class Meta:
        model=Flight
        fields='__all__'       



class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model =SeatType
        fields = ['id', 'seat_number', 'is_reserved']
        
class OfferSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    
    class Meta:
        model = Offer
        fields = '__all__'        





