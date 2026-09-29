# validator.py
# handles condition checks for income, percentage, caste and stream

def is_eligible(u_inc, u_pct, u_cat, u_stream, item):
    # income test
    if u_inc > item["max_inc"]:
        return False
        
    # marks check
    if u_pct < item["min_pct"]:
        return False
        
    # category match
    cat_match = False
    for c in item["cat"]:
        if c.lower() == "all" or c.lower() == u_cat.lower():
            cat_match = True
            break
    if cat_match == False:
        return False
        
    # stream check
    stream_match = False
    for s in item["stream"]:
        if s.lower() == "all" or s.lower() == u_stream.lower():
            stream_match = True
            break
    if stream_match == False:
        return False
        
    return True


def filter_scholarships(u_inc, u_pct, u_cat, u_stream, data_list):
    matched_results = []
    for item in data_list:
        if is_eligible(u_inc, u_pct, u_cat, u_stream, item):
            matched_results.append(item)
    return matched_results
