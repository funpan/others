
# coding: utf-8

# In[35]:

# To filter out any Teamsite users that are no longer exist in AD (Resigned)
# 1) Read 2 lists, 1 - AD_users.dat; 2 - ts_userslis.txt
# 2) Clean up the data and form into 2 dataframes, ad_users & ts_users
# 3) Compare TS user login with ad_users list, if not found in ad_users list, add the login ID into non_exist_users list
# 4) print the result

import re
import csv
import pandas as pd

file = open("./AD_users.dat", "r")
data = file.readlines()

file = open("./ts_users_prod.txt", "r")
data1 = list(csv.reader(file, delimiter='\t'))

ad_logins = []
ad_acc_names = []
ts_logins = []
ts_acc_names = []


# In[36]:

for line in data:
    if re.search("^SamAccountName", line) is not None:
        label = line.strip('\n')
        label = re.split(': ', label)
        ad_logins.append(label[1].upper())
    elif re.search("^Name", line) is not None:
        label = line.strip('\n')
        label = re.split(': ', label)
        ad_acc_names.append(label[1].upper())


# In[37]:

ad_list = pd.DataFrame({'login':ad_logins, 'ac name':ad_acc_names})
ad_list = ad_list.sort_values(by="login", ascending=1)
ad_list[:100]


# In[38]:

for line in data1:
    ln = line[0].replace("\\", "/")
    ts_logins.append(ln[10:].upper())
    n = line[1]
    ts_acc_names.append(n.upper())


# In[39]:

ts_list = pd.DataFrame({'login':ts_logins, 'ac name':ts_acc_names})
ts_list = ts_list.sort_values(by="login", ascending=1)
ts_list[:]


# In[40]:

non_exist_users = []
# use pd.values in pandas
#for ts in ts_list.values:
#    print ts

for ts in ts_list.values:
    if not (ad_list["login"] == ts[1]).any():
        non_exist_users.append(ts[1])
non_exist_users


# In[45]:

for ts in ts_list.values:
    if ts[1] == 'MINISTRATOR':
        print ts


# In[46]:

ts_list


# In[ ]:



