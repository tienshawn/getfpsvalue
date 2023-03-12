import re
import pandas as pd

def getfps(input_file, output_file):
    with open(input_file, "r") as f:
        log = f.read()

    fps_values = []
    for line in log.splitlines():
        fps_match = re.search(r"fps=([\d.]+)", line)
        if "fps" in line:
            fps = float(line.split('fps=')[1].split()[0])
            fps_values.append(fps)


    df = pd.DataFrame(fps_values, columns=["FPS value"])
    df.to_excel(output_file, index=False)

input_file = "./streamlog1.log"
output_file = "./output1.xlsx"
getfps(input_file, output_file)

