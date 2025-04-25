y=open("output.txt").read()
y_odd = y[0:32]
y_even = y[32:64]
x = [''] * 64
for i in range(64):
    if i % 2 == 0:
        # positions paires dans x ← deuxième moitié de y
        x[i] = y_even[i//2]
    else:
        # positions impaires dans x ← première moitié de y
        x[i] = y_odd[i//2]
x = "".join(x)

f = [''] * 64
for b in range(8):
    block = x[b*8:(b+1)*8]            # bloc b
    start = 56 + b                    # indice de départ dans f
    for j in range(8):
        idx = start - 8*j             # positions 56+b, 48+b, …, 0+b
        f[idx] = block[j]
original = "".join(f)

print(original)
