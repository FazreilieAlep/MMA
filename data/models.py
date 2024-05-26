from django.db import models
from .enums import State


class Host(models.Model):
    organization_name = models.CharField(max_length=200)
    acronyms = models.CharField(max_length=20, default=None, null=True)
    domain_name = models.CharField(max_length=200, unique=True)
    path = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.organization_name
    

class Web_API(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    data = models.CharField(max_length=200, null=True)
    path = models.CharField(max_length=30, null=False)
    url = models.CharField(max_length=200)
    
    def __str__(self):
            return self.data
    

class MyGovEconomicIndicator(models.Model):
    date =  models.DateField()
    lagging = models.DecimalField(max_digits=10, decimal_places=2)
    leading = models.DecimalField(max_digits=10, decimal_places=2)
    coincident = models.DecimalField(max_digits=10, decimal_places=2)
    leading_diffusion = models.DecimalField(max_digits=10, decimal_places=2)
    coincident_diffusion = models.DecimalField(max_digits=10, decimal_places=2)
        

class MyGovMonetoryAggregates(models.Model):
    date = models.DateField()
    value = models.DecimalField(max_digits=10000, decimal_places=2)
    measure = models.CharField(max_length=15, null=False)
    

class MyGovHouseholdIncomebyPercentile(models.Model):
    date = models.DateField()
    percentile = models.IntegerField()
    variable = models.CharField(max_length=8)
    income = models.IntegerField(null=True)
    

class MyGovHouseholdIncomeAndExpenditureStates(models.Model):
    date = models.DateField()
    state =  models.CharField(max_length=20)
    expenditure_mean = models.IntegerField(null=False)
    income_median = models.IntegerField(null=False)
    income_mean = models.IntegerField(null=False)
    gini = models.DecimalField(max_digits=20, decimal_places=8)
    poverty = models.DecimalField(max_digits=20, decimal_places=2, default=-0.0)
    # state = {
    #      JOHOR: "Johor",
    #      KEDAH: "Kedah",
    #      KELANTAN: "Kelantan",
    #      MELAKA: "Melaka",
    #      NEGERI_SEMBILAN: "Negeri Sembilan",
    #      PAHANG: "Pahang",
    #      PULAU_PINANG: "Pulau Pinang",
    #      PERAK: "Perak",
    #      PERLIS: "Perlis",
    #      SELANGOR: "Selangor",
    #      TERENGGANU: "Terengganu",
    #      SABAH: "Sabah",
    #      SARAWAK: "Sarawak",
    #      WP_KL: "W.P. Kuala Lumpur",
    #      WP_Labuan: "W.P Labuan",
    # }

    
    

    
