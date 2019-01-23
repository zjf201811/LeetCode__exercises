#Author:ZJF
def accm(chars):
    return "-".join(c.upper()+c.lower()*i for i,c in enumerate(chars))
print(accm("sdrfs"))