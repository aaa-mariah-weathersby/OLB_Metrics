import mysqlConnect

# RAW = 'demo-quote.txt'
RAW = 'testdata1b.txt'

HOST = 'localhost'
USER = 'root'
PASS = 'Autoclub.1!'
DB = 'OLB_Reports'

MySQL_Quotes = mysqlConnect.MySQL_Quotes()
File_Parser = mysqlConnect.File_Parser()
# DB_inject = mysqlConnect.DB_inject( HOST, USER, PASS, DB )

class Init():

    def __init__():
        self.data_dict = None
        self.quote_list = []

    data_list = File_Parser.parse_file(RAW)
    tuples = MySQL_Quotes.create_list(data_list)

    # DB_inject.db_inject(local_list, "a", "b")
    print tuples