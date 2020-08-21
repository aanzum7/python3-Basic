percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

resps=[]
for item in percent_rain:
    if item > 90:
        resps.append("Bring an umbrella.")
    elif item > 80:
        resps.append("Good for the flowers")
    elif item > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")
print(resps)



