import difflib
import jieba
def load_english_dict(file):
    with open(file, 'r', encoding='utf-8') as f:
        return [line.strip().lower() for line in f.readlines()]
common_typos_zh = {
    "蘋裡": "蘋果",
    "覺得的": "覺得",
    "我們們": "我們",
    "歡迎光臨嗎": "歡迎光臨",
}

def is_english_word(word):
    return all(ord(c) < 128 and c.isalpha() for c in word)

def correct_english(word, dictionary):
    matches = difflib.get_close_matches(word.lower(), dictionary, n=1, cutoff=0.😎
    return matches[0] if matches else word

def correct_chinese(sentence):
    words = jieba.lcut(sentence)
    corrected = []
    for word in words:
        if word in common_typos_zh:
            corrected.append(common_typos_zh[word])
        else:
            corrected.append(word)
    return ''.join(corrected)

def correct_sentence(text, english_dict):
    if all(ord(c) < 128 for c in text):  # 純英文
        words = text.strip().split()
        corrected = [correct_english(word, english_dict) for word in words]
        return ' '.join(corrected)
    else:
        return correct_chinese(text)

if __name__ == "__main__":
    english_dict = load_english_dict("dictionary.txt")
    print("請輸入一段中文或英文句子：")
    user_input = input()
    corrected = correct_sentence(user_input, english_dict)
    print("\n✅ 修正後句子：")
    print(corrected)
