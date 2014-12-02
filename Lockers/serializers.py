__author__ = 'luishoracio'
from rest_framework import serializers
from Lockers.models import *


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'user_name', 'user_ap', 'user_am', 'user_matricula', 'user_discount')
        # fields = ('user_id', 'user_name', 'user_ap', 'user_am', 'user_times', 'user_discount',
        #          'user_match', 'user_has_assigned_key')


class AreasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Areas
        fields = ('area_id', 'area_name', 'area_description', 'area_enable')


class LockersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lockers
        fields = ('locker_id', 'locker_name', 'locker_match', 'locker_status', 'locker_start_time', 'fk_area', 'fk_user')
        # fields = ('locker_id', 'locker_name', 'locker_match', 'locker_status', 'fk_area')


class RatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rates
        fields = ('rate_id', 'rate_name', 'rate_rate', 'rate_unit', 'rate_currency')


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = (
            'log_id', 'log_start_time', 'log_total_pay', 'log_rate', 'log_discount', 'log_used_time', 'fk_locker_id',
            'fk_user_id')