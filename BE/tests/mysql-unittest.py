import sys
sys.path.append("..")

import unittest
import json
import csv

import mysqlConnect

MOCK_INPUT_DATA = open('../data/mock/mock_formatted_data.txt')
MOCK_QUOTE = open('../data/mock/demo-quote.txt', 'r')

QuotesTable = mysqlConnect.QuotesData()
file_parser = mysqlConnect.FileParser()
QNBTable = mysqlConnect.QNBData()
string_parser = mysqlConnect.SQLStringParser()


MOCK_DATA = '../data/mock/test-data.txt'

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
        print("\n")
        
        expectedData = [('000000000999501123', '11/04/2016', 'Gold')]
        expected_data_type = type(expectedData)

        returned_data = file_parser.parse(MOCK_DATA)
        returned_data_type = type(returned_data)

        self.assertEqual(expected_data_type, returned_data_type)

    def test_string_formatter(self):
        print("Wrap string in quotes")
        print("\n")        

        expected_data = ["\'" + "testing" + "\'"]
        expected_data = tuple(expected_data)
        sample_data = ["testing"]
        
        self.assertEqual(string_parser.wrap_quotes(sample_data), expected_data)


    def test_MySQL_quotes_create_list(self):
        print("Expect to pass in list of quote objects and return formatted list of tuples")
        print("\n")

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

        
        expectedData = [("\'000000000999501123\'", "\'2016-11-04\'", "\'Unknown\'", "\'0\'")]
        self.assertEqual(QuotesTable.create_list(sample_data[0]), expectedData)

        expectedData = [("\'000000000999501123\'", "\'2016-11-04\'", "\'KO\'", "\'0\'")]
        self.assertEqual(QuotesTable.create_list(sample_data[1]), expectedData)

        expectedData = [("\'000000000999501123\'", "\'2016-11-04\'", "\'KO\'", "\'1\'")]
        self.assertEqual(QuotesTable.create_list(sample_data[2]), expectedData)
        
        expectedData = [("\'000000000999501123\'", "\'Unknown\'", "\'KO\'", "\'1\'")]
        self.assertEqual(QuotesTable.create_list(sample_data[4]), expectedData)


    # ----------------- UNIQUE ID ASSIGNED IF UNKNOWN -----------------
        # expectedData = [("\'Unknown\'", "\'2016-11-04\'", "\'KO\'", "\'1\'")]
        # self.assertEqual(QuotesTable.create_list(sample_data[3]), expectedData)

        # expectedData = [('Unknown', 'Unknown', 'Unknown', '0')]
        # self.assertEqual(QuotesTable.create_list(sample_data[5]), expectedData)
    # ----------------- UNIQUE ID ASSIGNED IF UNKNOWN -----------------
        


    def test_MySQL_QNB_create_list(self):
        print("Expect to pass in list of quote objects and return only QuoteId and MessageText if message type is QNB")
        print("\n")
        
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
        test_map = []
        
        expectedData = []
        self.assertEqual(QNBTable.create_list(sample_data[0]), expectedData)

        expectedData = []
        self.assertEqual(QNBTable.create_list(sample_data[1], test_map), expectedData)

        expectedData = []
        self.assertEqual(QNBTable.create_list(sample_data[2]), expectedData)

        expectedData = [("000000000999501123", '\"HighRiskVehicle BENT\"'), ('000000000999501123', '\"No coverage history found for policyholder\"')]
        self.assertEqual(QNBTable.create_list(sample_data[3]), expectedData)


if __name__ == '__main__':
    unittest.main()
