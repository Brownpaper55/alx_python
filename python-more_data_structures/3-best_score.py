def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = max(a_dictionary, key=a_dictionary.get)
    f =('Best score:{}'.format(best_key))
    return f
    
