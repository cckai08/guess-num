#產生一個隨機整數
#讓使用者重複輸入數字
#猜對的話印出"終於猜對了"
#猜錯的話要告訴他大小
import random
r = random.randint(1, 100)
while True:
	num = input('請輸入數字')
	num = int(num)
	if num == r :
		print('你猜中了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
		
