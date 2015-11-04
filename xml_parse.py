# 'xmldataset' test


#%% Clear variable list
def clearall():
    """clear all globals"""
    for uniquevar in [var for var in globals().copy()
                      if var[0] != "_" and var != 'clearall']:
        del globals()[uniquevar]
clearall()


#%% Import libraries
import pyodbc
# from datetime import datetime, timedelta
import pandas.io.sql
import xmldataset
# import pandas as pd
# import numpy as np
# from itertools import repeat
from pandas import DataFrame #Series, merge , ExcelWriter
# import win32com.client


#%% Query strings
query_shop = "SELECT data FROM dim_config WHERE created in (SELECT max(created) FROM dim_config) AND configName = 'ShopItemConfig'"
query_quest = "SELECT data FROM dim_config WHERE created in (SELECT max(created) FROM dim_config) AND configName = 'QuestConfig'"


#%% Query data
myconn = pyodbc.connect("DSN=" + "MMHO_CLB")

raw_shop = pandas.io.sql.read_sql(query_shop, myconn)['data'][0]
raw_quest = pandas.io.sql.read_sql(query_quest, myconn)['data'][0]
myconn.close()



#%% xmldataset setup
profile_shop = """
ShopItemConfigList
    ShopItemConfigData
        id = dataset:ShopItemConfigList
        name = dataset:ShopItemConfigList"""

profile_quest = """
QuestConfigList
    QuestConfigData
        id = dataset:QuestConfigList
        name = dataset:QuestConfigList
        repeatable = dataset:QuestConfigList
        questGiver = dataset:QuestConfigList
        type = dataset:QuestConfigList
        minLevel = dataset:QuestConfigList
        questRegion = dataset:QuestConfigList
        questLevel = dataset:QuestConfigList"""


#%% Parse XML
df_shop = xmldataset.parse_using_profile(raw_shop, profile_shop)
df_shop = DataFrame(df_shop['ShopItemConfigList'])

df_quest = xmldataset.parse_using_profile(raw_quest, profile_quest)
df_quest = DataFrame(df_quest['QuestConfigList'])





















