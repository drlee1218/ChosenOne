from collections import defaultdict

def solution(genres, plays):
    total = defaultdict(int) #장르별 총 재생수
    songs = defaultdict(list) #장르별 노래
    
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        total[g] += p
        songs[g].append((p, i))
        
    genre_order = sorted(total, key=lambda x: total[x], reverse=True)
    
    answer = []
    
    for g in genre_order:
        
        songs[g].sort(key=lambda x: (-x[0], x[1]))
        
        for p, i in songs[g][:2]:
            answer.append(i)
    
    return answer