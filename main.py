import re


def math(problems, ans=False):
    out = str()
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for i in problems:
        val = re.findall('\S+', i)
        if str(val[0]).isdigit() is not True or str(val[2]).isdigit() is not True:
            return 'Error: Numbers must only contain digits.'
        if val[1] != '-' and val[1] != '+':
            return "Error: Operator must be '+' or '-'."
        if len(str(val[0])) > 4 or len(str((val[2]))) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        s1.append(val[0])
        s2.append(val[1])
        s3.append(val[2])
        if val[1] == '-':
            s4.append(f'{int(val[0]) - int(val[2])}')
        elif val[1] == '+':
            s4.append(f'{int(val[0]) + int(val[2])}')
    for i in range(len(problems)):
        if i == 0:
            out = f'{s1[i]:>{2 + max(len(s1[i]), len(s3[i]))}}'
        else:
            out += f'    {s1[i]:>{2 + max(len(s1[i]), len(s3[i]))}}'
    out += '\n'
    for i in range(len(problems)):
        if i == 0:
            out += f'{s2[i]} {s3[i]:>{max(len(s1[i]), len(s3[i]))}}'
        else:
            out += f'    {s2[i]} {s3[i]:>{max(len(s1[i]), len(s3[i]))}}'
    out += '\n'
    for i in range(len(problems)):
        if i == 0:
            out += f'{"_" * (2 + max(len(s1[i]), len(s3[i]))):>{(2 + max(len(s1[i]), len(s3[i])))}}'
        else:
            out += f'    {"_" * (2 + max(len(s1[i]), len(s3[i]))):>{(2 + max(len(s1[i]), len(s3[i])))}}'
    out += '\n'
    if ans is True:
        for i in range(len(problems)):
            if i == 0:
                out += f'{s4[i]:>{2 + max(len(s1[i]), len(s3[i]))}}'
            else:
                out += f'    {s4[i]:>{2 + max(len(s1[i]), len(s3[i]))}}'
    return out
