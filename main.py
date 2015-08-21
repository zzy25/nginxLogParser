import sys
import getLogInfo as log
import mysqlParser as mysql
import jsonParser as json
import logParser as parser
import os.path


args = sys.argv

def errorMessage():
    msg = ("Usage: python main.py fileName <json/parser/mysql> [params]")
    msg += ("\nParameters\n")
    parameters = ["-n - get number of errors", "-h - get access by hour", "-m - get most access urls", "-c codeNumber - urls Per Code"]
    for a in parameters:
        msg += ("\t%s\n" % (a))
    return msg

def verifyCommands(command):
    commandList = ["-h", "-m","-c","-n"]
    if command in commandList:
        return True
    else:
        return False
def verifyType(type):
    typeList = ["parser", "json", "mysql"]
    if type in typeList:
        return True
    else:
        return False


def verifyFileExiste(file):
    return os.path.isfile(file)



if len(args) == 4 and verifyCommands(args[3]) and verifyFileExiste(args[1]) and verifyType(args[2]):
    fileName = args[1]
    type= args[2]
    command = args[3]
    code = False
elif len(args) == 5 and args[3] == "-c" and verifyFileExiste(args[1]) and verifyType(args[2]):
    fileName = args[1]
    type= args[2]
    command = args[3]
    code = args[4]
else:
    print errorMessage()
    exit (1)

# For Parser

if type == "parser":
    # launch parser instance
    p = parser.logParser(fileName)
    if command == "-n":
        res = p.parseNumberOfErrors()
    elif command == "-h":
        res = p.parseHoursAccess()
    elif command == "-m":
        res = p.parseMostAccessUrl()
    elif command == "-c":
        res = p.parseUrlPerCode(code)
# For Json
elif type == "json":
    p = json.jsonParser(fileName)
    if command == "-n":
        res = p.jsonNumberOfErrors()
    elif command == "-h":
        res = p.jsonHoursAccess()
    elif command == "-m":
        res = p.jsonMostAccessUrl()
    elif command == "-c":
        res = p.jsonUrlPerCode(code)

print res





