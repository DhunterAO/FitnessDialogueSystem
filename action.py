from connector import Mongo


class Action:
    def __init__(self, name):
        self.name = name
        res = Mongo.action.find_one({'name': name})
        print(res)
        # self.level = res['level']
        # self.type = res['type']
        self.mainMuscle = res['mainMuscle']
        self.assistantMuscle = res['assistantMuscle']
        self.equipment = res['equipment']
        self.details = res['details']
        self.describe = res['describe']

    def find_muscle_action(self, muscle):
        return Mongo.action.find({'mianMuscle': muscle})

    def match(self, require):
        require_type = require.get('type', None)
        if require_type is not None and require_type != self.type:
            return False
        require_level = require.get('level', None)
        if require_level is not None and require_level != self.level:
            return False
        require_equipment = require.get('equipment', None)
        if require_equipment is not None and require_equipment != self.equipment:
            return False
        return True

    def get_muscle(self):
        return self.mainMuscle + '、' + self.assistantMuscle

    def get_equipment(self):
        return self.equipment

    def get_type(self):
        return self.type

    def get_level(self):
        return self.level

    def get_details(self):
        return self.details

    def get_describe(self):
        return self.describe

