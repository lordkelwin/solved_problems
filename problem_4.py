from manim import *


class ProblemStatement(Scene):
    def construct(self):
        statement = VGroup(
            Tex(
                r"\begin{minipage}{9 cm}"
                r"Given the system defined below, find the transfer function "
                r"$T(s) = Y(s)/U(s)$, where $U(s)$ is the input and $Y(s)$ is the "
                r"output."
                r"\end{minipage}"
            ),
            MathTex(r"\dot{\mathbf{x}} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & -2 & -3 \end{bmatrix}\mathbf{x}"
                    r"+ \begin{bmatrix} 10 \\ 0 \\ 0 \end{bmatrix} u"),
            MathTex(r"y = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \mathbf{x}")
        )

        statement.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(statement[0])
        for i in range(3):
            self.play(Write(statement[i]))
            self.wait(0.2)
        self.wait(2.8)
        self.play(FadeOut(statement))


class ProblemSolution(Scene):
    def construct(self):
        lines = VGroup(
            Tex("To convert from state-space to transfer function:"),
            MathTex(r"T(s) = \frac{Y(s)}{U(s)} = C(sI-A)^{-1}B + D"),
            Tex("In a state-space representation:"),
            MathTex(r"\dot{\mathbf{x}} = A\mathbf{x} + Bu"),
            MathTex(r"y = C\mathbf{x} + Du"),
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        for i in range(5):
            self.play(Write(lines[i]))
            self.wait(0.3)
        self.wait(0.7)
        self.play(FadeOut(lines))

        lines = VGroup(
            Tex("In the context of the problem:"),
            MathTex(r"A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & -2 & -3 \end{bmatrix},\,"
                    r"B = \begin{bmatrix} 10 \\ 0 \\ 0 \end{bmatrix},\, C = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix},\,"
                    r"D = \begin{bmatrix} 0 \end{bmatrix}"),
            Tex("First, solve for the $(sI - A)^{-1}$"),
            MathTex(r"sI-A = s\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} - "
                    r"\begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & -2 & -3 \end{bmatrix}")
        )

        extra_lines = VGroup(
            MathTex(r"sI-A = \begin{bmatrix} s & 0 & 0 \\ 0 & s & 0 \\ 0 & 0 & s \end{bmatrix} - "
                    r"\begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & -2 & -3 \end{bmatrix}"),
            MathTex(r"sI-A = \begin{bmatrix} s & -1 & 0 \\ 0 & s & -1 \\ 1 & 2 & s+3 \end{bmatrix}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        for i in range(4):
            self.play(Write(lines[i]))
            self.wait(0.3)
        self.play(ReplacementTransform(lines[3], extra_lines[0].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(extra_lines[0], extra_lines[1].next_to(lines[2],
                                                                              direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(1)
        self.play(FadeOut(lines[0:3], extra_lines[1]))

        lines = VGroup(
            Tex("Recap: Formula for solving inverse matrix"),
            MathTex(r"\mathbf{A}^{-1} = \frac{\mathrm{adj}(\mathbf{A})}{\mathrm{det}(\mathbf{A})}"),
            Tex("Following the formula:"),
            MathTex(r"(sI-A)^{-1} = \frac{\mathrm{adj}(sI-A)}{\mathrm{det}(sI-A)}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.add(lines[0])
        for i in range(4):
            self.play(Write(lines[i]))
            self.wait(0.3)
        self.wait(0.7)
        self.play(FadeOut(lines))

        lines = VGroup(
            Tex("Solving the determinant first:"),
            MathTex(r"sI-A = \begin{vmatrix} s & -1 & 0 \\ 0 & s & -1 \\ 1 & 2 & s+3 \end{vmatrix} "
                    r"\begin{matrix} s & -1 \\ 0 & s \\ 1 & 2 \end{matrix}"),
            MathTex(r"\mathrm{det}(sI-A) = (s)(s)(s+3)")
        )

        extra_lines = VGroup(
            MathTex(r"\mathrm{det}(sI-A) = (s)(s)(s+3)+(-1)(-1)(1)"),
            MathTex(r"\mathrm{det}(sI-A) = (s)(s)(s+3)+(-1)(-1)(1)+\\(0)(0)(2)"),
            MathTex(r"\mathrm{det}(sI-A)=s^{3}+3s^{2}+1"),
            MathTex(r"\mathrm{det}(sI-A)=s^{3}+3s^{2}+1-(1)(s)(0)"),
            MathTex(r"\mathrm{det}(sI-A)=s^{3}+3s^{2}+1-(1)(s)(0)-\\(2)(-1)(s)"),
            MathTex(r"\mathrm{det}(sI-A)=s^{3}+3s^{2}+1-(1)(s)(0)-\\(2)(-1)(s)-(s+3)(0)(-1)"),
            MathTex(r"\mathrm{det}(sI-A)=s^{3}+3s^{2}+1+2s"),
            MathTex(r"\mathrm{det}(sI-A)=s^{3}+3s^{2}+2s+1")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1]))
        self.wait(0.3)
        line_1 = Line(lines[1][0][11].get_center(), lines[1][0][21:24].get_center(),
                      color=BLUE)
        self.play(Create(line_1))
        self.wait(0.2)
        self.play(Write(lines[2]))
        self.wait(0.2)
        line_2 = Line(lines[1][0][12:14].get_center(), lines[1][0][35].get_center(),
                      color=BLUE)
        self.play(Create(line_2))
        self.wait(0.2)
        self.play(Unwrite(lines[2], reverse=False),
                  Write(extra_lines[0].next_to(lines[1], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.2)
        line_3 = Line(lines[1][0][14].get_center(), lines[1][0][36].get_center(), color=BLUE)
        self.play(Create(line_3))
        self.wait(0.2)
        self.play(Unwrite(extra_lines[0], reverse=False), Write(extra_lines[1].next_to(lines[1], direction=DOWN,
                                                                                       buff=MED_LARGE_BUFF)))
        self.wait(0.2)
        self.play(ReplacementTransform(extra_lines[1], extra_lines[2].next_to(lines[1], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(0.2)
        line_4 = Line(lines[1][0][19].get_center(), lines[1][0][14].get_center(), color=YELLOW)
        self.play(Create(line_4))
        self.wait(0.2)
        self.play(Unwrite(extra_lines[2], reverse=False), Write(extra_lines[3].next_to(lines[1], direction=DOWN,
                                                                                       buff=MED_LARGE_BUFF)))
        self.wait(0.2)
        line_5 = Line(lines[1][0][20].get_center(), lines[1][0][30].get_center(), color=YELLOW)
        self.play(Create(line_5))
        self.wait(0.2)
        self.play(Unwrite(extra_lines[3], reverse=False), Write(extra_lines[4].next_to(lines[1], direction=DOWN,
                                                                                       buff=MED_LARGE_BUFF)))
        self.wait(0.2)
        line_6 = Line(lines[1][0][21:24].get_center(), lines[1][0][31:33].get_center(), color=YELLOW)
        self.play(Create(line_6))
        self.wait(0.2)
        self.play(Unwrite(extra_lines[4], reverse=False), Write(extra_lines[5].next_to(lines[1], direction=DOWN,
                                                                                       buff=MED_LARGE_BUFF)))
        self.wait(0.2)
        self.play(ReplacementTransform(extra_lines[5], extra_lines[6].next_to(lines[1], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(0.2)
        self.play(ReplacementTransform(extra_lines[6], extra_lines[7].next_to(lines[1], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        frameBox = SurroundingRectangle(extra_lines[7], buff=0.25)
        self.play(Create(frameBox))
        self.wait(1)
        self.play(FadeOut(lines[0:2], line_1, line_2, line_3, line_4, line_5,
                          line_6, extra_lines[7], frameBox))

        lines = VGroup(
            Tex("Solving for the adjoint matrix:"),
            MathTex(r"\mathrm{adj}(sI-A) = C_{sI-A}^{T}"),
            MathTex(r"sI-A = \begin{bmatrix} s & -1 & 0 \\ 0 & s & -1 \\ 1 & 2 & s+3 \end{bmatrix}"),
            MathTex(r"\mathbf{C}_{11}=(-1)^{(1+1)} \begin{vmatrix} s & -1 \\ 2 & s+3 \end{vmatrix}")
        )

        extra_lines = VGroup(
            MathTex(r"\mathbf{C}_{11} = (s)(s+3)-(-1)(2)"),
            MathTex(r"\mathbf{C}_{11} = s^{2}+3s+2"),
            MathTex(r"\mathbf{C}_{12}=(-1)^{(1+2)} \begin{vmatrix} 0 & -1 \\ 1 & s+3 \end{vmatrix}"),
            MathTex(r"\mathbf{C}_{12}=-1[(0)(s+3)-(-1)(1)]"),
            MathTex(r"\mathbf{C}_{12}=-1(1)"),
            MathTex(r"\mathbf{C}_{12}=-1"),
            MathTex(r"\mathbf{C}_{13}=(-1)^{(1+3)} \begin{vmatrix} 0 & s \\ 1 & 2 \end{vmatrix}"),
            MathTex(r"\mathbf{C}_{13}=(0)(2)-(s)(1)"),
            MathTex(r"\mathbf{C}_{13}=-s"),
            MathTex(r"\mathbf{C}_{21}=(-1)^{(2+1)} \begin{vmatrix} -1 & 0 \\ 2 & s+3 \end{vmatrix}"),
            MathTex(r"\mathbf{C}_{21}=(-1)[(-1)(s+3)-(2)(0)]"),
            MathTex(r"\mathbf{C}_{21}=(-1)(-1)(s+3)"),
            MathTex(r"\mathbf{C}_{21}=(s+3)"),
            MathTex(r"\mathbf{C}_{22}=(-1)^{(2+2)} \begin{vmatrix} s & 0 \\ 1 & s+3 \end{vmatrix}"),
            MathTex(r"\mathbf{C}_{22}=(s)(s+3)-(0)(1)"),
            MathTex(r"\mathbf{C}_{22}=s^{2}+3s"),
            MathTex(r"\mathbf{C}_{23}=(-1)^{(2+3)} \begin{vmatrix} s & -1 \\ 1 & 2 \end{vmatrix}"),
            MathTex(r"\mathbf{C}_{23}=(-1)[(s)(2)-(-1)(1)]"),
            MathTex(r"\mathbf{C}_{23}=(-1)(2s+1)"),
            MathTex(r"\mathbf{C}_{23}=-(2s+1)"),
            MathTex(r"\mathbf{C}_{31}=(-1)^{(3+1)} \begin{vmatrix} -1 & 0 \\ s & -1 \end{vmatrix}"),
            MathTex(r"\mathbf{C}_{31}=(-1)(-1)-(0)(s)"),
            MathTex(r"\mathbf{C}_{31}=1"),
            MathTex(r"\mathbf{C}_{32}=(-1)^{(3+2)} \begin{vmatrix} s & 0 \\ 0 & -1 \end{vmatrix}"),
            MathTex(r"\mathbf{C}_{32}=(-1)[(s)(-1)-(0)(0)]"),
            MathTex(r"\mathbf{C}_{32}=(-1)(-s)"),
            MathTex(r"\mathbf{C}_{32}=s"),
            MathTex(r"\mathbf{C}_{33}=(-1)^{(3+3)} \begin{vmatrix} s & -1 \\ 0 & s \end{vmatrix}"),
            MathTex(r"\mathbf{C}_{33}=(s)(s)-(-1)(0)"),
            MathTex(r"\mathbf{C}_{33}=s^{2}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        for i in range(3):
            self.play(Write(lines[i]))
            self.wait(0.3)
        line_1 = Line(lines[2][0][7].get_center(), lines[2][0][10].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][7].get_center(), lines[2][0][15].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][7], shape=Circle, color=YELLOW, run_time=3, fade_out=True), Create(line_1),
                  Create(line_2))
        self.play(Write(lines[3]))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[3], extra_lines[0].next_to(lines[2], direction=DOWN,
                                                                        buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(extra_lines[0], extra_lines[1].next_to(lines[2], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(line_1, line_2, extra_lines[1]))
        self.wait(0.3)
        line_1 = Line(lines[2][0][7].get_center(), lines[2][0][10].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][8:10].get_center(), lines[2][0][16].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][8:10], shape=Circle, color=YELLOW, run_time=3, fade_out=True),
                  Create(line_1),
                  Create(line_2))
        self.play(Write(extra_lines[2].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        for i in range(3, 6):
            self.play(ReplacementTransform(extra_lines[i - 1], extra_lines[i].next_to(lines[2], direction=DOWN,
                                                                                      buff=MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(line_1, line_2, extra_lines[5]))
        line_1 = Line(lines[2][0][10].get_center(), lines[2][0][7].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][10].get_center(), lines[2][0][17:20].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][10], shape=Circle, color=YELLOW, run_time=3, fade_out=True), Create(line_1),
                  Create(line_2))
        self.play(Write(extra_lines[6].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        for i in range(7, 9):
            self.play(ReplacementTransform(extra_lines[i - 1], extra_lines[i].next_to(lines[2], direction=DOWN,
                                                                                      buff=MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(line_1, line_2, extra_lines[8]))
        line_1 = Line(lines[2][0][11].get_center(), lines[2][0][13:15].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][7].get_center(), lines[2][0][15].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][11], shape=Circle, color=YELLOW, run_time=3, fade_out=True), Create(line_1),
                  Create(line_2))
        self.play(Write(extra_lines[9].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        for i in range(10, 13):
            self.play(ReplacementTransform(extra_lines[i - 1], extra_lines[i].next_to(lines[2], direction=DOWN,
                                                                                      buff=MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(line_1, line_2, extra_lines[12]))
        line_1 = Line(lines[2][0][11].get_center(), lines[2][0][13:15].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][8:10].get_center(), lines[2][0][16].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][12], shape=Circle, color=YELLOW, run_time=3, fade_out=True), Create(line_1),
                  Create(line_2))
        self.play(Write(extra_lines[13].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        for i in range(14, 16):
            self.play(ReplacementTransform(extra_lines[i - 1], extra_lines[i].next_to(lines[2], direction=DOWN,
                                                                                      buff=MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(line_1, line_2, extra_lines[15]))
        line_1 = Line(lines[2][0][10].get_center(), lines[2][0][17:20].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][11].get_center(), lines[2][0][13:15].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][13:15], shape=Circle, color=YELLOW, run_time=3, fade_out=True),
                  Create(line_1), Create(line_2))
        self.play(Write(extra_lines[16].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        for i in range(17, 20):
            self.play(ReplacementTransform(extra_lines[i - 1], extra_lines[i].next_to(lines[2], direction=DOWN,
                                                                                      buff=MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(line_1, line_2, extra_lines[19]))
        line_1 = Line(lines[2][0][15].get_center(), lines[2][0][17:20].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][7].get_center(), lines[2][0][15].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][15], shape=Circle, color=YELLOW, run_time=3, fade_out=True),
                  Create(line_1), Create(line_2))
        self.play(Write(extra_lines[20].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        for i in range(21, 23):
            self.play(ReplacementTransform(extra_lines[i - 1], extra_lines[i].next_to(lines[2], direction=DOWN,
                                                                                      buff=MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(line_1, line_2, extra_lines[22]))
        line_1 = Line(lines[2][0][15].get_center(), lines[2][0][17:20].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][8:10].get_center(), lines[2][0][16].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][16], shape=Circle, color=YELLOW, run_time=3, fade_out=True),
                  Create(line_1), Create(line_2))
        self.play(Write(extra_lines[23].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        for i in range(24, 27):
            self.play(ReplacementTransform(extra_lines[i - 1], extra_lines[i].next_to(lines[2], direction=DOWN,
                                                                                      buff=MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(line_1, line_2, extra_lines[26]))
        line_1 = Line(lines[2][0][15].get_center(), lines[2][0][17:20].get_center(), color=BLUE)
        line_2 = Line(lines[2][0][10].get_center(), lines[2][0][17:20].get_center(), color=BLUE)
        self.play(Circumscribe(lines[2][0][17:20], shape=Circle, color=YELLOW, run_time=3, fade_out=True),
                  Create(line_1), Create(line_2))
        self.play(Write(extra_lines[27].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        for i in range(28, 30):
            self.play(ReplacementTransform(extra_lines[i - 1], extra_lines[i].next_to(lines[2], direction=DOWN,
                                                                                      buff=MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(line_1, line_2, extra_lines[29], lines[0:3]))
        self.wait(1)

        lines = VGroup(
            Tex("The Cofactor Matrix $C_{sI-A}$ is:"),
            MathTex(r"C_{sI-A} = \begin{bmatrix} s^{2}+3s+2 & -1 & -s \\ s+3 & s^{2} + 3s & -(2s+1) \\"
                    r" 1 & s & s^{2} \end{bmatrix}"),
            Tex("The Adjoint Matrix $\\mathrm{adj}(sI-A)$:"),
            MathTex(r"\mathrm{adj}(sI-A) = C_{sI-A}^{T}")
        )

        extra_lines = VGroup(
            MathTex(r"\mathrm{adj}(sI-A) = \begin{bmatrix} s^{2}+3s+2 & -1 & -s \\ s+3 & s^{2} + 3s & -(2s+1) \\"
                    r" 1 & s & s^{2} \end{bmatrix}^{T}"),
            MathTex(r"\mathrm{adj}(sI-A)= \begin{bmatrix} s^{2}+3s+2 & s+3 & 1 \\ -1 & s^{2}+3s & s \\"
                    r"-s & -(2s+1) & s^{2} \end{bmatrix}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        for i in range(4):
            self.play(Write(lines[i]))
            self.wait(0.2)
        self.play(lines[:3].animate.shift(UP))
        self.play(ReplacementTransform(lines[3], extra_lines[0].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(extra_lines[0], extra_lines[1].next_to(lines[2], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(1)
        self.play(FadeOut(lines[:3], extra_lines[1]))

        lines = VGroup(
            Tex("Solving for the Transfer Function:"),
            MathTex(r"T(s) = C(sI-A)^{-1}B+D")
        )

        extra_lines = VGroup(
            MathTex(r"T(s) = \frac{\begin{bmatrix} 1 & 0 & 0 \end{bmatrix}"
                    r"\begin{bmatrix} s^{2}+3s+2 & s+3 & 1 \\ -1 & s^{2}+3s & s \\"
                    r"-s & -(2s+1) & s^{2} \end{bmatrix} \begin{bmatrix} 10 \\ 0 \\ 0 \end{bmatrix}}"
                    r"{s^{3}+3s^{2}+2s+1}"),
            MathTex(r"T(s)=\frac{\begin{bmatrix} s^{2}+3s+2 & s+3 & 1 \end{bmatrix}"
                    r"\begin{bmatrix} 10 \\ 0 \\ 0 \end{bmatrix}}{s^{3}+3s^{2}+2s+1} "),
            MathTex(r"T(s)=\frac{10(s^{2}+3s+2)}{s^{3}+3s^{2}+2s+1}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        lines.to_edge(UP)
        self.add(lines[0])

        for i in range(2):
            self.play(Write(lines[i]))
            self.wait(0.3)

        self.play(ReplacementTransform(lines[1], extra_lines[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.8)
        for i in range(1, 3):
            self.play(ReplacementTransform(extra_lines[i - 1],
                                           extra_lines[i].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
            self.wait(1)
        self.play(lines[0].animate.shift(2*DOWN), extra_lines[2].animate.shift(2*DOWN))
        frameBox = SurroundingRectangle(extra_lines[2], buff=0.2)
        self.play(Create(frameBox))
        self.wait(2)
        self.play(FadeOut(lines[0], extra_lines[2], frameBox))
