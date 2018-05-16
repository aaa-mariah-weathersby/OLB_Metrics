import MySQLdb
import json


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
    def create_list( list ):

        quote_list = []
        counter = 0

        for quote in list:

            quote_id, quote_date, quote_type, quote_premium = "\"Other\"", "\"Unknown\"", "\"Bound\"", "0"
            keys = quote.keys()

            if 'QuoteId' in keys:
                quote_id = str(quote['QuoteId'])

            else:
                quote_id = "\"Other%s\"" %(str(counter))
                counter+=1

            if 'EffectiveDate' in keys:
                quote_date = quote['EffectiveDate']
                modified_date = quote_date.replace("/", "")
            
            if 'Messages' in keys and len(quote['Messages']) > 0:
                quote_type = quote['Messages'][0]["Type"]
                quote_type = '"' + quote_type + '"'

            if 'AnnualPremium' in keys:
                quote_premium = "1"                

            quote_tup = (quote_id, modified_date, quote_type, quote_premium)
            quote_list.append(quote_tup)

        return quote_list


class MySQL_QNB():

    @staticmethod
    def create_list( list ):

        qnb_list = []
        counter = 0

        for quote in list:
            # qnb_message_list = []

            quote_id, qnb_message = "", []
            keys = quote.keys()

            if 'QuoteId' in keys:
                quote_id = quote['QuoteId']

            else:
                quote_id = "Unknown" + str(counter)
                counter+=1


            if 'Messages' in keys and len(quote['Messages']) > 0:
                for message in quote['Messages']:
                    qnb_message = message['MessageText']
                    mType = message['Type']
                    
                    if mType == 'QuoteNotBind':
                        qnb_tup = (quote_id, '"' + qnb_message + '"')
                        qnb_list.append(qnb_tup)

        return qnb_list 


class DB_inject(): 
    # def __init__(host, user, passwd, db):
    #     self.db_conn = MySQLdb.connect(host= host,
    #                     user=user,
    #                     passwd=passwd,
    #                     db=db)

    @staticmethod
    def db_inject(quote_list, db, db_table, table_conditions):

        conn = MySQLdb.connect(host= "localhost",
                        user="root",
                        passwd="Autoclub.1!",
                        db=db)
        x = conn.cursor()

        check_table_command = "CREATE TABLE IF NOT EXISTS %s (%s)" %(db_table, table_conditions)
        x.execute(check_table_command)
        
        clear_table_command = "TRUNCATE TABLE %s" %(db_table)
        x.execute(clear_table_command)

        sql_command_base = "INSERT INTO %s VALUES" %(db_table)

        for index, quote in enumerate(quote_list):
            quote_stuff = str(quote_list[index])
            sql_string = "("

            for data in quote_list[index]:
                sql_string = sql_string + data + ","

            sql_string = sql_string[:-1]
            sql_string = sql_string + ")"

            # sql_command = "INSERT INTO %s VALUES (%s,%s,%s,%s)" %(db_table, quote_list[index][0], quote_list[index][1], quote_list[index][2], quote_list[index][3])
            sql_command = "INSERT INTO %s VALUES %s" %(db_table, sql_string)
            print sql_command

            x.execute(sql_command)
            conn.commit()


