## Got to get the position(s) of a given substring in your string

def motif_count(test_str, test_sub):
    # if char in test starts with sub then add to list 'res'
    res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 
  
    ## Adding one to each int in list for question format
    new_res = [x+1 for x in res]
    print(*new_res, sep = ' ')

motif_count('', '')
