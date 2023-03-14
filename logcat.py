import re
import pandas as pd
import subprocess

def connect_get_namespaced_pod_exec(output_file):
    command = "cat streamlog.log"
    output = subprocess.check_output(['/bin/bash', '-c', command])
    output2 = output.decode().split("\n")
    fps_values = []
    for line in output2:
        fps_match = re.search(r"fps=([\d.]+)", line)
        if "fps" in line:
            fps = float(line.split('fps=')[1].split()[0])
            fps_values.append(fps)
    
    df = pd.DataFrame(fps_values, columns=["FPS value"])
    df.to_excel(output_file, index=False)

output_file = "/home/dell/logpy.xlsx"
connect_get_namespaced_pod_exec(output_file)
