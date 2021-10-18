 mrjob.job import
from mrjob.job import MRJob
import csv

cols = 'InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'
class retailCount(MRJob):

    def mapper(self, key, line):
        row = dict(zip(cols, [a.strip() for a in csv.reader([line]).next()]))
        itemName = 'itemName', (string(row['Description'][1:]), line)
        quantity = 'quantity', (int(row['Quantity'][1:]), line)
        unitPrice = 'unitPrice', (float(row['UnitPrice'][1:]), line)
        
        