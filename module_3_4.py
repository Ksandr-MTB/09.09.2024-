def single_root_words(root_words, *other_words):
    same_words=[]
    for i in range(len(other_words)):
        if root_words.lower() in other_words[i].lower():
            same_words.append(other_words[i])
        elif other_words[i].lower() in root_words.lower():
            same_words.append(other_words[i])
    print(same_words)


single_root_words('вел', 'Велосипед','велосипедист','велобег','волейбол','велик',)
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')







# print('вел' in 'велосипед')