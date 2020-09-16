temp = input("请输入带单位（C/F）的温度:")
if temp[-1] in ['c','C',]:
  f = eval(temp[0:-1])*1.8+32
  print('由摄氏度转换后得{:.2f}F'.format(f))
elif temp[-1] in ['f','F',]:
  c = (eval(temp[0:-1])-32)/1.8
  print('由华氏度转换后得{:.2f}C'.format(c))
else:
  print('输入格式错误！')
