alt = int(input('Enter altitude: - '))
if alt <= 1000:
    print('Safe to land')
elif 1000 < alt < 5000:
    print('Come down to 1000ft')
else:
    print('Go around and try later')
