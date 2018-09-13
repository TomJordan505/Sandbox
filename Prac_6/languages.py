
from Prac_6.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage.("Ruby", "Dynamic", "Yes", "1995")
    visual_basic = ProgrammingLanguage.("Visual Basic", "Static", "No", "1991")
    python = ProgrammingLanguage.("Python", "Dynamic", "Yes", "1991")
    c = ProgrammingLanguage.("C++", "Static", "No", "1983")
    java = ProgrammingLanguage.("Java", "Static", "Yes", "1995")

    languages = [ruby, visual_basic, python, c, java]

    print("The dynamic languages are: ")
    for language in languages:
        if language.is_dynamic:
            print(language.name)


main()