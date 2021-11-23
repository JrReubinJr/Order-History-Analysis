import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

def splitVariant(product: str) -> list:
    idx = product.index('-')
    return [product[:idx], product[idx+2:]]

def processSKU(orderhistory: DataFrame) -> DataFrame:

    #separate month and year
    orderhistory[['month','year']] = orderhistory.date.str.extract(r'(\d{1,2})(?:\/\d{1,2}\/)(\d{4})')

    #separate product and sku names
    orderhistory['ProductName'].apply(lambda x: splitVariant(x))

    # Group by month year, and sku
    groupedHistory = orderhistory[['month', 'year', 'partnumber', 'ProductName', 'Unit_price', 'Qty']].groupby(
        ['month', 'year', 'partnumber']).sum('qty').sort_values(by=['year', 'month'])

    print((groupedHistory))


    return groupedHistory

def processProduct():


def customers(orderhistory: DataFrame) -> DataFrame:
    customers = orderhistory[['CustomerEmail', 'InvoiceAmount']].groupby(
        ['CustomerEmail']).sum('InvoiceAmount').sort_values(by=['InvoiceAmount'], ascending=False)
    return customers



