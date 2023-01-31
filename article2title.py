def article2title(article):

    # если вся статья пустая - вернем пустую
    if len(article) == 0:
        return article

    # если первое слово больше 25 символов то возвратим пустую строку
    if len(article.split()[0]) > 25:
        return ""
    
    # если вся статья меньше или равна 25 символов то возвратим статью
    if len(article) <= 25:
        return article
    
    words = article.split()
    title = words[0]
    words.pop(0)
    break_out_flag = False
    for word in words:
        if len(title + " " + word) <= 22:
            title = title + " " + word
        else:
            break_out_flag = True  
        if break_out_flag:
            break
    title = title + "..."
    return title
