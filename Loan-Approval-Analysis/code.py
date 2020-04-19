# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
banks.replace(to_replace = np.nan, value = bank_mode,inplace = True) 
#banks = banks.fillna(bank_mode,inplace = True)
#print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks, values ='LoanAmount', index =['Gender', 'Married', 'Self_Employed'],aggfunc = np.mean)


# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].index)
loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].index)
Loan_Status = 614
percentage_se = (loan_approved_se *100)/Loan_Status
percentage_nse = (loan_approved_nse *100)/Loan_Status
# code ends here


# --------------
# code starts here
#loan_term = banks.apply(pd.DatetimeIndex(banks['Loan_Amount_Term']).year)
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x) / 12)
#print(loan_term)
big_loan_term = len(loan_term[loan_term >= 25])
#print(big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
#print(loan_groupby.head(5))


# code ends here


