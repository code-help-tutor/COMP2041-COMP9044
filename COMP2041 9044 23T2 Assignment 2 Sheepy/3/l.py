WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/usr/bin/python3 -u

import subprocess
import sys

subprocess.run(['ls', '-las'] + sys.argv[1:])
