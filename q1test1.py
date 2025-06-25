# 7 points
# Ecrivez une fonction nommée compose() qui prend un nombre variable
# de fonctions en paramètres. elle renverra une fonction
# équivalente à la composition des fonctions reçues en paramètres.
#
#     compose(sin, cos, pow)(x, y) <=> sin(cos(pow(x, y)))
#


def compose(*funs):
    funs = list(funs)
    def compute(x,y):
        final = funs[-1](x,y) 
        funs.remove(funs[-1])
        for i in range(len(funs)):
            a = funs[i-1]
            final = a(final)
            funs.remove(funs[-1])
        return final
    return compute
        

if __name__ == "__main__":
    from math import cos,sinh,atan2

    fun = compose(cos,sinh,atan2)
    if fun(0.42, 3) == cos(sinh(atan2(0.42, 3))):
        print("OK")
    else:
        print("KO")
        print(cos(sinh(atan2(0.42, 3))))
        
