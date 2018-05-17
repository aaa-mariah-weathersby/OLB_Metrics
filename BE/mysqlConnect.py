import MySQLdb
import datetime
import json
import csv


class FileParser():
    # def __init__():
    #     self.data_dict = None
    #     self.quote_list = []
    
    @staticmethod
    def parse(quotePath):
        data_dict = None

        with open(quotePath, 'r') as infile:
            data_dict = json.load(infile)

        dict_root = data_dict['Quotes']
        return dict_root

    @staticmethod
    def csv_parse(csvPath):
        data_dict = None

        with open(csvPath, 'r') as infile:
            reader = csv.reader(infile)
            dict_root = dict((str(rows[0]), str(rows[1])) for rows in reader)

        print dict_root.keys()
        print type(dict_root)
        return dict_root

class SQLStringParser():

    @staticmethod
    def wrap_quotes(list):
        formatted_list = []

        for index, string in enumerate(list):
            formatted_string = "'{}'".format(string)
            formatted_list.append(formatted_string)
        
        return tuple(formatted_list)
        

class QuotesData():
    # def __init__():
    #     self.data_dict = None
    #     self.quote_list = []
    
    @staticmethod
    def create_list( list ):

        quote_list = []
        counter = 0

        for quote in list:

            quote_id, formatted_date, quote_type, quote_premium = "Other", "Unknown", "Unknown", "0"
            keys = quote.keys()

            if 'QuoteId' in keys:
                quote_id = str(quote['QuoteId'])

            else:
                quote_id = "Other%s" %(str(counter))
                counter+=1

            if 'EffectiveDate' in keys:
                quote_date = quote['EffectiveDate']
                formatted_date = datetime.datetime.strptime(quote_date, "%m/%d/%Y").strftime("%Y-%m-%d")
            
            if 'Messages' in keys and len(quote['Messages']) > 0:
                quote_type = quote['Messages'][0]["Type"]

            if 'AnnualPremium' in keys:
                quote_premium = "1"                

            quote_tup = (quote_id, formatted_date, quote_type, quote_premium)
            quote_tup = SQLStringParser.wrap_quotes(quote_tup)
            quote_list.append(quote_tup)

        return quote_list


class QNBData():

    @staticmethod
    def create_list( list, map = [] ):

        qnb_list = []
        counter = 0

        if len(map) > 0:
            map_keys = map.keys()

        for quote in list:            
            quote_id, qnb_message = "", []
            keys = quote.keys()

            if 'QuoteId' in keys:
                quote_id = quote['QuoteId']

            else:
                quote_id = "Unknown" + str(counter)
                counter+=1

            if 'Messages' in keys and len(quote['Messages']) > 0:

                for message_obj in quote['Messages']:
                    mapped_rule = message_obj['MessageText']
                    message_obj_keys = message_obj.keys()

                    if 'RuleName' in message_obj_keys:
                        message_rule = message_obj["RuleName"] 

                        if map_keys:
                            if message_rule in map_keys:
                                mapped_rule = map[message_rule]                        

                    if message_obj['Type'] == 'QuoteNotBind':
                        qnb_tup = (quote_id, '"' + mapped_rule + '"')
                        qnb_list.append(qnb_tup)


        return qnb_list 


class DB_Inject(): 
    # def __init__(host, user, passwd, db):
    #     self.db_conn = MySQLdb.connect(host= host,
    #                     user=user,
    #                     passwd=passwd,
    #                     db=db)

    @staticmethod
    def inject(quote_list, db, db_table, table_conditions):

        conn = MySQLdb.connect(host= "localhost",
                        user="root",
                        passwd="Autoclub.1!",
                        db=db)
        x = conn.cursor()

        check_table_command = "CREATE TABLE IF NOT EXISTS %s (%s)" %(db_table, table_conditions)
        x.execute(check_table_command)
        
        clear_table_command = "TRUNCATE TABLE %s" %(db_table)
        x.execute(clear_table_command)

        insert_table_base = "INSERT INTO %s VALUES" %(db_table)

        for index, quote in enumerate(quote_list):
            sql_string = "("

            for data in quote_list[index]:
                sql_string = sql_string + data + ","

            sql_string = sql_string[:-1]
            sql_string = sql_string + ")"

            insert_value_command = "INSERT INTO %s VALUES %s" %(db_table, sql_string)
            print insert_value_command

            x.execute(insert_value_command)
            conn.commit()


