def solution(participant, completion):
    for p,c in zip(sorted(participant),sorted(completion+['z'*20])) :
        if p!=c : return p