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

# 檢查每個詞語是否符合規則
for w in words:
    # 如果詞語長度不是2或3，則不符合規則
    if len(w) != 2 and len(w) != 3:
        print(w + " 不符合規則：詞語長度不是1或2")
        continue
    # 如果詞語沒有拼音，則不符合規則
    if w[0] not in pingze.keys():
        print(w + " 不符合規則：詞語沒有拼音")
        continue

# 讀取字典檔案
with open("dictionary.txt", encoding="utf-8") as f:
    words = f.read().split()

# 過濾出符合五言絕句的詞語
words = [w for w in words if len(w) == 1 or len(w) == 2]

# 隨機選擇一個押韻類別
rhyme = random.choice(list(yayun.keys()))

# 隨機選擇四個押韻的詞語
rhyme_words = [w for w in words if w[-1] in yayun[rhyme]]
rhyme_words = random.sample(rhyme_words, k=4)

# 按照平仄規則和對偶法創造四句詩句
poem = []
for i in range(4):
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

# 輸出詩歌        
print("\n".join(poem))
