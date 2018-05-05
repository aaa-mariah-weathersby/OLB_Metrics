import datetime

"""
Usage:
    python transform_datetime_refactored.py

Note:
    Change values for 'INPUT_FILENAME' / 'OUTPUT_FILENAME' for file locations

"""

class QuoteTransform:
    SEPARATOR = " "
    NEWLINE = "\n"
    #INPUT_FILENAME = "C:\\Users\\E668872\\Documents\\BlueZone\\Transfer\\transfertest77.txt"
    #OUTPUTFILE = "C:\\files\\testDoc.txt"
    INPUT_FILENAME = "transfertest77.txt"
    OUTPUT_FILENAME = "testDoc.txt"
    OUTPUT_FILEMODE = "w"

    def __init__(self):
        self.INPUTFILE = None
        self.OUTPUTFILE = None

    def open_filehandles(self):
        self.INPUTFILE = open(self.INPUT_FILENAME)
        self.OUTPUTFILE = open(self.OUTPUT_FILENAME, self.OUTPUT_FILEMODE)

    def construct_header(self):
        return "QuoteID"+self.SEPARATOR+"CreateDate" + self.NEWLINE

    def write_header(self):
        self.OUTPUTFILE.write(self.construct_header())

    def split_datum(self, datum):
        return datum.split(self.SEPARATOR)

    def remove_plus_symbol(self, quoteid):
        return quoteid.replace("\x00+", "")

    def process_datein_to_dtime(self, datein):
        return datetime.datetime.strptime(datein[0:10], "%Y-%m-%d")

    def process_dtime_to_formatteddtime(self, dtime):
        return dtime.strftime("%m/%d/%Y")

    def join_datum(self, quoteid, createdate):
        return quoteid + self.SEPARATOR + createdate + self.NEWLINE

    def process_quoteid(self, rawquoteid):
        return self.remove_plus_symbol(rawquoteid)

    def process_createdate(self, rawcreatedate):
        return self.process_dtime_to_formatteddtime(
            self.process_datein_to_dtime(rawcreatedate)
        )

    def process_datum(self, line):
        parts = self.split_datum(line)
        quoteid = self.process_quoteid(parts[0])
        createdate = self.process_createdate(parts[1])
        return self.join_datum(quoteid, createdate)

    def process_data(self):
        for datum in self.INPUTFILE.readlines():
            if datum == "\x1a":
                continue
            self.OUTPUTFILE.write(self.process_datum(datum))

    def close_filehandles(self):
        self.INPUTFILE.close()
        self.INPUTFILE = None
        self.OUTPUTFILE.close()
        self.OUTPUTFILE = None

    @staticmethod
    def process_files():
        quoteTransform = QuoteTransform()
        quoteTransform.open_filehandles()
        quoteTransform.write_header()
        quoteTransform.process_data()
        quoteTransform.close_filehandles()

if __name__ == "__main__":
    QuoteTransform.process_files()
