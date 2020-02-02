import turtle
from antlr4 import *
from RubyParser import RubyParser
from RubyLexer import RubyLexer
from RubyListener import RubyListener

window = turtle.Screen()
window.screensize(60000, 60000)
a = turtle.Turtle()
a.pensize(2)
x_start = a.pos()[0]
y_start = a.pos()[1]
a.speed(3)
first_time = True;

xc_diamond = 0
yc_diamond = 0


class myListener(RubyListener):

    def enterProg(self, ctx: RubyParser.ProgContext):
        global first_time
        if first_time:
            a.fillcolor('blue')
            a.begin_fill()
            a.circle(40)
            a.end_fill()
            a.rt(90)
        first_time = False

    def exitProg(self, ctx: RubyParser.ProgContext):
        a.forward(40)
        a.right(90)
        a.fillcolor('blue')
        a.begin_fill()
        a.circle(30)
        a.end_fill()
        a.left(90)
        a.hideturtle()
        turtle.getscreen()._root.mainloop()

    # def enterExpression_list(self, ctx: RubyParser.Expression_listContext):

    # def exitExpression_list(self, ctx: RubyParser.Expression_listContext):

    # def enterExpression(self, ctx:RubyParser.ExpressionContext):
    def enterInt_assignment(self, ctx: RubyParser.Int_assignmentContext):
        a.forward(40)
        rectangle(ctx)

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
        a.forward(40)
        diamond(ctx)

    def enterCond_expression(self, ctx: RubyParser.Cond_expressionContext):
        diamond(ctx)
        arrowTrue()
        print('este')

    def enterString_result(self, ctx: RubyParser.String_resultContext):
        #a.forward(40)
        rectangle(ctx)

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
