import calendar

def oy_kalendari(year, month):
    oy_kalendar = calendar.month(year, month)
    return oy_kalendar

def yil_kalendari(year):
    yil_kalendar = calendar.calendar(year)
    return yil_kalendar


year = 2024
month = 7

print(f"{year} yil, {month}-oy kalendari:")
print(oy_kalendari(year, month))

print(f"{year} yil kalendari:")
print(yil_kalendari(year))
