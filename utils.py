# Master Period Life Table Variables and Operations
import pandas
sample = pandas.DataFrame.from_csv("sample.csv", sep=';', index_col=None)
input_lt_frame=sample.iloc[:,0:4]


# x is first age in the interval

# n is number of years in the age interval from x to x+n (provided)

# nNx is the midyear population in the age interval x to x+n (provided)

# nDx is the deaths between ages x and x+n during the year (provided)

# nmx is the death rate: nDx/nNx
nmx = input_lt_frame['nDx']/input_lt_frame['nNx']
nmx.name = 'nmx'

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
def calculate_nax(df):
   '''
   '''
   if mini['x']>=5:
       nax = mini['n']/2
   elif mini['x']==0 and mini['n']==1:
       #Assumes Male
       #@TODO deal with male or female
       if mini['nmx']>=.107:
           nax =.33
       else:
           nax = .45 + 2.684*mini['nmx']
   elif mini['x']==1 and mini['n']==4:
       #Assumes Male
       #@TODO deal with male or female
       if mini['nmx']>=.107:
           nax =1.352
       else:
           nax = 1.651-2.816*mini['nmx']
   return nax

nax_df_input = pandas.concat([nmx, input_lt_frame],axis=1)
nax=nax_df_input.apply(calculate_nax, axis=1)
nax.iloc[-1]=1/nmx.iloc[-1]
nax.name = 'nax'
# nqx = (n*nmx)/(1+(n-nax)*nmx)
# for last row, nqx = 1

nqx = (input_lt_frame['n'] * nmx )/(1+(input_lt_frame['n']-nax)*nmx) #TODO factor in last row is always 1
nqx.iloc[-1] = 1
nqx.name = 'nqx'
# npx = 1-nqx
npx = 1-nqx
npx.name = 'npx'

# l0 starts with 100000
# lx+n = lx*npx


def calculate_lx(df):
	100000 
	df['npx']


# ndx = lx - lx+n
# for last row, ndx=lx

# nLx = n*lx+n + nax*ndx
# open ended nx = lx/open ended nmx

# Tx = sum of all the nLx from x to the end

# ex = Tx/lx



