import os 
import pickle

filename = 'score.bin'


def input_scores():
    scores = []
    i = 0
    while True:
        n = int(input(f'#{i+1}? '))
        if n < 0:
            break
        scores.append(n)
        i += 1
    return scores    
    
def get_average(scores):
    total = 0
    for i in scores:
        total += i
    avg = total / len(scores)
    return avg

def show_scores(scores):
    for n in scores:
        print(n, end=' ')
    print()


def save_score(score, mean):
    with open(filename,'wb') as file:
        pickle.dump(score,file)
        pickle.dump(mean, file)

def load_score():
    with open(filename, 'rb') as file:
        s = pickle.load(file)
        mean = pickle.load(file)
    return s, mean


if os.path.exists(filename):
    scores, mean = load_score()
    print('[파일 읽기]')
    print('\n[점수 출력]')
    print('\n개인점수: ', end='')
    show_scores(scores)
    print(f'평균: {mean:.1f}')
else:
    print('[점수 입력]')
    scores = input_scores()
    mean = get_average(scores)
    print('\n[점수 출력]')
    print('\n개인점수: ', end='')
    show_scores(scores)
    print(f'평균: {mean:.1f}')
    save_score(scores, mean)