import mysqlConnect

# RAW = 'demo-quote.txt'
RAW = 'testdata1b.txt'

HOST = 'localhost'
USER = 'root'
PASS = 'Autoclub.1!'
DB = 'OLB_Reports'

QUOTES_TABLE = 'quotes1'
QUOTES_TABLE_SCHEMA = 'quote_id CHAR(20), date_created DATE, type CHAR(20), premium_offered CHAR(1)'

QNB_TABLE = 'quote_not_bind'
QNB_TABLE_SCHEMA = 'quote_id CHAR(20), rule_name CHAR(255)'

QuotesData = mysqlConnect.QuotesData()
FileParser = mysqlConnect.FileParser()
QNBData = mysqlConnect.QNBData()

DB_Inject = mysqlConnect.DB_Inject()

class Init():

    def __init__():
        self.data_dict = None
        self.quote_list = []
        self.qnb_list = []

    data_list = FileParser.parse(RAW)
    
    tuples = QuotesData.create_list(data_list)
    DB_Inject.inject(tuples, DB, QUOTES_TABLE, QUOTES_TABLE_SCHEMA)

    tuples2 = QNBData.create_list(data_list)
    DB_Inject.inject(tuples2, DB, QNB_TABLE, QNB_TABLE_SCHEMA)