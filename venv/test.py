import binascii


def binaryStringToInt(s):
    result = 0
    for i in range(0, len(s)):
        digit = s[len(s)-1-i]
        if digit == '1':
            result += 2**i
    return result


def makeEight(s):
    x = '0'
    s = s[2:]
    while len(s) < 8:
        s = x + s
    # print s
    return s


def convertChar(l):
    result = ''
    for i in range(0,len(l)):
        k = binascii.hexlify(l[i])
        j = bin(int(k, 16))
        x = makeEight(j)
        result = result + x
    return result


count = 0
with open("properties.db", "rb") as f:
    for lines in f:
        # line = ''.join(format(ord(x), 'b') for x in lines)
        print len(lines)
        g = binascii.hexlify(lines)
        line = convertChar(lines)
        if count > 10:
            break
        count += 1
        # test = line[:64]
        # test2 = line[64:]
        # print binaryStringToInt(test)
        # print binaryStringToInt(test2)


#
# counter = 0
# with open("properties.db", "rb") as f:
#     for lines in f:
#         print lines
#
#         line = ''.join(format(ord(x), 'b') for x in lines)
#
#         parentId = line[:64]
#         variable = line[64:96]
#         value = line[96:128]
#         dontcare = line[128:136]
#         propAddress = line[136:200]
#         timeBuff1 = line[200:248]
#         timeBuff2 = line[248:296]
#         timeBuff3 = line[296:344]
#         timeBuff4 = line[344:392]
#         timeBuff5 = line[392:440]
#         print line
#
#         writer.writerow([counter, binaryStringToInt(parentId), binaryStringToInt(variable), binaryStringToInt(value),
#                          binaryStringToInt(dontcare), binaryStringToInt(propAddress), binaryStringToInt(timeBuff1),
#                          binaryStringToInt(timeBuff2), binaryStringToInt(timeBuff3), binaryStringToInt(timeBuff4),
#                            binaryStringToInt(timeBuff5)])
#
#         counter += 1


# def createNodeFile():
#     # 9
#     parentIdMask = 0xffffffffffffffff
#     parentIdMask = parentIdMask << 384
#     # 5
#     variableMask = 0xffffffff
#     variableMask = variableMask << 352
#     # 5
#     valueMask = 0xffffffff
#     valueMask = valueMask << 320
#     # 2
#     dontcareMask = 0xf
#     dontcareMask = dontcareMask << 312
#     # 9
#     propAdressMask = 0xffffffffffffffff
#     propAdressMask = propAdressMask << 248
#     # 7 but there is 5 of them
#     timeBuffMask = 0xffffffffffff
#     timeBuffMask = timeBuffMask << 200
#
#     c = open('nodes.csv', 'wb')
#     writer = csv.writer(c, delimiter=',')
#     writer.writerow(['id', 'parentId', 'variable', 'value', 'dontcare', 'propAddress', 'timeBuff1', 'timeBuff2',
#           'timeBuff3', 'timeBuff4', 'timeBuff5'])
#
#     counter = 0
#     with open("properties.db", "rb") as f:
#         for lines in f:
#             line = ''.join(format(ord(x), 'b') for x in lines)
#
#             parentId = long(line) & parentIdMask
#             parentId = parentId >> 384
#
#             variable = long(line) & variableMask
#             variable = variable >> 352
#
#             value = long(line) & valueMask
#             value = value >> 320
#
#             dontcare = long(line) & dontcareMask
#             dontcare = dontcare >> 312
#
#             propAddress = long(line) & propAdressMask
#             propAddress = propAddress >> 248
#
#             timeBuff1 = long(line) & timeBuffMask
#             timeBuff1 = timeBuff1 >> 200
#
#             timeBuff2 = long(line) & (timeBuffMask >> 48)
#             timeBuff2 = timeBuff2 >> 152
#
#             timeBuff3 = long(line) & (timeBuffMask >> 96)
#             timeBuff3 = timeBuff3 >> 104
#
#             timeBuff4 = long(line) & (timeBuffMask >> 144)
#             timeBuff4 = timeBuff4 >> 56
#
#             timeBuff5 = long(line) & (timeBuffMask >> 192)
#             timeBuff5 = timeBuff5 >> 8
#
#             writer.writerow([counter, parentId, variable, value, dontcare, propAddress, timeBuff1, timeBuff2,
#                       timeBuff3, timeBuff4, timeBuff5])
#             counter += 1
#             print 'ParentID: {}'.format(parentId)
#             print 'Variable: {}'.format(variable)
#             print 'Value: {}'.format(value)
#             print 'Dontcare: {}'.format(dontcare)
#             print 'PropAddress: {}'.format(propAddress)
#             print 'TimeBuff1: {}'.format(timeBuff1)
#             print 'TimeBuff2: {}'.format(timeBuff2)
#             print 'TimeBuff3: {}'.format(timeBuff3)
#             print 'TimeBuff4: {}'.format(timeBuff4)
#             print 'TimeBuff5: {}'.format(timeBuff5)
#     c.close()
