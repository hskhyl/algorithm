def solution(genres, plays):
    temp_1dict = dict()
    temp_2dict = dict()
    best_album = []
    for index, (g, p) in enumerate(zip(genres, plays)):
        temp_1dict.setdefault(g, 0)
        temp_1dict[g] += p
        
        temp_2dict.setdefault(g, [])
        temp_2dict[g].append([index, p])


    sorted_d = dict(sorted(temp_1dict.items(), key = lambda x: x[1], reverse = True))
    sort = list(sorted_d.keys())

    for gen in sort:
        temp_2dict[gen].sort(key = lambda x: x[-1], reverse = True)

    for gen in sort:
        for index in temp_2dict[gen][:2]:
            best_album.append(index[0])
            
    return best_album