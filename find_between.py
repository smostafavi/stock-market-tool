
def find_between(begin_string, end_string, string):
    begin_pos = string.index(begin_string) + len(begin_string)
    reduce_str = string[(string.index(begin_string) + len(begin_string)):]
    end_pos = reduce_str.index(end_string)
    return reduce_str[:end_pos]
    
