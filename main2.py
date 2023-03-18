import random

# 定義平仄規則
pingze = {
    "a": "平",
    "o": "平",
    "e": "平",
    "i": "仄",
    "u": "仄",
    "v": "仄"
}

# 定義押韻規則
yayun = {
    1: ["a", "ia", "ua"],
    2: ["o", "uo"],
    3: ["e", "ie"],
    4: ["i",],
    5: ["u",],
    6: ["v",],
}

# 讀取字典檔案
with open("dictionary.txt", encoding="utf-8") as f:
    words = f.read().split()
for i in range(4):
    try:
        if i % 2 == 0:
            # 前兩句為仄起，第三句為平起，第四句為仄起
            start = random.choice([w for w in words if pingze[w[0]] == "仄"])
            end = rhyme_words[i]
            # 第二個字要與最後一個字相反
            mid = random.choice([w for w in words if pingze[w[0]] != pingze[end[-1]]])
            sentence = start + mid + end
            poem.append(sentence)
        else:
            # 前兩句為平收，第三句為仄收，第四句為平收
            start = rhyme_words[i]
            end = random.choice([w for w in words if pingze[w[-1]] != pingze[start[0]]])
            # 第二個字要與最後一個字相反
            mid = random.choice([w for w in words if pingze[w[-1]] != pingze[end[-1]]])
            sentence = start + mid + end
            poem.append(sentence)
    except KeyError:
        # 如果詞語的平仄無法正確讀取，則跳過這個詞語，繼續生成詩句
        continue