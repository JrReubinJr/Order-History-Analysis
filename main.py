import datatable as dt
import pandas as pd
from process import processSKU, processProduct, customers

#load the dataset -> dataframe
o1516 = dt.fread("res/moshi.com_orders_2015-2016_USD.csv").to_pandas()
o18_1_6 = dt.fread("res/moshi.com_orders_2018-01_06_USD.csv").to_pandas()
o18_7_12 = dt.fread("res/moshi.com_orders_2018-07_12_USD.csv").to_pandas()
o19 = dt.fread("res/moshi.com_orders_2019_USD.csv").to_pandas()
o20 = dt.fread("res/moshi.com_orders_2020_USD.csv").to_pandas()
eur17 = dt.fread("res/moshi.com_orders_eur_2017.csv").to_pandas()
gb17 = dt.fread("res/moshi.com_orders_gbp_2017.csv").to_pandas()
categories = dt.fread("res/categoryData.csv").to_pandas()
products = dt.fread("res/productData.csv").to_pandas()

#define the frames
framesUS = [o18_1_6, o18_7_12, o19, o20]
framesEURO = [eur17, gb17]

#concat the data
us = pd.concat(framesUS)
eur = pd.concat(framesEURO)


# Main
if __name__ == '__main__':

    #sku analysis
    usSKU = processSKU(us, categories, products)
    usSKU.to_csv('out/test.csv')
    #eurClean = process(eur)

    # sku analysis
    usProduct = processProduct(us)

    #customer data
    usCustomers = customers(us)
    #eurCustomers = customers(eur)


