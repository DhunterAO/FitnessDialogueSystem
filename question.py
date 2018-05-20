#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import re

'''
Question class is a util class to convert a question
from a string format to a searching format, such as
"平板支撑锻炼了哪块肌肉？"
 =>
    focus("action")
    content("平板支撑")
    target("action.muscle.txt")

The basic workflow to finish this requirement：
1. questionCut
'''

class Question:
    patternList = ['special', 'muscle', 'action', 'machine', 'negative']

    def __init__(self):
        self.matchPattern = {}
        self.patternSet = {}
        for pattern in Question.patternList:
            filename = 'dict/' + str(pattern) + '.txt'
            list = []
            with open(filename, 'rt', encoding='UTF-8') as file:
                for line in file.readlines():
                    list.append(line.strip())
            if list != []:
                self.matchPattern[str(pattern)] = re.compile(str(list) + str('+'), re.I | re.M)
                self.patternSet[str(pattern)] = set(list)
            else:
                self.matchPattern[str(pattern)] = None

    def questionCut(self, question):
        matchResult = []
        for pattern in Question.patternList:
            if self.matchPattern[str(pattern)] == None:
                continue
            for m in self.matchPattern[str(pattern)].finditer(question):
                content = m.group(0)
                if content in self.patternSet[str(pattern)]:
                    matchResult.append((str(pattern), content, m.start()))

        # for key in matchResult.keys():
        #     print(str(key), str(matchResult[str(key)]))
        matchResult.sort(key=lambda x:(x[2]))
        return matchResult

if __name__ == '__main__':

    # usage demo
    # step 1: get instance
    questionInstance = Question()

    # step 2: invoke questionCut function,
    question = "卧推锻炼了哪些肌肉？"
    print(question)
    print(questionInstance.questionCut(question))

    question = "平板支撑锻炼肌肉要多少天才有效果?"
    print(question)
    print(questionInstance.questionCut(question))
