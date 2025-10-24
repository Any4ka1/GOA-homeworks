def to_celcius(f):
    c = 5/9 * (f - 32)
    return c
print(to_celcius(100)) 
#37.77777777777778 f ~ 37.78f

def calculate_damage(op_attack, c_damage, f_move):
    total = op_attack + c_damage + f_move
    return (f"your wizzard's new life is {total}")
print(calculate_damage(10,20,30))

