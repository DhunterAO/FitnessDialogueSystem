from action import *
from muscle import *


def get_muscle_of_action(action):
    # 返回肌肉列表
    return Action(action).get_muscle()


def get_equipment_of_action(action):
    # 返回器械列表
    return Action(action).get_equipment()


def get_level_of_action(action):
    # 返回动作等级
    return Action(action).get_level()


def get_details_of_action(action):
    # 返回动作细节
    return Action(action).get_details()


def get_type_of_action(action):
    # 返回动作类别
    return Action(action).get_type()


def get_muscleGroup_action(muscleGroup):
    # 返回肌肉组 涵盖动作
    return MuscleGroup(muscleGroup).list_muscleGroup_action()


def get_describe_of_action(action):
    # 返回动作描述
    return Action(action).get_describe()


def get_actionlist_of_muscle(muscle):
    # 返回肌肉相关动作(detial肌肉类型)
    return MuscleGroup(muscle).find_related_action()


def get_equipmentlist_of_muscle(muscle):
    # 返回肌肉相关器械
    return MuscleGroup(muscle).find_related_equipments()


def find_action_of_euqipments(equipment):
    res = Mongo.action.find()
    action_list = []
    for i in res:
        if i['equipment'] == equipment:
            if i['name'] not in action_list:
                action_list.append(i['name'])
    return action_list


def clothes_advice():
    return '去健身房穿适合运动的服饰就行，不要太紧，也不要过于肥大。'

if __name__ == '__main__':
    # print(get_muscle_of_action('平板支撑'))
    # print(get_muscleGroup_action('肱二头肌'))
    print(get_equipmentlist_of_muscle('腹直肌'))
    # print(get_actionlist_of_muscle('腹直肌'))
    # print(find_action_of_euqipments('弹力带'))
