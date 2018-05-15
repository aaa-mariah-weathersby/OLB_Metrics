import MySQLdb
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
        return dict_root


class MySQL_Quotes():
    # def __init__():
    #     self.data_dict = None
    #     self.quote_list = []
    
    @staticmethod
    def create_list(quotePath):
        data_dict = None
        quote_list = []

        print quotePath

        with open(quotePath, 'r') as f:
            data_dict = json.load(f)

        dict_root = data_dict['Quotes']

        for quote in dict_root:
            print quote
            quote_id = quote['QuoteId']
            quote_date = quote['EffectiveDate']
            quote_type = "Gold"
            
            if 'Messages' in quote.keys():
                quote_type = quote['Messages'][0]["Type"]

            quote_tup = (quote_id, quote_date, quote_type)
            quote_list.append(quote_tup)

        print quote_list
        return quote_list


class DB_inject(): 
    def __init__(host, user, passwd, db):
        self.db_conn = MySQLdb.connect(host= host,
                        user=user,
                        passwd=passwd,
                        db=db)

    @staticmethod
    def db_inject(quote_list, db, db_table):

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

# class MySQL_QNB():
        # print "quote_list"

    #tuple list insert in mysqlDB quote_not_bind [quoteid, rules_list]

