from transform_datetime_refactored import QuoteTransform
import unittest
import json
import csv

import mysqlConnect

MOCK_QUOTE_DB_ROW = ('quote_id', 'created_date', 'type')
MOCK_INPUT_DATA = open('mock_formatted_data.txt')
MOCK_QUOTE = open('demo-quote.txt', 'r')

MySQL_Quotes = mysqlConnect.MySQL_Quotes()
File_Parser = mysqlConnect.File_Parser()

MOCK_DATA = 'test-data.txt'

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

    def test_parse_file(self):
        print("Parse file into list")
        
        expectedData = [('000000000999501123', '11/04/2016', 'Gold')]
        expected_data_type = type(expectedData)

        returned_data = File_Parser.parse_file(MOCK_DATA)
        returned_data_type = type(returned_data)

        self.assertEqual(expected_data_type, returned_data_type)


    # def test_create_list_gold(self):
        # print("Expect to pass in object with __ properties and return list of tuples")
        # expectedData = [('000000000999501123', '11/04/2016', 'Gold')]
        # self.assertEqual(MySQL_Quotes.create_list(MOCK_DATA), expectedData)


    # def test_create_list(self):
    #     print("Expect to pass in object with __ properties and return list of tuples")        


    # def tearDown(self):
        # self.widget.dispose()


if __name__ == '__main__':
    unittest.main()
