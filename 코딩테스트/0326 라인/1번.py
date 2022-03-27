def solution(logs):
    ret = 0
    for log in logs:
        if len(log)>100 :ret += 1 ; continue

        sp = log.split(" ")
        
        if len(sp) != 12 : ret += 1 ; continue
        
        if sp[0] != 'team_name' : ret += 1 ; continue
        if sp[1] != ':' : ret += 1 ; continue
        if not sp[2].isalpha() : ret += 1 ; continue

        if sp[3] != 'application_name' : ret += 1 ; continue
        if sp[4] != ':' : ret += 1 ; continue
        if not sp[5].isalpha() : ret += 1 ; continue

        if sp[6] != 'error_level' : ret += 1 ; continue
        if sp[7] != ':' : ret += 1 ; continue
        if not sp[8].isalpha() : ret += 1 ; continue

        if sp[9] != 'message' : ret += 1 ; continue
        if sp[10] != ':' : ret += 1 ; continue
        if not sp[11].isalpha() : ret += 1 ; continue
    return ret

