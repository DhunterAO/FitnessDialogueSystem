from question import *
from pattern import *


def answer(question):
    questionInstance = Question()
    cutRes = questionInstance.questionCut(question)
    cutQue = []
    for i in cutRes:
        cutQue.append(i[:-1])
    print(cutQue)
    return pattern(cutQue)


if __name__ == '__main__':
    print(answer('俯卧撑哪些肌肉'))
