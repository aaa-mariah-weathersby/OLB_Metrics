import MySQLdb
import json

# MOCK_QUOTE_DB_ROW = ('quote_id', 'created_date', 'type')

# conn = MySQLdb.connect(host= "localhost",
#                   user="root",
#                   passwd="Autoclub.1!",
#                   db="OLB_Reports")
# x = conn.cursor()

# x.execute("""SELECT * FROM quotes""")
# data = x.fetchall()


class MySQL_Quotes():

    # def __init__():
    #     self.data_dict = None
    #     self.quote_list = []
    
    @staticmethod
    def create_list(quotePath):
        data_dict = None
        quote_list = []

        with open(quotePath, 'r') as f:
            data_dict = json.load(f)

        dict_root = data_dict['Quotes']

        for quote in dict_root:
            quote_id = quote['QuoteId']
            quote_date = quote['EffectiveDate']
            quote_type = "Gold"
            
            if 'Message' in quote.keys():
                quote_type = quote['Message']

            quote_tup = (quote_id, quote_date, quote_type)
            quote_list.append(quote_tup)

        return quote_list

    #tuple list insert in mysqlDB quotes [quoteid, date created, type]

# class MySQL_QNB():
        # print "quote_list"

    #tuple list insert in mysqlDB quote_not_bind [quoteid, rules_list]

