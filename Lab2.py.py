# Converted Moore Machine Simulator

moore = {
    'A/A': {'0': 'A/A', '1': 'B/B'},
    'B/B': {'0': 'C/A', '1': 'D/B'},
    'C/A': {'0': 'D/C', '1': 'B/B'},
    'C/C': {'0': 'D/C', '1': 'B/B'},
    'D/B': {'0': 'B/B', '1': 'C/C'},
    'D/C': {'0': 'B/B', '1': 'C/C'},
    'E/C': {'0': 'D/C', '1': 'E/C'}
}

outputs = {
    'A/A': 'A', 'B/B': 'B', 'C/A': 'A', 'C/C': 'C',
    'D/B': 'B', 'D/C': 'C', 'E/C': 'C'
}

def run(input_string):
    state = 'A/A'
    result = []
    for ch in input_string:
        state = moore[state][ch]
        result.append(outputs[state])
    return ''.join(result)

tests = ["00110", "11001", "1010110", "101111"]

for t in tests:
    print(t, "→", run(t))
