#!/usr/bin/env python3

import datetime
from VisualLog.LogParser import logFileParser
from VisualLog.MatplotlibZoom import Show

class AmbienteLight:

    """
    可视化两个版本的Android bootprof

    @data(default/AmbienteLight.curf): 环境光数据
    """

    def __init__(self, kwargs):

        # 对比机
        data = kwargs["data"]

        self.labels = ["Light Sensor"]
        self.customData = {"xlabel": "X", "ylabel": "Y"}
        self.lineInfos = logFileParser(
            data,
            # 09-09 18:24:12.680436   571   628 I Light   : event->word[0]=400,  event->word[1]=0,event->word[2]=0
            r'(\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+Light\s*:\s.*=(\d*),\s*.*=(\d*),\s*.*=(\d*)',
            callback=self.dateLineCallback
        )

        # for lineInfo in self.lineInfos:
        #     print(lineInfo)

        Show(callback=self.defaultShowCallback, rows = 1, cols = 1)

    def defaultShowCallback(self, fig, index):
        print(index)

        ax = fig.get_axes()[index]
        ax.set_xlabel(self.customData["xlabel"])
        ax.set_ylabel(self.customData["ylabel"])

        # for i in range(1, len(self.lineInfos[0])):
        ax.plot([s[0] for s in self.lineInfos], [s[1] for s in self.lineInfos])

        ax.legend()

    def dateLineCallback(self, lineInfo, col = 1):
        lineInfoFixed = []
        today_year = str(datetime.date.today().year)
        # print(lineInfo)

        for index in range(len(lineInfo)):
            if index == 0:
                continue

            if index == col:
                timeString = today_year + "-" + lineInfo[0] + " " + lineInfo[index].split(".")[0]
                currentDate = datetime.datetime.strptime(timeString.split(".")[0], "%Y-%m-%d %H:%M:%S")
                lineInfoFixed.append(currentDate)
                continue

            lineInfoFixed.append(int(lineInfo[index]))
        
        return lineInfoFixed
    
if __name__ == "__main__" :
    AmbienteLight({"data": "default/AmbienteLight.curf"})
