def chrchar(s):
    res = ''
    l = len(s)
    for i in range(0,l):
        res += 'ChrW(' + str(ord(s[i])) + ') & '
    res = res[:-3]
    return res

def Addvariable(k):
    p = ""
    if (k==0):
        return p
    
    p += "    Dim " + chr(k) + " As String\n"

    return p

def split(s,l):
    
    res  = "    Dim str As String\n" 
    count = l // 30
    if (l % 30 != 0):
        last = l % 30
    for i in range (0,count+1):
        res += Addvariable(65+i)
    print(count)
    for i in range (0,count):
        s1 = s[:30]
        res += "    " + chr(65 + i) + " = " + chrchar(s1) +"\n"
        s = s[30:]
    res += "    "+chr(65+count) + " = " + chrchar(s) + "\n"
    res += "    str = "
    for i in range (0,count):
        res += chr(65+i) + " + "
    res += chr(65+count)+"\n"
    res += "    Shell(str)\n" 
    print(res)

s = input('Enter string to obfuscate:')
l = len(s)
split(s,l)