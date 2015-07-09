



def first (word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def pali(word):
    if len(word)<=1:
       print 'it is a palindrome'
    elif first(word)==last(word):
       return pali(middle(word))
       print 'it is a palindrome'
    else:
       print 'it is not a palindrome'    
pali('malayalam')
