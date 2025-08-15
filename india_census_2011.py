

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded=files.upload()

# from google.colab import drive
# drive.mount('/content/drive')

# file_path='/content/drive/MyDrive/IndiaCensus.csv'

# df=pd.read_csv(file_path)
df=pd.read_csv('IndiaCensus.csv')
df.head()

df.columns

df.duplicated().sum()

df.isna().sum()

df.head()

#What is the total population of India according to the 2011 Census?
df['Population'].sum()

#Which state has the highest and lowest population?
df.groupby('State_name')['Population'].sum().sort_values(ascending=False).head(1)

df.groupby('State_name')['Population'].sum().sort_values(ascending=False).tail(1)

high_low_pop=df.groupby('State_name')['Population'].sum().sort_values(ascending=False)
sns.barplot(x=high_low_pop.values,y=high_low_pop.index,palette='viridis')
plt.title('State with highest and lowest population')
plt.xlabel('Population')
plt.ylabel('State')
plt.show()

#What is the distribution of male and female population across India?
df['Male'].sum()

df['Female'].sum()

gender_dist=df.groupby('State_name')[['Male','Female']].sum().sort_values(by='Male',ascending=False)

states = gender_dist.index
male_counts = gender_dist['Male'].values
female_counts = gender_dist['Female'].values

x = np.arange(len(states))  # the label locations
width = 0.4  # width of the bars

plt.figure(figsize=(16, 8))
plt.bar(x-width/2, male_counts, width, label='Male', color='skyblue')
plt.bar(x+width/2, female_counts, width, label='Female', color='lightcoral')

plt.xlabel('States')
plt.ylabel('Population')
plt.title('Distribution of Male and Female Population Across States in India')
plt.xticks(x, states, rotation=90)
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# What is the sex ratio (females per 1000 males) state wise?
state_gender = df.groupby('State_name')[['Male', 'Female']].sum()
state_gender['Sex_Ratio'] = (state_gender['Female'] / state_gender['Male']) * 1000
state_sex_ratio = state_gender['Sex_Ratio'].sort_values(ascending=False)


plt.figure(figsize=(12, 8))
sns.barplot(x=state_sex_ratio.values, y=state_sex_ratio.index, palette='viridis')
plt.title('State-wise Sex Ratio (Females per 1000 Males)', fontsize=14)
plt.xlabel('Sex Ratio')
plt.ylabel('State')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# overall literacy rate of india
total_literate = df['Literate'].sum()
total_population = df['Population'].sum()

overall_lit_rate = (total_literate / total_population) * 100
print(f" Overall Literacy Rate in India: {overall_lit_rate:.2f}%")

#Which state has the highest literacy rate?
state_lit=df.groupby('State_name')[['Literate','Population']].sum()
state_lit['Literacy_Rate']=(state_lit['Literate']/state_lit['Population']) * 100
top_states=state_lit.sort_values(by='Literacy_Rate',ascending=False)

plt.figure(figsize=(18,6))
top_states['Literacy_Rate'].plot(kind='bar',color='mediumseagreen')
plt.title('Literacy Rate in Each State')
plt.xlabel('State')
plt.ylabel('Literacy Rate')
plt.xticks(rotation=90)
plt.show()

# What is the male vs female literacy rate by state?

# Group by state and sum required columns
state_lit = df.groupby('State_name')[['Male', 'Female', 'Literate']].sum()

# Total state population
state_lit['Total'] = state_lit['Male'] + state_lit['Female']

# Approximate male and female literates based on population share
state_lit['Literate_Male'] = (state_lit['Male'] / state_lit['Total']) * state_lit['Literate']
state_lit['Literate_Female'] = (state_lit['Female'] / state_lit['Total']) * state_lit['Literate']

# Calculate literacy rates
state_lit['Male_Lit_Rate'] = (state_lit['Literate_Male'] / state_lit['Male']) * 100
state_lit['Female_Lit_Rate'] = (state_lit['Literate_Female'] / state_lit['Female']) * 100

# Sort for better viewing
state_lit_sorted = state_lit.sort_values('Male_Lit_Rate', ascending=False)

# Plotting
x = np.arange(len(state_lit_sorted))

plt.figure(figsize=(16, 8))
plt.bar(x - 0.2, state_lit_sorted['Male_Lit_Rate'], width=0.3, label='Male Literacy Rate', color='steelblue')
plt.bar(x + 0.2, state_lit_sorted['Female_Lit_Rate'], width=0.3, label='Female Literacy Rate', color='lightcoral')

plt.xticks(x, state_lit_sorted.index, rotation=90)
plt.xlabel('State')
plt.ylabel('Literacy Rate (%)')
plt.title('Estimated Male vs Female Literacy Rate by State')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

df.columns

# Which states have the highest and lowest proportion of children/youth (Age 0–29)
#highest
proportion_youth=df.groupby('State_name')['Age_Group_0_29'].sum().sort_values(ascending=False).head(1)
print(proportion_youth)

# lowest
proportion_youth=df.groupby('State_name')['Age_Group_0_29'].sum().sort_values(ascending=False).tail(1)
print(proportion_youth)

proportion_youth=df.groupby('State_name')['Age_Group_0_29'].sum().sort_values(ascending=False).head(10)
plt.pie(proportion_youth,labels=proportion_youth.index)
plt.title('Porportion of children/youth of top 10 state')
plt.show()

# How does literacy relate to education levels (secondary, higher, graduate)?
edu_cols=['Literate','Secondary_Education','Higher_Education','Graduate_Education']
sns.heatmap(df[edu_cols].corr(),annot=True,cmap='coolwarm')
plt.title('Correlation between Literacy and Education Levels')
plt.show()

# Which states have the highest percentage of graduates?
df_grad=df.groupby('State_name')[['Graduate_Education','Population']].sum()
df_grad['Graduate_Percentage']=(df_grad['Graduate_Education']/df_grad['Population'])*100
top_graduate_states=df_grad.sort_values(by='Graduate_Percentage',ascending=False).head(1)
print(top_graduate_states.index[0])

df.columns

#What percentage of the population are workers in each state?
df_work=df.groupby('State_name')[['Population','Workers']].sum()
df_work['Workers_Percentage']=(df_work['Workers']/df_work['Population'])*100

df_work_sorted=df_work.sort_values(by='Workers_Percentage',ascending=False)

plt.figure(figsize=(16,8))
sns.barplot(y=df_work_sorted.index,x=df_work_sorted['Workers_Percentage'],hue=df_work_sorted.index,legend=False,palette="viridis")
plt.title('Percentage of workers in each state')
plt.xlabel('State')
plt.ylabel('Percentage of workers')
plt.grid()
plt.xticks(rotation=90)
plt.show()

# What is the male vs female participation in the workforce by state?
df_gender=df.groupby('State_name')[['Male_Workers','Female_Workers','Male','Female']].sum()
df_gender['Male_Participation']=(df_gender['Male_Workers']/df_gender['Male'])*100
df_gender['Female_Participation']=(df_gender['Female_Workers']/df_gender['Female'])*100

df_gender_sort=df_gender.sort_values(by='Male_Participation',ascending=False)

states=df_gender_sort.index
x=np.arange(len(states))
width=0.4

plt.figure(figsize=(16,8))
plt.bar(x-0.2,df_gender_sort['Male_Participation'],width=width,label='Male Participation',color="steelblue")
plt.bar(x+0.2,df_gender_sort['Female_Participation'],width=width,label='Female Participation',color='lightcoral')
plt.title('Male vs Female Participation in the Workforce by State')
plt.xlabel('State')
plt.ylabel('Participation (%)')
plt.xticks(x,states,rotation=90)
plt.legend()
plt.show()

# Which states have the highest proportion of female workers?
df_female_worker=df.groupby('State_name')[['Female_Workers','Population']].sum()
df_female_worker['Female_Worker_Percentage']=(df_female_worker['Female_Workers']/df_female_worker['Population'])*100
df_female_worker_sort=df_female_worker.sort_values(by='Female_Worker_Percentage',ascending=False)

plt.figure(figsize=(10,7))
sns.barplot(x=df_female_worker_sort['Female_Worker_Percentage'],y=df_female_worker_sort.index,palette='Set2')
plt.title('Proportion of Female Workers in Each State')
plt.xlabel('Female Worker Percentage')
plt.ylabel('States')
plt.show()

# How is the workforce distributed among cultivators, agricultural laborers, and household workers?

# Group and compute percentages
df_workers = df.groupby('State_name')[
    ['Cultivator_Workers', 'Agricultural_Workers', 'Household_Workers']
].sum()

df_workers['Total_Selected_Workers'] = df_workers.sum(axis=1)

df_workers['Cultivators_%'] = (df_workers['Cultivator_Workers'] / df_workers['Total_Selected_Workers']) * 100
df_workers['Agricultural_Labourers_%'] = (df_workers['Agricultural_Workers'] / df_workers['Total_Selected_Workers']) * 100
df_workers['Household_Industry_Workers_%'] = (df_workers['Household_Workers'] / df_workers['Total_Selected_Workers']) * 100

# Select only percentage columns
df_stacked = df_workers[['Cultivators_%', 'Agricultural_Labourers_%', 'Household_Industry_Workers_%']]

# Optional: sort by one of the components
df_stacked = df_stacked.sort_values(by='Cultivators_%', ascending=False)

# Plot
plt.figure(figsize=(14, 10))
bottom = None
colors = ['#e41a1c', '#377eb8', '#4daf4a']  # Set1-like colors

for i, column in enumerate(df_stacked.columns):
    plt.barh(
        df_stacked.index,
        df_stacked[column],
        left=bottom,
        label=column.replace('_%', '').replace('_', ' '),
        color=colors[i]
    )
    bottom = df_stacked[column] if bottom is None else bottom + df_stacked[column]

plt.title('Stacked Bar Chart: Workforce Distribution by Worker Type in Each State')
plt.xlabel('Percentage (%)')
plt.ylabel('State')
plt.legend(title='Worker Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# What is the relationship between education level and workforce participation?
df['Workforce_Participation_%'] = (df['Workers'] / df['Population']) * 100
df['Secondary_Edu_%'] = (df['Secondary_Education'] / df['Population']) * 100
df['Higher_Edu_%'] = (df['Higher_Education'] / df['Population']) * 100
df['Graduate_Edu_%'] = (df['Graduate_Education'] / df['Population']) * 100

# Correlation matrix
corr = df[['Secondary_Edu_%', 'Higher_Edu_%', 'Graduate_Edu_%', 'Workforce_Participation_%']].corr()
print("Correlation matrix:\n", corr)

# Pairplot for visual relationship
sns.pairplot(df, vars=['Secondary_Edu_%', 'Higher_Edu_%', 'Graduate_Edu_%', 'Workforce_Participation_%'])
plt.suptitle('Pairwise Relationships Between Education and Workforce Participation', y=1.02)
plt.show()

# Regression plot (e.g., Graduate education vs workforce participation)
plt.figure(figsize=(8, 8))
sns.regplot(x='Graduate_Edu_%', y='Workforce_Participation_%', data=df)
plt.title('Graduate Education vs Workforce Participation')
plt.xlabel('Graduate Education (%)')
plt.ylabel('Workforce Participation (%)')
plt.tight_layout()
plt.show()

# What is the religious composition of each state?
# Group by state and sum religion-wise population
df_religions = df.groupby('State_name')[['Hindus', 'Muslims', 'Sikhs', 'Christians', 'Buddhists', 'Jains']].sum()
df_religions['Total_Religions'] = df_religions.sum(axis=1)

# Calculate religion percentages
religions = ['Hindus', 'Muslims', 'Sikhs', 'Christians', 'Buddhists', 'Jains']
for religion in religions:
    df_religions[f'{religion}%'] = (df_religions[religion] / df_religions['Total_Religions']) * 100

# Create DataFrame with only percentage columns
df_stacked = df_religions[[f'{r}%' for r in religions]]

# Plot stacked horizontal bar chart
plt.figure(figsize=(14, 10))
bottom = None
colors = ['#fc8d62', '#66c2a5', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']


for i, religion in enumerate(df_stacked.columns):
    plt.barh(
        df_stacked.index,
        df_stacked[religion],
        left=bottom,
        label=religion.replace('%', ''),
        color=colors[i]
    )
    bottom = df_stacked[religion] if bottom is None else bottom + df_stacked[religion]

plt.title('Stacked Bar Chart: Religious Composition of Each State')
plt.xlabel('Percentage (%)')
plt.ylabel('State')
plt.legend(title='Religion', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Are there correlations between religion and education/literacy or gender ratio?
religions = ['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains']
for rel in religions:
    df[f'{rel}_%'] = (df[rel] / df['Population']) * 100

# Step 2: Education & literacy percentages
df['Literate_%'] = (df['Literate'] / df['Population']) * 100
df['Secondary_Edu_%'] = (df['Secondary_Education'] / df['Population']) * 100
df['Higher_Edu_%'] = (df['Higher_Education'] / df['Population']) * 100
df['Graduate_Edu_%'] = (df['Graduate_Education'] / df['Population']) * 100

# Step 3: Gender ratio (females per 1000 males)
df['Gender_Ratio'] = (df['Female'] / df['Male']) * 1000

# Select columns of interest
columns_to_correlate = [f'{rel}_%' for rel in religions] + [
    'Literate_%', 'Secondary_Edu_%', 'Higher_Edu_%', 'Graduate_Edu_%', 'Gender_Ratio'
]

# Compute correlation matrix
correlation_matrix = df[columns_to_correlate].corr()

# Display heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation between Religion, Education, Literacy, and Gender Ratio')
plt.tight_layout()
plt.show()

#What is the age group distribution across states (0–29, 30–49, 50+)?
age_groups = ['Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50']
df_age_group = df.groupby('State_name')[age_groups].sum()


#Plot horizontal stacked bars
plt.figure(figsize=(14, 10))
bottom = None
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

for i, column in enumerate(age_groups):
    plt.barh(
        df_age_group.index,
        df_age_group[column],
        left=bottom,
        label=column.replace('_', ' '),
        color=colors[i]
    )
    bottom = df_age_group[column] if bottom is None else bottom + df_age_group[column]

plt.title('Stacked Bar Chart: Age Group Distribution Across States')
plt.xlabel('Population')
plt.ylabel('State')
plt.legend(title='Age Group', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Which states have the highest aging populations (Age 50+)?
df_age_group=df.groupby('State_name')['Age_Group_50'].sum().sort_values(ascending=False).head(1)
print(df_age_group)

# Does age distribution correlate with literacy or employment levels?
# Step 1: Compute percentages (if not already done)
df['Literate_%'] = (df['Literate'] / df['Population']) * 100
df['Workers_%'] = (df['Workers'] / df['Population']) * 100
df['Male_Workers_%'] = (df['Male_Workers'] / df['Male']) * 100
df['Female_Workers_%'] = (df['Female_Workers'] / df['Female']) * 100

# Step 2: Group by state (or use district-level if preferred)
age_columns = ['Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50']
metric_columns = ['Literate_%', 'Workers_%', 'Male_Workers_%', 'Female_Workers_%']
correlation_data = df.groupby('State_name')[age_columns + metric_columns].mean()

# Step 3: Correlation matrix
correlation_matrix = correlation_data.corr()

# Step 4: Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation between Age Groups and Literacy/Employment')
plt.tight_layout()
plt.show()

