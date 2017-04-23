# -*-coding:utf-8 -*-
__author__ = 'Sean Gao'

def GiveMySaveMoney(savemoney,saveyear,rate):
	year = 1
	while year <= saveyear:
		print "开始第{year}年的！".format(year=year)
		savemoney = savemoney*rate + savemoney
		print "第{year}年可以取{money}圆".format(year=year,money=savemoney)
		year = year + 1 
	print(savemoney) 
	return savemoney

if __name__ == "__main__":
    print("高小恩 Create")
    savemoney = 20000
    rate = 0.2
    saveyear = 5   #存款的年数
    year = 1    #年数

    MyTotalMoney = GiveMySaveMoney(savemoney,saveyear,rate)
    print "可以从银行总共可以取{money}钱".format(money=MyTotalMoney)

    
    