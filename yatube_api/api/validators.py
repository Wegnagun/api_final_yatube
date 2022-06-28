from rest_framework import serializers


class UniqueFieldValidator:
    def __init__(self, *fields):
        self.fields = fields

    def field_picker(self, data) -> list:
        return [data[value] for value in self.fields]

    def __call__(self, data):
        iterated_data = self.field_picker(data)
        if len(iterated_data) != len(set(iterated_data)):
            raise serializers.ValidationError("Есть совпадение! (^_-)")
