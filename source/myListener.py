import turtle

import numpy as np
from antlr4 import *
from RubyParser import RubyParser
from RubyLexer import RubyLexer
from RubyListener import RubyListener

text_arr = np.array(["elsif.txt", "ifelseif.txt", "while.txt", "for.txt", "2.txt"])
text = text_arr[0]

window = turtle.Screen()
window.screensize(60000, 60000)
a = turtle.Turtle()
a.pensize(2)
x_start = a.pos()[0]
y_start = a.pos()[1]
a.speed(2)
first_time = True;
contextEnterLoop = ""

xc_diamond = 0
yc_diamond = 0
xc_end = 0
yc_end = 0
coor_end = np.array([[0, 0]])
while_statement = False
for_int_assignment = False


class myListener(RubyListener):

    def enterProg(self, ctx: RubyParser.ProgContext):
        code()
        global first_time
        if first_time:
            a.fillcolor('blue')
            a.begin_fill()
            a.circle(40)
            a.end_fill()
            a.color('white')
            penSetting(a.pos()[0], a.pos()[1] + 30)
            a.write('START', move=False, align='center', font=("Arial", 9, "bold"))
            penSetting(a.pos()[0], a.pos()[1] - 30)
            a.color('black')
            a.rt(90)
        first_time = False

    def exitProg(self, ctx: RubyParser.ProgContext):
        global coor_end
        a.forward(120)
        a.right(90)
        a.fillcolor('midnight blue')
        a.begin_fill()
        a.circle(30)
        a.end_fill()
        a.color('white')
        penSetting(a.pos()[0], a.pos()[1] - 35)
        a.write('END', move=False, align='center', font=("Arial", 9, "bold"))
        penSetting(a.pos()[0], a.pos()[1] + 35)
        a.color('black')
        a.left(90)
        global xc_end, yc_end
        xc_end = a.pos()[0]
        yc_end = a.pos()[1] + 20

        if len(coor_end) > 1:
            for i in range(1, len(coor_end) - 1):
                penSetting(coor_end[i][0], coor_end[i][1])
                a.forward(abs(yc_end) - abs(a.pos()[1]))
                a.left(90)
                a.forward(abs(xc_end) - abs(a.pos()[0]))
                a.right(90)

        a.hideturtle()
        turtle.getscreen()._root.mainloop()

    def enterInt_assignment(self, ctx: RubyParser.Int_assignmentContext):
        global for_int_assignment
        if not for_int_assignment:
            a.forward(40)
            rectangle(ctx)
        for_int_assignment = False

    def enterInitial_array_assignment(self, ctx: RubyParser.Initial_array_assignmentContext):
        a.forward(40)
        rectangle(ctx)

    def enterArray_assignment(self, ctx: RubyParser.Array_assignmentContext):
        a.forward(40)
        rectangle(ctx)

    #def enterDynamic_assignment(self, ctx: RubyParser.Dynamic_assignmentContext):
     #   a.forward(40)
      #  rectangle(ctx)



    # def exitExpression(self, ctx:RubyParser.ExpressionContext):

    # def enterIf_statement(self, ctx:RubyParser.If_statementContext):

    def enterIf_elsif_statement(self, ctx: RubyParser.If_elsif_statementContext):
        penSetting(xc_diamond + 194, yc_diamond)
        a.left(90)
        a.forward(180)
        a.color('red')
        a.write('False', move=False, align='center', font=("Arial", 9, "bold"))
        a.color('black')
        a.right(90)
        a.forward(40)

    def enterElse_token(self, ctx: RubyParser.Else_tokenContext):
        penSetting(xc_diamond + 194, yc_diamond)
        a.left(90)
        a.forward(180)
        a.color('red')
        a.write('False', move=False, align='center', font=("Arial", 9, "bold"))
        a.color('black')
        a.right(90)
        a.forward(40)

    def enterCond_expression(self, ctx: RubyParser.Cond_expressionContext):
        #a.forward(40)
        diamond(ctx)

    def enterCond_expression(self, ctx: RubyParser.Cond_expressionContext):
        diamond(ctx)
        arrowTrue()
        print('este')

    def enterString_result(self, ctx: RubyParser.String_resultContext):
        # a.forward(40)
        rectangle(ctx)

    #def enterDynamic_result(self, ctx: RubyParser.Dynamic_resultContext):
    #def enterArray_selector(self, ctx: RubyParser.Array_selectorContext):
        #rectangle(ctx)

    def exitStatement_expression_list(self, ctx: RubyParser.Statement_expression_listContext):
        global coor_end, while_statement
        if not while_statement:
            coor_end = np.append(coor_end, [[a.pos()[0], a.pos()[1]]], axis=0)
        print(coor_end)

    def enterLoop_expression(self, ctx: RubyParser.Loop_expressionContext):
        global contextEnterLoop
        contextEnterLoop = ctx
        print('el del loop expresion')
        print('contextloop')
        print(contextEnterLoop.getText())

    def exitWhile_statement(self, ctx: RubyParser.While_statementContext):
        a.forward(40)
        a.right(90)
        a.forward(a.pos()[0] - xc_diamond + 40)
        a.right(90)
        a.forward(yc_diamond - a.pos()[1])
        a.right(90)
        a.forward(40)
        penSetting(a.pos()[0] + 194, a.pos()[1])
        a.forward(100)
        a.right(90)

    def enterWhile_statement(self, ctx: RubyParser.While_statementContext):
        global while_statement
        while_statement = True

    def enterFor_loop_list(self, ctx: RubyParser.For_loop_listContext):
        global for_int_assignment
        for_int_assignment = True

    def exitFor_statement(self, ctx: RubyParser.For_statementContext):
        a.forward(40)
        print('contex rec')
        rectangle(contextEnterLoop)

        a.forward(40)
        a.right(90)
        a.forward(a.pos()[0] - xc_diamond + 40)
        a.right(90)
        a.forward(yc_diamond - a.pos()[1])
        a.right(90)
        a.forward(40)
        penSetting(a.pos()[0] + 194, a.pos()[1])
        a.forward(100)
        a.color('red')
        a.write('False', move=False, align='center', font=("Arial", 9, "bold"))
        a.color('black')
        a.right(90)


# functions for drawing

def arrowTrue():
    a.forward(20)
    a.color('green')
    a.write('True', move=False, align='center', font=("Arial", 9, "bold"))
    a.color('black')
    a.forward(20)
    return None


def penSetting(X_coordinate, Y_coordinate):
    a.pen({'pendown': False})
    a.setposition(X_coordinate, Y_coordinate)
    a.pen({'pendown': True})

    return None


def rectangle(ctx):
    a.color('blue')
    lar = len(ctx.getText()) * 9 + 5
    a.right(90)
    a.forward(lar / 2)
    a.left(90)
    a.forward(40)
    a.lt(90)
    a.fd(lar)
    a.lt(90)
    a.fd(40)
    a.lt(90)
    a.fd(lar / 2)
    a.lt(90)
    a.color('black')
    penSetting(a.pos()[0], a.pos()[1] - 25)
    a.write(ctx.getText(), move=False, align='center', font=("Arial", 9, "bold"))
    penSetting(a.pos()[0], a.pos()[1] - 15)


def code():
    file = open(text, "r")
    lines = file.readlines()
    len_lines = len(lines)
    print(len_lines)

    penSetting(a.pos()[0] - 500, a.pos()[1])
    a.fillcolor('black')
    a.begin_fill()
    a.right(90)
    a.forward(len_lines*30)
    a.left(90)
    a.forward(300)
    a.left(90)
    a.forward(len_lines*30)
    a.left(90)
    a.forward(300)
    a.end_fill()

    a.color('white')
    penSetting(a.pos()[0] + 20, a.pos()[1] - 40)
    a.write('>> RUBY CODE: ', font=("Arial", 10, "bold"))
    penSetting(a.pos()[0], a.pos()[1] - 40)

    for i in range(0, len_lines):
        print(lines[i])
        a.write(lines[i], font=("Arial", 9, "bold"))
        penSetting(a.pos()[0], a.pos()[1] - 20)

    a.left(180)
    a.color('black')
    penSetting(a.pos()[0] + 500, 0)


def diamond(ctx):
    global xc_diamond, yc_diamond
    a.forward(40)
    a.color("orange")
    a.right(75)
    a.forward(100)
    xc_diamond = a.pos()[0]
    yc_diamond = a.pos()[1]
    a.left(150)
    a.forward(100)
    a.left(30)
    a.forward(100)
    a.left(150)
    a.forward(100)
    a.left(105)
    penSetting(a.pos()[0], a.pos()[1] - 30)
    a.color("black")
    a.write("¿ " + ctx.getText() + " ?", move=False, align='center', font=("Arial", 9, "bold"))
    penSetting(a.pos()[0], a.pos()[1] - 22)

