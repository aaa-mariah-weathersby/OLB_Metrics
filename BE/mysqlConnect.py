# import MySQLdb
import json

# MOCK_QUOTE_DB_ROW = ('quote_id', 'created_date', 'type')



class File_Parser():
    # def __init__():
    #     self.data_dict = None
    #     self.quote_list = []
    
    @staticmethod
    def parse_file(quotePath):
        data_dict = None

        with open(quotePath, 'r') as f:
            data_dict = json.load(f)

        dict_root = data_dict['Quotes']
        print dict_root
        return dict_root


class MySQL_Quotes():
    # def __init__():
    #     self.data_dict = None
    #     self.quote_list = []
    
    @staticmethod
    def create_list( list ):

        quote_list = []

        for quote in list:

            quote_id, quote_date, quote_type, quote_premium = "Unknown", "Unknown", "Unknown", "0"
            keys = quote.keys()

            if 'QuoteId' in keys:
                quote_id = quote['QuoteId']

            if 'EffectiveDate' in keys:
                quote_date = quote['EffectiveDate']                                
            
            if 'Messages' in keys and len(quote['Messages']) > 0:
                quote_type = quote['Messages'][0]["Type"]

            if 'AnnualPremium' in keys:
                quote_premium = "1"                

            quote_tup = (quote_id, quote_date, quote_type, quote_premium)
            quote_list.append(quote_tup)

        return quote_list


class DB_inject(): 
    # def __init__(host, user, passwd, db):
    #     self.db_conn = MySQLdb.connect(host= host,
    #                     user=user,
    #                     passwd=passwd,
    #                     db=db)

    # @staticmethod
    # def db_inject(quote_list, db, db_table):

        # conn = MySQLdb.connect(host= "localhost",
        #                 user="root",
        #                 passwd="Autoclub.1!",
        #                 db=db)
        # x = conn.cursor()

        #Check to see if DB has exsistin table

            # drop table

            #create table

        #inject data into table

        sql_command = """INSERT INTO %s VALUES (%s, %s)""" %("a", "b", "c")
        print sql_command

        # x.execute("""SELECT * FROM quotes""")
        # data = x.fetchall()



    #tuple list insert in mysqlDB quotes [quoteid, date created, type]

class MySQL_QNB():

    @staticmethod
    def create_list( list ):

        qnb_list = []

        for quote in list:
            qnb_message_list = []
            isValid = 0

            quote_id, qnb_messages = "", []
            keys = quote.keys()

            if 'QuoteId' in keys:
                quote_id = quote['QuoteId']
                isValid = 1
            
            if 'Messages' in keys and len(quote['Messages']) > 0:
                qnb_message_list = []
                for msg in quote['Messages']:
                    messageText = msg['MessageText']
                    mType = msg['Type']
                    if mType == 'QuoteNotBind':
                        qnb_message_list.append(messageText)
            
            if isValid == 1 and len(qnb_message_list) > 0:
                qnb_tup = (quote_id, qnb_message_list)
                qnb_list.append(qnb_tup)
        
        return qnb_list 

            




    #tuple list insert in mysqlDB quote_not_bind [quoteid, rules_list]

