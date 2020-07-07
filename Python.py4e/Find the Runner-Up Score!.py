if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

Scores = set(arr)
Scores.remove(max(Scores))
print(max(Scores))
