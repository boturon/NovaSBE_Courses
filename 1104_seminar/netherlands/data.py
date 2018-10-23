
# coding: utf-8

# In[130]:


import pandas as pd
import os


# <br>

# # Tables of EU Policy
# - **tips** -  Macroeconomic imbalance procedure indicators
# - **shorties** -  Euro indicators / PEEIs
# - **t2020** -  Europe 2020 indicators
# - **cei** -  Circular economy indicators
# - **sdg** -  Sustainable development indicators
# - **es** -  Employment and social policy indicators
# - **tepsr** -  European pillar of social rights
# 

# <br>

# In[167]:


def tsv_converter(path,file):
    source = pd.read_csv(path+file, sep="\t")
    index_names = source.columns[0].split(","); index_names.extend(["date", "value"])
    
    output = pd.DataFrame(index=index_names); counter = 0
    for index, row in source.iterrows():
        for period in source.columns[1:]:
            if period[0].isdigit() == True:
                counter +=1
                values = row[source.columns[0]].split(","); values.extend([period, row[period]])
                output[counter] = values
    
    output = output.transpose()
    try:
        output.date = pd.to_datetime(output.date.str.strip())
    except ValueError:
        output.date = pd.to_datetime(output.date.str.strip(), format="%YM%m")
    
    output.to_csv(path+"converted/"+file[:-3]+"csv", index=False)


# In[ ]:


path = "./data/tables-of-EU-policy/"
for tsv_file in [i for i in os.listdir(path) if i[-3:]=="tsv"]:
    print(tsv_file)
    tsv_converter(path, tsv_file)
del path


# <br>

# ## **tips** Macroeconomic imbalance procedure indicators
# - **tips_h** - MIP Scoreboard indicators
# - **tipsbp** - Current account balance and balance of payments
# - **tipsii** - International investment position
# - **tipsed** - External debt
# - **tipser** - Effective exchange rates
# - **tipsex** - Export market shares
# - **tipsgo** - General government gross debt (EDP concept)
# - **tipsfs** - Financial sector liabilities
# - **tipspd** - Private sector debt
# - **tipspc** - Private sector credit flow
# - **tipsnf** - Non-financial transactions - annual data
# - **tipsun** - Unemployment
# - **tipslc** - Unit labour cost
# - **tipsho** - House price indices
# - **tipspo** - Poverty and social exclusion
# - **tipsgd** - Gross domestic product (GDP)
# - **tipsrd** - Research and development
# - **mips_sa** - Macroeconomic imbalance procedure - Statistical annex indicators

# <br>

# In[170]:



tsv_converter("./data/tables-of-EU-policy/", "t2020_50.tsv")

