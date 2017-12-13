
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import itertools
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


bbg_data = pd.read_excel('./data_bloomberg.xlsx', index_col='Dates').dropna(axis=1, how='any')
bbg_stocks = bbg_data[bbg_data.columns.tolist()[2:]]
bbg_ri = bbg_stocks.pct_change().drop(pd.Timestamp('2004-12-31'))
bbg_rM = bbg_data['SPX Index'].pct_change().drop(pd.Timestamp('2004-12-31'))
bbg_r_f = ((1+(bbg_data['USGG3M Index'].drop(pd.Timestamp('2004-12-31'))/100))**(3/12)-1)/(3*4.34812141)


# In[3]:


combs = list(itertools.combinations(bbg_stocks, 3))


# In[4]:


print('There are',len(combs),'combinations.')


# In[ ]:


results = np.zeros((6,len(combs)))
index_list = []
def get_best(i):
    if i%1000000 ==0:
        print(i)
    data = bbg_ri[[combs[i][0], combs[i][1], combs[i][2]]]
    mean = data.mean()*(365.25/7)
    r_f = bbg_r_f.mean()*(365.25/7)
    S = data.cov()*(365.25/7.)
    w_T = np.dot(np.linalg.inv(S), mean - r_f)/sum(np.dot(np.linalg.inv(S), mean - r_f))
    E_r_T = np.dot(w_T, mean)
    std_T = np.sqrt(np.dot(np.transpose(w_T), np.dot(S, w_T)))
    SR = (E_r_T-r_f)/std_T
    index_list.append("("+combs[i][0]+", "+combs[i][1]+", "+combs[i][2]+")")
    results[0,i] = E_r_T
    results[1,i] = std_T
    results[2,i] = SR
    for j in range(3):
        results[j+3,i] = np.transpose(w_T)[j]

[get_best(x) for x in range(len(combs))]

results_table = pd.DataFrame(results.T,columns=['ret','stdev','sharpe','w0', 'w1','w2'], index=index_list)

results_table.to_csv('q5.csv')


# In[ ]:


#results_table.head()


# In[ ]:


#results_table.transpose().idxmax()


# In[ ]:


#results_table.transpose().idxmin()

