from os import getcwd
from subprocess import Popen, PIPE
import pathlib

pipe = Popen('nslookup myip.opendns.com resolver1.opendns.com',stdout=PIPE)
outputText = pipe.communicate()[0]
print(outputText)

textList = outputText.split()
textLength = len(textList)
publicIp = textList[textLength-1]

filePath = pathlib.Path(__file__).parent.resolve().joinpath('public_ip.txt')
print(filePath)


file =open(filePath,"w")
file.write("%s" % publicIp.decode("utf-8"))
file.close()

print(publicIp)