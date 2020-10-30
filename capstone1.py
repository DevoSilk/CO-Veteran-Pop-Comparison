import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce

co_df = pd.read_csv('~/den-19/assignments/capstone1/DATA/CensusDataCos.csv')

co_df=co_df.loc[[8,9,10,11,12,13,14,15,16]]
#code below is getting rid of different columns that aren't needed for this
co_df=co_df.drop(['Fact Note', 'Value Note for Colorado Springs city, Colorado'], axis=1)
co_df=co_df.reset_index().drop(['index'],axis=1)

#this changes the shape of the dataframe so that I can rename the columns
co_df=co_df.transpose()
co_df=co_df.rename(columns={0:"White, alone, %",\
                            1:"Black or African American, alone, %",\
                            2:"American Indian/Alaska Native, alone, %",\
                            3:"Asian, alone, %",\
                            4:"Native Hawaiian/Pacific Islander, alone, %",\
                            5:"Two or more races, %",\
                            6:"Hispanic/Latino (of any race), %",\
                            7:"White alone, Not Hispanic/Latino, %",\
                            8:"All Veterans, 2014-2018 est, %"})


#this changes the data frame back so that I can once again drop a column not needed
co_df=co_df.transpose().drop(['Fact'], axis=1)
co_df= co_df.rename(columns={"Colorado Springs city, Colorado": "Colorado Springs"})
#print(co_df)

data1= [['Adams', 517421],
        ['Denver', 727211], 
        ['Jefferson', 582881], 
        ['El Paso', 720403], 
        ['Teller', 25388]]

cnt1_df=pd.DataFrame(data1, columns=['County Name', 'Population est for July 2019'])
#print(cnt1_df)

data2=[['Adams',85.7],
        ['Denver', 80.9], 
        ['Jefferson', 91.5], 
        ['El Paso', 83.3], 
        ['Teller', 93.8]]

cnt2_df=pd.DataFrame(data2, columns=['County Name', 'White alone, %'])
#print(cnt2_df)

data3= [['Adams', 4.0],
        ['Denver', 9.8], 
        ['Jefferson', 1.5], 
        ['El Paso', 6.9], 
        ['Teller', 1.0]]

cnt3_df=pd.DataFrame(data3, columns=['County Name', 'Black or African American alone, %'])
#print(cnt3_df)

data4=[['Adams', 2.3],
        ['Denver', 1.7], 
        ['Jefferson', 1.2], 
        ['El Paso', 1.4], 
        ['Teller', 1.4]]

cnt4_df= pd.DataFrame(data4, columns=['County Name', 'American Indian/Alaska Native alone, %'])
#print(cnt4_df)

data5=[['Adams', 4.5],
        ['Denver', 4.1], 
        ['Jefferson', 3.1], 
        ['El Paso', 3.1], 
        ['Teller', 1.1]]

cnt5_df=pd.DataFrame(data5, columns=['County Name', 'Asian alone, %'])
#print(cnt5_df)

data6=[['Adams', .2],
        ['Denver', .2], 
        ['Jefferson', .1], 
        ['El Paso', .4], 
        ['Teller', .1]]

cnt6_df=pd.DataFrame(data6,columns=['County Name', 'Native Hawaiian/Pacific Islander alone, %'])
#print(cnt6_df)

data7=[['Adams', 3.2],
        ['Denver', 3.3], 
        ['Jefferson', 2.6], 
        ['El Paso', 4.9], 
        ['Teller', 2.6]]

cnt7_df=pd.DataFrame(data7, columns=['County Name', 'Two or More Races, %'])
#print(cnt7_df)

data8=[['Adams', 40.8],
        ['Denver', 29.3], 
        ['Jefferson', 15.6], 
        ['El Paso', 17.7], 
        ['Teller', 7.1]]

cnt8_df=pd.DataFrame(data8, columns=['County Name', 'Hispanic/Latino, %'])
#print(cnt8_df)

data9=[['Adams', 49.0],
        ['Denver', 54.9], 
        ['Jefferson', 77.7], 
        ['El Paso', 68.6], 
        ['Teller', 88.0]]

cnt9_df=pd.DataFrame(data9, columns=['County Name', 'White alone, not Hispanic/Latino, %'])
#print(cnt9_df)

data10=[['Adams', 26733],
        ['Denver', 29648], 
        ['Jefferson', 38191], 
        ['El Paso', 83973], 
        ['Teller', 3073]]

cnt10_df=pd.DataFrame(data10,columns=['County Name', 'Veterans est. 2014-2018'])
#print(cnt10_df)

merged_inner = pd.merge(left=cnt1_df, right=cnt10_df, left_on='County Name', right_on='County Name')
#print(merged_inner)

cnt_percent_data=[cnt2_df, cnt3_df, cnt4_df, cnt5_df, cnt6_df, cnt7_df, cnt8_df, cnt9_df]



cnt_vet_data= [cnt1_df,cnt10_df]

cnt_percent_merged = reduce(lambda  left,right: pd.merge(left,right,on=['County Name'],
                                            how='outer'), cnt_percent_data)

cnt_vet_merged = pd.merge(cnt1_df, cnt10_df, on=['County Name'])

corrMatrix=cnt_percent_merged.corr()
print(corrMatrix)



us_percent= pd.read_csv('~/den-19/assignments/capstone1/DATA/CensusDataUS.csv')

us_avg= us_percent.loc[[8,9,10,11,12,13,14,15]]
us_eth_avg=us_avg.reset_index().drop(['index', 'Fact Note', 'Value Note for United States'],axis=1)
#rename the columns
us_eth_avg1=us_eth_avg.T

us_eth_avg2=us_eth_avg1.rename(columns={0:'White alone, %', 
                                       1:'Black or African American alone, %', 
                                       2:'American Indian/Alaska Native alone, %', 
                                       3:'Asian alone, %', 
                                       4:'Native Hawaiian/Pacific Islander alone, %', 
                                       5:'Two or More Races, %', 
                                       6:'Hispanic/Latino, %', 
                                       7: 'White alone, not Hispanic/Latino, %'})


us_eth_avg2=us_eth_avg2.T.drop(['Fact'], axis=1)


def replace_percent_float(df, str):
    df = df[str].str.replace(r'%', r'').astype('float')
    
    return df


def replace_comma_float(df, str):
    df = df[str].str.replace(r',', r'').astype('float')
    
    return df
#print(replace_comma_float(us_eth_avg2,'United States'))





us_eTh1_data= [['White alone, %',76.3],
               ['Black or African American, alone, %', 13.4],
               ['American Indian/Alaska Native, alone, %', 1.3],
               ['Asian, alone, %', 5.9],
               ['Native Hawaiian/Pacific Islander, alone, %',0.2],
               ['Two or More Races, %',2.8],
               ['Hispanic/Latino, %',18.5],
               ['White alone, Not Hispanic/Latino, %',60.1]]

us_eTh1_df=pd.DataFrame(us_eTh1_data, columns=['Ethnicities', 'United States'])

co_df_cos_data = [['White alone, %',78.3],
                  ['Black or African American, alone, %',6.2],
                  ['American Indian/Alaska Native, alone, %',0.7],
                  ['Asian, alone, %',3.0],
                  ['Native Hawaiian/Pacific Islander, alone, %',0.3],
                  ['Two or More Races, %',6.0],
                  ['Hispanic/Latino, %',17.7],
                  ['White alone, Not Hispanic/Latino, %',68.7]]

co_cos_df=pd.DataFrame(co_df_cos_data, columns=['Ethnicities', 'Colorado Springs'])

co_CO_data=    [['White alone, %',86.9],
                ['Black or African American, alone, %',4.6],
                ['American Indian/Alaska Native, alone, %',1.6],
                ['Asian, alone, %',3.5],
                ['Native Hawaiian/Pacific Islander, alone, %',0.2],
                ['Two or More Races, %',3.1],
                ['Hispanic/Latino, %', 21.8],
                ['White alone, Not Hispanic/Latino, %',67.7]]

co_CO_df=pd.DataFrame(co_CO_data, columns=['Ethnicities', 'Colorado'])


all_avg_data=[co_CO_df, co_cos_df, us_eTh1_df]
all_avgs_df = reduce(lambda  left,right: pd.merge(left,right,on=['Ethnicities'],
                                            how='outer'), all_avg_data)



all_avgs_dfT =all_avgs_df.T.rename(columns={
                    0:'White alone, %', 
                    1:'Black or African American, alone, %', 
                    2:'American Indian/Alaska Native, alone, %', 
                    3:'Asian, alone, %', 
                    4:'Native Hawaiian/Pacific Islander, alone, %', 
                    5:'Two or More Races, %',
                    6:'Hispanic/Latino, %', 
                    7:'White alone, Not Hispanic/Latino, %'})

all_avg_df=all_avgs_dfT.T.drop(['Ethnicities'],axis=1)
#print(all_avg_df)


'''
def mergefiles(dfs=[], on=''):
    """Merge a list of files based on one column"""
    if len(dfs) == 1:
         return "List only have one element."

    elif len(dfs) == 2:
        df1 = dfs[0]
        df2 = dfs[1]
        df = df1.merge(df2, on=on)
        return df

    # Merge the first and second datafranes into new dataframe
    df1 = dfs[0]
    df2 = dfs[1]
    df = dfs[0].merge(dfs[1], on=on)

    # Create new list with merged dataframe
    dfl = []
    dfl.append(df)

    # Join lists
    dfl = dfl + dfs[2:] 
    dfm = mergefiles(dfl, on)
    return dfm
    '''