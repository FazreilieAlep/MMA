from rest_framework import serializers
from .models import Web_API, Host, MyGovEconomicIndicator, MyGovHouseholdIncomeAndExpenditureStates, MyGovHouseholdIncomebyPercentile, MyGovMonetoryAggregates

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['organization_name', 'domain_name', 'path', 'acronyms']

class Web_APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Web_API
        fields = ['data', 'path']

class MyGovEconomicIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGovEconomicIndicator
        fields = ['date' , 'lagging', 'leading', 'coincident', 'leading_diffusion', 'coincident_diffusion']     

class MyGovHouseholdIncomeAndExpenditureStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGovHouseholdIncomeAndExpenditureStates
        fields = ['date', 'state', 'expenditure_mean', 'income_median', 'income_mean', 'gini', 'poverty']
        
class MyGovHouseholdIncomebyPercentileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGovHouseholdIncomebyPercentile
        fields = ['date', 'percentile', 'variable', 'income']

class MyGovMonetoryAggregatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGovMonetoryAggregates
        fields = ['date', 'value', 'measure']