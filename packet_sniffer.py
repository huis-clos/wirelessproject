#Python script to parse tcpDump file and get out 
#signal strength while also formatting. Reads in a
#tcpdump that has been written to a file and writes
#out desired output to a new file

#open file

tcpFile = open('tcpDump', 'r')

sigList = []

print "\n\n********** Begin parsing file for signal strength *********\n\n"

count = 0
countTA = 0

for line in tcpFile:
	aLine = line.split()
	for i in aLine:
		if 'TA' in i.split(':'):
			if 'dB' in aLine[8]:
				aWord = aLine[8].strip('dB')
				aWord = int(aWord)
				sigList.append(aWord)
			countTA = countTA + 1
	count = count + 1


tcpFile.close()

print sigList
print len(sigList)
print count
print countTA


print "\n\n*********** Writing to file ***********\n\n"

tcpOutput = open('output', 'w')

for i in sigList:
	tcpOutput.write("%s\n" % i)

tcpOutput.close()

print "\n\n*********** Done **************\n\n"
 
