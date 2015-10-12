# Master Life Table Variables and Operations
import pandas
import pandas
sample = pandas.DataFrame.from_csv("sample.csv", index_col=None)
newsample=sample.applymap(str)
newsample=newsample.apply(lambda x: x.str.replace(',', ''))
newsample=newsample.applymap(float)
processed_sample=newsample.iloc[:,0:4]
processed_sample
nMx = processed_sample['nDx']/processed_sample['nPx']
nAx = processed_sample['n']/2 #TODO factor in open interval and young ages
nqx = (processed_sample['n'] * nMx )/(1+(processed_sample['n']-nAx)*nMx) #TODO factor in last row is always 1
npx = 1-nqx