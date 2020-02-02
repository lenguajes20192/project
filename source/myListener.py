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


class myListener(RubyListener):

    def enterProg(self, ctx:RubyParser.ProgContext):
        a.right(90)

    def exitProg(self, ctx:RubyParser.ProgContext):
        a.hideturtle()
        turtle.done

    def enterExpression_list(self, ctx: RubyParser.Expression_listContext):

        global first_time
        a.right(135)
        if not first_time:
            a.fillcolor('blue')
            a.begin_fill()
            a.circle(40)
            a.end_fill()
            a.rt(90)
        first_time = False

    #def enterExpression_list(self, ctx: RubyParser.Expression_listContext):
    def enterExpression(self, ctx:RubyParser.ExpressionContext):
        global first_time
        a.forward(40)
        if not first_time:
            rectangle(ctx)
        first_time = False
    #def exitExpression(self, ctx:RubyParser.ExpressionContext):
    
    #def enterIf_statement(self, ctx:RubyParser.If_statementContext):


    def enterIf_elsif_statement(self, ctx: RubyParser.If_elsif_statementContext):
        a.forward(40)


    def enterCond_expression(self, ctx: RubyParser.Cond_expressionContext):
        a.forward(40)
        diamond(ctx)
    #def exitIfStatement(self, ctx:RubyParser.If_statementContext):

# functions for drawing

def arrowTrue(a):
    a.forward(30)
    a.color('green')
    a.write("True", False, align="center")
    return None

def penSetting(X_coordinate,Y_coordinate):
    a.pen({'pendown': False})
    a.setposition(X_coordinate, Y_coordinate)
    a.pen({'pendown': True})

    return None
def rectangle(ctx):
    a.color('blue')
    lar = len(ctx.getText()) * 5 + 5
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
    penSetting(a.pos()[0], a.pos()[1] - 20)
    a.write(ctx.getText(), move=False, align='center', font=("Arial", 9, "bold"))
    penSetting(a.pos()[0], a.pos()[1] - 20)

def diamond(ctx):
    a.color("red")
    a.right(75)
    a.forward(100)
    a.left(150)
    a.forward(100)
    a.left(30)
    a.forward(100)
    a.left(150)
    a.forward(100)
    a.left(105)
    penSetting(a.pos()[0], a.pos()[1] - 30)
    a.color("black")
    a.write(ctx.getText(), move=False, align='center', font=("Arial", 9, "bold"))
    penSetting(a.pos()[0], a.pos()[1] - 22)
