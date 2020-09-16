import turtle as t
d = {1:'orange' ,2:'blue',3:'yellow',4:'red',5:'purple',6:'green'}  #使用dict词典语法定义各颜色对应的代号（其实使用list更简便）
t.setup(600,600)                                                    #设定画布窗口大小（窗口位置默认屏幕居中）
t.speed(300)                                                        #设定画笔速度:300
t.pensize(2)                                                        #设定画笔尺寸:2
t.bgcolor('black')                                                  #设定画布背景为:黑   
for i in range(50):                                                 #定义一个变量名为i，步长为1，循环序列从0-49的循环（以下循环体将循环五十次）
   for c in range(1,7):                                             #再镶嵌一个变量名为c，步长为1，循环序列从1-6的循环（实现六个颜色的循环）
    t.color(d[c])                                                   #设定画笔颜色值为变量c对应的词典中颜色代码
    t.fd(i*5+c+1)                                                   #设定每步线长
    t.right(59)                                                     #设定每步后旋转的角度
