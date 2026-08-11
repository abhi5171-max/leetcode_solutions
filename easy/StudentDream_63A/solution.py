def possible(g, b):
    return g - 1 <= b <= 2 * g + 2


gl, gr = map(int, input().split())
bl, br = map(int, input().split())

# Boy is on the left:
# Girl's left hand touches Boy's right hand
if possible(gl, br):
    print("YES")

# Boy is on the right:
# Girl's right hand touches Boy's left hand
elif possible(gr, bl):
    print("YES")

else:
    print("NO")