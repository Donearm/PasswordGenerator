#!/usr/bin/env python
###############################################################################
# Copyright (c) 2010-2011, Gianluca Fiore
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
###############################################################################

__author__ = "Gianluca Fiore"
__license__ = "GPLv3"
__version__ = "0.1"
__date__ = "18/05/2011"
__email__ = "forod.g@gmail.com"


from random import choice, shuffle, sample
import getopt
import string
import sys
import locale

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = [a for a in string.ascii_lowercase if a not in vowels]

def gen_passwd(length=8, lc='C', easy=False):
    locale.setlocale(locale.LC_ALL, lc)
    # check password length
    if length < 6:
        print("Password would be too short, at least 6 characters please")
        sys.exit(2)

    # two routines, one for a random password and another for a more human
    # readable one
    if easy == False:
        print("No easy to remember password chosen")
        chars = string.ascii_letters + string.digits
        return ''.join([choice(chars) for i in range(length)])
    elif easy == True:
        print("Easy to remember password mode enabled")
        password = [] # the list which will contain the final password
        if length % 2 == 0:
            if length == 6:
                # 6 chars then 2 words + 2 digits
                for n in range(2):
                    password.append(give_syllable())
                password.append(sample(string.digits, 2))
                # randomize it
                shuffle(password)
                return ''.join(flatten(password))
            elif length == 8:
                # 8 chars then 3 words + 2 digits
                for n in range(3):
                    password.append(give_syllable())
                password.append(sample(string.digits, 2))
                # randomize it
                shuffle(password)
                return ''.join(flatten(password))
            elif length == 10:
                # 10 chars then 4 words + 2 digits
                for n in range(4):
                    password.append(give_syllable())
                password.append(sample(string.digits, 2))
                # randomize it
                shuffle(password)
                return ''.join(flatten(password))
            elif length == 12:
                # 12 chars then 4 words + 4 digits
                for n in range(4):
                    password.append(give_syllable())
                for n in range(2):
                    password.append(sample(string.digits, 2))
                # randomize it
                shuffle(password)
                return ''.join(flatten(password))
            else:
                # at least 14 chars, 4 words + 4 digits + a random word/digit 
                # couple
                for n in range(4):
                    password.append(give_syllable())
                for n in range(2):
                    password.append(sample(string.digits, 2))

                # check how much bigger is length in relation with the base 
                # number (14)
                rest = length - 14
                if rest != 0:
                    password.append(sample(string.ascii_letters, rest))
                else:
                    # exactly 14 chars then  
                    password.append(sample(string.ascii_letters, 2))
                # randomize it
                shuffle(password)
                return ''.join(flatten(password))
        else:
            print("Odd length")
            # calculate the rest. 6 is the minimum required length
            rest = length - 6

            for n in range(2):
                password.append(give_syllable())
            password.append(sample(string.digits, 2))
            # add random letters according to rest
            password.append(sample(string.ascii_letters, rest))
            # randomize it
            shuffle(password)
            return ''.join(flatten(password))


def flatten(seq):
    """flatten a nested list"""
    for x in seq:
        if type(x) is list:
            for y in flatten(x):
                yield y
        else:
            yield x

def give_syllable():
    """return a syllable string"""
    return sample(consonants, 1) + sample(vowels, 1)

class Options(object):
    pass

def main(argv):
    try:
        (option_list, args) = getopt.getopt(argv[1:],"r:l:o:e",["repeat=","length=","locale=","easy"])
    except getopt.GetoptError as err:
        print((str(err)))
        sys.exit(2)

    options = Options()
    options.repeat = 1
    options.length = 8
    options.locale = 'C'
    options.easy = False
    for (key, value) in option_list:
        if key == "-r" or key == "--repeat":
            options.repeat = int(value)
        elif key == "-l" or key == "--length":
            options.length = int(value)
        elif key == "-o" or key == "--locale":
            options.locale = str(value)
        elif key == "-e" or key == "--easy":
            options.easy = True


    for i in range(options.repeat):
        try:
            print((gen_passwd(options.length, options.locale, options.easy)))
        except ValueError as v:
            print("")
            print("Password requested too long, exiting...")
            print("Please refrain from using passwords longer than 50 char/digits thanks")
            sys.exit(2)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

