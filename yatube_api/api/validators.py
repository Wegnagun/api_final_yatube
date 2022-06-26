from rest_framework import serializers


class ValidateSelfSubscription:
    def __init__(self, user='user', following='following'):
        self.user = user
        self.following = following

    def __call__(self, data):
        if data[self.user] == data[self.following]:
            raise serializers.ValidationError(
                'На себя подписываться запрещено.')
        return data
