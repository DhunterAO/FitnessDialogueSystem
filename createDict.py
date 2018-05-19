from connector import Mongo


def creat_action_dict(file):
    res = Mongo.action.find()

    File = open(file, 'w')
    for action in res:
        name = action['name']
        if name[-1] == ')':
            l = name.find('(')
            name = name[:l]
            File.write(name + '\n')
        elif name[-1] == 'L':
            name = name[:-1]
            File.write(name + '\n')


def create_muscle_dict(file):
    res = Mongo.muscle.find()
    File = open(file, 'w')
    for muscle in res:
        name = muscle['name']
        File.write(name + '\n')


def create_machine_dict(file):
    res = Mongo.action.find()

    File = open(file, 'w')
    for action in res:
        machine = action['equipment']
        File.write(machine + '\n')


if __name__ == '__main__':
    create_machine_dict('dict/machine.txt')
