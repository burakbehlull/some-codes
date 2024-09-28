# pip install psutil
import psutil
battery = psutil.sensors_battery()

print("PC Şarjı: ", battery.percent)