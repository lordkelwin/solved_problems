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
            MathTex(r"S_{1}+S_{2}+S_{3}=\left[(2u^{3}+13u^{2}y+34u^{2}x+221uxy)-\\(58u^{2}+377uy+986ux+6409xy)\right]+"
                    r"\left[(-20u^{3}+260u^{2}-85u^{2}y+1105uy)-\\(-116u^{2}x+1508ux-493uxy+6409xy)\right]+"
                    r"\left[(6u^{3}-26u^{2}x-102u^{2}+442ux)-\\(87u^{2}y-377uxy-1479uy+6409xy)\right]", font_size=60),
            MathTex(r"S_{1}+S_{2}+S_{3}=-12u^{3}+\left[13u^{2}y+34u^{2}x+221uxy)-\\(58u^{2}+377uy+986ux+6409xy)\right]+"
                    r"\left[(260u^{2}-85u^{2}y+1105uy)-\\(-116u^{2}x+1508ux-493uxy+6409xy)\right]+"
                    r"\left[(-26u^{2}x-102u^{2}+442ux)-\\(87u^{2}y-377uxy-1479uy+6409xy)\right]", font_size=60),
            MathTex(r"S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+\left[34u^{2}x+221uxy)-\\"
                    r"(58u^{2}+377uy+986ux+6409xy)\right]+\left[(260u^{2}+1105uy)-\\(-116u^{2}x+1508ux-493uxy+6409xy)"
                    r"\right]+\left[(-26u^{2}x-102u^{2}+442ux)-\\(377uxy-1479uy+6409xy)\right]", font_size=60),
            MathTex(r"S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+\left[221uxy-\\"
                    r"(58u^{2}+377uy+986ux+6409xy)\right]+\left[(260u^{2}+1105uy)-\\(1508ux-493uxy+6409xy)"
                    r"\right]+\left[(-102u^{2}+442ux)-\\(377uxy-1479uy+6409xy)\right]", font_size=60),
            MathTex(r"S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+\left[-\\"
                    r"(58u^{2}+377uy+986ux+6409xy)\right]+\left[(260u^{2}+1105uy)-\\(1508ux+6409xy)"
                    r"\right]+\left[(-102u^{2}+442ux)-\\(-1479uy+6409xy)\right]", font_size=60),
            MathTex(r"S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+\left[-\\"
                    r"(377uy+986ux+6409xy)\right]+\left[1105uy-\\(1508ux+6409xy)"
                    r"\right]+\left[442ux-\\(-1479uy+6409xy)\right]", font_size=60),
            MathTex(r"S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+2207uy+\left[-\\"
                    r"(986ux+6409xy)\right]+\left[-(1508ux+6409xy)"
                    r"\right]+\left[442ux-6409xy\right]", font_size=60),
            MathTex(r"S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+1091uxy+100u^{2}+2207uy-2052ux+(-"
                    r"6409xy-6409xy-6409xy)", font_size=60),
            MathTex(r"S_{1}+S_{2}+S_{3}=-12u^{3}-159u^{2}y+124u^{2}x+\\1091uxy+100u^{2}+2207uy-2052ux-19227xy",
                    font_size=60),
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
            self.play(ReplacementTransform(lines[i-1], lines[i].next_to(lines[12], DOWN, LARGE_BUFF)))
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
            self.play(ReplacementTransform(lines[i-1], lines[i].next_to(lines[16], DOWN, MED_LARGE_BUFF)))
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
                lines[i][0][71].set_color(BLUE)
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
        self.play(lines[27].animate.shift(5 * UP), lines[29].animate.shift(5 * UP))
        self.wait(0.25)
        arrows = VGroup(
            Arrow(lines[29][0][6:12].get_center(), lines[29][0][52:56].get_center(), color=BLUE),
            Arrow(lines[29][0][12:19], lines[29][0][88:94].get_center(), color=BLUE),
            Arrow(lines[29][0][19:23], lines[29][0][94:100].get_center(), color=BLUE),
            Arrow(lines[29][0][40:46].get_center(), lines[29][0][19:23].get_center(), color=YELLOW),
            Arrow(lines[29][0][46:52].get_center(), lines[29][0][62:68].get_center(), color=YELLOW),
            Arrow(lines[29][0][52:56].get_center(), lines[29][0][68:75].get_center(), color=YELLOW)
        )

        labels = VGroup(
            MathTex(r"S_{1}", font_size=40, color=YELLOW).next_to(lines[29][0][52:56].get_corner(DR), DOWN, MED_SMALL_BUFF),
            MathTex(r"S_{2}", font_size=40, color=YELLOW).next_to(lines[29][0][88:94].get_corner(DR), DOWN, MED_SMALL_BUFF),
            MathTex(r"S_{3}", font_size=40, color=YELLOW).next_to(lines[29][0][94:100].get_corner(DR), DOWN, MED_SMALL_BUFF),
            MathTex(r"S_{4}", font_size=40, color=BLUE).next_to(lines[29][0][19:23].get_corner(UR), UP, MED_SMALL_BUFF),
            MathTex(r"S_{5}", font_size=40, color=BLUE).next_to(lines[29][0][62:68].get_corner(UR), UP, MED_SMALL_BUFF),
            MathTex(r"S_{6}", font_size=40, color=BLUE).next_to(lines[29][0][68:75].get_corner(UR), UP, MED_SMALL_BUFF)
        )

        self.play(Create(arrows[0]))
        self.play(Write(labels[0]))
        self.wait(0.3)
        self.play(Write(lines[30].next_to(lines[29], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[30], lines[31].next_to(lines[29], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[31], lines[32].next_to(lines[29], DOWN, LARGE_BUFF)))

        self.play(Create(arrows[1]))
        self.play(Write(labels[1]))
        self.wait(0.3)
        self.play(Write(lines[33].next_to(lines[32], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[33], lines[34].next_to(lines[32], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[34], lines[35].next_to(lines[32], DOWN, LARGE_BUFF)))

        self.play(Create(arrows[2]))
        self.play(Write(labels[2]))
        self.wait(0.3)
        self.play(Write(lines[36].next_to(lines[35], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[36], lines[37].next_to(lines[35], DOWN, LARGE_BUFF)))
        self.wait(0.25)
        self.play(ReplacementTransform(lines[37], lines[38].next_to(lines[35], DOWN, LARGE_BUFF)))

        self.wait(1.25)
