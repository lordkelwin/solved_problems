from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=90)
        problemStatement = VGroup(
            Tex(r"\begin{minipage}{6 cm}"
                r"Evaluate the determinant of the given matrix:"
                r"\end{minipage}"),
            MathTex(r"\begin{vmatrix} 1 & 1 & -3 & 0 \\ 1 & 5 & 3 & 2 \\ 1 & -2 & 1 & 0 \\ 4 & 8 & 0 & 0 \end{vmatrix}")
        )

        problemStatement.arrange(DOWN, buff=LARGE_BUFF)
        self.add(problemStatement[0])
        self.play(Write(problemStatement[0]))
        self.wait(0.5)
        self.play(Write(problemStatement[1]))
        self.wait(2)
        self.play(FadeOut(problemStatement))


class ProblemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=90)
        solutionLines = VGroup(
            Tex(r"\begin{minipage}{6 cm}"
                r"One approach when solving a 4 $\times$ 4 \\ determinant is to use Chio's \\ Condensation Method."
                r"\end{minipage}"),
            MathTex(r"\det{\mathbf{A}} = \frac{1}{a_{11}^{n-2}} \begin{vmatrix} \begin{vmatrix} a_{11} & "
                    r"a_{12} \\ a_{21} & a_{22} \end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{21} & a_{23} "
                    r"\end{vmatrix} & \cdots & \begin{vmatrix} a_{11} & a_{1n} \\ a_{21} & a_{2n} "
                    r"\end{vmatrix} \\ \begin{vmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{31} & a_{33} "
                    r"\end{vmatrix} & \cdots & \begin{vmatrix} a_{11} & a_{1n} \\ a_{31} & a_{3n} "
                    r"\end{vmatrix} \\ \vdots & \vdots & \ddots & \vdots \\ \begin{vmatrix} a_{11} & a_{12} \\ "
                    r"a_{n1} & a_{n2} \end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{n1} & a_{n3} "
                    r"\end{vmatrix} & \cdots & \begin{vmatrix} a_{11} & a_{1n} \\ a_{n1} & a_{nn} "
                    r"\end{vmatrix}\end{vmatrix}", font_size=56),
            Tex(r"In the context of 4 $\times$ 4 determinant:"),
            MathTex(r"\det{\mathbf{A}} = \frac{1}{a_{11}^{n-2}} \begin{vmatrix} \begin{vmatrix} a_{11} & "
                    r"a_{12} \\ a_{21} & a_{22} \end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{21} & a_{23} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{14} \\ a_{21} & a_{24} "
                    r"\end{vmatrix} \\ \begin{vmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{31} & a_{33} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{14} \\ a_{31} & a_{34} "
                    r"\end{vmatrix} \\ \begin{vmatrix} a_{11} & a_{12} \\ "
                    r"a_{41} & a_{42} \end{vmatrix} & \begin{vmatrix} a_{11} & a_{13} \\ a_{41} & a_{43} "
                    r"\end{vmatrix} & \begin{vmatrix} a_{11} & a_{14} \\ a_{41} & a_{44} "
                    r"\end{vmatrix}\end{vmatrix}", font_size=65),
            Tex(r"Substituting:"),
            MathTex(r"\det{\mathbf{A}} = \frac{1}{1^{(4-2)}} \begin{vmatrix} \begin{vmatrix} 1 & "
                    r"1 \\ 1 & 5 \end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 1 & 3 \end{vmatrix} & \begin{vmatrix} 1 & 0 "
                    r"\\ 1 & 2 \end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\ 1 & -2 \end{vmatrix} & \begin{vmatrix} 1 & -3 "
                    r"\\ 1 & 1 \end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 1 & 0 \end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\"
                    r"4 & 8 \end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 4 & 0 \end{vmatrix} & \begin{vmatrix} 1 & 0 \\ "
                    r"4 & 0 \end{vmatrix}\end{vmatrix}", font_size=65),
            MathTex(r"\det{\mathbf{A}} = \frac{1}{1} \begin{vmatrix} 4 & "
                    r"\begin{vmatrix} 1 & -3 \\ 1 & 3 \end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 1 & 2 "
                    r"\end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\ 1 & -2 \end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 1 & 1 "
                    r"\end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 1 & 0 \end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\ "
                    r"4 & 8 \end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 4 & 0 "
                    r"\end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 4 & 0  \end{vmatrix}\end{vmatrix}", font_size=65),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & "
                    r"6 & \begin{vmatrix} 1 & 0 \\ 1 & 2 \end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\ 1 & -2 "
                    r"\end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 1 & 1 \end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 1 & 0 "
                    r"\end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\ 4 & 8 \end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 4 & 0 "
                    r"\end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 4 & 0 \end{vmatrix}\end{vmatrix}", font_size=65),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & "
                    r"6 & 2 \\ \begin{vmatrix} 1 & 1 \\ 1 & -2 \end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 1 & 1 "
                    r"\end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 1 & 0 \end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\ "
                    r"4 & 8 \end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 4 & 0 \end{vmatrix} & \begin{vmatrix} 1 & 0 \\ "
                    r"4 & 0 \end{vmatrix}\end{vmatrix}", font_size=65),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & "
                    r"6 & 2 \\ -3 & \begin{vmatrix} 1 & -3 \\ 1 & 1 \end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 1 & 0 "
                    r"\end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\ 4 & 8 \end{vmatrix} & \begin{vmatrix} 1 & -3 \\ 4 & 0 "
                    r"\end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 4 & 0 \end{vmatrix}\end{vmatrix}", font_size=65),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & 6 & 2 \\ -3 & 4 & "
                    r"\begin{vmatrix} 1 & 0 \\ 1 & 0 \end{vmatrix} \\ \begin{vmatrix} 1 & 1 \\ 4 & 8 \end{vmatrix} & "
                    r"\begin{vmatrix} 1 & -3 \\ 4 & 0 \end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 4 & 0 "
                    r"\end{vmatrix}\end{vmatrix}", font_size=65),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & "
                    r"6 & 2 \\ -3 & 4 & 0 \\ \begin{vmatrix} 1 & 1 \\ 4 & 8 \end{vmatrix} & \begin{vmatrix} 1 & -3 "
                    r"\\ 4 & 0 \end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 4 & 0 \end{vmatrix}\end{vmatrix}",
                    font_size=65),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & "
                    r"6 & 2 \\ -3 & 4 & 0 \\ 4 & \begin{vmatrix} 1 & -3 \\ 4 & 0 "
                    r"\end{vmatrix} & \begin{vmatrix} 1 & 0 \\ 4 & 0 "
                    r"\end{vmatrix}\end{vmatrix}", font_size=65),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & "
                    r"6 & 2 \\ -3 & 4 & 0 \\ 4 & 12 & \begin{vmatrix} 1 & 0 \\ 4 & 0 "
                    r"\end{vmatrix}\end{vmatrix}", font_size=65),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & "
                    r"6 & 2 \\ -3 & 4 & 0 \\ 4 & 12 & 0 \end{vmatrix}", font_size=65),
        )

        solutionLines[0].move_to(ORIGIN)
        solutionLines[0].move_to(5 * UP)
        self.play(Write(solutionLines[0]))
        self.wait(0.3)
        self.play(Write(solutionLines[1].next_to(solutionLines[0], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(solutionLines[:2]))

        solutionLines[2].move_to(ORIGIN)
        solutionLines[2].move_to(3 * UP)
        self.play(Write(solutionLines[2]))
        self.wait(0.3)
        self.play(Write(solutionLines[3].next_to(solutionLines[2], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(solutionLines[2:4]))

        solutionLines[4].move_to(ORIGIN)
        solutionLines[4].move_to(3 * UP)
        self.play(Write(solutionLines[4]))
        self.wait(0.3)
        self.play(Write(solutionLines[5].next_to(solutionLines[4], direction=DOWN, buff=LARGE_BUFF)))
        solutionLines[5][0][29].set_color(BLUE)
        solutionLines[5][0][32].set_color(BLUE)
        solutionLines[5][0][30].set_color(YELLOW)
        solutionLines[5][0][31].set_color(YELLOW)
        self.wait(0.3)
        for i in range(6, 15):
            self.play(TransformMatchingTex(solutionLines[i-1], solutionLines[i].next_to(solutionLines[4],
                                                                                        direction=DOWN,
                                                                                        buff=LARGE_BUFF)))
            self.wait(0.5)
        self.wait(0.75)
        self.play(FadeOut(solutionLines[4], solutionLines[14]))
