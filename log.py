import os
import time

src = "C:/epshil/.logs/HILTest/build_14480.log"
dst = "C:/epshil/.logs/HILTest/out.log"

if os.path.exists(dst):
    os.remove(dst)

with open(src, "r") as fsrc:
    with open(dst, "w+") as fdst:
        for line in fsrc.readlines():
            fdst.write(line)
            # time.sleep(0.0000001)
