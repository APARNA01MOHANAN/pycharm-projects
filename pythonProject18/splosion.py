def string_bits(str):
    result=""
    for i in range(0,len(str),2):
        result=result+str[i]
    return result
string_bits("hello")
string_bits("hi")
string_bits("heeololeo")
