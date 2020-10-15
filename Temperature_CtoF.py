# 攝氏度C轉換成華氏F程式

print('攝氏(°C)轉換成華氏(°F)')
temp_c = input('請轉入攝氏溫度(°C)： ')
temp_c = float(temp_c)

temp_f = temp_c * 9 / 5 + 32

print('華氏溫度為(°F)： ', temp_f,'°F')