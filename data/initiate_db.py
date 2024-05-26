from data.models import Host, Web_API

host = Host(organization_name="government of malaysia", domain_name="api.data.gov.my/", path="my_gov", acronyms="dosm")
host.save()

host2 = Host(organization_name="bank negara malaysia", domain_name="api.bnm.gov.my/", path="bnm", acronyms="bnm")
host2.save()


url_list = [{"data": "malaysia economic indicator", "url": "data-catalogue?id=economic_indicators", "path": "economic-indicator"}, 
            {"data": "monetory aggregates", "url": "data-catalogue?id=monetary_aggregates", "path": "monetory-aggregates"},
            {"data": "household income by percentile", "url": "data-catalogue?id=hies_malaysia_percentile", "path": "household-income-by-percentile"},
            {"data": "household income and expenditure: states", "url": "data-catalogue?id=hies_state", "path": "household-income-and-expenditure-states"},]

for item in url_list:  # Iterate over each dictionary in url_list
    data = item["data"]  # Access the "data" key
    url = item["url"]    # Access the "url" key
    path = item["path"]
    web_api = Web_API(data=data, url=url, host=host, path=path)
    web_api.save()
    

username = admin
password = 1234


host_instance = Host.objects.get(id=1)  # Replace id=1 with the appropriate filter condition
web_api_instance = Web_API.objects.get(id=1)  # Replace id=1 with the appropriate filter condition

# Delete the instances
host_instance.delete()
web_api_instance.delete()


# Delete multiple instances using queryset
Host.objects.filter(id=1).delete()  # Replace 'condition' with appropriate filter condition
Host.objects.all().delete()

Web_API.objects.all().delete()  # Replace 'condition' with appropriate filter condition





url_list = [{"data": "malaysia economic indicator", "url": "data-catalogue?id=economic_indicators", "path": "economic-indicator"}, 
            {"data": "monetory aggregates", "url": "data-catalogue?id=monetary_aggregates", "path": "monetory-aggregates"}]

host = Host(organization_name=organization_name, domain_name=domain_name, path=path)
host.save()

for item in url_list:  # Iterate over each dictionary in url_list
    data = item["data"]  # Access the "data" key
    url = item["url"]    # Access the "url" key
    path = item["path"]
    web_api = Web_API(data=data, url=url, host=host, path=path)
    web_api.save()




