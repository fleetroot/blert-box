# coding=utf-8
"""
This program does the following:
1. Prompts the user for input
2. Prints the entire Mad Libs story with the user's input in the right spaces"""

print("Mad Libs Begins!")

first_adj = raw_input("Enter an adjective: ")
second_adj = raw_input("Enter an adjective: ")

first_verb = raw_input("Enter a verb: ")
second_verb = raw_input("Enter a verb: ")

first_noun = raw_input("Enter a noun: ")
second_noun = raw_input("Enter a noun: ")
third_noun = raw_input("Enter a noun: ")
fourth_noun = raw_input("Enter a noun: ")
fifth_noun = raw_input("Enter a noun: ")

first_plural_noun = raw_input("Enter a plural noun: ")
second_plural_noun = raw_input("Enter a plural noun: ")

name = raw_input("Enter a name: ")

#The template for the story

STORY = ("In a %s far, far, away... \n"
         "    It is a period of civil war. Rebel %s, \n"
         "    striking from a hidden %s, have won their first victory \n"
         "    against the evil %s Empire. During the battle, Rebel \n"
         "    spies managed to %s secret %s to the Empire’s ultimate \n"
         "    weapon, the %s , an armored %s with enough power to %s an %s. \n"
         "    Pursued by the Empire’s %s agents, Princess %s races home \n"
         "    aboard her starship, custodian of the stolen %s that can save \n"
         "    her people and restore freedom to the galaxy…")

print STORY % (first_noun, first_plural_noun, second_noun,
               first_adj, first_verb, second_plural_noun,
               third_noun, fourth_noun, second_verb, fifth_noun,
               second_adj, name, second_plural_noun)