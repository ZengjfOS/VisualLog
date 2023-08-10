#!/usr/bin/env python3

import os
from VisualLog.LogParser import logFileParser

class SecImageFile:

    """
    QCOM签名log

    @data(default/SecImage_log.txt): 环境光数据
    """

    def __init__(self, kwargs):

        # 对比机
        data = kwargs["data"]

        self.labels = ["Light Sensor"]
        self.customData = {"xlabel": "X", "ylabel": "Y"}
        self.outputLineInfos = logFileParser(
            data,
            # 09-19 14:19:17.183  1027  1110 I DisplayPowerController[0]: No longer ignoring proximity [1]
            # Signed image is stored at /home/zengjf/zengjf/android/6552/Divar.LA.2.0/common/sectools/divar/xbl/xbl.elf
            # Processing 1/25: /home/zengjf/zengjf/android/6552/BOOT.XF.4.1/boot_images/QcomPkg/SocPkg/DivarPkg/Bin/LAA/RELEASE/xbl.elf
            r'(Signed image is stored at (.*)|Processing \d*/\d*: (.*))',
            callback=self.dataLineCallback,
            fileEncode="ISO-8859-1"
        )

        print("--------------------------------------")
        count = 0
        maxOutputFileLength = 0
        for lineInfo in self.outputLineInfos:
            count += 1

            print(("%02d" % (count)) + ". " + lineInfo[0] + " --> " + lineInfo[1])

            if len(lineInfo[1]) > maxOutputFileLength:
                maxOutputFileLength = len(lineInfo[1]) + 2      # 2是为了后面加注释对其

        print("--------------------------------------")
        count = 0
        for lineInfo in self.outputLineInfos:
            count += 1

            print(("%02d" % (count)) + ". " + lineInfo[1].ljust(maxOutputFileLength) + " --> " + lineInfo[0])

        print("--------------------------------------")
        count = 0
        print("echo \"start to replace with signed file, code export by tool from SecImage_log.txt\"")
        for lineInfo in self.outputLineInfos:
            count += 1

            if os.path.basename(lineInfo[1]) in ["a610_zap.elf", "abl.elf", "ipa_fws.elf"]:
                print(("%02d" % (count)) + ". # CpFile " + lineInfo[1].ljust(maxOutputFileLength - 2) + " ${SRC_DIR}/" + lineInfo[0])
            else:
                print(("%02d" % (count)) + ". CpFile " + lineInfo[1].ljust(maxOutputFileLength) + " ${SRC_DIR}/" + lineInfo[0])
        print("echo \"replaced with signed file\"")

    def dataLineCallback(self, lineInfo, col = 1):
        print(lineInfo)

        if lineInfo[0].startswith("Signed image is"):
            self.currentInfo.append(lineInfo[1].split("/sectools/")[1])
            return self.currentInfo

        if lineInfo[0].startswith("Processing "):
            self.currentInfo = []
            self.currentInfo.append(lineInfo[2].split("/6552/")[1])
            return None

        return None

if __name__ == "__main__" :
    SecImageFile({"data": "default/SecImage_log.txt"})
