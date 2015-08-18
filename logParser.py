import re
import itertools
import operator

filename = "example"
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
	return re.findall(r'http://[\w\:\/\.]+', data)

def getMostAccessedUrl(L):
    # get an iterable of (item, iterable) pairs
    SL = sorted((x, i) for i, x in enumerate(L))
    # print 'SL:', SL
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
    # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index
    # pick the highest-count/earliest item
    def f7(seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if not (x in seen or seen_add(x))]
    return f7(max(groups, key=_auxfun)[0])

def getNumberOfError(errorCode):
    listAllErrors = getAllErrorsCode()
    errors = []
    for a in listAllErrors:
        if bool(re.search(r'%s' % errorCode, a)):
            errors.append(re.findall(r'errorCode', a))

    return len(errors)


b = getAccessedUrl();
c = getMostAccessedUrl(b)
print (b)

