from rest_framework import serializers


class ValidateSelfSubscription:
    def __init__(self, *fields):
        self.fields = fields

    def iterator(self, data):
        return [data[value] for value in self.fields]

    def __call__(self, data):
        iterated_data = self.iterator(data)
        if all(
                iterated_data[i] == iterated_data[0]
                for i in range(1, len(iterated_data))):
            raise serializers.ValidationError("Есть сопадение! (^_-)")
