from solve import *

patternList = [
    #（个人觉得其实动作对应的元组差不太多，基本都能覆盖，主要是要涉及一些会经常被问到很频繁的关键词）
    ['action'],# 怎样做俯卧撑
    ['action','肌肉'],# 卧推锻炼哪些肌肉
    ['action','组'],# 卧推怎样做组训练
    ['action','防具'],# 深蹲防具该准备哪些
    ['action','注意'],# 卧推要有什么特别注意事项
    ['action','副作用'],# 深蹲会有什么副作用吗
    ['action','累'],# 深蹲超级累怎么回事
    ['action', '要', '器'],# 平板支撑需要什么器械/道具/设备/条件
    ['action', '动作'],# 跟仰卧起坐差不多的动作有什么
    ['action','练','muscle'],# 俯卧撑除了练胸还能练哪里
    ['action','muscle','痛'],#卧推时肩部酸痛怎么回事
    ['action','muscle','special'],# 哑铃飞鸟练二头有效果吗
    
    ['muscle', '练'],# 腹肌怎么练
    ['muscle','拉伸'],# 背阔肌怎样拉伸

    ['muscle','热身'],# 背阔肌怎样热身
    ['muscle','肌肉群'],# 肩部由哪些肌肉群组成
    ['muscle','时间','合适'],# 胸肌每次锻炼多长时间合适
    
    #（因为这些关键词只要有一个较为完整的回答基本就够了，问的比较频繁）
    ['想','健身'],# 你好，我想了解一些健身健身方面的知识（返回问候语和一些鼓励的话）
    ['谢谢'],# 对我很有帮助，谢谢啦（返回励志的话）
    ['练','水'],# 锻炼怎样补充水
    ['练','能量'],# 锻炼能量怎样补充
    ['练', 'muscle'],# 怎么样可以锻炼腹肌
    ['极限','action','保护'],# 极限重量深蹲怎样保护避免受伤
    ['服饰'],# 去健身房穿什么运动服饰比较好
    ['增肌'],#增肌该做些什么动作
    ['减脂'],#减脂该怎么做
    ['礼仪'],#要注意的健身礼仪是什么
    ['休息'],#健身后如何合理休息
    ['饮食'],#健身期间如何注意饮食搭配
    ['练','规划'],#能给我提点简单的训练时间规划吗（主要是不同训练阶段的频次安排，每周几练，时间间隔等）
    ['健身房','special'],# 去健身房效果更好还是不去呢
    ['户外','健身房','special'],# 户外健身和健身房相比效果好吗
    ['不','健身房','muscle'],# 不去健身房怎样锻炼胸肌
    ['避免','代偿'],# 锻炼时怎样避免次肌肉群代偿
    ['有氧'],# 有氧锻炼怎样进行
    
    ['machine','动作'],# 哑铃主要可以做哪些动作
    ['machine','action','重量'],# 杠铃卧推重量该怎么选择
    ['machine','action','special'],# 哑铃卧推比杠铃卧推效果好吗
    ['machine','action','muscle'],# 哑铃卧推怎样锻炼到胸中束
    ['machine','muscle','special'],# 杠铃怎样练二头有效果
    ['machine','action','muscle','special'],# 哑铃卧推对二头效果好吗
    
    #（以下为重复内容）
    ['action', '肌肉'],# 卧推锻炼哪些肌肉1 return muscle of action
    ['action', 'muscle'],# 俯卧撑除了练腹肌 return muscle of action
    ['action'],# 怎样做俯卧撑3 return detial of action ##如果只有一个词，返回动作整体信息
    ['练', 'muscle'],# 怎么样可以锻炼腹肌4 return detial of action
    ['action', '要', '器'],# 平板支撑需要什么器械/道具/设备/条件5 return equipment of action
    ['action', '动作'],# 跟仰卧起坐差不多的动作有什么6 return action of muscle
    ['muscle', '练'],# 腹肌怎么练7 return detail of action


    ['machine', '动作'],  # 哑铃主要可以做哪些动作
    ['machine', 'action', 'muscle'],  # 哑铃卧推怎样锻炼到胸中束  #14  5.17号解决以上pattern
    
    # （因为这些关键词只要有一个较为完整的回答基本就够了，问的比较频繁）##更新于5.18
    ['了解', '健身'],  # 你好，我想了解一些健身健身方面的知识（返回问候语和一些鼓励的话）
    ['谢谢'],  # 对我很有帮助，谢谢啦（返回励志的话）
    ['炼', '补充水'],  # 锻炼怎样补充水
    ['炼', '补水'],  # 锻炼怎样补充水
    ['炼', '补充能量'],  # 锻炼能量怎样补充
    ['练', 'muscle'],  # 怎么样可以锻炼腹肌
    ['action', '保护'],  # 深蹲怎样保护自己
    ['action', '避免'],   #深度怎么避免受伤
    ['健身', '保护'],   #健身中怎么保护自己
    ['健身', '避免'],   #健身中怎么避免受伤
    ['健身','服饰'],  # 去健身房穿什么运动服饰比较好
    ['增肌', '动作'],  # 增肌该做些什么动作
    ['减脂'],  # 减脂该怎么做
    ['健身','礼仪'],  # 健身礼仪是什么
    ['健身','休息'],  # 健身后如何合理休息
    ['健身','注意','饮食'],  # 健身期间如何注意饮食搭配
    ['健身','饮食'], #健身中的饮食搭配 健身后的饮食搭配 健身如何进行饮食搭配
    ['练', '规划'],  # 能给我提点简单的训练时间规划吗（主要是不同训练阶段的频次安排，每周几练，时间间隔等）
    ['健身房', 'special'],  # 去健身房有效果嘛
    # ['户外', '健身房', 'special'],  # 户外健身和健身房相比效果好吗
    ['不', '健身房', 'muscle'],  # 不去健身房怎样锻炼胸肌
    ['避免', '代偿'],  # 锻炼时怎样避免次肌肉群代偿
    # ['有氧训练'],  # 有氧训练怎样进行

    ['machine', '动作'],  # 哑铃主要可以做哪些动作
    ['machine', 'action', '重量'],  # 杠铃卧推重量该怎么选择
    ['machine', 'action', 'special'],  # 哑铃卧推比杠铃卧推效果好吗
    ['machine', 'action', 'muscle'],  # 哑铃卧推怎样锻炼到胸中束
    ['machine', 'muscle', 'special'],  # 杠铃怎样练二头有效果
    ['machine', 'action', 'muscle', 'special'],  # 哑铃卧推对二头效果好吗
    # ['action','防具'],# 深蹲防具该准备哪些
    # ['muscle','热身'],# 背阔肌怎样热身
    # ['练','水'],# 锻炼怎样补充水
    # ['练','能量'],# 锻炼能量怎样补充
    # ['极限','action','保护'],# 极限重量深蹲怎样保护避免受伤
    # ['服饰'],# 去健身房穿什么运动服饰比较好
    # ['machine', 'action', 'special'],  # 哑铃卧推比杠铃卧推效果好吗
    # ['machine', 'action', '重量'],  # 杠铃卧推重量该怎么选择
]


def pattern_match(pattern, sentence):
    #print(pattern)
    #print(sentence)
    #1 split sentence
    #2 find out focus word  eg muscle/special/action
    #3
    if len(pattern) != len(sentence):
        return False
    l = len(sentence)
    # print(l)
    for i in range(l):
        #print(pattern[i])
        #print(sentence[i])
        if pattern[i] == 'action':
            if sentence[i][0] == 'action':
                continue
            return False
        if pattern[i] == 'muscle':
            if sentence[i][0] == 'muscle':
                continue
            return False
        if sentence[i][1] == pattern[i]:
            continue
        return False
    return True


def pattern(sentence):
    for index, p in enumerate(patternList):
        # print(index)

        if pattern_match(p, sentence):
            print(sentence)
            if index == 0:
                return get_muscle_of_action(sentence[0][1])
            if index == 1:
                return get_muscle_of_action(sentence[0][1])
            if index == 2:
                if sentence[0][2] != 0:
                    return get_details_of_action(sentence[0][1])
                else:
                    return get_describe_of_action(sentence[0][1])
            if index == 3:
                return get_details_of_action(sentence[0][1])
            if index == 4:
                return get_equipment_of_action(sentence[0][1])
            if index == 5:
                return get_muscleGroup_action(sentence[0][1])
            if index == 6 or index == 7:
                return get_muscleGroup_action(sentence[0][1])
            if index == 8 or index == 9 or index == 10:
                return get_details_of_action(sentence[0][1])
            if index == 11:
                return ###need to be solve
            if index == 12:
                return get_muscleGroup_action(sentence[0][1])
            if index == 13:
                return ###need to be solve
            if index == 14:
                return get_muscleGroup_action(sentence[1][1])
    return 'unknown'


if __name__ == '__main__':
    print(pattern([('action', '平板支撑'), ('special', '肌肉')]))
    print(pattern([('action', '平板支撑'), ('muscle', '腹肌')]))
    print(pattern([('action', '平板支撑'), ('special','有效')]))
    print(pattern([('special', '可以'), ('muscle', '腹肌')]))
    print(pattern([('action', '平板支撑'), ('special', '器材')]))
    # print(pattern([('action', '平板支撑'), ('special', '动作')]))#unsovle
