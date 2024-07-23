import calendar

def saqlash_html_kalendari(year, filename='calendar.html'):
    yil_kalendar = calendar.HTMLCalendar(calendar.SUNDAY).formatyear(year)

    with open(filename, 'w') as f:
        f.write('<html>\n<head>\n<title>{0} Year Calendar</title>\n</head>\n<body>\n'.format(year))
        f.write(yil_kalendar)
        f.write('\n</body>\n</html>')

saqlash_html_kalendari(2024)
