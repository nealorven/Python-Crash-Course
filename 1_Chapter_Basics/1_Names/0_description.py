Языки программирвоания:
                     идентификатор ↓   ↓ числовой литерал
                                   a = 1
                                     ↑
                               оператор связи

evaluate - python читает и сравнивает кусочки кода слева направо:

                     код          evaluate          value
                      ↑              ↑               ↑
         текст программы    выполнение программы    байты в памяти

Expression:
    Минимайльный кусок кода это                      : expression
        если сам по себе                             : literal expression
        если использует слева/справа                 : compound
            если делает переменную                   : assignment
            если проверяет                           : condition
            если считает                             : arithmetic

    специальный кусочек кода(костыль синтаксиса)     : statement
        -нехватка спецсимволов

    спецсимволы и statement вроде return называют    : operator
        -операторы тесно связаны с expression

foo = (v) => v * 2      : function definition operator(толстая строка)

def foo(v):             : function definition statement(синтаксис python)
    return v * 2

                               Пример evaluate
>>>1 : number literal expression
1    : number value

>>>"Hi" : string literal expression
'Hi'    : string value

>>>1 == 2 : conditional expression
False     : bolean value

1 == 2    : compound expression
                                  1 == 2
                                  ↑    ↑
                       использует результат evaluate
                              слева и справа

Лево и право, affinity(1+2, -1, 1==2):

          1 + 2            + 1              1 +             foo()
      both affinity   right affinity    no affinity     affinity (yes)

Side-effects:

>>> import sys                        : импорт библиотеки
>>> sys.stdout.write("foo\n")         : объект вывода
foo                                   : side-effect
4                                     : результат evaluate

Operator precedence:
        :        (('-%s' if order else '%s') % column_name)

        :        (                                        )
        #        1                                        1
        :         (                        )
        #         2                        2
        :          '-%s'               '%s'
        #            5                  6
        :                                    %
        #
        :                if order else         column_name
        #                3    4    3                8

Кусочки кода:
expression:
literal expression
conditional expression:
