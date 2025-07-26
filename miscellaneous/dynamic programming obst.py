import sys

def optimal_bst(p, q, n):
    c = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    w = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    r = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        w[i][i] = q[i]
        c[i][i] = 0
        r[i][i] = 0

    for i in range(n):
        w[i][i + 1] = q[i] + q[i + 1] + p[i]
        c[i][i + 1] = w[i][i + 1]
        r[i][i + 1] = i + 1

    for m in range(2, n + 1):
        for i in range(n - m + 1):
            j = i + m
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            min_cost = sys.maxsize

            for k in range(r[i][j - 1], r[i + 1][j] + 1):
                cost = c[i][k - 1] + c[k][j]
                if cost < min_cost:
                    min_cost = cost
                    r[i][j] = k

            c[i][j] = w[i][j] + min_cost

    return c, w, r

def print_results(c, w, r, n):
    print("Cost Matrix (c):")
    for i in range(n + 1):
        print(c[i][:n + 1])
    print("\nWeight Matrix (w):")
    for i in range(n + 1):
        print(w[i][:n + 1])
    print("\nRoot Matrix (r):")
    for i in range(n + 1):
        print(r[i][:n + 1])

def get_user_input():
    n = int(input("Enter the number of keys: "))
    p = list(map(float, input(f"Enter {n} probabilities for keys (p): ").split()))
    q = list(map(float, input(f"Enter {n + 1} probabilities for gaps (q): ").split()))
    return p, q, n

if __name__ == "__main__":
    p, q, n = get_user_input()
    c, w, r = optimal_bst(p, q, n)
    print_results(c, w, r, n)
