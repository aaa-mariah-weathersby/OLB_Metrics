import mysqlConnect

RAW = 'demo-quote.txt'

HOST = 'localhost'
USER = 'root'
PASS = 'Autoclub.1!'
DB = 'OLB_Reports'

MySQL_Quotes = mysqlConnect.MySQL_Quotes()
File_Parser = mysqlConnect.File_Parser()
DB_inject = mysqlConnect.DB_inject( HOST, USER, PASS, DB )

class Init():

    def __init__():
        self.data_dict = None
        self.quote_list = []

    # local_list = MySQL_Quotes.create_list(RAW)
    # DB_inject.db_inject(local_list, "a", "b")
    print DB_inject