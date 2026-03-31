import math
ang =float(input('qual é o angulo:?'))
cose =  math.acosh (math.radians(ang) )
seno = math.asinh (math.radians(ang))
tang = math.atanh (math.radians(ang))
print(' o angulo foi de{} tem cos de{:2f}'.format(cose))
print(' o angulo foi de {} tem seno de {:2f}'.format(seno))
print(' o angulo foi de {} tem tang de {:2f}'.format(tang))