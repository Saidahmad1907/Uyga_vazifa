import datetime

def haftaning_tartib_raqami(sana):
    sana_obj = datetime.datetime.strptime(sana, '%Y-%m-%d')
    tartib_raqami = sana_obj.weekday()
    return tartib_raqami

sana = '2024-07-19'
print(f"{sana} sanasi haftaning {haftaning_tartib_raqami(sana)}-kuni.")
