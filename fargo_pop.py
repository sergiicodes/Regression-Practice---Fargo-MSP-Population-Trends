import numpy as np 
import pandas as pd

years= np.linspace(1880,2020, num=15)
years = list(years)
population = [2693, 5664, 9589, 14331, 21961, 28619, 32580, 38256, 46662, 53365, 61383, 74111, 90599, 105549, 125990]

fargo_pop_dict = {years[i]: population[i] for i in range(len(years))}

df_fargo = pd.DataFrame([fargo_pop_dict])

import matplotlib.pyplot as plt
plt.bar(years, population, width=8)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Census Numbers: Fargo, ND")

#plt.scatter(years, population)

#calculate equation for trendline
z = np.polyfit(years, population, 2)
p = np.poly1d(z)
#add trendline to plot
plt.plot(years, p(years), color="red")

print(p)
