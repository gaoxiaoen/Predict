# -*- coding:utf-8 -*-
__author__ = 'Sean Gao'
from Common.DealExcel import CDealExcel
# iii 

if __name__ == "__main__":
    print("高小恩 Create")
    a = CDealExcel()
    a.GetExcelData("Data\LotteryPredict.xlsx")
    # a.GetExcelData("LotteryPredict.xlsx")
    a.Show()
