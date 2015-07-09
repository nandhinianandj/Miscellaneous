import pandas as pdi# conventional way to import pandas
import pandas as pd

# read CSV file directly from a URL and save the results
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)

# display the first 5 rows
data.head()

# display the last 5 rows
data.tail()

# conventional way to import seaborn
import seaborn as sns

# allow plots to appear within the notebook
#%matplotlib inline

# visualize the relationship between the features and the response using scatterplots
sns.pairplot(data, x_vars=['TV','Radio','Newspaper'], y_vars='Sales', size=7, aspect=0.7, kind='reg')

