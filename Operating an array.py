def searchEle(a, x):
    return x in a
    # Code here


# fucntion must return true if
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    a.insert(yi, y)
    return True
    # Code here


# fucntion must return true if
# deletion is successful or else
# return false
def deleteEle(a, z):
    while z in a:
        a.remove(z)
    return True