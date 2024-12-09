################################################################ Exercise 4
########################################### Task 2 - Scheduling
### Define Jobs in a list
Jobs = [
  {'job': 'A', 'time': 10, 'prio': 3},
  {'job': 'B', 'time': 6, 'prio': 5},
  {'job': 'C', 'time': 4, 'prio': 2},
  {'job': 'D', 'time': 2, 'prio': 1},
  {'job': 'E', 'time': 8, 'prio': 4}
]

### Sort Jobs by priority
def Priority(p):
    return p['prio']
Jobs.sort(reverse = True, key=Priority)

### Calculate retention times
totals = []
for i in range(len(Jobs)):
    Jobs[0].update({'total': Jobs[0]['time']})
    if i > 0:
        Jobs[i].update({'total': Jobs[i]['time']+Jobs[i-1]['total']})
    totals.append(Jobs[i].get('total'))

### Take mean of retention times
import statistics
print(statistics.mean(totals))












