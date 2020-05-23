# Import numpy as np


# Store pop as a numpy array: np_pop


# Double np_pop


# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()
