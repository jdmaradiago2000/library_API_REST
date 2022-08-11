from rest_framework import serializers

from .models import ShelfBookCopy


# class ShelfCopySerializer(serializers.ModelSerializer):
#     class Meta:
#         fields ="__all__"
#         model =Shelf
class ShelfSerializer(serializers.ModelSerializer):
    #  shelf = ShelfCopySerializer()
    class Meta:
        fields = "__all__"
        model = ShelfBookCopy
        depth = 1
