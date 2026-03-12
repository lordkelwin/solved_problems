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
                    r"6 & 2 \\ -3 & 4 & 0 \\ 4 & 12 & 0 \end{vmatrix}", font_size=90),
            Tex(r"\begin{minipage}{5 cm}Solving for the determinant \\ using the basket method:\end{minipage}"),
            MathTex(r"\det{\mathbf{A}} = \begin{vmatrix} 4 & "
                    r"6 & 2 \\ -3 & 4 & 0 \\ 4 & 12 & 0 \end{vmatrix} \begin{matrix} 4 & 6 \\ -3 & 4 \\ 4 &12 "
                    r"\end{matrix}", font_size=90),
            MathTex(r"\det{\mathbf{A}}=[(4)(4)(0)]"),
            MathTex(r"\det{\mathbf{A}}=[0+(6)(0)(4)]"),
            MathTex(r"\det{\mathbf{A}}=[0+0+(2)(-3)(12)]"),
            MathTex(r"\det{\mathbf{A}}=[0+0-72]-[(4)(4)(2)]"),
            MathTex(r"\det{\mathbf{A}}=[0+0-72]-\\ [32+(12)(0)(4)]"),
            MathTex(r"\det{\mathbf{A}}=[0+0-72]- \\ [32+0+(0)(-3)(6)]"),
            MathTex(r"\det{\mathbf{A}}=[0+0-72]-[32+0+0]"),
            MathTex(r"\det{\mathbf{A}}=-72-32"),
            MathTex(r"\det{\mathbf{A}}=-104")
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
        arrowLine_1 = Arrow(solutionLines[5][0][29].get_center(), solutionLines[5][0][32].get_center(),
                            color=BLUE)
        arrowLine_2 = Arrow(solutionLines[5][0][31].get_center(), solutionLines[5][0][30].get_center(),
                            color=BLUE)
        self.wait(0.3)
        self.play(Create(arrowLine_1), Create(arrowLine_2))
        self.wait(0.3)
        self.play(FadeOut(arrowLine_2, arrowLine_1), TransformMatchingTex(solutionLines[5],
                                                                          solutionLines[6].next_to(
                                                                              solutionLines[4],
                                                                              direction=DOWN,
                                                                              buff=LARGE_BUFF)))
        self.wait(0.5)
        for i in range(6, 14):
            if i == 6:
                solutionLines[i][0][25].set_color(BLUE)
                solutionLines[i][0][29].set_color(BLUE)
                solutionLines[i][0][26:28].set_color(YELLOW)
                solutionLines[i][0][28].set_color(YELLOW)
                arrowLine_1 = Arrow(solutionLines[i][0][25].get_center(), solutionLines[i][0][29].get_center(),
                                    color=BLUE)
                arrowLine_2 = Arrow(solutionLines[i][0][28].get_center(), solutionLines[i][0][26:28].get_center(),
                                    color=YELLOW)
            elif i == 7:
                solutionLines[i][0][23].set_color(BLUE)
                solutionLines[i][0][26].set_color(BLUE)
                solutionLines[i][0][24].set_color(YELLOW)
                solutionLines[i][0][25].set_color(YELLOW)
                arrowLine_1 = Arrow(solutionLines[i][0][23].get_center(), solutionLines[i][0][26].get_center(),
                                    color=BLUE)
                arrowLine_2 = Arrow(solutionLines[i][0][25].get_center(), solutionLines[i][0][24].get_center(),
                                    color=YELLOW)
            elif i == 8:
                solutionLines[i][0][22].set_color(BLUE)
                solutionLines[i][0][25:27].set_color(BLUE)
                solutionLines[i][0][23].set_color(YELLOW)
                solutionLines[i][0][24].set_color(YELLOW)
                arrowLine_1 = Arrow(solutionLines[i][0][22].get_center(), solutionLines[i][0][25:27].get_center(),
                                    color=BLUE)
                arrowLine_2 = Arrow(solutionLines[i][0][24].get_center(), solutionLines[i][0][23].get_center(),
                                    color=YELLOW)
            elif i == 9:
                solutionLines[i][0][24].set_color(BLUE)
                solutionLines[i][0][28].set_color(BLUE)
                solutionLines[i][0][25:27].set_color(YELLOW)
                solutionLines[i][0][27].set_color(YELLOW)
                arrowLine_1 = Arrow(solutionLines[i][0][24].get_center(), solutionLines[i][0][28].get_center(),
                                    color=BLUE)
                arrowLine_2 = Arrow(solutionLines[i][0][27].get_center(), solutionLines[i][0][25:27].get_center(),
                                    color=YELLOW)
            elif i == 10:
                solutionLines[i][0][25].set_color(BLUE)
                solutionLines[i][0][28].set_color(BLUE)
                solutionLines[i][0][26].set_color(YELLOW)
                solutionLines[i][0][27].set_color(YELLOW)
                arrowLine_1 = Arrow(solutionLines[i][0][25].get_center(), solutionLines[i][0][28].get_center(),
                                    color=BLUE)
                arrowLine_2 = Arrow(solutionLines[i][0][27].get_center(), solutionLines[i][0][26].get_center(),
                                    color=YELLOW)
            elif i == 11:
                solutionLines[i][0][24].set_color(BLUE)
                solutionLines[i][0][27].set_color(BLUE)
                solutionLines[i][0][25].set_color(YELLOW)
                solutionLines[i][0][26].set_color(YELLOW)
                arrowLine_1 = Arrow(solutionLines[i][0][24].get_center(), solutionLines[i][0][27].get_center(),
                                    color=BLUE)
                arrowLine_2 = Arrow(solutionLines[i][0][26].get_center(), solutionLines[i][0][25].get_center(),
                                    color=YELLOW)
            elif i == 12:
                solutionLines[i][0][25].set_color(BLUE)
                solutionLines[i][0][29].set_color(BLUE)
                solutionLines[i][0][26:28].set_color(YELLOW)
                solutionLines[i][0][28].set_color(YELLOW)
                arrowLine_1 = Arrow(solutionLines[i][0][25].get_center(), solutionLines[i][0][29].get_center(),
                                    color=BLUE)
                arrowLine_2 = Arrow(solutionLines[i][0][28].get_center(), solutionLines[i][0][26:28].get_center(),
                                    color=YELLOW)
            elif i == 13:
                solutionLines[i][0][27].set_color(BLUE)
                solutionLines[i][0][30].set_color(BLUE)
                solutionLines[i][0][28].set_color(YELLOW)
                solutionLines[i][0][29].set_color(YELLOW)
                arrowLine_1 = Arrow(solutionLines[i][0][27].get_center(), solutionLines[i][0][30].get_center(),
                                    color=BLUE)
                arrowLine_2 = Arrow(solutionLines[i][0][29].get_center(), solutionLines[i][0][28].get_center(),
                                    color=YELLOW)
            self.play(Create(arrowLine_1), Create(arrowLine_2))
            self.wait(0.3)
            self.play(FadeOut(arrowLine_1, arrowLine_2),
                      TransformMatchingTex(solutionLines[i], solutionLines[i+1].next_to(solutionLines[4],
                                                                                        direction=DOWN,
                                                                                        buff=LARGE_BUFF)))
            self.wait(0.5)
        self.wait(0.75)
        self.play(FadeOut(solutionLines[4], solutionLines[14]))

        solutionLines[15].move_to(ORIGIN)
        solutionLines[15].move_to(UP * 3)
        self.play(Write(solutionLines[15]))
        self.wait(0.3)
        self.play(Write(solutionLines[16].next_to(solutionLines[15], direction=DOWN, buff=LARGE_BUFF)))
        arrowLines = VGroup(
            Arrow(solutionLines[16][0][11].get_center(), solutionLines[16][0][21].get_center(),
                  color=BLUE),
            Arrow(solutionLines[16][0][12].get_center(), solutionLines[16][0][33].get_center(),
                  color=BLUE),
            Arrow(solutionLines[16][0][13].get_center(), solutionLines[16][0][34:36].get_center(),
                  color=BLUE),
            Arrow(solutionLines[16][0][18].get_center(), solutionLines[16][0][13].get_center(),
                  color=YELLOW),
            Arrow(solutionLines[16][0][19:21].get_center(), solutionLines[16][0][28].get_center(),
                  color=YELLOW),
            Arrow(solutionLines[16][0][21].get_center(), solutionLines[16][0][29].get_center(),
                  color=YELLOW)
        )
        self.play(Create(arrowLines[0]))
        self.play(Write(solutionLines[17].next_to(solutionLines[16], direction=DOWN, buff=LARGE_BUFF)))

        for i in range(18, 26):
            if i <= 22:
                self.play(Create(arrowLines[i-17]))
            self.play(ReplacementTransform(solutionLines[i-1], solutionLines[i].next_to(solutionLines[16],
                                                                                        direction=DOWN,
                                                                                        buff=LARGE_BUFF)))
            self.wait(0.5)
        rectangleFrame = SurroundingRectangle(solutionLines[25], buff=0.5)
        self.play(Create(rectangleFrame))
        self.wait(1.25)
        self.play(FadeOut(solutionLines[15:17], solutionLines[25], rectangleFrame, arrowLines))
