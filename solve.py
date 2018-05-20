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


def get_actionlist_of_muscleGroup(muscleGroup):
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


def get_actionlist_of_euqipments(equipment):
    res = Mongo.action.find()
    action_list = []
    for i in res:
        if i['equipment'] == equipment:
            if i['name'] not in action_list:
                action_list.append(i['name'])
    return action_list


def clothes_advice():
    return '去健身房穿适合运动的服饰就行，不要太紧，也不要过于肥大。'


def get_muscle_of_equipments(equipment):
    res = Mongo.action.find()
    muscle_list = []
    for i in res:
        if i['equipment'] == equipment:
            if i['mainMuscle'] not in muscle_list:
                muscle_list.append(i['mainMuscle'])
    return muscle_list

def get_actionlist_of_action(action):
    res = Mongo.action.find()
    action_list = []
    for i in res:
        if i['name'] == action:
            muscle_temp = i['mainMuscle']
            break
    for i in res:
        if['mainMuscle'] == muscle_temp:
            if i['name'] not in action_list:
                action_list.append(i['name'])
    return action_list

def welcoming():
    return('您好，欢迎使用THU健身问答任务系统！\n这里有人体肌肉示意图供您参考，请问您对健身哪方面感兴趣呢。\n')

def goodbye():
    return('非常感谢您使用THU健身回答任务系统，希望系统对您的健身需求有所帮助！\n')

def water_replenishing():
    return ('剧烈健身后饮用8-14℃的温水为佳，补水应遵循先少后多的原则，逐步补充水分：可以先用水漱漱口，滋润口腔，喝少量的水，然后在健身后的20-30分钟内，补充150-200mL含糖10%左右的糖盐水最为适宜。\n')

def energy_replenishing():
    return('选择低淀粉蔬菜作为每餐摄入，每餐吃两个拳头大小的蔬菜量，尽量每天吃到7~10种蔬菜，并且新鲜的调味类蔬菜也是非常好的食物补充。\n蔬菜选择：橄榄、甘蓝、黄瓜、胡萝卜、洋葱、西兰花、芹菜、芦笋、番茄、辣椒、菠菜、葫芦等 \n香料选择：八角、桂皮、葱姜蒜、罗勒、百里香、薄荷、洋葱、胡椒等\n水果的选择：水果的问题在于有些水果果糖很高，如一些浆果类：葡萄等，还有一些瓜类如甜瓜\n有些水果是很好的运动补充，因为富含钾，如香蕉\n有些水果是低卡路里，可以每天吃50~75克，如草莓\n饮料：首选是水，优质的水每天要补充2000毫升以上，水可以帮助加快代谢，更有助身体塑形\n无糖咖啡、茶也是很好的饮料\n也可以选择无糖的运动机能饮料，帮助提升运动效果。\n')

def fitness_protection():
    return('1.每次锻炼前要做好充分的准备活动，使肌肉发热有弹性，做好高度紧张的准备。\n2.完成每个动作都要高度集中注意力。\n3.认真学习正确的锻炼动作，逐渐提高负荷量。\n4.学会正确的呼吸方法，避免过分憋气。\n5.初学者宜慎重加量，以便使身体各部位适应不断改变的负荷。尤其要加强对抗肌，小肌群的补偿锻炼。\n6.当肌肉出现疼痛，变硬时，应注意调整负荷。\n7.注意个人卫生。\n8.锻炼后要采用各种各样快速恢复的重建措施。')

def lose_weight():
    return('腹部：西西里卷腹、仰卧抬腿、卷腹、反向卷腹、仰卧风车。（进阶加哑铃）\n腿部：深蹲、单腿硬拉、保加利亚式深蹲。（进阶加哑铃）\n臀部：跪姿后踢腿、俯卧后踢腿、保加利亚式深蹲、各种臀桥。\n背部：俯卧Y字伸展、俯卧TW伸展、俯卧挺身转体。（进阶加哑铃）\n手臂：哑铃俯身臂屈伸、天鹅臂肩膀：哑铃侧平举、天鹅臂。\n胸部：各种俯卧撑、哑铃臀桥飞鸟。')

def musculus_muscle():
    return('增肌需要注意的三个事项：\n1.制定训练计划，一周五天最为适宜，可以保持肌肉的强度(周一:胸部,周二:背部,周三:腿部,周四:肩部,周五:手臂)\n2.注意饮食，补充足够能量.\n3.增肌期不做有氧训练，阻碍肌肉增长')

def increase_weight():
    return('1. 多做身体各部位肌肉训练，强化肌肉纤维。\n2. 摄入大量蛋白与碳水化合物，保证肌肉的修复和生长，保证摄入能量大于你消耗的能量\n')

def relax():
    return('初级训练者:练一天休息一天：肌肉需要更多休息来慢慢适应训练强度，获得更好增长。\n中级训练者:练2天休息1天：在适应了训练节奏和强度后，肌肉恢复能力有所增强，增加训练天数，促进肌肉生长。\n高级训练者:练3天休息1天：如果为了比赛准备可采取此种方式，每天上下午练，上午小肌肉群，下午大肌肉群，三天正好走完一个循环第四天休息。\n')

def fitness_planing():
    return ('起步期: 1-4周，主要以激活肌肉为目的进行训练，主要多做一下初级的健身动作。\n上升期: 5-8周，动作模式建立后，通过四周的时间提升训练强度，需要有组数的，有计划的进行动作组合，动作可参考初级与中级的健身动作。\n冲刺期: 9-12周，在计划中加入高级健身动作进行健身计划的规划，增加爆发力的训练，提升肌肉的控制力。\n')


if __name__ == '__main__':
    # print(get_muscle_of_action('平板支撑'))
    # print(get_muscleGroup_action('肱二头肌'))
    print(fitness_planing())
    # print(get_actionlist_of_muscle('腹直肌'))
    # print(find_action_of_euqipments('弹力带'))
