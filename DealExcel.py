# -*- coding: utf-8 -*-
# 用来读取excel文件的数据
import xlrd
#Author=Sean Gao


class CDealExcel(object):
    def __init__(self):
        self.tBefore = {}
        self.tRedPoint = {}    #红球
        self.tBluePoint = {}   #篮球

    def Show(self):
        for key in self.tBefore.keys():
            print(" key = {key} value == {value}".format(key=key,value =str(self.tBefore[key])))
            print(" blue value = {value}".format(value=self.tBluePoint[key]))
            print(" red value = {value}".format(value = str(self.tRedPoint[key])))

    def GetExcelData(self,sName):
        data = None
        try:
            data = xlrd.open_workbook(sName)
        except:
            print("解析xlsx文件失败")

        table = data.sheets()[0]  # 通过索引顺序获取
        nrows = table.nrows
        ncols = table.ncols
        # 循环行列表数据
        for i in xrange(nrows):
            if i is 0:
                continue
            else:
                tRowValue = table.row_values(i)
                # print(tRowValue)
                if int(tRowValue[ncols-1]) in self.tBefore:
                    print "已经存在此值"
                    continue      
                iLastIdx = int(tRowValue[ncols-1])      
                self.tBefore[iLastIdx] = []                                 
                self.tRedPoint[iLastIdx] = []
                self.tBluePoint[iLastIdx] = None
                for j in xrange(ncols-1):
                    value = int(tRowValue[j])
                    self.tBefore[iLastIdx].append(value)
                    if j == ncols-2:
                        self.tBluePoint[iLastIdx] = value
                    else:
                        self.tRedPoint[iLastIdx].append(value)

