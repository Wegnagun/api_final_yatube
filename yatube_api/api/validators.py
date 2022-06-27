from rest_framework import serializers


class ValidateSelfSubscription:
    requires_context = True

    def __call__(self, serializer_field):
        print(f'dfdfdfdf   {serializer_field.context["request"].user}')
        # for i, y in serializer_field[0].items():
        #     print(f'dfdfdfdf   {y}')
        # if all(field == serializer_field[field] for field in serializer_field):
        #     raise serializers.ValidationError("Name already exists!")
        # return serializer_field
