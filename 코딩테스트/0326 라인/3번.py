def solution(num_teams, remote_tasks, office_tasks, employees):
    isRemote = [1 for _ in range(len(employees)+1)]
    teams = [[] for _ in range(num_teams + 1)]
    for index,employee in enumerate(employees):
        index += 1
        l = employee.split()
        teams[int(l[0])].append(index)
        for work in l[1:]:
            if work in office_tasks : isRemote[index] = 0 ; break
    for team in teams[1:]:
        everyone = True
        for member in team:
            if not isRemote[member]: everyone = False;break
        if everyone : isRemote[sorted(team)[0]] = 0
    return [i for i,v in enumerate(isRemote) if i and v]          