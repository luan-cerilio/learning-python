import math
num = int(input('Digite um angulo: '))
angle = math.radians(num)
sen = math.sin(angle)
cos = math.cos(angle)
tg = math.tan(angle)
print('sen {} = {:.4f}\ncos {} = {:.4f}\ntan {} = {:.4f}'.format(num, sen, num, cos, num, tg))