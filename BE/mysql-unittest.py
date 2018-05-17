from transform_datetime_refactored import QuoteTransform
import unittest
import json
import csv

import mysqlConnect

MOCK_QUOTE_DB_ROW = ('quote_id', 'created_date', 'type')
MOCK_INPUT_DATA = open('mock_formatted_data.txt')
MOCK_QUOTE = open('demo-quote.txt', 'r')

QuotesTable = mysqlConnect.QuotesData()
FileParser = mysqlConnect.FileParser()
QNBTable = mysqlConnect.QNBData()

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


    def test_MySQL_quotes_create_list(self):
        print("Expect to pass in list of quote objects and return formatted list of tuples")
        
        sample_data = [
            [{
                "QuoteId": "000000000999501123",
                "EffectiveDate": "11/04/2016",
            }],
            [{
                "QuoteId": "000000000999501123",
                "EffectiveDate": "11/04/2016",
                "Messages": [{"Type" : "KO"}]
            }],
            [{
                "QuoteId": "000000000999501123",
                "EffectiveDate": "11/04/2016",
                "Messages": [{"Type" : "KO"}],
                "AnnualPremium": "$445"
            }],
            [{
                "EffectiveDate": "11/04/2016",
                "Messages": [{"Type" : "KO"}],
                "AnnualPremium": "$445"
            }],
            [{
                "QuoteId": "000000000999501123",
                "Messages": [{"Type" : "KO"}],
                "AnnualPremium": "$445"
            }],
            [{
                # no required keys are found in object list
            }],
            

        ]

        
        expectedData = [('000000000999501123', '11/04/2016', 'Unknown', '0')]
        self.assertEqual(MySQL_Quotes.create_list(sample_data[0]), expectedData)

        expectedData = [('000000000999501123', '11/04/2016', 'KO', '0')]
        self.assertEqual(MySQL_Quotes.create_list(sample_data[1]), expectedData)

        expectedData = [('000000000999501123', '11/04/2016', 'KO', '1')]
        self.assertEqual(MySQL_Quotes.create_list(sample_data[2]), expectedData)

        expectedData = [('Unknown', '11/04/2016', 'KO', '1')]
        self.assertEqual(MySQL_Quotes.create_list(sample_data[3]), expectedData)
        
        expectedData = [('000000000999501123', 'Unknown', 'KO', '1')]
        self.assertEqual(MySQL_Quotes.create_list(sample_data[4]), expectedData)

        expectedData = [('Unknown', 'Unknown', 'Unknown', '0')]
        self.assertEqual(MySQL_Quotes.create_list(sample_data[5]), expectedData)


    def test_MySQL_QNB_create_list(self):
        print("Expect to pass in list of quote objects and return only QuoteId and MessageText if message type is QNB")
        
        sample_data = [
            [{

            }],
            [{
                "QuoteId": "000000000999501123",
                "Messages": [
                    {
                        "MessageText": "VSR > 27", 
                        "Type" : "KO"
                    }
                ]
            }],
            [{
                "Messages": [{"MessageText": "VSR > 27", 
                            "Type" : "KO"}]
            }],
            [{
                "QuoteId": "000000000999501123",
                "Messages": [
                    {
                        "MessageText": "HighRiskVehicle BENT", 
                        "Type" : "QuoteNotBind"
                    },
                    {
                        "MessageText": "VSR > 27", 
                        "Type" : "KO"
                    },
                    {
                        "MessageText": "No coverage history found for policyholder", 
                        "Type" : "QuoteNotBind"
                    },
                ]
            }]
         ]

        
        expectedData = []
        self.assertEqual(MySQL_QNB.create_list(sample_data[0]), expectedData)

        expectedData = []
        self.assertEqual(MySQL_QNB.create_list(sample_data[1]), expectedData)

        expectedData = []
        self.assertEqual(MySQL_QNB.create_list(sample_data[2]), expectedData)

        expectedData = [('000000000999501123', "HighRiskVehicle BENT"), ('000000000999501123', "No coverage history found for policyholder")]
        self.assertEqual(MySQL_QNB.create_list(sample_data[3]), expectedData)

    # def test_create_list(self):
    #     print("Expect to pass in object with __ properties and return list of tuples")        


    # def tearDown(self):
        # self.widget.dispose()


if __name__ == '__main__':
    unittest.main()

            # [{
            #     "QuoteId": "000000000999501123",
            #     "Messages": [
            #         {
            #             "MessageText": "HighRiskVehicle BENT", 
            #             "Type" : "QuoteNotBind"
            #         },
            #         {
            #             "MessageText": "VSR > 27", 
            #             "Type" : "KO"
            #         },
            #         {
            #             "MessageText": "No coverage history found for policyholder", 
            #             "Type" : "QuoteNotBind"
            #         },
            #     ]
            # }]