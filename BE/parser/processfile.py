"""utility to process db2 dump of quotes

currently hardcoded to process "transfertest79.txt"

"""

import json
import re

def split_line(line):
    """split bytes at first \x00\x00 entry"""
    return line.split(b'\x00\x00', 1)

def cleanup_quoteblob(quoteblob):
    """cleanup the quote-blob with the following steps:

    * remove the first 2 bytes
    * remove any \x00 bytes
    """
    if(quoteblob == b'\x1a'):
        return ("")
    quoteblob = quoteblob.split(b'\x00\x00', 1)[1]
    quoteblob = quoteblob[2:]
    quoteblob = quoteblob.replace(b'\x00', b'')
    if(len(quoteblob) >= 32743):
        return('')
    return quoteblob.decode()

def tso_encode_quoteid(quoteid):
    """tso encoding of quote id
    take example quote idea and transform it:

    * reverse the first 8 digits

    before:
    589359991

    after:
    999539851
    """
    return (quoteid[0:8])[::-1] + quoteid[8:9]

def processfile(inputfilename):
    """process binary file in following steps:
    read contents of file
    split on '\r\n' character
    process each entry
    """

    inputfile = open(inputfilename, "r+b")
    data = inputfile.read()
    lines = data.split(b'\r\n')

    final_obj = "{\"Quotes\":["
     
    # line = cleanup_quoteblob(lines[0])

    # process only 1 line right now...
    # lines = [lines[3]]

    for indx, line in enumerate(lines):

        obj = cleanup_quoteblob(line)
        if (len(obj) != 0):
            if(indx != 0):
                obj = ',' + obj
            final_obj += obj
   
    final_obj = final_obj + ']}'
    inputfile.close()

    return final_obj

def createmassagedfile(data):
    f = open("DATA.txt","w+")
    f.write(data)
    f.close()
    

if __name__ == '__main__':
    data = processfile("transfertest79.txt")
    #data = processfile("transfertestApril.txt")
    createmassagedfile(data)

