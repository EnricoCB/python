def maior(*lst):
    for c in range (0, len(lst)):
        if c == 0:
            m = lst[c]
        else:
            if m < lst[c]:
                m = lst[c]  
    print(m)

maior(-4, -5)
maior(1, 5)