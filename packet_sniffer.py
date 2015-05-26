#!/usr/bin/python
#Python script to parse tcpDump file and get out 
#signal strength while also formatting. Reads in a
#tcpdump that has been written to a file and writes
#out desired output to a new file

#runs as ./packet_sniffer <filename> <filename> ...
import sys


def main(argv):
    sigList = []

    print "\n\n********** Begin parsing file for signal strength *********\n\n"

    count = 0
    countTA = 0
    print "\nFiles given: ",  argv
    print '\n\n'
    if len(argv) == 0:
	sys.exit("\nNo files given\n")
    for item in argv:
	try:
        	aFile = open(item, 'r')
	except IOError:
		print "Cannot open file ", item
		aFile = None
	if aFile is not None:
        	for line in aFile:
            		aLine = line.split()
            		for i in aLine:
                		if 'SA' in i.split(':'):
                    			if 'dB' in aLine[8]:
                        			aWord = aLine[8].strip('dB')
                        			aWord = int(aWord)
                        			sigList.append(aWord)
                		countTA = countTA + 1
            		count = count + 1
	if aFile is not None:
        	aFile.close()

    print sigList
    print len(sigList)

    print "\n\n*********** Writing to file ***********\n\n"

    tcpOutput = open('output' + argv[0] + '.txt', 'w')

    for i in sigList:
        tcpOutput.write("%s\n" % i)

    tcpOutput.close()

    print "\n\n*********** Done **************\n\n"


if __name__ == "__main__":
    main(sys.argv[1:])

 
