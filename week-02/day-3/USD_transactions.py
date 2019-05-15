"""
In the transactions.xml you can find money transfers. 
Your task is to filter all USD transactions and print them to the console in a user friendly format.

"""

#Read XML file
import xml.etree.ElementTree as ET
def extracttransaction(filename, currency):
    tree = ET.parse(filename)
    root = tree.getroot()
    filter_transaction_data = []
    title = ['from', 'to', 'amount']
    for i in range(len(root)):
        if root[i][2].attrib['currency'] == currency:
            temp = {}
            for j in range(len(root[0])):
                temp[title[j]] = (root[i][j].text)
            temp['currency'] = currency
            filter_transaction_data.append(temp)
    return filter_transaction_data

extracttransaction('transactions.xml', 'USD')

        
            
        