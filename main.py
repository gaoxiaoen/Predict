# -*- coding:utf-8 -*-
__author__ = 'Sean Gao'
from DealExcel import CDealExcel


if __name__ == "__main__":
    print("高小恩 Create")
    a = CDealExcel()
    a.GetExcelData("LotteryPredict.xlsx")
    a.Show()
