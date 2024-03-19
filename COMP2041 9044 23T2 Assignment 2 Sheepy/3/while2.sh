WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/bin/dash

x='###'
while test $x != '########'
do
    y='#'
    while test $y != $x
    do
        echo $y
        y="${y}#"
    done
    x="${x}#"
done
