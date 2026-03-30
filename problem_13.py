import numpy as np
from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=70)
        MathTex.set_default(font_size=80)
        statement = VGroup(
            Tex(r"\begin{minipage}{5cm}"
                r"Find the equation of the circle passing through the points $(2,3)$, $(3,4)$, and $(-1,2)$."
                r"\end{minipage}")
        )

        statement[0].move_to(3 * UP)
        self.play(Write(statement))
        self.wait(3)
        self.play(FadeOut(statement))


class ProblemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=70)
        MathTex.set_default(font_size=80)

        ax = Axes(x_range=[-7, 5, 1], y_range=[0, 15, 1], x_length=12, y_length=15)
        dots = VGroup(
            Dot(color=BLUE, radius=0.15).move_to(ax.c2p(2, 3)),
            Dot(color=YELLOW, radius=0.15).move_to(ax.c2p(3, 4)),
            Dot(color=RED, radius=0.15).move_to(ax.c2p(-1, 2)),
            Dot(color=GOLD, radius=0.15).move_to(ax.c2p(-1, 7))
        )

        arrow = VGroup(
            CurvedArrow(ax.c2p(4, 15), ax.c2p(1.12, 11.53), color=YELLOW),
            Arrow(ax.c2p(-1, 7), ax.c2p(3, 4), color=BLUE)
        )

        labels = VGroup(
            MathTex(r"(2,3)", font_size=50).next_to(dots[0], RIGHT, SMALL_BUFF),
            MathTex(r"(3,4)", font_size=50).next_to(dots[1], RIGHT, SMALL_BUFF),
            MathTex(r"(-1,2)", font_size=50).next_to(dots[2], DOWN, SMALL_BUFF),
            MathTex(r"C(h,k)", font_size=50).next_to(dots[3], UP, SMALL_BUFF),
            MathTex(r"f(x,y)=0", font_size=50).next_to(arrow[0].get_start(), RIGHT, SMALL_BUFF),
            MathTex(r"r", font_size=50).next_to(arrow[1].get_midpoint(), UP, MED_SMALL_BUFF)
        )

        self.play(Create(ax))
        self.wait(0.2)

        for i in range(3):
            self.play(Create(dots[i]))
            self.play(Write(labels[i]))
            self.wait(0.3)

        circle = ax.plot_parametric_curve(
            lambda t: np.array([5*np.cos(t)-1, 5*np.sin(t)+7, 0]),
            t_range=[0, 2*PI]
        )

        self.play(Create(dots[3]))
        self.play(Write(labels[3]))
        self.play(Create(circle))
        self.wait(0.3)
        self.play(Create(arrow[1]))
        self.play(Write(labels[5]))
        self.wait(0.3)
        self.play(Write(labels[4]))
        self.play(Create(arrow[0]))
        self.wait(1.5)
        self.play(FadeOut(circle, ax, dots, labels, arrow))

        solutions = VGroup(

        )
