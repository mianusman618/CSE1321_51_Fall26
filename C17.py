phone_battery = 50.0
if phone_battery == 100:
    print("Your phone is fully charged")
elif phone_battery >= 75:
    print("Your phone battery is almost full")
elif phone_battery >= 50:
    print("Your phone battery is about half-charged")
elif phone_battery >= 25:
    print("Your phone battery is low")
else:
    print("Your phone battery is critical, please charge!")