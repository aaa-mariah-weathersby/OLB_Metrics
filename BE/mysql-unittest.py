from transform_datetime_refactored import QuoteTransform
import unittest
import json
import csv

MOCK_QUOTE_DB_ROW = ('quote_id', 'created_date', 'type')
MOCK_INPUT_DATA = open('mock_formatted_data.txt')
MOCK_QUOTE = open('demo-quote.txt', 'r')

class MySQLDataInjection(unittest.TestCase):
    print('Coverage Summary:')
    def setUp(self):

        '''
        Need to add    
            { "Quotes": [
        to beginning and 
            ] }
        to end
        '''

    def test_mysql_data_format(self):

        data = MOCK_INPUT_DATA.readlines()
        data = data[0]

        data_dict = None
        quote_list = []

        with open('demo-quote.txt', 'r') as f:
            data_dict = json.load(f)

        dict_root = data_dict['Quotes']

        print(data_dict.keys())

        for quote in dict_root:
            quote_id = quote['QuoteId']
            quote_date = quote['EffectiveDate']
            quote_type = "Gold"
            
            if 'Message' in quote.keys():
                quote_type = quote['Message']

            quote_tup = (quote_id, quote_date, quote_type)
            quote_list.append(quote_tup)

        print quote_list

        for quote in quote_list:


    # def tearDown(self):
        # self.widget.dispose()


if __name__ == '__main__':
    unittest.main()
