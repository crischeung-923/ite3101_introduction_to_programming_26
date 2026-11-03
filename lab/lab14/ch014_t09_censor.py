def censor(text:str, word:str)->str:
    words = text.split()
    result = []
    for w in words:
        if w == word:
            result.append("*" * len(word))
        else:
            result.append(w)
    return " ".join(result)