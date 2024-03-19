WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/usr/bin/python3 -u
import sys
# print a contiguous integer sequence
start = sys.argv[1]
finish = sys.argv[2]

number = start
while int(number) <= int(finish):
    print(number)
    number = int(number) + 1  # increment number
