MAC='56:00:00:24:2f:5d'.replace(':','')
KEY = '%02X%02X%02X%02X%02X%02X%02X%02X'%((int(MAC[0:2],16)+int(MAC[4:6],16)+10)%256,(int(MAC[2:4],16)+int(MAC[6:8],16)+13)%256,(int(MAC[4:6],16)+int(MAC[8:10],16)+16)%256,(int(MAC[6:8],16)+int(MAC[10:12],16)+19)%256,(int(MAC[8:10],16)+int(MAC[0:2],16)+16)%256,(int(MAC[10:12],16)+int(MAC[2:4],16)+19)%256,(int(MAC[0:2],16)+int(MAC[4:6],16)+22)%256,(int(MAC[2:4],16)+int(MAC[6:8],16)+26)%256)
def gen_lrc(s):
    lic_6479 = ''
    rd = [162,15,239,202,57,14,45,164,147,232,120,90,117,15,239,232]
    for idx in range(len(s)):
        lic_6479 += '%02X' %((ord(s[idx]) + rd[idx]) % 256) + ' '
    return lic_6479
print gen_lrc(KEY);
