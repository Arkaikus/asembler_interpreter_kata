from unittest import TestCase

def eval_val(val,env):
    if val in env:
        return env[val]
    else:
        return int(val)

def eval_exp(exp,env):
    parts = exp.split(' ')
    instruction = parts[0]
    if instruction == "mov":
        id = parts[1]
        val=parts[2]
        env[id]=eval_val(val,env)
    elif instruction == "inc":
        id = parts[1]
        if id in env:
            env[id]+=1
    elif instruction == "dec":
        id = parts[1]
        if id in env:
            env[id]-=1
    elif instruction == "jnz":
        not_zero = eval_val(parts[1],env) != 0
        jump_val = eval_val(parts[2],env)
        if not_zero:
            return jump_val
    return 1


def simple_assembler(program):
    # return a dictionary with the registers
    head = 0
    env = {}
    size = len(program)
    while(head<size):
        exp = program[head]
        next = eval_exp(exp,env)
        if next>size-1 or next< 1-size:
            break
        else:
            head+=next
    return env



def doTest():
    test = TestCase()
    code = '''\
    mov a 5
    inc a
    dec a
    dec a
    jnz a -1
    inc a'''
    program1 = code.splitlines()
    program1 = list(map(lambda x: x.strip(), program1))

    result1 = simple_assembler(program1)
    test.assertEqual(result1, {'a': 1})

    code = '''\
    mov c 12
    mov b 0
    mov a 200
    dec a
    inc b
    jnz a -2
    dec c
    mov a b
    jnz c -5
    jnz 0 1
    mov c a'''
    program2 = code.splitlines()
    program2 = list(map(lambda x: x.strip(), program2))
    result2 = simple_assembler(program2)
    test.assertEqual(result2, {'a': 409600, 'c': 409600, 'b': 409600})   


if __name__ == "__main__":
    doTest()