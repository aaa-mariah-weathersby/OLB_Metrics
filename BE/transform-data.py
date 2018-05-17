import mysqlConnect

RAW = 'data/mock/testdata1b.txt'
CSV_RAW = 'data/QNB-map.csv'

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

    # def __init__():
    #     self.data_dict = None
    #     self.quote_list = []
    #     self.qnb_list = []
    
    data_list = FileParser.parse(RAW)

    quotes_list = QuotesData.create_list(data_list)
    DB_Inject.inject(quotes_list, DB, QUOTES_TABLE, QUOTES_TABLE_SCHEMA)

    qnb_map = FileParser.csv_parse(CSV_RAW)
    qnb_list = QNBData.create_list(data_list, qnb_map)
    DB_Inject.inject(qnb_list, DB, QNB_TABLE, QNB_TABLE_SCHEMA)