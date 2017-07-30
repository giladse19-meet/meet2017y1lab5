def special_draw_2d(n, m, border, fill):
    n = int(n)
    m = int(m)
    print(border*(m + 2))
    for num in range(n):
        print(border + fill*m + border)
    print(border*(m + 2))
        
