import pandas as pd
# 8 Countries ki dictionary jahan values ek list hain
countries_dict = {
    "Pakistan": ["Islamabad", "240 Million", "South Asia"],
    "Saudi Arabia": ["Riyadh", "36 Million", "Middle East"],
    "Japan": ["Tokyo", "125 Million", "East Asia"],
    "United Kingdom": ["London", "67 Million", "Europe"],
    "Canada": ["Ottawa", "40 Million", "North America"],
    "Egypt": ["Cairo", "112 Million", "Africa"],
    "Brazil": ["Brasilia", "215 Million", "South America"],
    "Australia": ["Canberra", "26 Million", "Oceania"]
}

# Kisi specific country ki details access karne ka tareeqa
# print(countries_dict["Pakistan"])  # Output: ['Islamabad', '240 Million', 'South Asia']

data_= pd.DataFrame(countries_dict)
print(data_)
# into jason
data_.to_json('data-dict_json.json',indent=5)
# read the 