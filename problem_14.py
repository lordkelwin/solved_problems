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
            Arrow(ax.c2p(-2, 3), ax.c2p(-2 + 5 * np.sqrt(2), 3), color=RED),
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
            self.wait(0.1)
        self.play(Create(dots[3]), Write(labels[3]))
        self.play(Create(edges[3]))
        self.play(Rotate(edges[3], angle=2 * PI, about_point=edges[3].get_start()), Create(circle))
        self.play(Write(labels[4]))
        self.play(Write(labels[5]))
        self.play(Create(edges[4]))
        self.wait(1.5)
        self.play(FadeOut(edges, labels, circle, dots, ax))

        lines = VGroup(
            Tex(r"\begin{minipage}{5cm}"
                r"To find the equation of the circle, we can use this equation given three points of a circle:"
                r"\end{minipage}"),
            MathTex(r"\begin{vmatrix}"
                    r"(x^{2}+y^{2}) & x & y & 1 \\"
                    r"(x_{1}^{2}+y_{1}^{2}) & x_{1} & y_{1} & 1 \\"
                    r"(x_{2}^{2}+y_{2}^{2}) & x_{2} & y_{2} & 1 \\"
                    r"(x_{3}^{2}+y_{3}^{2}) & x_{3} & y_{3} & 1"
                    r"\end{vmatrix} = 0"),
            Tex(r"Substituting the given points:"),
            MathTex(r"\begin{vmatrix}"
                    r"(x^{2}+y^{2}) & x & y & 1 \\"
                    r"\left[(-1)^{2}+(-4)^{2}\right] & -1 & -4 & 1 \\"
                    r"\left[3^{2}+(-2)^{2}\right] & 3 & -2 & 1 \\"
                    r"\left(5^{2}+2^{2}\right) & 5 & 2 & 1"
                    r"\end{vmatrix} = 0"),
            MathTex(r"\begin{vmatrix}"
                    r"(x^{2}+y^{2}) & x & y & 1 \\"
                    r"(1 + 16) & -1 & -4 & 1 \\"
                    r"(9+4) & 3 & -2 & 1 \\"
                    r"(25+4) & 5 & 2 & 1"
                    r"\end{vmatrix} = 0"),
            MathTex(r"\begin{vmatrix}"
                    r"(x^{2}+y^{2}) & x & y & 1 \\"
                    r"17 & -1 & -4 & 1 \\"
                    r"13 & 3 & -2 & 1 \\"
                    r"29 & 5 & 2 & 1"
                    r"\end{vmatrix} = 0"),
            Tex(r"Using Chio's Pivotal Condensation:"),
            MathTex(r"\frac{1}{a_{11}^{n-2}} \begin{vmatrix} \begin{vmatrix} a_{11} & "
                    r"a_{12} \\ a_{21} & a_{22} \end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{21} & a_{23} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{14} \\ a_{21} & a_{24} "
                    r"\end{vmatrix} \\ \begin{vmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{31} & a_{33} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{14} \\ a_{31} & a_{34} "
                    r"\end{vmatrix} \\ \begin{vmatrix} a_{11} & a_{12} \\ "
                    r"a_{41} & a_{42} \end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{41} & a_{43} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{14} \\ a_{41} & a_{44} "
                    r"\end{vmatrix}\end{vmatrix} = 0", font_size=60),
            Tex(r"Substituting:"),
            MathTex(r"\frac{1}{(x^{2}+y^{2})^{2}}"
                    r"\begin{vmatrix}"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 17 & -1 \end{vmatrix} & "
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 17 & -4 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 17 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 13 & 3 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 13 & -2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 13 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=50),
            Tex(r"Let: "),
            MathTex(r"D = \begin{vmatrix}"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 17 & -1 \end{vmatrix} & "
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 17 & -4 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 17 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 13 & 3 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 13 & -2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 13 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix}", font_size=55),
            Tex(r"Substitute to simplify:"),
            MathTex(r"\frac{1}{(x^{2}+y^{2})^{2}}"
                    r"D = 0", font_size=60),
            MathTex(r"(x^{2}+y^{2})^{2} \times \frac{1}{(x^{2}+y^{2})^{2}}"
                    r"D = 0\times{(x^{2}+y^{2})^{2}", font_size=60),
            MathTex(r"D=0", font_size=60),
            Tex(r"Reverse substitute and simplify:"),
            MathTex(r"\begin{vmatrix}"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 17 & -1 \end{vmatrix} & "
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 17 & -4 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 17 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 13 & 3 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 13 & -2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 13 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=60),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & \begin{vmatrix} (x^{2}+y^{2}) & y \\ 17 & -4 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 17 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 13 & 3 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 13 & -2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 13 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=55),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & -4(x^{2}+y^{2})-17y & "
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 17 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 13 & 3 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 13 & -2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 13 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=55),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & -4(x^{2}+y^{2})-17y & "
                    r"(x^{2}+y^{2})-17 \\ \begin{vmatrix} (x^{2}+y^{2}) & x \\ 13 & 3 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 13 & -2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 13 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=55),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & -4(x^{2}+y^{2})-17y & "
                    r"(x^{2}+y^{2})-17 \\ 3(x^{2}+y^{2})-13x & "
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 13 & -2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 13 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=55),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & -4(x^{2}+y^{2})-17y & "
                    r"(x^{2}+y^{2})-17 \\ 3(x^{2}+y^{2})-13x & "
                    r"-2(x^{2}+y^{2})-13y & \begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 13 & 1 \end{vmatrix} \\"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=55),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & -4(x^{2}+y^{2})-17y & "
                    r"(x^{2}+y^{2})-17 \\ 3(x^{2}+y^{2})-13x & "
                    r"-2(x^{2}+y^{2})-13y & (x^{2}+y^{2})-13 \\ "
                    r"\begin{vmatrix} (x^{2}+y^{2}) & x \\ 29 & 5 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=55),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & -4(x^{2}+y^{2})-17y & "
                    r"(x^{2}+y^{2})-17 \\ 3(x^{2}+y^{2})-13x & "
                    r"-2(x^{2}+y^{2})-13y & (x^{2}+y^{2})-13 \\ "
                    r"5(x^{2}+y^{2})-29x & \begin{vmatrix} (x^{2}+y^{2}) & y \\ 29 & 2 \end{vmatrix} &"
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=55),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & -4(x^{2}+y^{2})-17y & "
                    r"(x^{2}+y^{2})-17 \\ 3(x^{2}+y^{2})-13x & "
                    r"-2(x^{2}+y^{2})-13y & (x^{2}+y^{2})-13 \\ "
                    r"5(x^{2}+y^{2})-29x & 2(x^{2}+y^{2})-29y & "
                    r"\begin{vmatrix} (x^{2}+y^{2}) & 1 \\ 29 & 1 \end{vmatrix}"
                    r"\end{vmatrix} = 0", font_size=55),
            MathTex(r"\begin{vmatrix}"
                    r"-(x^{2}+y^{2})-17x & -4(x^{2}+y^{2})-17y & (x^{2}+y^{2})-17 \\ 3(x^{2}+y^{2})-13x & "
                    r"-2(x^{2}+y^{2})-13y & (x^{2}+y^{2})-13 \\ 5(x^{2}+y^{2})-29x & 2(x^{2}+y^{2})-29y & "
                    r"(x^{2}+y^{2})-29"
                    r"\end{vmatrix} = 0", font_size=55),
            Tex(r"Let $u=x^{2}+y^{2}$:"),
            MathTex(r"\begin{vmatrix}"
                    r"-u-17x & -4u-17y & u-17 "
                    r"\\ 3u-13x & -2u-13y & u-13 \\ "
                    r"5u-29x & 2u-29y & u-29"
                    r"\end{vmatrix} = 0", font_size=65),
            MathTex(r"\begin{vmatrix}"
                    r"-u-17x & -4u-17y & u-17 "
                    r"\\ 3u-13x & -2u-13y & u-13 \\ "
                    r"5u-29x & 2u-29y & u-29"
                    r"\end{vmatrix} "
                    r"\begin{matrix}"
                    r"-u-17x & -4u-17y \\"
                    r"3u-13x & -2u-13y \\"
                    r"5u-29x & 2u-29y"
                    r"\end{matrix} = 0", font_size=55),
            MathTex(r"S_{1} = (-u-17x)(-2u-13y)(u-29)"),
            MathTex(r"S_{1} = (2u^{2}+13uy+34ux+221xy)(u-29)"),
            MathTex(r"S_{1} = (2u^{3}+13u^{2}y+34u^{2}x+221uxy)-\\(58u^{2}+377uy+986ux+6409xy)", font_size=65),
            MathTex(r"S_{2} = (-4u-17y)(u-13)(5u-29x)"),
            MathTex(r"S_{2} = (-4u^{2}+52u-17uy+221y)(5u-29x)"),
            MathTex(r"S_{2} = (-20u^{3}+260u^{2}-85u^{2}y+1105uy)-\\(-116u^{2}x+1508ux-493uxy+6409xy)", font_size=65),
            MathTex(r"S_{3} = (u-17)(3u-13x)(2u-29y)"),
            MathTex(r"S_{3} = (3u^{2}-13ux-51u+221x)(2u-29y)"),
            MathTex(r"S_{3} = (6u^{3}-26u^{2}x-102u^{2}+442ux)-\\(87u^{2}y-377uxy-1479uy+6409xy)", font_size=65),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=[(2u^{3}+13u^{2}y+34u^{2}x+221uxy)-(58u^{2}+377uy+986ux+6409xy)]+"
                r"[(-20u^{3}+260u^{2}-85u^{2}y+1105uy)-(-116u^{2}x+1508ux-493uxy+6409xy)]+"
                r"[(6u^{3}-26u^{2}x-102u^{2}+442ux)-(87u^{2}y-377uxy-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=-12u^{3}+[13u^{2}y+34u^{2}x+221uxy)-(58u^{2}+377uy+986ux+6409xy)]+"
                r"[(260u^{2}-85u^{2}y+1105uy)-(-116u^{2}x+1508ux-493uxy+6409xy)]+"
                r"[(-26u^{2}x-102u^{2}+442ux)-(87u^{2}y-377uxy-1479uy+\\6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+[34u^{2}x+221uxy)-"
                r"(58u^{2}+377uy+986ux+6409xy)]+[(260u^{2}+1105uy)-(-116u^{2}x+1508ux-493uxy+6409xy)"
                r"]+[(-26u^{2}x-102u^{2}+442ux)-(377uxy-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+[221uxy-"
                r"(58u^{2}+377uy+986ux+6409xy)]+[(260u^{2}+1105uy)-(1508ux-493uxy+6409xy)"
                r"]+[(-102u^{2}+442ux)-(377uxy-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+[-"
                r"(58u^{2}+377uy+986ux+6409xy)]+[(260u^{2}+1105uy)-(1508ux+6409xy)"
                r"]+[(-102u^{2}+442ux)-(-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+[-"
                r"(377uy+986ux+6409xy)]+[1105uy-(1508ux+6409xy)"
                r"]+[442ux-(-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+2207uy+[-"
                r"(986ux+6409xy)]+[-(1508ux+6409xy)]+\left[442ux-6409xy\right]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+2207uy-2052ux+(-"
                r"6409xy-6409xy-6409xy)$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+2207uy-2052ux-19227xy$"
                r"\end{minipage}",
                font_size=70),
            MathTex(r"S_{4} = (5u-29x)(-2u-13y)(u-17)"),
            MathTex(r"S_{4} = (-10u^{2}-65uy+58ux+377xy)(u-17)"),
            MathTex(r"S_{4} = (-10u^{3}-65u^{2}y+58u^{2}x+377uxy)-\\(-170u^{2}-1105uy+986ux+6409xy)", font_size=65),
            MathTex(r"S_{5} = (2u-29y)(u-13)(-u-17x)"),
            MathTex(r"S_{5} = (2u^{2}-26u-29uy+377y)(-u-17x)"),
            MathTex(r"S_{5} = (-2u^{3}+26u^{2}+29u^{2}y-377uy)-\\(34u^{2}x-442ux-493uxy+6409xy)", font_size=65),
            MathTex(r"S_{6} = (u-29)(3u-13x)(-4u-17y)"),
            MathTex(r"S_{6} = (3u^{2}-13ux-87u+377x)(-4u-17y)"),
            MathTex(r"S_{6} = (-12u^{3}+52u^{2}x+348u^{2}-1508ux)-\\(51u^{2}y-221uxy-1479uy+6409xy)", font_size=65),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=[(-10u^{3}-65u^{2}y+58u^{2}x+377uxy)-(-170u^{2}-1105uy+986ux+6409xy)]+"
                r"[(-2u^{3}+26u^{2}+29u^{2}y-377uy)-(34u^{2}x-442ux-493uxy+6409xy)]+"
                r"[(-12u^{3}+52u^{2}x+348u^{2}-1508ux)-(51u^{2}y-221uxy-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=-24u^{3}+[(-65u^{2}y+58u^{2}x+377uxy)-(-170u^{2}-1105uy+986ux+6409xy)]+"
                r"[(26u^{2}+29u^{2}y-377uy)-(34u^{2}x-442ux-493uxy+6409xy)]+"
                r"[(52u^{2}x+348u^{2}-1508ux)-(51u^{2}y-221uxy-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=-24u^{3}-87u^{2}y+[(58u^{2}x+377uxy)-(-170u^{2}-1105uy+986ux+6409xy)]+"
                r"[(26u^{2}-377uy)-(34u^{2}x-442ux-493uxy+6409xy)]+"
                r"[(52u^{2}x+348u^{2}-1508ux)-(-221uxy-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=-24u^{3}-87u^{2}y+76u^{2}x+[377uxy-(-170u^{2}-1105uy+986ux+6409xy)]+"
                r"[(26u^{2}-377uy)-(-442ux-493uxy+6409xy)]+"
                r"[(348u^{2}-1508ux)-(-221uxy-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=-24u^{3}-87u^{2}y+76u^{2}x+1091uxy+[-(-170u^{2}-1105uy+986ux+6409xy)]+"
                r"[(26u^{2}-377uy)-(-442ux+6409xy)]+"
                r"[(348u^{2}-1508ux)-(-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=-24u^{3}-87u^{2}y+76u^{2}x+1091uxy+544u^{2}+[-(-1105uy+986ux+6409xy)]+"
                r"[-377uy-(-442ux+6409xy)]+[-1508ux-(-1479uy+6409xy)]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=-24u^{3}-87u^{2}y+76u^{2}x+1091uxy+544u^{2}+2207uy+[-(986ux+6409xy)]+"
                r"[-(-442ux+6409xy)]+[-1508ux-6409xy]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=-24u^{3}-87u^{2}y+76u^{2}x+1091uxy+544u^{2}+2207uy-2052ux+[-6409xy"
                r"-6409xy-6409xy]$"
                r"\end{minipage}", font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$S_{4}+S_{5}+S_{6}=-24u^{3}-87u^{2}y+76u^{2}x+1091uxy+544u^{2}+2207uy-2052ux-19227xy$"
                r"\end{minipage}",
                font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$\det{D}=\left[S_{1}+S_{2}+S_{3}\right]-\left[S_{4}+S_{5}+S_{6}\right]=0$"
                r"\end{minipage}",
                font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$[-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+2207uy-2052ux-19227xy]-"
                r"[-24u^{3}-87u^{2}y+76u^{2}x+1091uxy+544u^{2}+2207uy-2052ux-19227xy]=0$"
                r"\end{minipage}",
                font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$12u^{3}+[-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+2207uy-2052ux-19227xy]-"
                r"[-87u^{2}y+76u^{2}x+1091uxy+544u^{2}+2207uy-2052ux-19227xy]=0$"
                r"\end{minipage}",
                font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$12u^{3}-72u^{2}y+[124u^{2}x+1091uxy+100u^{2}+2207uy-2052ux-19227xy]-"
                r"[76u^{2}x+1091uxy+544u^{2}+2207uy-2052ux-19227xy]=0$"
                r"\end{minipage}",
                font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$12u^{3}-72u^{2}y+48u^{2}x+[1091uxy+100u^{2}+2207uy-2052ux-19227xy]-"
                r"[1091uxy+544u^{2}+2207uy-2052ux-19227xy]=0$"
                r"\end{minipage}",
                font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$12u^{3}-72u^{2}y+48u^{2}x+[100u^{2}+2207uy-2052ux-19227xy]-"
                r"[544u^{2}+2207uy-2052ux-19227xy]=0$"
                r"\end{minipage}",
                font_size=70),
            Tex(r"\begin{minipage}{7cm}"
                r"$12u^{3}-72u^{2}y+48u^{2}x-444u^{2}+[2207uy-2052ux-19227xy]-"
                r"[2207uy-2052ux-19227xy]=0$"
                r"\end{minipage}",
                font_size=70),
            MathTex(r"12u^{3}-72u^{2}y+48u^{2}x-444u^{2}=0",
                    font_size=70),
            MathTex(r"12u^{2}\left(u+4x-6y-37\right)=0",
                    font_size=70),
            MathTex(r"\frac{1}{12u^{2}} \times 12u^{2}\left(12u-72y+48x-444\right)=0 \times \frac{1}{12u^{2}}",
                    font_size=65),
            MathTex(r"u+4x-6y-37=0",
                    font_size=70),
            Tex(r"Reverse substitute $u=x^{2}+y^{2}$:"),
            MathTex(r"x^{2}+y^{2}+4x-6y-37=0",
                    font_size=70),
            Tex(r"Equation of the circle:")
        )

        lines[0].move_to(8 * UP)
        self.play(Write(lines[0]))
        self.play(Write(lines[1].next_to(lines[0], DOWN, MED_LARGE_BUFF)))
        self.wait(0.2)
        self.play(Write(lines[2].next_to(lines[1], DOWN, LARGE_BUFF)))
        self.play(Write(lines[3].next_to(lines[2], DOWN, MED_LARGE_BUFF)))
        self.wait(0.1)
        self.play(ReplacementTransform(lines[3], lines[4].next_to(lines[2], DOWN, MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[4], lines[5].next_to(lines[2], DOWN, MED_LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(lines[:3]))
        self.play(lines[5].animate.shift(5 * UP))
        self.play(Write(lines[6].next_to(lines[5], DOWN, MED_SMALL_BUFF)))
        self.play(Write(lines[7].next_to(lines[6], DOWN, MED_SMALL_BUFF)))
        self.play(ReplacementTransform(lines[6], lines[8].next_to(lines[5], DOWN, MED_SMALL_BUFF)))
        self.play(ReplacementTransform(lines[7], lines[9].next_to(lines[8], DOWN, MED_SMALL_BUFF)))
        self.wait(0.3)
        self.play(FadeOut(lines[8:10]))
        self.play(Write(lines[10].next_to(lines[5], DOWN, LARGE_BUFF)),
                  Write(lines[11].next_to(lines[10], DOWN, MED_SMALL_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[10], lines[12].next_to(lines[5], DOWN, LARGE_BUFF)),
                  ReplacementTransform(lines[11], lines[13].next_to(lines[12], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        for i in range(14, 16):
            self.play(ReplacementTransform(lines[i - 1], lines[i].next_to(lines[12], DOWN, LARGE_BUFF)))
            if i == 14:
                lines[i][0][:8].set_color(BLUE)
                lines[i][0][11:19].set_color(YELLOW)
                arrows = VGroup(
                    Arrow(lines[i][0][:8].get_corner(DL), lines[i][0][:8].get_corner(UR), color=YELLOW),
                    Arrow(lines[i][0][11:19].get_corner(DL), lines[i][0][11:19].get_corner(UR), color=BLUE)
                )
                self.play(Create(arrows[0]), Create(arrows[1]))
                self.wait(0.3)
                self.play(FadeOut(arrows, run_time=0.25))
            else:
                self.wait(0.3)
        self.play(ReplacementTransform(lines[12], lines[16].next_to(lines[5], DOWN, LARGE_BUFF)),
                  ReplacementTransform(lines[15], lines[17].next_to(lines[16], DOWN, MED_LARGE_BUFF)))
        lines[17][0][16:23].set_color(BLUE)
        lines[17][0][26:28].set_color(BLUE)
        lines[17][0][23].set_color(YELLOW)
        lines[17][0][24:26].set_color(YELLOW)
        arrows = VGroup(
            Arrow(lines[17][0][16:23].get_center(), lines[17][0][26:28].get_center(), color=YELLOW),
            Arrow(lines[17][0][24:26].get_center(), lines[17][0][23].get_center(), color=BLUE)
        )
        self.play(Create(arrows[0]), Create(arrows[1]))
        self.wait(0.3)
        self.play(FadeOut(arrows[:2]))
        for i in range(18, 27):
            self.play(ReplacementTransform(lines[i - 1], lines[i].next_to(lines[16], DOWN, MED_LARGE_BUFF)))
            if i == 18:
                lines[i][0][28:35].set_color(BLUE)
                lines[i][0][38:40].set_color(BLUE)
                lines[i][0][35].set_color(YELLOW)
                lines[i][0][36:38].set_color(YELLOW)
                arrows.add(Arrow(lines[i][0][28:35].get_center(), lines[i][0][38:40].get_center(), color=YELLOW))
                arrows.add(Arrow(lines[i][0][36:38].get_center(), lines[i][0][35].get_center(), color=BLUE))
                self.play(Create(arrows[2]), Create(arrows[3]))
                self.wait(0.3)
                self.play(FadeOut(arrows[2:4]))
            elif i == 19:
                lines[i][0][41:48].set_color(BLUE)
                lines[i][0][51].set_color(BLUE)
                lines[i][0][48].set_color(YELLOW)
                lines[i][0][49:51].set_color(YELLOW)
                arrows.add(Arrow(lines[i][0][41:48].get_center(), lines[i][0][51].get_center(), color=YELLOW))
                arrows.add(Arrow(lines[i][0][49:51].get_center(), lines[i][0][48].get_center(), color=BLUE))
                self.play(Create(arrows[4]), Create(arrows[5]))
                self.wait(0.3)
                self.play(FadeOut(arrows[4:6]))
            elif i == 20:
                lines[i][0][49:56].set_color(BLUE)
                lines[i][0][59].set_color(BLUE)
                lines[i][0][56].set_color(YELLOW)
                lines[i][0][57:59].set_color(YELLOW)
                arrows.add(Arrow(lines[i][0][49:56].get_center(), lines[i][0][59].get_center(), color=YELLOW))
                arrows.add(Arrow(lines[i][0][57:59].get_center(), lines[i][0][56].get_center(), color=BLUE))
                self.play(Create(arrows[6]), Create(arrows[7]))
                self.wait(0.3)
                self.play(FadeOut(arrows[6:8]))
            elif i == 21:
                lines[i][0][61:68].set_color(BLUE)
                lines[i][0][71:73].set_color(BLUE)
                lines[i][0][68].set_color(YELLOW)
                lines[i][0][69:71].set_color(YELLOW)
                arrows.add(Arrow(lines[i][0][61:68].get_center(), lines[i][0][71].get_center(), color=YELLOW))
                arrows.add(Arrow(lines[i][0][69:71].get_center(), lines[i][0][68].get_center(), color=BLUE))
                self.play(Create(arrows[8]), Create(arrows[9]))
                self.wait(0.3)
                self.play(FadeOut(arrows[8:10]))
            elif i == 22:
                lines[i][0][74:81].set_color(BLUE)
                lines[i][0][84].set_color(BLUE)
                lines[i][0][81].set_color(YELLOW)
                lines[i][0][82:84].set_color(YELLOW)
                arrows.add(Arrow(lines[i][0][74:81].get_center(), lines[i][0][84].get_center(), color=YELLOW))
                arrows.add(Arrow(lines[i][0][82:84].get_center(), lines[i][0][81].get_center(), color=BLUE))
                self.play(Create(arrows[10]), Create(arrows[11]))
                self.wait(0.3)
                self.play(FadeOut(arrows[10:12]))
            elif i == 23:
                lines[i][0][82:89].set_color(BLUE)
                lines[i][0][92].set_color(BLUE)
                lines[i][0][89].set_color(YELLOW)
                lines[i][0][90:92].set_color(YELLOW)
                arrows.add(Arrow(lines[i][0][82:89].get_center(), lines[i][0][92].get_center(), color=YELLOW))
                arrows.add(Arrow(lines[i][0][90:92].get_center(), lines[i][0][89].get_center(), color=BLUE))
                self.play(Create(arrows[12]), Create(arrows[13]))
                self.wait(0.3)
                self.play(FadeOut(arrows[12:14]))
            elif i == 24:
                lines[i][0][94:101].set_color(BLUE)
                lines[i][0][104].set_color(BLUE)
                lines[i][0][101].set_color(YELLOW)
                lines[i][0][102:104].set_color(YELLOW)
                arrows.add(Arrow(lines[i][0][94:101].get_center(), lines[i][0][104].get_center(), color=YELLOW))
                arrows.add(Arrow(lines[i][0][102:104].get_center(), lines[i][0][101].get_center(), color=BLUE))
                self.play(Create(arrows[14]), Create(arrows[15]))
                self.wait(0.3)
                self.play(FadeOut(arrows[14:16]))
            elif i == 25:
                lines[i][0][106:113].set_color(BLUE)
                lines[i][0][116].set_color(BLUE)
                lines[i][0][113].set_color(YELLOW)
                lines[i][0][114:116].set_color(YELLOW)
                arrows.add(Arrow(lines[i][0][106:113].get_center(), lines[i][0][116].get_center(), color=YELLOW))
                arrows.add(Arrow(lines[i][0][114:116].get_center(), lines[i][0][113].get_center(), color=BLUE))
                self.play(Create(arrows[16]), Create(arrows[17]))
                self.wait(0.3)
                self.play(FadeOut(arrows[16:18]))

        self.wait(0.4)
        self.play(ReplacementTransform(lines[16], lines[27].next_to(lines[5], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[26], lines[28].next_to(lines[27], DOWN, MED_LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[28], lines[29].next_to(lines[27], DOWN, MED_LARGE_BUFF)))
        self.play(FadeOut(lines[5]))
        self.play(lines[27].animate.shift(7 * UP), lines[29].animate.shift(7 * UP))
        self.wait(0.25)
        arrowsDet = VGroup(
            Arrow(lines[29][0][6:12].get_center(), lines[29][0][52:56].get_center(), color=BLUE),
            Arrow(lines[29][0][12:19].get_center(), lines[29][0][88:94].get_center(), color=BLUE),
            Arrow(lines[29][0][19:23].get_center(), lines[29][0][94:100].get_center(), color=BLUE),
            Arrow(lines[29][0][40:46].get_center(), lines[29][0][19:23].get_center(), color=YELLOW),
            Arrow(lines[29][0][46:52].get_center(), lines[29][0][62:68].get_center(), color=YELLOW),
            Arrow(lines[29][0][52:56].get_center(), lines[29][0][68:75].get_center(), color=YELLOW)
        )

        labels = VGroup(
            MathTex(r"S_{1}", font_size=40, color=YELLOW).next_to(lines[29][0][52:56].get_corner(DR), DOWN,
                                                                  MED_SMALL_BUFF),
            MathTex(r"S_{2}", font_size=40, color=YELLOW).next_to(lines[29][0][88:94].get_corner(DR), DOWN,
                                                                  MED_SMALL_BUFF),
            MathTex(r"S_{3}", font_size=40, color=YELLOW).next_to(lines[29][0][94:100].get_corner(DR), DOWN,
                                                                  MED_SMALL_BUFF),
            MathTex(r"S_{4}", font_size=40, color=BLUE).next_to(lines[29][0][19:23].get_corner(UR), UP, MED_SMALL_BUFF),
            MathTex(r"S_{5}", font_size=40, color=BLUE).next_to(lines[29][0][62:68].get_corner(UR), UP, MED_SMALL_BUFF),
            MathTex(r"S_{6}", font_size=40, color=BLUE).next_to(lines[29][0][68:75].get_corner(UR), UP, MED_SMALL_BUFF)
        )

        self.play(Create(arrowsDet[0]))
        self.play(Write(labels[0]))
        self.wait(0.3)
        self.play(Write(lines[30].next_to(lines[29], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[30], lines[31].next_to(lines[29], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[31], lines[32].next_to(lines[29], DOWN, LARGE_BUFF)))

        self.play(Create(arrowsDet[1]))
        self.play(Write(labels[1]))
        self.wait(0.3)
        self.play(Write(lines[33].next_to(lines[32], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[33], lines[34].next_to(lines[32], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[34], lines[35].next_to(lines[32], DOWN, LARGE_BUFF)))

        self.play(Create(arrowsDet[2]))
        self.play(Write(labels[2]))
        self.wait(0.3)
        self.play(Write(lines[36].next_to(lines[35], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[36], lines[37].next_to(lines[35], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[37], lines[38].next_to(lines[35], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(lines[38], lines[35]), ReplacementTransform(lines[32],
                                                                      lines[39].next_to(lines[29], DOWN, LARGE_BUFF)))
        lines[39][0][11:14].set_color(BLUE)
        lines[39][0][64:69].set_color(BLUE)
        lines[39][0][124:127].set_color(BLUE)
        arrows = VGroup(
            Line(lines[39][0][11:14].get_corner(DL), lines[39][0][11:14].get_corner(UR), color=YELLOW),
            Line(lines[39][0][64:69].get_corner(DL), lines[39][0][64:69].get_corner(UR), color=YELLOW),
            Line(lines[39][0][124:127].get_corner(DL), lines[39][0][124:127].get_corner(UR), color=YELLOW)
        )
        tempText = MathTex(r"-12u^{3}", font_size=50, color=YELLOW).next_to(lines[39][0][11:14].get_corner(UR), UP,
                                                                            SMALL_BUFF)

        self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
        self.play(Write(tempText))
        self.wait(0.25)
        self.play(FadeOut(tempText, arrows))

        for i in range(40, 48):
            self.play(ReplacementTransform(lines[i - 1], lines[i].next_to(lines[29], DOWN, LARGE_BUFF)))
            if i == 40:
                lines[i][0][16:21].set_color(BLUE)
                lines[i][0][70:76].set_color(BLUE)
                lines[i][0][140:145].set_color(BLUE)
                arrows[0].replace(Line(lines[i][0][16:21].get_corner(DL), lines[i][0][16:21].get_corner(UR),
                                       color=YELLOW))
                arrows[1].replace(Line(lines[i][0][70:76].get_corner(DL), lines[i][0][70:76].get_corner(UR),
                                       color=YELLOW))
                arrows[2].replace(Line(lines[i][0][140:145].get_corner(DL), lines[i][0][140:145].get_corner(UR),
                                       color=YELLOW))
                tempText = MathTex(r"-159u^{2}y", font_size=50, color=YELLOW).next_to(lines[i][0][16:21].get_corner(UR),
                                                                                      UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 41:
                lines[i][0][23:28].set_color(BLUE)
                lines[i][0][81:88].set_color(BLUE)
                lines[i][0][114:120].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][23:28].get_corner(DL), lines[i][0][23:28].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][81:88].get_corner(DL), lines[i][0][81:88].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][114:120].get_corner(DL), lines[i][0][114:120].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"124u^{2}x", font_size=50, color=YELLOW).next_to(lines[i][0][23:28].get_corner(UR),
                                                                                     UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 42:
                lines[i][0][30:36].set_color(BLUE)
                lines[i][0][87:94].set_color(BLUE)
                lines[i][0][121:127].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][30:36].get_corner(DL), lines[i][0][30:36].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][87:94].get_corner(DL), lines[i][0][87:94].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][121:127].get_corner(DL), lines[i][0][121:127].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"1091uxy", font_size=50, color=YELLOW).next_to(lines[i][0][30:36].get_corner(UR),
                                                                                   UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 43:
                lines[i][0][40:44].set_color(BLUE)
                lines[i][0][68:73].set_color(BLUE)
                lines[i][0][101:107].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][40:44].get_corner(DL), lines[i][0][40:44].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][68:73].get_corner(DL), lines[i][0][68:73].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][101:107].get_corner(DL), lines[i][0][101:107].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"100u^{2}", font_size=50, color=YELLOW).next_to(lines[i][0][40:44].get_corner(UR),
                                                                                    UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 44:
                lines[i][0][46:51].set_color(BLUE)
                lines[i][0][68:74].set_color(BLUE)
                lines[i][0][100:107].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][46:51].get_corner(DL), lines[i][0][46:51].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][68:74].get_corner(DL), lines[i][0][68:74].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][100:107].get_corner(DL), lines[i][0][100:107].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"2207uy", font_size=50, color=YELLOW).next_to(lines[i][0][46:51].get_corner(UR),
                                                                                  UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 45:
                lines[i][0][53:58].set_color(BLUE)
                lines[i][0][71:77].set_color(BLUE)
                lines[i][0][88:93].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][53:58].get_corner(DL), lines[i][0][53:58].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][71:77].get_corner(DL), lines[i][0][71:77].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][88:93].get_corner(DL), lines[i][0][88:93].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"-2052ux", font_size=50, color=YELLOW).next_to(lines[i][0][53:58].get_corner(UR),
                                                                                   UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 46:
                lines[i][0][58:65].set_color(BLUE)
                lines[i][0][65:72].set_color(BLUE)
                lines[i][0][72:79].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][58:65].get_corner(DL), lines[i][0][58:65].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][65:72].get_corner(DL), lines[i][0][65:72].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][72:79].get_corner(DL), lines[i][0][72:79].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"-19227xy", font_size=50, color=YELLOW).next_to(lines[i][0][58:65].get_corner(UR),
                                                                                    UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            else:
                self.wait(0.25)

        self.play(Create(arrowsDet[3]))
        self.play(Write(labels[3]))
        self.wait(0.3)
        self.play(Write(lines[48].next_to(lines[47], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[48], lines[49].next_to(lines[47], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[49], lines[50].next_to(lines[47], DOWN, LARGE_BUFF)))

        self.play(Create(arrowsDet[4]))
        self.play(Write(labels[4]))
        self.wait(0.3)
        self.play(Write(lines[51].next_to(lines[50], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[51], lines[52].next_to(lines[50], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[52], lines[53].next_to(lines[50], DOWN, LARGE_BUFF)))

        self.play(Create(arrowsDet[5]))
        self.play(Write(labels[5]))
        self.wait(0.3)
        self.play(Write(lines[54].next_to(lines[53], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[54], lines[55].next_to(lines[53], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[55], lines[56].next_to(lines[53], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(lines[50], lines[53]), ReplacementTransform(lines[56],
                                                                      lines[57].next_to(lines[47], DOWN, LARGE_BUFF)))
        lines[57][0][11:16].set_color(BLUE)
        lines[57][0][69:73].set_color(BLUE)
        lines[57][0][123:128].set_color(BLUE)
        arrows = VGroup(
            Line(lines[57][0][11:16].get_corner(DL), lines[57][0][11:16].get_corner(UR), color=YELLOW),
            Line(lines[57][0][69:73].get_corner(DL), lines[57][0][69:73].get_corner(UR), color=YELLOW),
            Line(lines[57][0][123:128].get_corner(DL), lines[57][0][123:128].get_corner(UR), color=YELLOW)
        )
        tempText = MathTex(r"-24u^{3}", font_size=50, color=YELLOW).next_to(lines[57][0][11:16].get_corner(UR), UP,
                                                                            SMALL_BUFF)

        self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
        self.play(Write(tempText))
        self.wait(0.25)
        self.play(FadeOut(tempText, arrows))

        for i in range(58, 66):
            self.play(ReplacementTransform(lines[i - 1], lines[i].next_to(lines[47], DOWN, LARGE_BUFF)))
            if i == 58:
                lines[i][0][17:23].set_color(BLUE)
                lines[i][0][75:80].set_color(BLUE)
                lines[i][0][140:145].set_color(BLUE)
                arrows[0].replace(Line(lines[i][0][17:23].get_corner(DL), lines[i][0][17:23].get_corner(UR),
                                       color=YELLOW))
                arrows[1].replace(Line(lines[i][0][75:80].get_corner(DL), lines[i][0][75:80].get_corner(UR),
                                       color=YELLOW))
                arrows[2].replace(Line(lines[i][0][140:145].get_corner(DL), lines[i][0][140:145].get_corner(UR),
                                       color=YELLOW))
                tempText = MathTex(r"-87u^{2}y", font_size=50, color=YELLOW).next_to(lines[i][0][17:23].get_corner(UR),
                                                                                     UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 59:
                lines[i][0][23:28].set_color(BLUE)
                lines[i][0][81:87].set_color(BLUE)
                lines[i][0][112:117].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][23:28].get_corner(DL), lines[i][0][23:28].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][81:87].get_corner(DL), lines[i][0][81:87].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][114:120].get_corner(DL), lines[i][0][112:117].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"76u^{2}x", font_size=50, color=YELLOW).next_to(lines[i][0][23:28].get_corner(UR),
                                                                                    UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 60:
                lines[i][0][28:34].set_color(BLUE)
                lines[i][0][87:93].set_color(BLUE)
                lines[i][0][120:127].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][28:34].get_corner(DL), lines[i][0][28:34].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][87:93].get_corner(DL), lines[i][0][87:93].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][120:127].get_corner(DL), lines[i][0][120:127].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"1091uxy", font_size=50, color=YELLOW).next_to(lines[i][0][28:34].get_corner(UR),
                                                                                   UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 61:
                lines[i][0][38:44].set_color(BLUE)
                lines[i][0][69:73].set_color(BLUE)
                lines[i][0][100:105].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][38:44].get_corner(DL), lines[i][0][38:44].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][69:73].get_corner(DL), lines[i][0][69:73].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][100:105].get_corner(DL), lines[i][0][100:105].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"544u^{2}", font_size=50, color=YELLOW).next_to(lines[i][0][38:44].get_corner(UR),
                                                                                    UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 62:
                lines[i][0][44:51].set_color(BLUE)
                lines[i][0][68:74].set_color(BLUE)
                lines[i][0][102:109].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][44:51].get_corner(DL), lines[i][0][44:51].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][68:74].get_corner(DL), lines[i][0][68:74].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][102:109].get_corner(DL), lines[i][0][102:109].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"2207uy", font_size=50, color=YELLOW).next_to(lines[i][0][44:51].get_corner(UR),
                                                                                  UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 63:
                lines[i][0][51:56].set_color(BLUE)
                lines[i][0][69:75].set_color(BLUE)
                lines[i][0][87:93].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][51:56].get_corner(DL), lines[i][0][51:56].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][69:75].get_corner(DL), lines[i][0][69:75].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][87:93].get_corner(DL), lines[i][0][87:93].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"-2052ux", font_size=50, color=YELLOW).next_to(lines[i][0][51:56].get_corner(UR),
                                                                                   UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 64:
                lines[i][0][56:63].set_color(BLUE)
                lines[i][0][64:70].set_color(BLUE)
                lines[i][0][71:77].set_color(BLUE)
                arrows[0].replace(
                    Line(lines[i][0][56:63].get_corner(DL), lines[i][0][56:63].get_corner(UR), color=YELLOW))
                arrows[1].replace(
                    Line(lines[i][0][64:70].get_corner(DL), lines[i][0][64:70].get_corner(UR), color=YELLOW))
                arrows[2].replace(
                    Line(lines[i][0][71:77].get_corner(DL), lines[i][0][71:77].get_corner(UR), color=YELLOW))
                tempText = MathTex(r"-19227xy", font_size=50, color=YELLOW).next_to(lines[i][0][56:63].get_corner(UR),
                                                                                    UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            else:
                self.wait(0.25)
        self.wait(0.3)
        self.play(FadeOut(lines[65]),
                  ReplacementTransform(lines[47], lines[66].next_to(lines[29], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        for i in range(67, 77):
            self.play(ReplacementTransform(lines[i - 1], lines[i].next_to(lines[29], DOWN, LARGE_BUFF)))
            if i == 67:
                lines[i][0][1:6].set_color(BLUE)
                lines[i][0][59:64].set_color(BLUE)
                arrows = VGroup(
                    Line(lines[i][0][1:6].get_corner(DL), lines[i][0][1:6].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][59:64].get_corner(DL), lines[i][0][59:64].get_corner(UR),
                         color=YELLOW)
                )
                tempText = MathTex(r"12u^{3}", font_size=50, color=YELLOW).next_to(lines[i][0][1:6].get_corner(UR),
                                                                                   UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 68:
                lines[i][0][6:13].set_color(BLUE)
                lines[i][0][59:65].set_color(BLUE)
                arrows = VGroup(
                    Line(lines[i][0][6:13].get_corner(DL), lines[i][0][6:13].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][59:65].get_corner(DL), lines[i][0][59:65].get_corner(UR),
                         color=YELLOW)
                )
                tempText = MathTex(r"-72u^{2}y", font_size=50, color=YELLOW).next_to(lines[i][0][6:13].get_corner(UR),
                                                                                     UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 69:
                lines[i][0][12:18].set_color(BLUE)
                lines[i][0][57:62].set_color(BLUE)
                arrows = VGroup(
                    Line(lines[i][0][12:18].get_corner(DL), lines[i][0][12:18].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][57:62].get_corner(DL), lines[i][0][57:62].get_corner(UR),
                         color=YELLOW)
                )
                tempText = MathTex(r"48u^{2}x", font_size=50, color=YELLOW).next_to(lines[i][0][12:18].get_corner(UR),
                                                                                    UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 70:
                lines[i][0][18:25].set_color(BLUE)
                lines[i][0][56:63].set_color(BLUE)
                arrows = VGroup(
                    Line(lines[i][0][18:25].get_corner(DL), lines[i][0][18:25].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][56:63].get_corner(DL), lines[i][0][56:63].get_corner(UR),
                         color=YELLOW)
                )
                tempText = MathTex(r"0", font_size=50, color=YELLOW).next_to(lines[i][0][18:25].get_corner(UR),
                                                                             UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 71:
                lines[i][0][18:23].set_color(BLUE)
                lines[i][0][48:53].set_color(BLUE)
                arrows = VGroup(
                    Line(lines[i][0][18:23].get_corner(DL), lines[i][0][18:23].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][48:53].get_corner(DL), lines[i][0][48:53].get_corner(UR),
                         color=YELLOW)
                )
                tempText = MathTex(r"-444u^{2}", font_size=50, color=YELLOW).next_to(lines[i][0][18:23].get_corner(UR),
                                                                                     UP, SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 72:
                lines[i][0][24:30].set_color(BLUE)
                lines[i][0][31:37].set_color(BLUE)
                lines[i][0][38:45].set_color(BLUE)
                lines[i][0][48:54].set_color(BLUE)
                lines[i][0][55:61].set_color(BLUE)
                lines[i][0][62:69].set_color(BLUE)
                arrows = VGroup(
                    Line(lines[i][0][24:30].get_corner(DL), lines[i][0][24:30].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][31:37].get_corner(DL), lines[i][0][31:37].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][38:45].get_corner(DL), lines[i][0][38:45].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][48:54].get_corner(DL), lines[i][0][48:54].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][55:61].get_corner(DL), lines[i][0][55:61].get_corner(UR), color=YELLOW),
                    Line(lines[i][0][62:69].get_corner(DL), lines[i][0][62:69].get_corner(UR), color=YELLOW)
                )
                tempText = VGroup(
                    MathTex(r"0", font_size=50, color=YELLOW).next_to(lines[i][0][24:30].get_corner(UR),
                                                                      UP, SMALL_BUFF),
                    MathTex(r"0", font_size=50, color=YELLOW).next_to(lines[i][0][31:37].get_corner(UR),
                                                                      UP, SMALL_BUFF),
                    MathTex(r"0", font_size=50, color=YELLOW).next_to(lines[i][0][38:45].get_corner(UR),
                                                                      UP, SMALL_BUFF),
                )
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]), Create(arrows[3]),
                          Create(arrows[4]), Create(arrows[5]))
                self.play(Write(tempText[0]), Write(tempText[1]), Write(tempText[2]))
                self.wait(0.25)
                self.play(FadeOut(tempText, arrows))
            elif i == 73:
                lines[i][0][:4].set_color(YELLOW)
                lines[i][0][5:9].set_color(YELLOW)
                lines[i][0][11:15].set_color(YELLOW)
                lines[i][0][17:22].set_color(YELLOW)
            elif i == 75:
                lines[i][0][2:6].set_color(YELLOW)
                lines[i][0][7:11].set_color(BLUE)
                lines[i][0][-8:].set_color(BLUE)
                arrows = VGroup(
                    Arrow(lines[i][0][2:6].get_corner(DL), lines[i][0][2:6].get_corner(UR), color=BLUE),
                    Arrow(lines[i][0][7:11].get_corner(DL), lines[i][0][7:11].get_corner(UR), color=YELLOW),
                    Arrow(lines[i][0][-8:].get_corner(DL), lines[i][0][-8:].get_corner(UR), color=YELLOW)
                )
                tempText = MathTex(r"0", font_size=50, color=YELLOW).next_to(lines[i][0][-8:].get_corner(UR), UP,
                                                                             SMALL_BUFF)
                self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]))
                self.play(Write(tempText))
                self.wait(0.25)
                self.play(FadeOut(arrows, tempText))
            self.wait(0.25)
        lines[77].move_to(UP * 3)
        self.play(FadeOut(arrowsDet, lines[29], labels))
        self.play(ReplacementTransform(lines[27], lines[77]),
                  ReplacementTransform(lines[76], lines[78].next_to(lines[77], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        lines[79].move_to(UP * 3)
        self.play(ReplacementTransform(lines[77], lines[79]))
        boxRectangle = SurroundingRectangle(lines[78], buff=0.3)
        self.play(Create(boxRectangle))
        self.wait(1.25)
        self.play(FadeOut(boxRectangle, lines[79], lines[78]))
