#!/usr/bin/python3
"""
defining a class Base
"""
import csv
import json


class Base():
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialising instance
        Args
            id: id of the instance created
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert a list of dicts to a json string obj
        Args:
            list_dictionaries: list of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return str([])
        elif type(list_dictionaries) == list and\
                all(isinstance(ele, dict) for ele in list_dictionaries):
            return json.dumps(list_dictionaries)
        else:
            raise TypeError("epecting list of dictionaries")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save a json str repr of a list obj into a file
        Args:
            cls: class of obj
            list_objs: list of obj
        """
        file_name = cls.__name__
        my_list = []
        if list_objs is None or list_objs == []:
            my_list = []
        else:
            for ele in list_objs:
                my_list.append(ele.to_dictionary())
        data = cls.to_json_string(my_list)
        with open(f"{file_name}.json", "w") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
        retrives an obj from its json str repr
        Args:
            json_string: json_string repr of the obj
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create an instance of a class(obj) from its dict repr
        Args:
            cls: the instance class
            dictionary: dict repr of instance
        """
        name = cls.__name__
        if name == "Rectangle":
            rectangle = cls(5, 10)
            rectangle.update(**dictionary)
            return rectangle
        else:
            square = cls(2)
            square.update(**dictionary)
            return square

    @classmethod
    def load_from_file(cls):
        """
        return a list of instances fron a file
        obj with json repr of those instances
        """
        instancelist = []
        name = cls.__name__
        try:
            with open(f"{name}.json") as f:
                mylist = cls.from_json_string(f.read())
                for ele in mylist:
                    instancelist.append(cls.create(**ele))
                return instancelist
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Stores rectangle/square objects to a .csv file

        Args:
           list_objs (list): A list of Square/Rectangle objects.
        '''
        name = cls.__name__
        with open(f"{name}.csv", 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            if list_objs is None or list_objs == []:
                csv_writer.writerow("")
            else:
                for obj in list_objs:
                    if name == "Square":
                        csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])
                    elif name == "Rectangle":
                        csv_writer.writerow([obj.id, obj.width,
                                             obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''Retrieves data from a .csv file and
        returns a list of Square/Rectangle Objects
        '''
        result = []
        name = cls.__name__
        with open(f"{name}.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if name == "Square":
                    result.append(cls.create(id=int(row[0]), size=int(row[1]),
                                             x=int(row[2]), y=int(row[3])))
                elif name == "Rectangle":
                    result.append(cls.create(id=int(row[0]), width=int(row[1]),
                                             height=int(row[2]), x=int(row[3]),
                                             y=int(row[4])))
        return result
