import sys
import os
import inspect


class TooYoungException(Exception):
    pass


class Padawan:
    def __init__(self, age, name):
        if age <= 10:
            raise TooYoungException(self.__name)
        self.__age = age
        self.__name = name
        self.mentor = None
        self.pass_test = False

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, p):
        if p <= 10:
            raise TooYoungException(self.__name + ' is too young to start!')
        self.__age = p

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, p):
        if self.age < 20:
            self.__name = p

    def train(self, mentor):
        ## see description for details
        print('taking more and more training...')
        print('training complete')
        self.mentor = mentor
        self.pass_test = True

    def __repr__(self):
        if self.pass_test == False:
            return str(self.age) + '-year old ' + self.__class__.__name__ + ' ' + self.name + ' needs more training!'
        else:
            return str(
                self.age) + '-year old ' + self.__class__.__name__ + ' ' + self.name + ' may continue to pursue further education!'


class JediKnight(Padawan):
    def __init__(self, age, name):
        super().__init__(age, name)


class JediMaster(JediKnight):
    def __init__(self, age, name, padawan):
        super().__init__(age, name)
        self.mentee = padawan
        self.pass_test = True

    def train(self):
        print("giving more and more training ...")
        print("training complete")
        self.mentee.mentor = self
        self.mentee.pass_test = True

    def __repr__(self):
        return str(
            self.age) + '-year old ' + self.__class__.__name__ + ' ' + self.name + ' is training ' + self.mentee.name + '.'


def test_padawan_initiated_correctly():
