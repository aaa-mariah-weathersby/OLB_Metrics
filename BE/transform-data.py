import mysqlConnect

# RAW = 'demo-quote.txt'
RAW = 'testdata1b.txt'

HOST = 'localhost'
USER = 'root'
PASS = 'Autoclub.1!'
DB = 'OLB_Reports'

QUOTES_TABLE = 'quotes1'
QUOTES_TABLE_SCHEMA = 'quote_id CHAR(20), date_created CHAR(20), type CHAR(20), premium_offered CHAR(1)'

QNB_TABLE = 'quote_not_bind'
QNB_TABLE_SCHEMA = 'quote_id CHAR(20), rule_name CHAR(255)'

MySQL_Quotes = mysqlConnect.MySQL_Quotes()
File_Parser = mysqlConnect.File_Parser()
MySQL_QNB = mysqlConnect.MySQL_QNB()

DB_inject = mysqlConnect.DB_inject()

class Init():

    def __init__():
        self.data_dict = None
        self.quote_list = []
        self.qnb_list = []

    data_list = File_Parser.parse_file(RAW)
    
    tuples = MySQL_Quotes.create_list(data_list)
    DB_inject.db_inject(tuples, DB, QUOTES_TABLE, QUOTES_TABLE_SCHEMA)

    tuples2 = MySQL_QNB.create_list(data_list)
    DB_inject.db_inject(tuples2, DB, QNB_TABLE, QNB_TABLE_SCHEMA)


    # DB_inject.db_inject(local_list, "a", "b")
    # print tuples