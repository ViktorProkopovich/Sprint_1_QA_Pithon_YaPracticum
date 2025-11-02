times_list = '1h 45m,360s,25m,30m 120s,2h 60s'
total_min = 0

for times in times_list.split(','):
    times = times.replace(' ', ',')
    times = times.split(',')

    for time in times:
        if 'h' in time:
            hours = int(time.replace('h', ''))
            total_min += hours * 60
        elif 'm' in time:
            minutes = int(time.replace('m', ''))
            total_min += minutes
        elif 's' in time:
            seconds = int(time.replace('s', ''))
            total_min += seconds // 60
print(total_min)