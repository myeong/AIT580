import pandas as pd

df = pd.read_csv('olympics_clean.csv')

#Q1: Which country has won the most gold medals in summer games?
def answer_one():
    x = max(df['Gold'])
    ans = df[df['Gold'] == x].index.tolist()
    return df['Country'][ans[0]]

print(answer_one())


#Q2; Which country had the biggest difference between their summer and winter gold medal counts?
def answer_two():
    x = max(df['Gold'] - df['Gold.1'])
    ans = df[(df['Gold'] - df['Gold.1']) == x].index.tolist()
    return df['Country'][ans[0]]

print(answer_two())

#Q3: Which country has the biggest difference between their summer and winter gold medal counts relative to their total gold medal count?
# Only include countries that have won at least 1 gold in both summer and winter.
def answer_three():
    df_gold = df[(df['Gold']>0) & (df['Gold.1']>0)]
    df_max_diff = (abs(df_gold['Gold']-df_gold['Gold.1'])/df_gold['Gold.2'])
    max_diff_index =  df_max_diff.idxmax()
    return df['Country'][max_diff_index]

print(answer_three())

#Q4: Write a function to update the dataframe to include a new column called "Points" which is a weighted value
# where each gold medal counts for 3 points, silver medals for 2 points, and bronze mdeals for 1 point.
# The function should return only the column Points which you created.

def answer_four():
    Points = 3*df['Gold.2'] + 2*df['Silver.2'] + 1*df['Bronze.2']
    return Points

print(answer_four())