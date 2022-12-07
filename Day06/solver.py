data = [line.replace("\n", "") for line in open('input', 'r')][0]


def is_unique(s):
    unique = False
    if len(s) == len(set(s)):
        unique = True
    return unique


def detect_marker(d, marker_length):
    for i in range(0, len(d)-marker_length+1):
        potential_marker = d[i:i+marker_length]
        if is_unique(potential_marker):
            first_marker = i+marker_length
            return f"Start marker ({potential_marker}) at position {first_marker}"
            break


print(detect_marker(data, 4))
print(detect_marker(data, 14))