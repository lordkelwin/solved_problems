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

