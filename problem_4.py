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

        )

        line_1 = Line(extra_lines[1][0][7].get_corner(UL), extra_lines[1][0][17:20].get_corner(DR),
                      color=BLUE)

        extra_lines[1][0][7].set_color(YELLOW)
        extra_lines[1][0][12].set_color(YELLOW)
        extra_lines[1][0][17:20].set_color(YELLOW)

        MathTex(r"sI-A = \begin{bmatrix} s & -1 & 0 \\ 0 & s & -1 \\ 1 & 2 & s+3 \end{bmatrix} "
                r"\begin{matrix} s & -1 \\ 0 & s \\ 1 & 2 \end{matrix}")
