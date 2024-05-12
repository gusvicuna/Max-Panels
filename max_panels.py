def max_paneles(a, b, x, y) -> int:
    panels_count_normal = (x // a) * (y // b)
    if a < b:
        panels_count_normal += (x // b) * ((y % b) // a)
    else:
        panels_count_normal += ((x % a) // b) * (y // a)
    panels_count_rotated = (x // b) * (y // a)
    if a < b:
        panels_count_rotated += (x // a) * ((y % a) // b)
    else:
        panels_count_rotated += ((x % b) // a) * (y // b)
    return max(panels_count_normal, panels_count_rotated)


print(max_paneles(a=1, b=2, x=3, y=5)) # 7
