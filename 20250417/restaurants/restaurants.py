# This program loads all the restaurants from the dst_restaurant.xml file
# with pandas.dataframe

import pandas as pd

df = pd.read_xml("dst_restaurant.xml")

# print(df.columns)

available_columns = ['id', 'dish_name_zh', 'dish_name_gb', 'dish_name_en', 'dish_name_pt',
       'name_cn', 'name_gb', 'name_en', 'name_pt', 'address_cn', 'address_gb',
       'address_en', 'address_pt', 'hours_cn', 'hours_en', 'hours_pt', 'tel',
       'fax', 'email', 'website', 'class']

pick_columns = ['dish_name_zh', 'name_cn', 'address_cn']

# Random pick one
random_dish = df.sample(1)[pick_columns]

print(random_dish)