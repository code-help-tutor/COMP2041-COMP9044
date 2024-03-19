WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/bin/dash

status=off
while test "$status" != on
do
    echo "status is $status"
    if test "$status" = "half on"
    then
        status="on"
    else
        status="half on"
    fi
done
