
# coding: utf-8

# In[63]:


import pandas as pd
import numpy as np
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

# In[244]:


def tsv_converter(path,file):
    source = pd.read_csv(path+file, sep="\t")
    index_names = [s.replace('\\', '') for s in source.columns[0].split(",")] 
    index_names.extend(["date", "value"])
    
    output = pd.DataFrame(index=index_names); counter = 0
    for index, row in source.iterrows():
        for period in source.columns[1:]:
            if period[0].isdigit() == True:
                counter +=1
                values = row[source.columns[0]].split(","); values.extend([period, row[period]])
                output[counter] = values
    
    if output.shape[1] == 0:
        return("Problem in "+file)
    
    output = output.transpose()
    output.value = output.value.astype(str).str.replace(r"[a-zA-Z\s\:]", "").replace("", np.nan).astype(float)

    try:
        output.date = pd.to_datetime(output.date.str.strip())
    except ValueError:
        output.date = pd.to_datetime(output.date.str.strip(), format="%YM%m")
    
    output.to_csv(path+"converted/"+file[:-3]+"csv", index=False)


# In[ ]:


path = "./data/tables-of-EU-policy/"
files_done = os.listdir(path+"converted/")
for tsv_file in [i for i in os.listdir(path) if i[-3:]=="tsv"]:
    if tsv_file[:-3]+"csv" not in files_done:
        print(tsv_file)
        tsv_converter(path, tsv_file)
del path

