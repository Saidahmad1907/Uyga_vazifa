import time

def bugungi_sana():
    hozir = time.localtime()
    
    today_format1 = time.strftime("Today:\n%A %d %B %Y %H:%M:%S", hozir)
    today_format2 = time.strftime("%d.%m.%Y", hozir)
    
    return today_format1, today_format2

format1, format2 = bugungi_sana()
print(format1)
print(format2)
