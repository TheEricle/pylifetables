# Master Life Table Variables and Operations
import pandas

class LifeTable:
	def __init__(self, pop_distribution_csv, gender="M"):
		pop_dataframe = preprocess_pop(pop_distribution_csv)
		self.gender = gender
		self.pop_distribution = pandas.concat([pop_dataframe['x'],
												pop_dataframe['n'],
												pop_dataframe['nDx'],
												pop_dataframe['nNx']
												], axis=1)

	
	def preprocess_pop(pop_distribution_csv):
		pop_distribution_raw = pandas.DataFrame.from_csv(pop_distribution_csv, sep=';', index_col=None)
		pop_distribution_raw = pop_distribution_raw.applymap(str)
		pop_distribution_raw = pop_distribution_raw.applymap(float)
		pop_distribution = pop_distribution_raw.iloc[:,0:4]
		return pop_distribution

	def get_pop_distribution(self):
		return self.pop_distribution

	def get_pop_x(self):
		# x is first age in the interval
		return self.get_pop_distribution()['x']

	def get_pop_n(self):
		# n is number of years in the age interval from x to x+n (provided)
		return self.get_pop_distribution()['n']
	
	def get_pop_ndx(self):
		# nDx is the deaths between ages x and x+n during the year (provided)
		return self.get_pop_distribution()['nDx']

	def get_pop_nnx(self):
		# nNx is the midyear population in the age interval x to x+n (provided)
		return self.get_pop_distribution()['nNx']

	def calculate_nmx(nnx, ndx):
		return nnx/ndx

	def get_pop_nmx(self):
		return calculate_nmx(self.get_pop_nnx(), self.get_pop_ndx())

	def calculate_nqx(n, nmx, nax):
		 #TODO factor in last row is always 1
		return(n * nmx)/(1+(n-nax)*nmx)

	def get_pop_nqx(self):
		return self.calculate_nqx(self.get_pop_n(),self.get_pop_nmx(), self.get_pop_nax())

	def calculate_nax_first(nmx):
		#Assumes Male @TODO deal with male or female
	    if nmx >=.107:
	        nax=.33
	    else:
	        nax = .45 + 2.684*nmx
		return nax

	def calculate_nax_to_5(nmx):
	    #Assumes Male
	    #@TODO deal with male or female
	    if nmx >=.107:
	        nax = 1.352
	    else:
	        nax = 1.651-2.816*nmx

	def calculate_nax_middle(n):
		return n/2

	def calculate_nax_last(nmx):
		return 1/nmx

	def get_pop_nax(self):
		# nax is the average number of person-years lived by those dying in the interval:
		# unless provided, it is assumed to be n/2 for ages 5+. 
	    nmx = self.get_pop_nmx()
	    nmx.name = "nmx"
	    pop_plus_nmx = pandas.concat([self.get_pop_distribution(), nmx], axis=1)
	    calculate_nax_first(pop_plus_nmx.head(n=1)["nmx"])
	    calculate_nax_last(pop_plus_nmx.tail(n=1)["nmx"])
	    # Remove head_and_tail
	    headless_pop_distribution = pop_plus_nmx.ix[1:1]
	    calculate_nax_middle(headless_pop_distribution.query('n>5')['n'])
	    calculate_nax_to_5(headless_pop_distribution.query('n<5')['nmx'])
	    nax = pandas.concat([first, under_5, middle, last])
	    return nax		

	def get_pop_nqx(self):
		# nqx = (n*nmx)/(1+(n-nax)*nmx)
		# for last row, nqx = 1
		 #TODO factor in last row is always 1
		return (self.get_pop_n() * self.get_pop_nmx())/(1+(self.get_pop_n()-self.get_pop_nax)*self.get_pop_nmx())

	def get_pop_npx(self):
		# npx = 1-nqx
		return 1-self.get_pop_nqx()











# nmx is the death rate: nDx/nNx

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





# l0 starts with 100000
# lx+n = lx*npx

# ndx = lx - lx+n
# for last row, ndx=lx

# nLx = n*lx+n + nax*ndx
# open ended nx = lx/open ended nmx

# Tx = sum of all the nLx from x to the end

# ex = Tx/lx



