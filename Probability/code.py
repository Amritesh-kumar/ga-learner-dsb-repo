# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
#print((df['fico'] > 700).size)
#print(df.size)
#p_a = ((df['fico'] > 700).size)/ df.size
p_a =  df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
#p_b = (df['purpose']  == 'debt_consolation').size/ df.size
p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
#p_b = round(p_b,2)
#print(df['purpose'])
df1 = df[df['purpose'] == 'debt_consolidation']
#p_a_b = p_a + p_b
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
result = p_a_b == p_a
print(result)
# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]
new_df = df[df['paid.back.loan'] == 'Yes']
#prob_pd_cs = new_df[new_df['paid.back.loan']  == 'Yes'].shape[0]/new_df.shape[0]
prob_pd_cs =  new_df[new_df['credit.policy'] == 'Yes'].shape[0]/ new_df.shape[0]
bayes = (prob_pd_cs *  prob_lp) / prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind='bar')
df1 = df[df['paid.back.loan'] == 'No']
df1.plot(kind='bar')
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
df.hist(column='installment', bins=8, figsize=(10,10))
df.hist(column='log.annual.inc', bins=8, figsize=(10,10))

# code ends here


