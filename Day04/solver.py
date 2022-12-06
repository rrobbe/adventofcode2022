data = [line.strip() for line in open('input', 'r')]

overlaps_1 = 0
overlaps_2 = 0

for pair in data:
    p1, p2 = pair.split(",")
    p1_s, p1_e = p1.split("-")
    p2_s, p2_e = p2.split("-")
    p1_r = [*range(int(p1_s), int(p1_e)+1, 1)]
    p2_r = [*range(int(p2_s), int(p2_e)+1, 1)]
    check1 = (len(set(p1_r).intersection(set(p2_r))))/len(p1_r)*100
    check2 = (len(set(p2_r).intersection(set(p1_r))))/len(p2_r)*100
    if int(check1) == 100 or int(check2) == 100:
        overlaps_1 += 1
    if int(check1) != 0 or int(check2) != 0:
        overlaps_2 += 1

print(f"overlap 1: {overlaps_1}")
print(f"overlap 2: {overlaps_2}")