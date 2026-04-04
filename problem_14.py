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
            else:
                self.wait(0.4)
        self.wait(1.25)
