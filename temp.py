#攝氏Celsius轉換成華氏Fahrenheit  F=C*9/5+32
celsius=input('請輸入攝氏溫度')
celsius=int(celsius)
fahrenheit = celsius*9/5+3
print(type(fahrenheit))
print('華氏溫度為', fahrenheit)       #if we use , python don't care if fahrenheit is float or not
print('華氏溫度為'+str(fahrenheit))   #if we use + then if should be str + str