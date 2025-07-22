#exp1
# n = 3
# m = 2
# subjects = ['yuwen', 'shuxue']
# score_dict = {'fangfang': [95, 90], 'xiaohua': [88, 98], 'minmin': [100, 82]}
# subject = 'yingyu'
def get_data():
    n, m = map(int, input().strip().split())
    subjects = []
    subjects.extend(input().strip().split())
    score_dict = {}
    i = 0
    while i < n + 1:
        if i == n:
            subject = input().strip()
        else:
            curr = input().strip().split()
            score_dict[curr[0]] = [int(score) for score in curr[1:]]
        i += 1
    return subjects, subject, score_dict

def sort_score(subjects, subject, score_dict):
    if subject in subjects:
        idx = subjects.index(subject)
        score_list = sorted(score_dict.items(), key = lambda x: (-x[1][idx],x[0][0]))
    else:
        score_list = sorted(score_dict.items(), key = lambda x: (-sum(x[1]),x[0][0]))
    return score_list

subjects, subject, score_dict = get_data()
print(f'subjects:{subjects}, subject:{subject}, score_dict{score_dict}')

score_list = sort_score(subjects, subject, score_dict)
print(" ".join([person[0] for person in score_list]))
