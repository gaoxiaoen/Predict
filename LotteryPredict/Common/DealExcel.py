# -*- coding: utf-8 -*-
# 用来读取excel文件的数据
import xlrd
import os
import pandas as pd
#Author=Sean Gao
# 处理excel表
class CDealExcel(object):
    def __init__(self):
        self.tRedPoint = {}    #红球  map<日期：列表>
        self.tBluePoint = {}   #篮球 map<日期：列表>
        self.tRow = {}
        self.tBefore={}   # 之前的数据

    def Show(self):
        pass
        # for key in self.tBefore.keys():
        #     print(" key = {key} value == {value}".format(key=key,value =str(self.tBefore[key])))
        #     print(" blue value = {value}".format(value=self.tBluePoint[key]))
        #     print(" red value = {value}".format(value = str(self.tRedPoint[key])))

    def GetExcelData(self,sName):
        print os.getcwd()
        data = None
        try:
            data = xlrd.open_workbook(sName)
        except:
            print("解析xlsx文件失败")

        if data is None:
            print("文件不存在，路径为" + sName)
            exit(0)

        table = data.sheets()[0]  # 通过索引顺序获取 获取第一个sheet的值
        nrows = table.nrows
        ncols = table.ncols
        # 循环行列表数据
        for i in xrange(nrows):
            if i is 0:
                continue
            else:
                tRowValue = table.row_values(i)
                # print(tRowValue)
                if int(tRowValue[ncols-1]) in self.tBefore:  #清除重复的数据结果
                    print "已经存在此值"
                    continue      
                iLastIdx = int(tRowValue[ncols-1])      
                self.tBefore[iLastIdx] = []                                 
                self.tRedPoint[iLastIdx] = []
                for j in xrange(ncols-1):
                    value = int(tRowValue[j])
                    self.tBefore[iLastIdx].append(value)
                    if j == ncols-2:
                        self.tBluePoint[iLastIdx] = value
                    else:
                        self.tRedPoint[iLastIdx].append(value)
    # 通过pandas处理excels 数据
    # return list[红球数据，篮球数据，列名]
    def getPandasData(self,sName):
        # pd.read_excel(sName)
        print "this is a begin。。。"
        pex = pd.read_excel(sName,sheet_name=0)
        # pex = pd.read_excel(sName)
        loaddata = pd.DataFrame(pex)
        rows = loaddata._info_axis._values
        self.tRow = rows   # 获取列名字
        for values in loaddata.iterrows():
            print values[1]
            date = values[1]['date']
            blue = values[1]['blue']
            self.tRedPoint[date]= list()
            red1 = values[1]['red1']
            self.tRedPoint[date].append(red1)
            red2 = values[1]['red2']
            self.tRedPoint[date].append(red2)
            red3 = values[1]['red3']
            self.tRedPoint[date].append(red3)
            red4 = values[1]['red4']
            self.tRedPoint[date].append(red4)
            red5 = values[1]['red5']
            self.tRedPoint[date].append(red5)
            red6 = values[1]['red6']
            self.tRedPoint[date].append(red6)
            self.tBluePoint[date] = blue
        return [self.tRedPoint,self.tBluePoint,self.tRow]