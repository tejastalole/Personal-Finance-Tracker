from rest_framework import serializers

class TransactionSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=200)
    amount = serializers.FloatField()
    category = serializers.CharField(max_length=100)
    date = serializers.DateField()
