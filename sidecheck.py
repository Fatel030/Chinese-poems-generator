# 讀取字典檔案
with open("dictionary.txt", encoding="utf-8") as f:
    words = f.read().split()

# 定義平仄規則
pingze = {
    "a": "平",
    "o": "平",
    "e": "平",
    "i": "仄",
    "u": "仄",
    "v": "仄"
}

# 檢查每個詞語是否符合規則
for w in words:
    # 如果詞語長度不是2或3，則不符合規則
    if len(w) != 2 and len(w) != 3:
        print(w + " 不符合規則：詞語長度不是2或3")
        continue
    # 如果詞語沒有拼音，則不符合規則
    if w[0] not in pingze.keys():
        print(w + " 不符合規則：詞語沒有拼音")
        continue
