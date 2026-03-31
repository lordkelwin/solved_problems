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
        MathTex.set_default(font_size=70)

        ax = Axes(x_range=[-7, 5, 1], y_range=[0, 15, 1], x_length=12, y_length=15)
        dots = VGroup(
            Dot(color=BLUE, radius=0.15).move_to(ax.c2p(2, 3)),
            Dot(color=YELLOW, radius=0.15).move_to(ax.c2p(3, 4)),
            Dot(color=RED, radius=0.15).move_to(ax.c2p(-1, 2)),
            Dot(color=GOLD, radius=0.15).move_to(ax.c2p(-1, 7))
        )

        arrow = VGroup(
            CurvedArrow(ax.c2p(4, 15), ax.c2p(1.12, 11.53), color=YELLOW),
            Arrow(ax.c2p(-1, 7), ax.c2p(4, 7), color=BLUE)
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
            lambda t: np.array([5 * np.cos(t) - 1, 5 * np.sin(t) + 7, 0]),
            t_range=[0, 2 * PI]
        )

        self.play(Create(dots[3]))
        self.play(Write(labels[3]))
        self.play(Create(arrow[1]))
        self.play(Rotate(arrow[1], angle=2 * PI, about_point=arrow[1].get_start()), Create(circle))
        self.play(Write(labels[5]))
        self.wait(0.3)
        self.play(Create(arrow[0]))
        self.play(Write(labels[4]))
        self.wait(1.5)
        self.play(FadeOut(circle, ax, dots, labels, arrow))

        solutions = VGroup(
            Tex(r"\begin{minipage}{5cm}"
                r"For a circle, its standard form is:"
                r"\end{minipage}"),
            MathTex(r"Ax^{2}+Cy^{2}+Dx+Ey+F=0"),
            Tex(r"Assuming $A=C=1$:"),
            MathTex(r"x^{2}+y^{2}+Dx+Ey+F=0"),
            Tex(r"\begin{minipage}{5cm}"
                r"To solve for the variables $D$, $E$, and $F$, substitute the given points:"
                r"\end{minipage}"),
            Tex(r"if $x=2$, $y=3$:"),
            MathTex(r"(2)^{2}+(3)^{2}+D(2)+E(3)+F=0"),
            MathTex(r"4+9+2D+3E+F=0"),
            MathTex(r"13+2D+3E+F=0"),
            MathTex(r"2D+3E+F=-13"),
            Tex(r"(eq. 1)", font_size=60),
            Tex(r"if $x=3$, $y=4$:"),
            MathTex(r"(3)^{2}+(4)^{2}+D(3)+E(4)+F=0"),
            MathTex(r"9+16+3D+4E+F=0"),
            MathTex(r"25+3D+4E+F=0"),
            MathTex(r"3D+4E+F=-25"),
            Tex(r"(eq. 2)", font_size=60),
            Tex(r"if $x=-1$, $y=2$:"),
            MathTex(r"(-1)^{2}+(2)^{2}+D(-1)+E(2)+F=0"),
            MathTex(r'1+4-D+2E+F=0'),
            MathTex(r"5-D+2E+F=0"),
            MathTex(r"-D+2E+F=-5"),
            Tex(r"(eq. 3)", font_size=60),
            Tex(r"Using Cramer's Rule to solve\\ for the variables:"),
            MathTex(r"C=\frac{\Delta_{C}}{\Delta}"),
            MathTex(r"D=\frac{\Delta_{D}}{\Delta}"),
            MathTex(r"F=\frac{\Delta_{F}}{\Delta}"),
            Tex(r"Where:"),
            MathTex(r"\Delta = \begin{vmatrix}"
                    r"2 & 3 & 1 \\ 3 & 4 & 1 \\ -1 & 2 & 1"
                    r"\end{vmatrix}"),
            MathTex(r"\Delta_{C} = \begin{vmatrix}"
                    r"-13 & 3 &  1 \\ -25 & 4 & 1 \\ -5 & 2 & 1"
                    r"\end{vmatrix}"),
            MathTex(r"\Delta_{D} = \begin{vmatrix}"
                    r"2 & -13 & 1 \\ 3 & -25 & 1 \\ -1 & -5 & 1"
                    r"\end{vmatrix}"),
            MathTex(r"\Delta_{F} = \begin{vmatrix}"
                    r"2 & 3 & -13 \\ 3 & 4 & -25 \\ -1 & 2  & -5"
                    r"\end{vmatrix}}"),
            Tex(r"Solving the determinant in every matrix:"),
            MathTex(r"\Delta = \begin{vmatrix}"
                    r"2 & 3 & 1 \\ 3 & 4 & 1 \\ -1 & 2 & 1"
                    r"\end{vmatrix}"
                    r"\begin{matrix}"
                    r"2 & 3 \\ 3 & 4 \\ -1 & 2"
                    r"\end{matrix}"),
            MathTex(r"\Delta = [(2)(4)(1)]"),
            MathTex(r"\Delta = [8+(3)(1)(-1)]"),
            MathTex(r"\Delta = [8+(-3)+(1)(3)(2)]"),
            MathTex(r"\Delta = [8-3+6] - [(-1)(4)(1)]"),
            MathTex(r"\Delta = 11 - [-4+(2)(1)(2)]"),
            MathTex(r"\Delta = 11 - [-4+4+(1)(3)(3)]"),
            MathTex(r"\Delta = 11-[-4+4+9]"),
            MathTex(r"\Delta = 11 - 9"),
            MathTex(r"\Delta = 2"),
            MathTex(r"\Delta_{C} = \begin{vmatrix}"
                    r"-13 & 3 &  1 \\ -25 & 4 & 1 \\ -5 & 2 & 1"
                    r"\end{vmatrix}"
                    r"\begin{matrix}"
                    r"-13 & 3 \\ -25 & 4 \\ -5 & 2"
                    r"\end{matrix}"),
            MathTex(r"\Delta_{C} = [(-13)(4)(1)]"),
            MathTex(r"\Delta_{C} = [-52+(3)(1)(-5)]"),
            MathTex(r"\Delta_{C} = [-52-15+(1)(-25)(2)]"),
            MathTex(r"\Delta_{C} = [-52-15-50] - [(-5)(4)(1)]"),
            MathTex(r"\Delta_{C} = -117 - [-20+(2)(1)(-13)]"),
            MathTex(r"\Delta_{C} = -117 - [-20-26+(1)(-25)(3)]"),
            MathTex(r"\Delta_{C} = -117 - [-20-26-75]"),
            MathTex(r"\Delta_{C} = -117-(-121)"),
            MathTex(r"\Delta_{C} = -117+121"),
            MathTex(r"\Delta_{C} = 4"),
            MathTex(r"\Delta_{D} = \begin{vmatrix}"
                    r"-2 & -13 &  1 \\ 3 & -25 & 1 \\ -1 & -5 & 1"
                    r"\end{vmatrix}"
                    r"\begin{matrix}"
                    r"-2 & -13 \\ 3 & -25 \\ -1 & -5"
                    r"\end{matrix}"),
            MathTex(r"\Delta_{D} = [(2)(-25)(1)]"),
            MathTex(r"\Delta_{D} = [-50+(-13)(1)(-1)]"),
            MathTex(r"\Delta_{D} = [-50+13+(1)(3)(-5)]"),
            MathTex(r"\Delta_{D} = [-50+13-15] - [(-1)(-25)(1)]"),
            MathTex(r"\Delta_{D} = -52 - [25+(-5)(1)(2)]"),
            MathTex(r"\Delta_{D} = -52 - [25-10+(1)(3)(-13)]"),
            MathTex(r"\Delta_{D} = -52 -[25-10-39]"),
            MathTex(r"\Delta_{D} = -52+24"),
            MathTex(r"\Delta_{D} = -28"),
            MathTex(r"\Delta_{F} = \begin{vmatrix}"
                    r"-2 & 3 & -13 \\ 3 & 4 & -25 \\ -1 & 2 & -5"
                    r"\end{vmatrix}"
                    r"\begin{matrix}"
                    r"-2 & 3 \\ 3 & 4 \\ -1 & 2"
                    r"\end{matrix}"),
            MathTex(r"\Delta_{F} = [(2)(4)(-5)]"),
            MathTex(r"\Delta_{F} = [-40+(3)(-25)(-1)]"),
            MathTex(r"\Delta_{F} = [-40+75+(-13)(3)(2)]"),
            MathTex(r"\Delta_{F} = [-40+75-78] - [(-1)(4)(-13)]"),
            MathTex(r"\Delta_{F} = -43 - [52+(2)(-25)(2)]"),
            MathTex(r"\Delta_{F} = -43 - [52-100+(-5)(3)(3)]"),
            MathTex(r"\Delta_{F} = -43 -[52-100-45]"),
            MathTex(r"\Delta_{F} = -43-(-93)"),
            MathTex(r"\Delta_{F} = -43+93"),
            MathTex(r"\Delta_{F} = 50"),
            Tex(r"Substituting the values \\of the determinant:"),
            MathTex(r"C=\frac{\Delta_{C}}{\Delta}"),
            MathTex(r"C=\frac{4}{2}"),
            MathTex(r"C=2"),
            MathTex(r"D=\frac{\Delta_{D}}{\Delta}"),
            MathTex(r"D=\frac{-28}{2}"),
            MathTex(r"D=-14"),
            MathTex(r"F=\frac{\Delta_{F}}{\Delta}"),
            MathTex(r"F=\frac{50}{2}"),
            MathTex(r"F=25"),
            Tex(r"Substituting the values:"),
            MathTex(r"x^{2}+y^{2}+2x-14y+25=0"),
            Tex(r"\begin{minipage}{5cm}"
                r"Determining the location of the center of the circle and its radius:"
                r"\end{minipage}"),
            MathTex(r"x^{2}+y^{2}+2x-14y+25=0"),
            MathTex(r"\left(x^{2}+2x\right)+\left(y^{2}-14y\right)=-25"),
            Tex(r"Using the Completing the squares:"),
            MathTex(r"C=\frac{b^{2}}{4a}"),
            MathTex(r"C_{x}=\frac{2^{2}}{4(1)}"),
            MathTex(r"C_{x}=\frac{4}{4}"),
            MathTex(r"C_{x}=1"),
            MathTex(r"C_{y}=\frac{(-14)^{2}}{4(1)}"),
            MathTex(r"C_{y}=\frac{196}{4}"),
            MathTex(r"C_{y}=49"),
            Tex(r"Adding both sides by $C_{x}$ and $C_{y}$:"),
            MathTex(r"\left(x^{2}+2x+C_{x}\right)+\left(y^{2}-14y+C_{y}\right)=-25+C_{x}+C_{y}"),
            MathTex(r"\left(x^{2}+2x+1\right)+\left(y^{2}-14y+49\right)=-25+1+49"),
            MathTex(r"\left(x^{2}+2x+1\right)+\left(y^{2}-14y+49\right)=25"),
            MathTex(r"(x+1)^{2}+(y-7)^{2}=5^{2}"),
            Tex(r"Based on the Center-Radius\\ Form of the Circle:"),
            MathTex(r"(x-h)^{2}+(y-k)^{2}=r^{2}"),
            Tex(r"Where: $C(h,k)$ is the location of\\ the center of circle"),
            Tex(r"$r$ is the length of radius\\ of the circle"),
            Tex(r"Therefore:"),
            MathTex(r"Center C(1,-7)"),
            MathTex(r"Radius r=5")
        )

        solutions[0].move_to(6 * UP)
        self.play(Write(solutions[0]))
        for i in range(1, 4):
            self.play(Write(solutions[i].next_to(solutions[i - 1], DOWN, LARGE_BUFF)))
            self.wait(0.3)
        self.wait(1.25)

        self.play(FadeOut(solutions[:4]))

        solutions[4].move_to(8 * UP)
        self.play(Write(solutions[4]))
        self.wait(0.3)
        self.play(Write(solutions[5].next_to(solutions[4], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutions[6].next_to(solutions[5], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(7, 10):
            self.play(ReplacementTransform(solutions[i - 1], solutions[i].next_to(solutions[5], DOWN, LARGE_BUFF)))
            if i == 7:
                solutions[i][0][:3].set_color(BLUE)
                arrow = Arrow(solutions[i][0][:3].get_corner(DL),
                              solutions[i][0][:3].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"13", font_size=50)
                self.play(Create(arrow))
                self.play(Write(tempText.next_to(solutions[i][0][:3].get_corner(UR), UP, SMALL_BUFF)))
                self.play(FadeOut(arrow, tempText, run_time=0.3))
            elif i == 8:
                solutions[i][0][:2].set_color(BLUE)
                arrow = CurvedArrow(solutions[i][0][:2].get_bottom(),
                                    solutions[i][0][-1].get_bottom(), color=YELLOW)
                self.play(Create(arrow))
                self.wait(0.2)
                self.play(FadeOut(arrow, run_time=0.3))
            else:
                self.wait(0.5)
        BoxRectangle = VGroup(
            SurroundingRectangle(solutions[9], buff=0.3)
        )
        self.play(Create(BoxRectangle[0]))
        self.play(Write(solutions[10].next_to(solutions[9], RIGHT, LARGE_BUFF)))

        self.play(Write(solutions[11].next_to(solutions[9], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutions[12].next_to(solutions[11], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(13, 16):
            self.play(ReplacementTransform(solutions[i - 1], solutions[i].next_to(solutions[11], DOWN, LARGE_BUFF)))
            if i == 13:
                solutions[i][0][:4].set_color(BLUE)
                arrow = Arrow(solutions[i][0][:4].get_corner(DL),
                              solutions[i][0][:4].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"25", font_size=50)
                self.play(Create(arrow))
                self.play(Write(tempText.next_to(solutions[i][0][:4].get_corner(UR), UP, SMALL_BUFF)))
                self.play(FadeOut(arrow, tempText, run_time=0.3))
            elif i == 14:
                solutions[i][0][:2].set_color(BLUE)
                arrow = CurvedArrow(solutions[i][0][:2].get_bottom(),
                                    solutions[i][0][-1].get_bottom(), color=YELLOW)
                self.play(Create(arrow))
                self.wait(0.2)
                self.play(FadeOut(arrow, run_time=0.3))
            else:
                self.wait(0.5)
        BoxRectangle.add(SurroundingRectangle(solutions[15], buff=0.3))
        self.play(Create(BoxRectangle[1]))
        self.play(Write(solutions[16].next_to(solutions[15], RIGHT, LARGE_BUFF)))

        self.play(Write(solutions[17].next_to(solutions[15], DOWN, LARGE_BUFF)))
        self.wait(0.1)
        self.play(Write(solutions[18].next_to(solutions[17], DOWN, LARGE_BUFF)))
        self.wait(0.2)
        for i in range(19, 22):
            self.play(ReplacementTransform(solutions[i - 1], solutions[i].next_to(solutions[17], DOWN, LARGE_BUFF)))
            if i == 19:
                solutions[i][0][:3].set_color(BLUE)
                arrow = Arrow(solutions[i][0][:3].get_corner(DL),
                              solutions[i][0][:3].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"5", font_size=50)
                self.play(Create(arrow))
                self.play(Write(tempText.next_to(solutions[i][0][:3].get_corner(UR), UP, SMALL_BUFF)))
                self.play(FadeOut(arrow, tempText, run_time=0.3))
            elif i == 20:
                solutions[i][0][0].set_color(BLUE)
                arrow = CurvedArrow(solutions[i][0][0].get_bottom(),
                                    solutions[i][0][-1].get_bottom(), color=YELLOW)
                self.play(Create(arrow))
                self.wait(0.2)
                self.play(FadeOut(arrow))
            else:
                self.wait(0.2)
        BoxRectangle.add(SurroundingRectangle(solutions[21], buff=0.3))
        self.play(Create(BoxRectangle[2]))
        self.play(Write(solutions[22].next_to(solutions[21], RIGHT, LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(solutions[4:6], solutions[11], solutions[17], BoxRectangle))
        self.play(solutions[9].animate.shift(5 * UP), solutions[10].animate.shift(5 * UP),
                  solutions[15].animate.shift(7 * UP), solutions[16].animate.shift(7 * UP),
                  solutions[21].animate.shift(9 * UP), solutions[22].animate.shift(9 * UP))
        self.play(Write(solutions[23].next_to(solutions[21], DOWN, LARGE_BUFF)))
        self.play(Write(solutions[24].next_to(solutions[23], DOWN, LARGE_BUFF)),
                  Write(solutions[25].next_to(solutions[24], DOWN, LARGE_BUFF)),
                  Write(solutions[26].next_to(solutions[25], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(solutions[24:27]))
        self.play(Write(solutions[27].next_to(solutions[23], DOWN, MED_LARGE_BUFF)))
        self.play(Write(solutions[28].next_to(solutions[27], DOWN, MED_LARGE_BUFF)),
                  Write(solutions[29].next_to(solutions[28], DOWN, MED_LARGE_BUFF).set_color(BLUE)),
                  Write(solutions[30].next_to(solutions[29], DOWN, MED_LARGE_BUFF).set_color(YELLOW)),
                  Write(solutions[31].next_to(solutions[30], DOWN, MED_LARGE_BUFF).set_color(RED)))
        self.wait(0.5)
        self.play(FadeOut(solutions[29:32], solutions[27], solutions[23], solutions[9],
                          solutions[10], solutions[15], solutions[16], solutions[21], solutions[22]))
        self.play(solutions[28].animate.shift(3 * UP))
        solutions[33].move_to(solutions[28].get_center())
        self.play(Write(solutions[32].next_to(solutions[28], UP, LARGE_BUFF)))
        self.play(ReplacementTransform(solutions[28], solutions[33]))
        arrowDelta = VGroup(
            Arrow(solutions[33][0][8].get_corner(UL), solutions[33][0][17].get_corner(DR), color=YELLOW),
            Arrow(solutions[33][0][9].get_corner(UR), solutions[33][0][28:30].get_corner(DR), color=YELLOW),
            Arrow(solutions[33][0][10].get_corner(UR), solutions[33][0][30].get_corner(DR), color=YELLOW),
            Arrow(solutions[33][0][14:16].get_corner(DL), solutions[33][0][10].get_corner(UR), color=BLUE),
            Arrow(solutions[33][0][16].get_corner(DL), solutions[33][0][24].get_corner(UR), color=BLUE),
            Arrow(solutions[33][0][17].get_corner(DL), solutions[33][0][25].get_corner(UR), color=BLUE),
        )
        self.play(Create(arrowDelta[0]))
        self.play(Write(solutions[34].next_to(solutions[33], DOWN, LARGE_BUFF)))
        arrowDet = Arrow(solutions[34][0][3:-1].get_corner(DL),
                         solutions[34][0][3:-1].get_corner(UR), color=YELLOW)
        tempText = MathTex(r"8", font_size=50)
        self.play(Create(arrowDet))
        self.play(Write(tempText.next_to(solutions[34][0][3:-1].get_corner(UR), UP, SMALL_BUFF)))
        self.play(FadeOut(arrowDet, tempText, arrowDelta[0]))
        for i in range(35, 43):
            if i < 40:
                self.play(Create(arrowDelta[i - 34]))

            self.play(ReplacementTransform(solutions[i - 1], solutions[i].next_to(solutions[28], DOWN, LARGE_BUFF)))

            if i == 35:
                solutions[i][0][5:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][5:-1].get_corner(DL),
                                 solutions[i][0][5:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-3", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][5:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 36:
                solutions[i][0][10:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][10:-1].get_corner(DL),
                                 solutions[i][0][10:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"6", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][10:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 37:
                solutions[i][0][11:-1].set_color(BLUE)
                solutions[i][0][3:8].set_color(YELLOW)
                arrowDet = VGroup(
                    Arrow(solutions[i][0][3:8].get_corner(DL),
                          solutions[i][0][3:8].get_corner(UR), color=BLUE),
                    Arrow(solutions[i][0][11:-1].get_corner(DL),
                          solutions[i][0][11:-1].get_corner(UR), color=YELLOW)
                )
                tempText = VGroup(
                    MathTex(r"-3", font_size=50),
                    MathTex(r"11", font_size=50)
                )
                self.play(Create(arrowDet[1]), Create(arrowDet[0]))
                self.play(Write(tempText[0].next_to(solutions[i][0][11:-1].get_corner(UR), UP, SMALL_BUFF)),
                          Write(tempText[1].next_to(solutions[i][0][3:8].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 38:
                solutions[i][0][9:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][9:-1].get_corner(DL),
                                 solutions[i][0][9:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"4", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][9:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 39:
                solutions[i][0][11:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][11:-1].get_corner(DL),
                                 solutions[i][0][11:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"9", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][11:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 40:
                solutions[i][0][6:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][6:-1].get_corner(DL),
                                 solutions[i][0][6:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"9", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][6:-1].get_corner(UR), UP, SMALL_BUFF)))
            if i < 40:
                self.play(FadeOut(arrowDelta[i - 34], arrowDet, tempText))
            elif i == 40:
                self.play(FadeOut(arrowDet, tempText))
        BoxRectangle.add(SurroundingRectangle(solutions[42], buff=0.3))
        self.play(Create(BoxRectangle[3]))
        self.wait(0.3)
        self.play(FadeOut(BoxRectangle[3], solutions[33]))
        self.play(solutions[42].animate.shift(4 * UP))
        self.play(Write(solutions[43].next_to(solutions[42], DOWN, LARGE_BUFF)))
        arrowDelta = VGroup(
            Arrow(solutions[43][0][9:12].get_corner(UL), solutions[43][0][22].get_corner(DR), color=YELLOW),
            Arrow(solutions[43][0][12].get_corner(UR), solutions[43][0][37:39].get_corner(DR), color=YELLOW),
            Arrow(solutions[43][0][13].get_corner(UR), solutions[43][0][39].get_corner(DR), color=YELLOW),
            Arrow(solutions[43][0][19:21].get_corner(DL), solutions[43][0][13].get_corner(UR), color=BLUE),
            Arrow(solutions[43][0][21].get_corner(DL), solutions[43][0][29:32].get_corner(UR), color=BLUE),
            Arrow(solutions[43][0][22].get_corner(DL), solutions[43][0][32].get_corner(UR), color=BLUE),
        )
        self.play(Create(arrowDelta[0]))
        self.play(Write(solutions[44].next_to(solutions[43], DOWN, LARGE_BUFF)))
        arrowDet = Arrow(solutions[44][0][4:-1].get_corner(DL),
                         solutions[44][0][4:-1].get_corner(UR), color=YELLOW)
        tempText = MathTex(r"-52", font_size=50)
        self.play(Create(arrowDet))
        self.play(Write(tempText.next_to(solutions[44][0][4:-1].get_corner(UR), UP, SMALL_BUFF)))
        self.play(FadeOut(arrowDet, tempText, arrowDelta[0]))
        self.wait(0.5)
        for i in range(45, 54):
            if i < 50:
                self.play(Create(arrowDelta[i - 44]))

            self.play(ReplacementTransform(solutions[i - 1], solutions[i].next_to(solutions[43], DOWN, LARGE_BUFF)))

            if i == 45:
                solutions[i][0][8:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][8:-1].get_corner(DL),
                                 solutions[i][0][8:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-15", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][8:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 46:
                solutions[i][0][11:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][11:-1].get_corner(DL),
                                 solutions[i][0][11:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-50", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][11:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 47:
                solutions[i][0][16:-1].set_color(BLUE)
                solutions[i][0][4:13].set_color(YELLOW)
                arrowDet = VGroup(
                    Arrow(solutions[i][0][4:13].get_corner(DL),
                          solutions[i][0][4:13].get_corner(UR), color=BLUE),
                    Arrow(solutions[i][0][16:-1].get_corner(DL),
                          solutions[i][0][16:-1].get_corner(UR), color=YELLOW)
                )
                tempText = VGroup(
                    MathTex(r"-20", font_size=50),
                    MathTex(r"-117", font_size=50)
                )
                self.play(Create(arrowDet[1]), Create(arrowDet[0]))
                self.play(Write(tempText[0].next_to(solutions[i][0][16:-1].get_corner(UR), UP, SMALL_BUFF)),
                          Write(tempText[1].next_to(solutions[i][0][4:13].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 48:
                solutions[i][0][13:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][13:-1].get_corner(DL),
                                 solutions[i][0][13:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-26", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][13:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 49:
                solutions[i][0][16:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][16:-1].get_corner(DL),
                                 solutions[i][0][16:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-75", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][16:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 50:
                solutions[i][0][9:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][9:-1].get_corner(DL),
                                 solutions[i][0][9:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-121", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][9:-1].get_corner(UR), UP, SMALL_BUFF)))
            if i < 50:
                self.play(FadeOut(arrowDelta[i - 44], arrowDet, tempText))
            elif i == 50:
                self.play(FadeOut(arrowDet, tempText))
        BoxRectangle.add(SurroundingRectangle(solutions[53], buff=0.3))
        self.play(Create(BoxRectangle[4]))
        self.wait(0.3)
        self.play(FadeOut(BoxRectangle[4], solutions[43]))
        self.play(solutions[53].animate.shift(3.5 * UP).set_color(BLUE))
        self.play(Write(solutions[54].next_to(solutions[53], DOWN, LARGE_BUFF)))
        arrowDelta = VGroup(
            Arrow(solutions[54][0][9:11].get_corner(UL), solutions[54][0][24].get_corner(DR), color=YELLOW),
            Arrow(solutions[54][0][12:14].get_corner(UR), solutions[54][0][40:42].get_corner(DR), color=YELLOW),
            Arrow(solutions[54][0][14].get_corner(UR), solutions[54][0][42:44].get_corner(DR), color=YELLOW),
            Arrow(solutions[54][0][20:22].get_corner(DL), solutions[54][0][14].get_corner(UR), color=BLUE),
            Arrow(solutions[54][0][22:24].get_corner(DL), solutions[54][0][31:33].get_corner(UR), color=BLUE),
            Arrow(solutions[54][0][24].get_corner(DL), solutions[54][0][33:36].get_corner(UR), color=BLUE),
        )
        self.play(Create(arrowDelta[0]))
        self.play(Write(solutions[55].next_to(solutions[54], DOWN, LARGE_BUFF)))
        arrowDet = Arrow(solutions[55][0][4:-1].get_corner(DL),
                         solutions[55][0][4:-1].get_corner(UR), color=YELLOW)
        tempText = MathTex(r"-50", font_size=50)
        self.play(Create(arrowDet))
        self.play(Write(tempText.next_to(solutions[55][0][4:-1].get_corner(UR), UP, SMALL_BUFF)))
        self.play(FadeOut(arrowDet, tempText, arrowDelta[0]))
        for i in range(56, 64):
            if i < 61:
                self.play(Create(arrowDelta[i - 55]))

            self.play(ReplacementTransform(solutions[i - 1], solutions[i].next_to(solutions[54], DOWN, LARGE_BUFF)))

            if i == 56:
                solutions[i][0][8:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][8:-1].get_corner(DL),
                                 solutions[i][0][8:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"13", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][8:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 57:
                solutions[i][0][11:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][11:-1].get_corner(DL),
                                 solutions[i][0][11:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-15", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][11:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 58:
                solutions[i][0][16:-1].set_color(BLUE)
                solutions[i][0][4:13].set_color(YELLOW)
                arrowDet = VGroup(
                    Arrow(solutions[i][0][4:13].get_corner(DL),
                          solutions[i][0][4:13].get_corner(UR), color=BLUE),
                    Arrow(solutions[i][0][16:-1].get_corner(DL),
                          solutions[i][0][16:-1].get_corner(UR), color=YELLOW)
                )
                tempText = VGroup(
                    MathTex(r"-25", font_size=50),
                    MathTex(r"-52", font_size=50)
                )
                self.play(Create(arrowDet[1]), Create(arrowDet[0]))
                self.play(Write(tempText[0].next_to(solutions[i][0][16:-1].get_corner(UR), UP, SMALL_BUFF)),
                          Write(tempText[1].next_to(solutions[i][0][4:13].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 59:
                solutions[i][0][11:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][11:-1].get_corner(DL),
                                 solutions[i][0][11:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-10", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][11:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 60:
                solutions[i][0][14:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][14:-1].get_corner(DL),
                                 solutions[i][0][14:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-39", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][14:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 61:
                solutions[i][0][8:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][8:-1].get_corner(DL),
                                 solutions[i][0][8:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-24", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][9:-1].get_corner(UR), UP, SMALL_BUFF)))
            if i < 61:
                self.play(FadeOut(arrowDelta[i - 55], arrowDet, tempText))
            elif i == 61:
                self.play(FadeOut(arrowDet, tempText))
        BoxRectangle.add(SurroundingRectangle(solutions[63], buff=0.3))
        self.play(Create(BoxRectangle[5]))
        self.wait(0.1)
        self.play(FadeOut(BoxRectangle[5], solutions[54]))
        self.play(solutions[63].animate.shift(3.5 * UP).set_color(YELLOW))
        self.play(Write(solutions[64].next_to(solutions[63], DOWN, LARGE_BUFF)))
        arrowDelta = VGroup(
            Arrow(solutions[64][0][9:11].get_corner(UL), solutions[64][0][23:25].get_corner(DR), color=YELLOW),
            Arrow(solutions[64][0][11].get_corner(UR), solutions[64][0][36:38].get_corner(DR), color=YELLOW),
            Arrow(solutions[64][0][12:15].get_corner(UR), solutions[64][0][38].get_corner(DR), color=YELLOW),
            Arrow(solutions[64][0][20:22].get_corner(DL), solutions[64][0][12:15].get_corner(UR), color=BLUE),
            Arrow(solutions[64][0][22].get_corner(DL), solutions[64][0][31:33].get_corner(UR), color=BLUE),
            Arrow(solutions[64][0][23:25].get_corner(DL), solutions[64][0][33].get_corner(UR), color=BLUE),
        )
        self.play(Create(arrowDelta[0]))
        self.play(Write(solutions[65].next_to(solutions[64], DOWN, LARGE_BUFF)))
        arrowDet = Arrow(solutions[65][0][4:-1].get_corner(DL),
                         solutions[65][0][4:-1].get_corner(UR), color=YELLOW)
        tempText = MathTex(r"-40", font_size=50)
        self.play(Create(arrowDet))
        self.play(Write(tempText.next_to(solutions[65][0][4:-1].get_corner(UR), UP, SMALL_BUFF)))
        self.play(FadeOut(arrowDet, tempText, arrowDelta[0]))
        for i in range(66, 74):
            if i < 71:
                self.play(Create(arrowDelta[i - 65]))

            self.play(ReplacementTransform(solutions[i - 1], solutions[i].next_to(solutions[64], DOWN, LARGE_BUFF)))

            if i == 66:
                solutions[i][0][8:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][8:-1].get_corner(DL),
                                 solutions[i][0][8:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"75", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][8:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 67:
                solutions[i][0][11:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][11:-1].get_corner(DL),
                                 solutions[i][0][11:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-78", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][11:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 68:
                solutions[i][0][16:-1].set_color(BLUE)
                solutions[i][0][4:13].set_color(YELLOW)
                arrowDet = VGroup(
                    Arrow(solutions[i][0][4:13].get_corner(DL),
                          solutions[i][0][4:13].get_corner(UR), color=BLUE),
                    Arrow(solutions[i][0][16:-1].get_corner(DL),
                          solutions[i][0][16:-1].get_corner(UR), color=YELLOW)
                )
                tempText = VGroup(
                    MathTex(r"52", font_size=50),
                    MathTex(r"-43", font_size=50)
                )
                self.play(Create(arrowDet[1]), Create(arrowDet[0]))
                self.play(Write(tempText[0].next_to(solutions[i][0][16:-1].get_corner(UR), UP, SMALL_BUFF)),
                          Write(tempText[1].next_to(solutions[i][0][4:13].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 69:
                solutions[i][0][11:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][11:-1].get_corner(DL),
                                 solutions[i][0][11:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-100", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][11:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 70:
                solutions[i][0][15:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][15:-1].get_corner(DL),
                                 solutions[i][0][15:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-45", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][15:-1].get_corner(UR), UP, SMALL_BUFF)))
            elif i == 71:
                solutions[i][0][8:-1].set_color(BLUE)
                arrowDet = Arrow(solutions[i][0][8:-1].get_corner(DL),
                                 solutions[i][0][8:-1].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-93", font_size=50)
                self.play(Create(arrowDet))
                self.play(Write(tempText.next_to(solutions[i][0][9:-1].get_corner(UR), UP, SMALL_BUFF)))
            if i < 71:
                self.play(FadeOut(arrowDelta[i - 65], arrowDet, tempText))
            elif i == 71:
                self.play(FadeOut(arrowDet, tempText))
        BoxRectangle.add(SurroundingRectangle(solutions[73], buff=0.3))
        self.play(Create(BoxRectangle[5]))
        self.wait(0.15)
        self.play(FadeOut(BoxRectangle[5], solutions[64]))
        self.play(solutions[73].animate.shift(3.5 * UP).set_color(RED))
        self.play(Write(solutions[74].next_to(solutions[73], DOWN, LARGE_BUFF)))
        self.wait(1.25)
