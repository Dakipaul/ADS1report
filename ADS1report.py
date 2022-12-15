
#Installing the package
pip install wbgapi




#Importing the packages required
import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt




#Pandas library and function to read a dataset
dframe=pd.read_csv(r"D:\Datasets\Economic_Climate_Indicator.csv", low_memory=False)




#Printing the data
dframe.head(10)



# Index to be set as economy
dframe1=dframe.set_index('economy')




#Printing the transpose form of new dataframe
dframe1.T.head(10)



#Initialising the indicators for climate and economy
indic_econo = ['SP.POP.TOTL','NY.GDP.MKTP.CD','NE.DAB.TOTL.ZS','SL.UEM.1524.MA.ZS']
indic_clmat=['EG.ELC.NGAS.ZS','EN.ATM.CO2E.GF.KT','EG.ELC.RNWX.KH','EG.ELC.ACCS.ZS']
countries = ['ESP','CHL','AUS','DNK','BMU','ARG','JAM','CHN']
ECONOMIC  = wb.data.DataFrame(indic_econo, countries, mrv=7)
CLIMATIC = wb.data.DataFrame(indic_clmat, countries, mrv=7)

#SP.POP.TOTL: Current population
#NY.GDP.MKTP.CD: Current GDP calculated in USD
#NE.DAB.TOTL.ZS: Current Expenditure
#SL.UEM.1524.MA.ZS Unemployment for male youths
#EG.ELC.NGAS.ZS: Electricity % production from natural gas
#EN.ATM.CO2E.GF.KT: Gaseous consumption of fuel as CO2 emissions 
#EG.ELC.RNWX.KH: Electricity % production from renewable sources
#EG.ELC.ACCS.ZS: Electricity access in the country


# Forming the economic indicators data
ECONOMIC.columns = [i.replace('YR','') for i in ECONOMIC.columns]      
ECONOMIC=ECONOMIC.stack().unstack(level=1)                             
ECONOMIC.index.names = ['Cntry_Name', 'Year']                           
ECONOMIC.columns                                                     
ECONOMIC.fillna(0)
ECONOMIC.head(10)



# Forming the climatic indicators data
CLIMATIC.columns = [y.replace('YR','') for y in CLIMATIC.columns]      
CLIMATIC=CLIMATIC.stack().unstack(level=1)                             
CLIMATIC.index.names = ['Cntry_Name', 'Year']                           
CLIMATIC.columns                                                     
CLIMATIC.fillna(0)
CLIMATIC.head(10)



#Dataframe formation after resetting index reset and removing null values
a1=ECONOMIC.reset_index()
b1=CLIMATIC.reset_index()
a2=a1.fillna(0)
b2=b1.fillna(0)



#Dataframe after merging economic and climatic indicators
final_merged= pd.merge(a2, b2)
final_merged.head(10)



# Statistical information on Spain
n1=final_merged[(final_merged['Cntry_Name']=='ESP')]
n1.describe()


# **The average total electricity % production from natural gas in Spain is 3.15 and the total gaseous consumption of fuel as CO2 emissions in Spain is 18924.76**


#Visualisation of youth unemployment for males in Spain in a Line Chart format
plt.plot(n1["Year"], n1["SL.UEM.1524.MA.ZS"],color="violet")
plt.ylabel("SL.UEM.1524.MA.ZS")
plt.xlabel("Year")
plt.show()



# Statistical information on Chile
n2=final_merged[(final_merged['Cntry_Name']=='CHL')]
n2.describe()


# **The average total electricity access in Chile is lower than Spain. The average electricity % production from natural gas in Chile is lower than Spain**



#Visualisation of electricity access in Chile in a Line Chart format
plt.plot(n2["Year"], n2["EG.ELC.ACCS.ZS"],color="violet")
plt.ylabel("EG.ELC.ACCS.ZS")
plt.xlabel("Year")
plt.show()



# Statistical information on Australia
n3=final_merged[(final_merged['Cntry_Name']=='AUS')]
n3.describe()


# **The average total population in Australia is higher than Chile but lower than Spain. The average total % of electricity production from renewable sources in Australia is higher than Chile but lower than Spain.**


#Visualisation of youth unemployment for males in Australia in a Line Chart format
n3.plot(x="Year", y="SL.UEM.1524.MA.ZS", kind="bar",color="violet")



# Statistical information on Denmark
n4=final_merged[(final_merged['Cntry_Name']=='DNK')]
n4.describe()


# **The average electricity production from natural gas sources in Denmark is lower than Chile and Australia. The average greenhouse gas emission in Denmark is lower than Chile and Australia.** 


#Visualisation of total population in Denmark in a Scatter Chart format
n4.plot(x="Year", y="SP.POP.TOTL", kind="scatter",color="violet")



# Statistical information on Bermuda
n5=final_merged[(final_merged['Cntry_Name']=='BMU')]
n5.describe()


# **The average total population in Bermuda is lower than Denmark and Australia. The aevrage total expenditure in Bermuda is lower than Denmark and Australia.**



#Visualisation of total expenditure in Bermuda in a Scatter Chart format
n5.plot(x="Year", y="NE.DAB.TOTL.ZS", kind="scatter",color="violet")




# Statistical information on Argentina
n6=final_merged[(final_merged['Cntry_Name']=='ARG')]
n6.describe()


# **The average total electricity access in Argentina is lower than Bermuda and Denmark. The average total electricity % production from renewable sources is lower than Denmark and Australia**



#Visualisation of total GDP in USD in Argentina in a Bar Chart format
n6.plot(x="Year", y="NY.GDP.MKTP.CD", kind="bar",color="violet")




# Statistical information on Jamaica
n7=final_merged[(final_merged['Cntry_Name']=='JAM')]
n7.describe()


# **The average male youth unemployment in Jamaica is higher than Argentina and Denmark. The electricity access in Jamaica is lower than Argentina and Bermuda**



#Visualisation of electricity access in Jamaica in a Scatter Chart format 
n7.plot(x="Year", y="EG.ELC.ACCS.ZS", kind="scatter",color="violet")



# Statistical information on China
n8=final_merged[(final_merged['Cntry_Name']=='CHN')]
n8.describe()


# **The average gaseous consumption of fuel as CO2 emissions in China is higher than Argentina and Denmark. The average expenditure in China is lower than Jamaica and Argentina**



#Visualisation of GDP in USD in China in a Bar Chart format 
n8.plot(x="Year", y="NY.GDP.MKTP.CD", kind="bar",color="violet")


# **CORRELATION ANALYSIS - CHILE**



plt.plot(n2["SL.UEM.1524.MA.ZS"], n2["NY.GDP.MKTP.CD"],color="violet")
plt.ylabel("NY.GDP.MKTP.CD")
plt.xlabel("SL.UEM.1524.MA.ZS")
plt.show()



plt.plot(n2["SP.POP.TOTL"], n2["NY.GDP.MKTP.CD"],color="violet")
plt.ylabel("NY.GDP.MKTP.CD")
plt.xlabel("SP.POP.TOTL")
plt.show()


# **CORRELATION ANALYSIS - DENMARK**



plt.plot(n4["NY.GDP.MKTP.CD"], n4["SP.POP.TOTL"],color="violet")
plt.ylabel("SP.POP.TOTL")
plt.xlabel("NY.GDP.MKTP.CD")
plt.show()



plt.plot(n4["NY.GDP.MKTP.CD"], n4["SL.UEM.1524.MA.ZS"],color="violet")
plt.ylabel("SL.UEM.1524.MA.ZS")
plt.xlabel("NY.GDP.MKTP.CD")
plt.show()






