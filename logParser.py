import re

filename = "sportcarveiculos-access"
logFile = open(filename)
data = logFile.read()


def getIpAddress():
    return re.findall( r'[0-9]+(?:\.[0-9]+){3}', data)

def getUniqIpAddress():
    unique = getIpAddress()
    return list(set(unique))

def getMissedUrls():
    return re.findall( r'(\"GET\ [\\\/\\\ \w\.]+\"\ 40[0-9])', data)

def getCoolUrls():
    return re.findall( r'(\"GET\ [\\\/\\\ \w\.]+\"\ 20[0-9])', data)

def getServerErrosUrls():
    return re.findall( r'(\"GET\ [\\\/\\\ \w\.]+\"\ 50[0-9])', data)

def getRedirectsUrls():
    return re.findall( r'(\"GET\ [\\\/\\\ \w\.]+\"\ 30[0-9])', data)

def getAllErrorsCode():
    return re.findall( r'(\"GET\ [\\\/\\\ \w\.]+\"\ [0-9]{3})', data)

def getErrorsCode():
		listAllErros = getAllErrorsCode()
		e400 = []
		e500 = []
		for a in listAllErros:
				if bool(re.search(r'4[0-9]{2}', a)):
						e400.append(re.findall(r'4[0-9]{2}', a))
				if bool(re.search(r'5[0-9]{2}', a)):
						e500.append(re.findall(r'5[0-9]{2}', a))

		return [e400,e500]

def getAccessedUrl():
    return 0

def getNumberOfError(errorCode):
		listAllErrors = getAllErrorsCode()
		errors = []
		for a in listAllErrors:
				if bool(re.search(r"errorCode", a)):
						errors.append(re.findall(r"errorCode", a))

		return len(errors)

def getMostAccessedUrl():
    return 0


b = getNumberOfError(408)
print (b)

