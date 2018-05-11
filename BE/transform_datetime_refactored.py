# -*- coding: utf-8 -*-
"""Usage:
    python transform_datetime_refactored.py

Note:
    Change values for 'INPUT_FILENAME' / 'OUTPUT_FILENAME' for file locations

"""

import datetime

class QuoteTransform:
    """This class contains methods used to transform Quote record entries from
    the file created by the database drop to a 2-column text format
    """

    SEPARATOR = " "
    NEWLINE = "\n"
    #INPUT_FILENAME = "C:\\Users\\E668872\\Documents\\BlueZone\\Transfer\\transfertest77.txt"
    #OUTPUT_FILE = "C:\\files\\testDoc.txt"
    INPUT_FILENAME = "transfertest77.txt"
    OUTPUT_FILENAME = "testDoc.txt"
    OUTPUT_FILEMODE = "w"

    def __init__(self):
        self.input_file = None
        self.output_file = None

    def open_filehandles(self):
        """Opens filehandles from values INPUT_FILENAME and OUTPUT_FILENAME"""
        self.input_file = open(self.INPUT_FILENAME)
        self.output_file = open(self.OUTPUT_FILENAME, self.OUTPUT_FILEMODE)

    def construct_header(self):
        """returns output file header"""
        return "QuoteID"+self.SEPARATOR+"CreateDate" + self.NEWLINE

    def write_header(self):
        """writes output file header to OUTPUT_FILE"""
        self.output_file.write(self.construct_header())

    def split_datum(self, datum):
        """splits input datum based on SEPARATOR"""
        return datum.split(self.SEPARATOR)

    @staticmethod
    def remove_plus_symbol(quoteid):
        """removes invalid characters from quoteid"""
        return quoteid.replace("\x00+", "")

    @staticmethod
    def process_datein_to_dtime(datein):
        """string YYYY-mm-dd to datetime"""
        return datetime.datetime.strptime(datein[0:10], "%Y-%m-%d")

    @staticmethod
    def process_dtime_to_formatteddtime(dtime):
        """datetime to string mm/dd/YYYY"""
        return dtime.strftime("%m/%d/%Y")

    def join_datum(self, quoteid, createdate):
        """"create entry joined by SEPARATOR"""
        return quoteid + self.SEPARATOR + createdate + self.NEWLINE

    def process_quoteid(self, rawquoteid):
        """"process quoteid string"""
        return self.remove_plus_symbol(rawquoteid)

    def process_createdate(self, rawcreatedate):
        """"process createdate string"""
        return self.process_dtime_to_formatteddtime(
            self.process_datein_to_dtime(rawcreatedate)
        )

    def process_datum(self, line):
        """"process datum entry"""
        parts = self.split_datum(line)
        quoteid = self.process_quoteid(parts[0])
        createdate = self.process_createdate(parts[1])
        return self.join_datum(quoteid, createdate)

    def process_data(self):
        """"process data"""
        for datum in self.input_file.readlines():
            if datum == "\x1a":
                continue
            self.output_file.write(self.process_datum(datum))

    def close_filehandles(self):
        """"closes filehandles"""
        self.input_file.close()
        self.input_file = None
        self.output_file.close()
        self.output_file = None

    @staticmethod
    def process_files():
        """"static method that does the following:
        opens filehandles
        writes header to output file
        process data - reach each line from input, transform, and write to output
        closes filehandles
        """
        quotetransform = QuoteTransform()
        quotetransform.open_filehandles()
        quotetransform.write_header()
        quotetransform.process_data()
        quotetransform.close_filehandles()

if __name__ == "__main__":
    QuoteTransform.process_files()
