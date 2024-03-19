WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/usr/bin/python3 -u

import subprocess

a = subprocess.run(['printf', 'hi'], text=True, stdout=subprocess.PIPE).stdout
print(' '.join(a.strip().split()))
