from datetime import datetime, timedelta


def solution(lines):
    transactions = []
    events = set()

    for line in lines:
        s = line[:23]
        t = float(line[24:][:-1])

        end = datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")
        delta = timedelta(seconds=t)
        start = end - delta + timedelta(milliseconds=1)
        transactions.append((start, end))
        events.add(start)
        events.add(end)

    max_count = 0
    transactions = list(sorted(transactions))
    events = list(sorted(events))
    for event in events:
        event_start = event
        event_end = event + timedelta(seconds=1)

        count = 0
        for transaction in transactions:
            if event_start <= transaction[0] < event_end or event_start <= transaction[1] < event_end:
                count += 1
            elif transaction[0] <= event_start and event_end <= transaction[1]:
                count += 1

        max_count = max(max_count, count)

    return max_count
