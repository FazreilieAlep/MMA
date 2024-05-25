from data.models import MyGovEconomicIndicator, MyGovMonetoryAggregates, MyGovHouseholdIncomebyPercentile, MyGovHouseholdIncomeAndExpenditureStates
from . import common

def update_table(model_class, json_data, col_check):
    # Iterate over json_data and update or create objects
    for entry in json_data:
        # Construct dictionary containing values for columns to check
        condition_kwargs = {col: entry.pop(col) for col in col_check}
        
        # Check if an object with the same values on specific columns exists
        obj, created = model_class.objects.update_or_create(defaults=entry, **condition_kwargs)
        
    if created:
        return "Updated"
    else:
        return "Already up to date"

def updateDB(host_path, data_path, json_data):
    url = common.get_web_url(host_path, data_path)
    json_data = common.get_response_json(url)
    if host_path == 'my_gov':
        if data_path == 'economic-indicator':
            return update_table(MyGovEconomicIndicator, json_data, ['date'])
        elif data_path == 'monetory-aggregates':
            return update_table(MyGovMonetoryAggregates, json_data, ['date', 'measure'])
        elif data_path == "household-income-by-percentile":
            return update_table(MyGovHouseholdIncomebyPercentile, json_data, ['date', 'variable', 'percentile'])
        elif data_path == "household-income-and-expenditure-states":
            return update_table(MyGovHouseholdIncomeAndExpenditureStates, json_data, ['date', 'state'])
        else:
            return "Invalid data path"
    else:
        return "Invalid data path"
    
def updateAllDB():
    return "Under development"
    # KIV
