def findvalue(obj, key):
    length = len(key)
    for o in obj:
        try:
            if(o == key[0]):
                if(length > 0):
                    k = key[0+2:length]
                    if k == "":
                        return obj[o]
                    return findvalue(obj[o], k)
                else:
                    return obj[o]
            else:
                return "Key value pair not found!!"
        except Exception as e:
            return "Key value pair not found!!"
        
