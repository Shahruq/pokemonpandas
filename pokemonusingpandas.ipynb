### I am starting my journey as a coder in python after being an R user for years,
### so let's get started

import pandas as pd

df = pd.read_csv('pokemon_data.csv')  #very easy to read files compared to R, way to go!

df.head() #gives you the first six rows, you can also manipulate with the head function

print(df.columns) #tp print the columns



#let us do some filtering and other stuff etc.
# let's mutate

df['Total'] = df['HP'] + df['Speed'] 
print(df.columns)
#simply done! you created a new variable by adding two variables... simple innit?

a = df[(df['HP'] <= 50) & (df['Attack'] <= 50)] # a simple filtering technique in Python

print(a)


#let us filter out the legendary pokemon from the first gen

legend1 = df[(df['Generation'] == 1) & (df['Legendary'] == 1)] #boolean is representated as 0 or 1

print(legend1)

### nice to see some names there

#to save the the csv file

legend1.to_csv('legendarypokemon1stgen.csv')

##dropping the old index

lengend1 = legend1.reset_index(drop = True)

print(lengend1)


#### we'll remove the Mega pokemons from the list

lengend1[~lengend1['Name'].str.contains('Mega')] 
# very powerful technique in NLP

###more powerul technique

import re

z = df.loc[df['Name'].str.contains('^pi[a-z]*', flags = re.I, regex=True)]
##filtering out the name of pokemon which start pi
print(z)

##replacing text

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Firez'
# so the above script replaces 
## now further if you want to work on more variables at a time

#### group by

### highest attacking pokemons

df.groupby(['Type 1']).mean().sort_values('Attack', ascending = False)
#mean, sum, count

###count 
df.groupby(['Type 1']).count()

###################################
#for big datasets you can you chunk size in the read

for df in pd.read_csv('pokemon_data.csv', chunksize = 5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])
    
######################################################################
    