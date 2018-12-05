import csv
import binascii


def makeEight(s):
    x = '0'
    s = s[2:]
    while len(s) < 8:
        s = x + s
    return s


def binaryStringToInt(s):
    result = ''
    for i in range(len(s)):
        digit = ord(s[len(s)-1-i])
        digitSTR = makeEight(bin(digit))
        result = digitSTR + result
    return result


def createNodeFile():
    c = open('nodes.csv', 'wb')
    writer = csv.writer(c, delimiter=',')
    writer.writerow(['id', 'parentId', 'variable', 'value', 'dontcare', 'propAddress', 'timeBuff1', 'timeBuff2',
                     'timeBuff3', 'timeBuff4', 'timeBuff5'])

    counter = 0
    with open("properties.db", "rb") as f:
        while True:
            binary = f.read(56)
            if not binary:
                break
            line = binaryStringToInt(binary)

            parentId = line[:64]
            variable = line[64:96]
            value = line[96:128]
            dontcare = line[128:136]
            propAddress = line[136:200]
            timeBuff1 = line[200:248]
            timeBuff2 = line[248:296]
            timeBuff3 = line[296:344]
            timeBuff4 = line[344:392]
            timeBuff5 = line[392:440]

            parentId = int(parentId, 2)
            variable = int(variable, 2)
            value = int(value, 2)
            dontcare = int(dontcare, 2)
            propAddress = int(propAddress, 2)
            timeBuff1 = int(timeBuff1, 2)
            timeBuff2 = int(timeBuff2, 2)
            timeBuff3 = int(timeBuff3, 2)
            timeBuff4 = int(timeBuff4, 2)
            timeBuff5 = int(timeBuff5, 2)

            # print 'parent: {}'.format(parentId)
            # print 'variable: {}'.format(variable)
            # print 'value: {}'.format(value)
            # print 'dontcare: {}' .format(dontcare)
            # print 'propAddress {}'.format(propAddress)
            # print 'timeBuff1 {}'.format(timeBuff1)
            # print 'timeBuff2 {}'.format(timeBuff2)
            # print 'timeBuff3 {}'.format(timeBuff3)
            # print 'timeBuff4 {}'.format(timeBuff4)
            # print 'timeBuff5 {}'.format(timeBuff5)

            writer.writerow([counter, (parentId), (variable), (value),
                             (dontcare), (propAddress), (timeBuff1),
                             (timeBuff2), (timeBuff3), (timeBuff4), (timeBuff5)])
            counter += 1
    c.close()


def createRelFile():
    c = open('relations.csv', 'wb')
    writer = csv.writer(c, delimiter=',')
    writer.writerow(
        ['parentNode', 'nextRel'])

    with open("child.db", "rb") as f:
        while True:
            binary = f.read(16)
            if not binary:
                break
            line = binaryStringToInt(binary)

            parentNode = line[:64]
            nextRel = line[64:]

            parentNode = int(parentNode, 2)
            nextRel = int(nextRel, 2)
            writer.writerow([parentNode, nextRel])


    c.close()
createNodeFile()
createRelFile()