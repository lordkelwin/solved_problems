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
            Tex(r"(eq. 1)"),
            Tex(r"if $x=3$, $y=4$:"),
            MathTex(r"(3)^{2}+(4)^{2}+D(3)+E(4)+F=0"),
            MathTex(r"9+16+3D+4E+F=0"),
            MathTex(r"25+3D+4E+F=0"),
            MathTex(r"3D+4E+F=-25"),
            Tex(r"(eq. 2)"),
            Tex(r"if $x=-1$, $y=2$:"),
            MathTex(r"(-1)^{2}+(2)^{2}+D(-1)+E(2)+F=0"),
            MathTex(r'1+4-D+2E+F=0'),
            MathTex(r"5-D+2E+F=0"),
            MathTex(r"-D+2E+F=-5"),
            Tex(r"(eq. 3)"),
            Tex(r"Using Cramer's Rule to solve for the variables:"),
            MathTex(r"C=\frac{\Delta_{C}}{\Delta}"),
            MathTex(r"D=\frac{\Delta_{D}}{\Delta}"),
            MathTex(r"F=\frac{\Delta_{F}}{\Delta}"),
            Tex(r"Where:"),
            MathTex(r"\Delta = \begin{vmatrix}"
                    r"2 & 3 & 1 \\ 3 & 4 & 1 \\ -1 & 2 & 1"
                    r"'end{vmatrix}"),
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
                    r"'end{vmatrix}"),
            MathTex(r"\Delta = [(2)(4)(1)]"),
            MathTex(r"\Delta = [(2)(4)(1)+(3)(1)(-1)]"),
            MathTex(r"\Delta = [(2)(4)(1)+(3)(1)(-1)+(1)(3)(2)]"),
            MathTex(r"\Delta = [(2)(4)(1)+(3)(1)(-1)+(1)(3)(2)] - [(-1)(4)(1)]"),
            MathTex(r"\Delta = [(2)(4)(1)+(3)(1)(-1)+(1)(3)(2)] - [(-1)(4)(1)+(2)(1)(2)]"),
            MathTex(r"\Delta = [(2)(4)(1)+(3)(1)(-1)+(1)(3)(2)] - [(-1)(4)(1)+(2)(1)(2)+(1)(3)(3)]"),
            MathTex(r"\Delta = [8-3+6]-[-4+4+9]"),
            MathTex(r"\Delta = 11 - 9"),
            MathTex(r"\Delta = 2"),
            MathTex(r"\Delta_{C} = \begin{vmatrix}"
                    r"-13 & 3 &  1 \\ -25 & 4 & 1 \\ -5 & 2 & 1"
                    r"\end{vmatrix}"),
            MathTex(r"\Delta_{C} = [(-13)(4)(1)]"),
            MathTex(r"\Delta_{C} = [(-13)(4)(1)+(3)(1)(-5)]"),
            MathTex(r"\Delta_{C} = [(-13)(4)(1)+(3)(1)(-5)+(1)(-25)(2)]"),
            MathTex(r"\Delta_{C} = [(-13)(4)(1)+(3)(1)(-5)+(1)(-25)(2)] - [(-5)(4)(1)]"),
            MathTex(r"\Delta_{C} = [(-13)(4)(1)+(3)(1)(-5)+(1)(-25)(2)] - [(-5)(4)(1)+(2)(1)(-13)]"),
            MathTex(r"\Delta_{C} = [(-13)(4)(1)+(3)(1)(-5)+(1)(-25)(2)] - [(-5)(4)(1)+(2)(1)(-13)+(1)(-25)(3)]"),
            MathTex(r"\Delta_{C} = [-52-15-50]-[-20-26-75]"),
            MathTex(r"\Delta_{C} = -117+121"),
            MathTex(r"\Delta_{C} = 4"),
            MathTex(r"\Delta_{D} = \begin{vmatrix}"
                    r"-2 & -13 &  1 \\ 3 & -25 & 1 \\ -1 & -5 & 1"
                    r"\end{vmatrix}"),
            MathTex(r"\Delta_{D} = [(2)(-25)(1)]"),
            MathTex(r"\Delta_{D} = [(2)(-25)(1)+(-13)(1)(-1)]"),
            MathTex(r"\Delta_{D} = [(2)(-25)(1)+(-13)(1)(-1)+(1)(3)(-5)]"),
            MathTex(r"\Delta_{D} = [(2)(-25)(1)+(-13)(1)(-1)+(1)(3)(-5)] - [(-1)(-25)(1)]"),
            MathTex(r"\Delta_{D} = [(2)(-25)(1)+(-13)(1)(-1)+(1)(3)(-5)] - [(-1)(-25)(1)+(-5)(1)(2)]"),
            MathTex(r"\Delta_{D} = [(2)(-25)(1)+(-13)(1)(-1)+(1)(3)(-5)] - [(-1)(-25)(1)+(-5)(1)(2)+(1)(3)(-13)]"),
            MathTex(r"\Delta_{D} = [-50+13-15]-[-25-10-39]"),
            MathTex(r"\Delta_{D} = -52+24"),
            MathTex(r"\Delta_{D} = -28"),
            MathTex(r"\Delta_{F} = \begin{vmatrix}"
                    r"-2 & 3 & -13 \\ 3 & 4 & -25 \\ -1 & 2 & -5"
                    r"\end{vmatrix}"),
            MathTex(r"\Delta_{F} = [(2)(4)(-5)]"),
            MathTex(r"\Delta_{F} = [(2)(4)(-5)+(3)(-25)(-1)]"),
            MathTex(r"\Delta_{F} = [(2)(4)(-5)+(3)(-25)(-1)+(-13)(3)(2)]"),
            MathTex(r"\Delta_{F} = [(2)(4)(-5)+(3)(-25)(-1)+(-13)(3)(2)] - [(-1)(4)(-13)]"),
            MathTex(r"\Delta_{F} = [(2)(4)(-5)+(3)(-25)(-1)+(-13)(3)(2)] - [(-1)(4)(-13)+(2)(-25)(2)]"),
            MathTex(r"\Delta_{F} = [(2)(4)(-5)+(3)(-25)(-1)+(-13)(3)(2)] - [(-1)(4)(-13)+(2)(-25)(2)+(-5)(3)(3)]"),
            MathTex(r"\Delta_{F} = [-40+75-78]-[52-100-45]"),
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
