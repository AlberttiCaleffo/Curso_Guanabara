metros = float(input('Digite um valor em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f'Os metros convertidos em cada medida são:\n'
f'{km:.3f}km\n'
f'{hm:.2f}hm\n'
f'{dam:.2f}dam\n'
f'{dm:.2f}dm\n'
f'{cm:.2f}cm\n'
f'{mm:.2f}mm')



