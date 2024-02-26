import argparse


def get_user_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", help="""simple arithmetic problem like:
                        a+b, a-b, axb, a/b
                        Use letter x for multiplication""",
                        type=str)
    args = parser.parse_args()
    # print(args.problem)
    return args.problem


def calculate(s: str):
    if '+' in s:
        a, b = s.split('+')
        res = float(a)+float(b)
    if '-' in s:
        a, b = s.split('-')
        res = float(a)-float(b)
    if '/' in s:
        a, b = s.split('/')
        res = float(a)/float(b)
    if 'x' in s:
        a, b = s.split('x')
        res = float(a)*float(b)
    return res


problem = get_user_data()
solution = calculate(problem)
print(solution)
