WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/usr/bin/python3 -u

status = 'off'
while status != 'on':
    print(f'status is {status}')
    if status == 'half on':
        status = 'on'
    else:
        status = 'half on'
