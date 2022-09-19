#!/usr/bin/env python3

import VisualLog.ShellCmd as ShellCmd
import _thread
from time import sleep

shell = ShellCmd.Shell()

print(shell.run('adb devices'))
print(shell.run('adb shell ls'))

# _thread.start_new_thread(shell.run, ('adb logcat',))
# sleep(2)
# shell.stop()
# sleep(2)

print("----------------------")
def callback(line):
    print(line)
    if "sys" in line:
        return True
    else:
        return False

print(shell.reset(callback=callback).run('top'))
