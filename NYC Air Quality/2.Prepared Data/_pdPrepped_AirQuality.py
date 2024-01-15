import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Options:
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # Disable scientific notation

# Import the NYC data
df = pd.read_csv(r"2.Prepared Data/_ExPrepped_AirQuality.csv")

# --------- Just learning some Pandas --------- #

# Shows the top 5 rows of the data frame as well as their columns
# print(df.head())

# Shows all the columns, how many cells are non-null, and their data types.
# print(df.info())

# Drop message column:
df = df.drop(columns='Message')
# print(df.info())

# Gain a high level statistical understanding of your data frame:
# print(df.describe())

# Figure out which columns have null values.
# print(df.isnull().sum())

# Tells us which columns have unique values in them. i.e, Unique ID has a number
# of unique values equal to the number of rows in the df.
# print(df.nunique())

# Sorts the values of the specified columnl into descending order then shows 
# the first five rows.
# print(df.sort_values('Data Value', ascending=False).head())

# Looking at a numeric correlation matrix:

# First, make a new dataframe only include numeric values
# numeric_df = df.select_dtypes(include='number')

# # Second calculate the correlation matrix:
# numeric_df_corr = numeric_df.corr()

# Display it
# print(numeric_df_corr)

# ------------------------------------------ #
# --------- NO2 Related Exploration --------- #

# Just pulling rows related to NO2
n_O_2_df = df[df['Name'] == 'Nitrogen dioxide (NO2)']
# print(n_O_2_df.info())

# Investigating the types of things that can be found in the Name column.
names_count = df['Name'].nunique()
names_l = df['Name'].unique()
name_occurences = df['Name'].value_counts()
# print(names_count)  # Number of unique names in the data frame
# print(names_l)      # List of unique names in the data frame
# print(name_occurences)  # Series of name, occurrences in the data frame

# Start Date column manipulation, doing this so that I can place the dates into
# bins based on their year.
n_O_2_df['Start_Date'] = pd.to_datetime(n_O_2_df['Start_Date'])  # Converts col. to panda date format
n_O_2_df['Year'] = n_O_2_df['Start_Date'].dt.year  # So that we can extract just the year and place it in its own col.

# Sort by years from oldest to most recent
n_O_2_df = n_O_2_df.sort_values('Year', ascending=True)


# TODO: Figure out how to calculate the mean of the pollution level for the year
#       then use that to plot the bar chart.

# Display 
# plt.figure(figsize=(10,6))
# sns.barplot(x=n_O_2_df['Year'], y=n_O_2_df['Data Value'], palette='RdYlGn')
# plt.title('NO2 over the years in NYC')
# plt.xlabel('Years')
# plt.ylabel('NO2 in PPB')
# plt.xticks(rotation=45, ha='right')
# plt.axhline(y=53, color='red', label='Dangerous Levels')
# plt.show()

print(n_O_2_df.sort_values('Data Value', ascending=False).head())
# ------------------------------------------ #
