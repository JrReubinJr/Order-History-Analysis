import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

def splitVariant(product: str) -> list:
    idx = product.index('-')
    return [product[:idx], product[idx+2:]]

def processSKU(orderhistory: DataFrame, categories: DataFrame, products: DataFrame) -> DataFrame:

    #separate month and year
    orderhistory[['month','year']] = orderhistory.date.str.extract(r'(\d{1,2})(?:\/\d{1,2}\/)(\d{4})')

    print(type(orderhistory))


    #separate product and sku names
    #orderhistory['ProductName'].apply(lambda x: splitVariant(x))

    # Group by month year, and sku
    # groupedHistory = orderhistory[['month', 'year', 'partnumber', 'ProductName', 'Unit_price', 'Qty']].groupby(
    #     ['month', 'year', 'partnumber']).sum('qty').sort_values(by=['year', 'month'])
    grouped = orderhistory[['month', 'year', 'partnumber','Qty']].groupby(
             ['month', 'year', 'partnumber']).toDataFrame().sum('Qty').sort_values(by=['year', 'month'])
    #grouped.reset_index()
    print(type(grouped))
    #print(groupedHistory.columns.values)
    print('plang')
    print(grouped.dtypes)
    #df = groupedHistory.join(categories, on='partnumber')
    #print(df)

    #groupedHistory.merge(categories, how='left', on='partnumber')

    #print(groupedHistory)

    return grouped

def processProduct(orderhistory: DataFrame) -> DataFrame:
    # separate month and year
    orderhistory[['month', 'year']] = orderhistory.date.str.extract(r'(\d{1,2})(?:\/\d{1,2}\/)(\d{4})')

    return orderhistory



def customers(orderhistory: DataFrame) -> DataFrame:
    customers = orderhistory[['CustomerEmail', 'InvoiceAmount']].groupby(
        ['CustomerEmail']).sum('InvoiceAmount').sort_values(by=['InvoiceAmount'], ascending=False)
    return customers



