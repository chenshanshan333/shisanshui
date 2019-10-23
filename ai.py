

import re

used = [0 for i in range(13)]
pai = [0 for i in range(14)]

ms1 = 0
ms2 = 0
ms3 = 0
duiyin = {0: '&', 1: '$', 2: '#', 3: '*'}

    for i in range(n):
        if i != 0:
            tt += ' '
        tt += duiyin[b[i]]
        if a[i] == 11:
            tt += 'J'
        elif a[i] == 12:
            tt += 'Q'
        elif a[i] == 13:
            tt += 'K'
        elif a[i] == 14:
            tt += 'A'
        else:
            tt += str(a[i])
    return tt

    for i in range(13):
        if used[i] == 1:
            a.append(pai[i])
            b.append(paise[i])
        elif used[i] == 0:
            c.append(pai[i])
            d.append(paise[i])
        else:
            e.append(pai[i])
            f.append(paise[i])

    for i in range(2):

    node = 1
    for i in range(4):
        if a[i] + 1 != a[i + 1] or b[i] != b[i + 1]:
            node = 0
    if 1 == node:
        return 170 + a[4] / 100
    if (a[0] == a[1] and a[1] == a[2] and a[2] == a[3]) or (a[3] == a[4] and a[1] == a[2] and a[2] == a[3]):
        return 120 + a[3] / 100

    if ((a[0] == a[1]) and (a[2] == a[3])) or ((a[0] == a[1]) and (a[4] == a[3])) or (a[2] == a[1] and a[4] == a[3]):
        return 30 + a[3] / 100 + a[1] / 10000

    for i in range(4):
        if a[i] == a[i + 1]:
            if i == 3:


def find2(pos, n):
    if pos == 13 and n == 0:
        score()
        return True
    if pos == 13:
        return False
    while used[pos] == 2:
        pos += 1

            score()
            return True
        if pos == 13:
            return False
    if n > 0:
        used[pos] = 1
        find2(pos + 1, n - 1)
        used[pos] = 0
    find2(pos + 1, n)

        for i in range(13):
            if used[i] == 2:
                a.append(pai[i])
                b.append(paise[i])

            return False
        find2(0, 3)
        return True
    if pos == 13:
        return False
    if n > 0:
        used[pos] = 2
        find1(pos + 1, n - 1)
        used[pos] = 0
    find1(pos + 1, n)


    maxnc = 0
    predeal(t)
    find1(0, 5)
    print(qans1)
    print(qans2)
    print(qans3)

idd = 0


def log_in():
    url = "https://api.shisanshui.rtxux.xyz/auth/login"
    headers = {
        'content-type': 'application/json'
    }

    payload = "{\"username\":\"hhh\",\"password\":\"0000\"}"

    response = requests.request("POST", url, data=payload, headers=headers)

    aaa = str(response.text)

    response = requests.request("POST", url, headers=headers)

    tok1 = str(response.text)


def submit():
    url = "https://api.shisanshui.rtxux.xyz/game/submit"
    headers = {
        'content-type': "application/json",

    }
    payload = "{\"id\":"
    payload = payload + str(idd)
    payload = payload + ",\"card\":[\""
    payload = payload + str(qans1)
    payload = payload + "\",\""
    payload = payload + str(qans2)
    payload = payload + "\",\""
    payload = payload + str(qans3)
    payload = payload + "\"]}"

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text


# a = [5,5,14]
# b=[0,1,2]
# c =[2,3,4,13,13]
# d = [2,3,3,2,1]
#
# print(score1(a,b),score2(c,d))
#
# a=[2,4,14]
# b=[2,3,2]
# c=[3,5,5,13,13]
# d=[3,0,1,2,1]
# print(score1(a,b),score2(c,d))

    ans = submit()
    if ans != anss:
        print(ans)
        print("error")
        print(qans1)
        print(qans2)
        print(qans3)
        break
    if ttt > 1000:
        print("finish")
        break
    ttt += 1
    print(ttt)
