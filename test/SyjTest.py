#-*-coding:utf-8 -*-
print ("hello world")
def mytotalmoney(savemoney,saveyear,rate):
	year=1
	while year<=saveyear:
		savemoney=savemoney*rate+savemoney
		print("第{year}年").format(year=year)
		print ("可以取{savemoney}元").format(savemoney=savemoney)
		year+=1
		print(savemoney)
	return savemoney



if __name__ == "__main__":
	savemoney = 20000
	saveyear = 5
	rate = 0.2
	year = 1
	total=mytotalmoney(savemoney,saveyear,rate)
	print("能从银行领取{money}元").format(money=total)
	while year <=saveyear:
		savemoney=savemoney*rate+savemoney
		# print("第{year}年").format(year=year)
		# print("可以取{savemoney}元").format(savemoney=savemoney)
		year = year + 1


