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


# x is first age in the interval

# n is number of years in the age interval from x to x+n (provided)

# nNx is the midyear population in the age interval x to x+n (provided)

# nDx is the deaths between ages x and x+n during the year (provided)

# nmx is the death rate: nDx/nNx

# nax is the average number of person-years lived by those dying in the interval:
# unless provided, it is assumed to be n/2 for ages 5+. 
# Coale-Demeny (1983) assumptions apply for ages 0-5:
## for males ages 0-1 and 1m0 >= .107: nax = .330
## for females ages 0-1 and 1m0 >= .107: nax = .350
## for males ages 0-1 and 1m0 <.107: 0.45+2.684*1m0
## for females ages 0-1 and 1m0 <.107: 0.53+2.8*1m0
## for males ages 1-4 and 4m1 >= .107: nax = 1.352
## for females ages 1-4 and 4m1 >= .107: nax = 1.361
## for males ages 1-4 and 4m1 <.107: 1.651-2.816*4m1
## for females ages 1-4 and 4m1 <.107: 1.522-1.518*4m1
## for open age interval (last row): nax = 1/nmx 

# nqx = (n*nmx)/(1+(n-nax)*nmx)
# for last row, nqx = 1

# npx = 1-nqx

# l0 starts with 100000
# lx+n = lx*npx

# ndx = lx - lx+n
# for last row, ndx=lx

# nLx = n*lx+n + nax*ndx
# open ended nx = lx/open ended nmx

# Tx = sum of all the nLx from x to the end

# ex = Tx/lx



