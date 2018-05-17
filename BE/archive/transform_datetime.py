import datetime
def ParseFile():
	SEPARATOR = " "
	NEWLINE = "\n"
	f = open ("C:\\Users\\E668872\\Documents\\BlueZone\\Transfer\\transfertest77.txt")
	outputFile = open ("C:\\files\\transfertest_filtered.txt", "w")
	outputFile.write("QuoteID"+SEPARATOR+"CreateDate"+NEWLINE)
	data = f.readlines()
#	data = [data[0]]
	for datum in data:
		if datum == "\x1a":
			continue
		parts = datum.split(SEPARATOR)
		parts[0]= parts[0].replace("\x00+", "")
		dateIn = parts[1]
#		print(dateIn)
		
#		print(dateIn[0:10])
		dtime = datetime.datetime.strptime(dateIn[0:10], "%Y-%m-%d")
#		print(dtime)
#		print(dtime.strftime("%m/%d/%Y"))
#		print(datum)
#		print (parts)
		formatteddtime = dtime.strftime("%m/%d/%Y")

		
		outputFile.write(parts[0]+SEPARATOR+formatteddtime+NEWLINE)
	outputFile.close()
	f.close()
	
if __name__ == "__main__":
	ParseFile()
	
#ParseFile()
	