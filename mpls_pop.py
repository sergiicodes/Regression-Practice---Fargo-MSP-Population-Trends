import pandas as pd
import numpy as np

location = input("CSV Location: ")
file_name = input("File name: ")    # In this case it is 'data.csv'

file = location + "/" + file_name

excelfile = pd.read_csv(file)
df = pd.DataFrame(excelfile)

years = df.iloc[:,0]
population = df.iloc[:,1]

import matplotlib.pyplot as plt
plt.bar(years, population, width=8)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Census Numbers: Minneapolis, MN")

z = np.polyfit(years, population, 4)
p = np.poly1d(z)
#add trendline to plot
plt.plot(years, p(years), color="red")

print(p)
