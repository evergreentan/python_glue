# run launcher.do in the same folder
import subprocess
import platform

dofile = "launcher.do"
cmd_osx = ["stata-se", "do", dofile, "mpg", "weight", "foreign"]
pathStata = "C:\Program Files (x86)\Stata14\StataSE-64"
cmd_win = [pathStata, "do", dofile, "mpg", "weight", "foreign"]
subprocess.call(cmd_win) if platform.system() == 'Windows' else subprocess.call(cmd_osx) 
