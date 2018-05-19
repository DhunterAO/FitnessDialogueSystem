#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import thulac

'''
Question class is a util class to convert a question
from a string format to a searching format, such as
"平板支撑锻炼了哪块肌肉？"
 =>
    focus("action")
    content("平板支撑")
    target("action.muscle")

The basic workflow to finish this requirement：
1. questionCut
'''


class Question:

    def questionCut(question):
        thu1 = thulac.thulac(user_dict="userDict.txt", filt=True)  # 默认模式
        questionCut = thu1.cut(question, text=False)  # 进行一句话分词
        print(questionCut)


if __name__ == '__main__':
    # Question.questionCut("举哑铃除了锻炼肱三头肌还有什么作用?")
    a = {
        '1': 3,
        '2': 4
    }
    for i in a:
        print(i)
        print(a[i])