WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/bin/dash
# print a contiguous integer sequence
start=$1
finish=$2

number=$start
while [ $number -le $finish ]
do
    echo $number
    number=$((number + 1))  # increment number
done
