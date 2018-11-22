from sklearn.ensemble import *
import pandas as pd

data = pd.read_excel('2018 APMCM Problems/2018 APMCM Problem B/Annex Job market of A-City Market Demand Statistics/2015/09.xlsx')
data.drop([0,1],axis=0)
