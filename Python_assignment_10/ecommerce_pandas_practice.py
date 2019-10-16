import pandas as pd

ecom = pd.read_csv('EcommercePurchases.csv')

print(ecom.head())

#Q1: How many rows and columns are there?
print(ecom.info())

#Q2: What is the average Purchase Price?
print(ecom['Purchase Price'].mean())

#Q3: What were the highest and lowest purchase prices?

print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())

#Q4: How many people have English 'en' as their Language of choice on the website?
print(ecom[ecom['Language']=='en'].count()[1])

#Q5: How many people have the job title of "Lawyer" ?
print(ecom[ecom['Job'] == 'Lawyer'].count()[1])

#Q6: How many people made the purchase during the AM and how many people made the purchase during PM ? (Hint: use value_count())
print(ecom['AM or PM'].value_counts())

#Q7: What are the 5 most common/frequent Job Titles?
print(ecom['Job'].value_counts().head(5))

#Q8: Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
print(ecom[ecom['Lot']=='90 WT']['Purchase Price'])

#Q9: What is the email of the person with the following Credit Card Number: 4926535242672853
print(ecom[ecom["Credit Card"] == 4926535242672853]['Email'])

#Q10: How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
print(ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count())

##Adnavce
#Q11: How many people have a credit card that expires in 2025?
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))

#Q12: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc.)
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))


