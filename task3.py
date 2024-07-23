from datetime import datetime

def check_date(sana1, sana2):
    sana1_obj = datetime.strptime(sana1, '%Y-%m-%d')
    sana2_obj = datetime.strptime(sana2, '%Y-%m-%d')
    
    farq = sana2_obj - sana1_obj
    kunlar_soni = farq.days
    
    return kunlar_soni

sana1 = '2024-07-01'
sana2 = '2024-07-19'

print(f"{sana1} va {sana2} orasida {check_date(sana1, sana2)} kun bor.")


from time import time
start = time()
rate_per_minute = 0.25

call_duration_seconds = 180
call_duration_minutes = call_duration_seconds / 60

call_cost = call_duration_minutes * rate_per_minute

print(f"Qo'ng'iroq davomiyligi edi {call_duration_minutes:.2f} minutes.")
print(f"Qo'ng'iroq narxi sum { call_cost:.2f}.")