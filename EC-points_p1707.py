from tinyec.ec import SubGroup, Curve


g = (15, 13)
g = (5, 9)
field = SubGroup(p=17, g=g, n=18, h=1)
curve = Curve(a=0, b=7, field=field, name='p1707')
print('curve:', curve)

for k in range(0, 25):
    p = k * curve.g
    print(f"{k} * G = ({p.x}, {p.y})")
