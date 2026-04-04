import numpy as np
from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=75)
        MathTex.set_default(font_size=75)
        statement = VGroup(
            Tex(r"\begin{minipage}{5cm}"
                r"Find the equation of the circle circumscribing the triangle with vertices $(-1,-4)$, $(3,-2)$, $(5,"
                r"2)$."
                r"\end{minipage}")
        )

        statement[0].move_to(3 * UP)
        self.play(Write(statement))
        self.wait(3)
        self.play(FadeOut(statement))


class ProblemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=75)
        MathTex.set_default(font_size=75)
        ax = Axes(x_range=[-10, 6, 1], y_range=[-5, 11, 1], x_length=12, y_length=12)
        dots = VGroup(
            Dot(color=BLUE, radius=0.2).move_to(ax.c2p(-1, -4)),
            Dot(color=YELLOW, radius=0.2).move_to(ax.c2p(3, -2)),
            Dot(color=GREEN, radius=0.2).move_to(ax.c2p(5, 2)),
            Dot(color=RED, radius=0.2).move_to(ax.c2p(-2, 3))
        )

        edges = VGroup(
            Line(ax.c2p(-1, -4), ax.c2p(3, -2), color=BLUE),
            Line(ax.c2p(3, -2), ax.c2p(5, 2), color=YELLOW),
            Line(ax.c2p(5, 2), ax.c2p(-1, -4), color=GREEN),
            Arrow(ax.c2p(-2, 3), ax.c2p(-2+5*np.sqrt(2), 3), color=RED),
            CurvedArrow(ax.c2p(1, 13), ax.c2p(-2, 3 + 5 * np.sqrt(2)), color=GOLD)
        )

        circle = ax.plot_parametric_curve(
            lambda t: np.array([5 * np.sqrt(2) * np.cos(t) - 2, 5 * np.sqrt(2) * np.sin(t) + 3, 0]),
            t_range=[0, 2 * PI],
            color=RED
        )

        labels = VGroup(
            MathTex(r"(-1, -4)", font_size=50).next_to(dots[0], DOWN, SMALL_BUFF),
            MathTex(r"(3, -2)", font_size=50).next_to(dots[1], RIGHT, SMALL_BUFF),
            MathTex(r"(5, 2)", font_size=50).next_to(dots[2], RIGHT, SMALL_BUFF),
            MathTex(r"(h, k)", font_size=50).next_to(dots[3], UP, SMALL_BUFF),
            MathTex(r"r", font_size=50).next_to(edges[3].get_midpoint(), UP, MED_SMALL_BUFF),
            MathTex(r"f(x,y)=0", font_size=55).next_to(edges[4].get_start(), RIGHT, SMALL_BUFF)
        )

        self.play(Create(ax))
        self.play(Create(dots[:3]))
        self.play(Write(labels[:3]))
        for i in range(3):
            self.play(Create(edges[i]))
            self.wait(0.2)
        self.play(Create(dots[3]))
        self.play(Write(labels[3]))
        self.play(Create(edges[3]))
        self.play(Rotate(edges[3], angle=2 * PI, about_point=edges[3].get_start()), Create(circle))
        self.play(Write(labels[4]))
        self.play(Write(labels[5]))
        self.play(Create(edges[4]))
        self.wait(1.5)
        self.play(FadeOut(edges, labels, circle, dots, ax))

        lines = VGroup(

        )
