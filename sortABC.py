import math, sys

N, Q = map(int, input().split(" "))
alpha = [chr(i) for i in range(65, 65+N)]

def ret_ans(a, b):
    print("? {} {}".format(a, b))
    sys.stdout.flush()
    return input()

if N == 5:
    ans = ret_ans("A", "B")
    if ans == ">":
        ab = ["B", "A"]
    else:
        ab = ["A", "B"]
    ans = ret_ans("C", "D")
    if ans == ">":
        cd = ["D", "C"]
    else:
        cd = ["C", "D"]
    ans = ret_ans(ab[0], cd[0])
    if ans == ">":
        mom = ab
        ab = cd
        cd = mom
    ac = [ab[0], cd[0]]
    ans = ret_ans(cd[0], "E")
    if ans == "<":
        ans = ret_ans(cd[1], "E")
        if ans == "<":
            cd.insert(2, "E")
        else:
            cd.insert(1, "E")
        cde = cd
        ans = ret_ans(cde[1], ab[1])
        if ans == "<":
            ans = ret_ans(cde[2], ab[1])
            if ans == "<":
                answer = [ac[0], ac[1], cde[1], cde[2], ab[1]]
            else:
                answer = [ac[0], ac[1], cde[1], ab[1], cde[2]]
        else:
            ans = ret_ans(cde[0], ab[1])
            if ans == "<":
                answer = [ac[0], ac[1], ab[1], cde[1], cde[2]]
            else:
                answer = [ac[0], ab[1], ac[1], cde[1], cde[2]]
    else:
        cd.insert(0, "E")
        cde = cd
        ans = ret_ans(ac[0], cde[0])
        if ans == "<":
            ans = ret_ans(cde[1], ab[1])
            if ans == "<":
                ans = ret_ans(cde[2], ab[1])
                if ans == "<":
                    answer = [ac[0], cde[0], cde[1], cde[2], ab[1]]
                else:
                    answer = [ac[0], cde[0], cde[1], ab[1], cde[2]]
            else:
                ans = ret_ans(cde[0], ab[1])
                if ans == "<":
                    answer = [ac[0], cde[0], ab[1], cde[1], cde[2]]
                else:
                    answer = [ac[0], ab[1], cde[0], cde[1], cde[2]]
        else:
            cde.insert(1, ac[0])
            eacd = cde
            ans = ret_ans(eacd[2], ab[1])
            if ans == "<":
                ans = ret_ans(eacd[3], ab[1])
                if ans == "<":
                    answer = [eacd[0], eacd[1], eacd[2], eacd[3], ab[1]]
                else:
                    answer = [eacd[0], eacd[1], eacd[2], ab[1], eacd[3]]
            else:
                answer = [eacd[0], eacd[1], ab[1], eacd[2], eacd[3]]

else:
    beta =["A"]
    for i in range(1,N):
        num = i
        zero = 0
        for _ in range(math.floor(i/2)+1):
            target = zero + math.floor(num/2)
            ans = ret_ans(beta[target], alpha[i])
            if ans == ">":
                num = target - zero
                if num == 0:
                    pos = target
                    break
            else:
                num -= (target - zero + 1)
                zero = target + 1
                if num == 0:
                    pos = target + 1
                    break
        beta.insert(pos, alpha[i])
    answer = beta
print("! {}".format("".join(answer)))
sys.stdout.flush()
