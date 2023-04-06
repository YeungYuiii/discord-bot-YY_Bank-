import random

check_list = ["紅色", "綠色", "紫色", "灰色", "白色", "藍色", "黃色", "黑色", "緣色", "青色", "彩色", "色色", "無色"]
color_list = ['blurple', 'grey', 'gray', 'green', 'red']

color = random.sample(color_list, k=5)
print(color[0])
