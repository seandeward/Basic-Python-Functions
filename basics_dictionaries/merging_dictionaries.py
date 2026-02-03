
#* simple version, second dictionary overwrites first:
def merge(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        merged_dict[key] = dict1[key]
    for key in dict2:
        merged_dict[key] = dict2[key]
        
    return merged_dict

#* if you want to take the highest of all values when merging the two dictionaries:
def merge(dict1, dict2):
    merged_dict = {}
    dicts = dict1, dict2
    
    for d in dicts:
        for key in d:
            value = d[key]
            if key in merged_dict:
                merged_value = merged_dict[key]
                if value > merged_value:
                    merged_dict[key] = value
            else:
                merged_dict[key] = value

    return merged_dict
