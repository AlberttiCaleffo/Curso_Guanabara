metros = float(input('Digite os metros a serem convertidos: '))

print(f'''Os metros convertidos em:
Km: {metros / 1000:.3f}
hm: {metros / 100:.2f}
dam: {metros / 10:.1f}
dm: {int(metros * 10)}
cm: {int(metros * 100)}
mm: {int(metros * 1000)}''')