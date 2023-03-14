import re
import pandas as pd
import subprocess

def getlogvalues(output_file):
    command = "cat streamlog.log"
    output = subprocess.check_output(['/bin/bash', '-c', command])
    output2 = output.decode().split("\n")
    fps_values = []
    bitrate_values = []
    for line in output2:
        if "fps" and "bitrate" in line:
            fps = float(line.split('fps=')[1].split()[0])
            fps_values.append(fps)

            bit = str(line.split('bitrate')[1].split()[0])
            bitrate = ''.join(letter for letter in bit if letter.isnumeric() or letter == '.')
            bitrate_values.append(float(bitrate))

    data = {'FPS':fps_values, 
            'Bitrate':bitrate_values}
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

output_file = "./logpy1.xlsx"
getlogvalues(output_file)
