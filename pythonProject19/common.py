def common_end(a,b):
    if(a[-1]==b[-1])or(a[0]==b[0]):
        return ("True")
    else:
        return ("False")
common_end(a=[1,2,3],b=[3,4,5])
common_end(a=[1,2,3],b=[4,2,3])
common_end(a=[5,6,7],b=[9,8,7])