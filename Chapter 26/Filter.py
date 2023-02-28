#ilter() is a built-in function that allows us to process an iterable and extract those items that satisfy a given condition
lst=[1,2,3,4,5,6,7,8,9,10]
def is_gretter_5(num):
    return num>5
gr_than_5=list(filter(is_gretter_5,lst))
print(gr_than_5)