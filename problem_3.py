from manim import *


class ProblemStatement(Scene):
    def construct(self):
        problemStatement = VGroup(
            Tex(
                r"\begin{minipage}{9 cm}"
                r"Find the state-space representation in phase-variable form for the transfer function:\\"
                r"\end{minipage}"),
            MathTex(r"\frac{C(s)}{R(s)} = \frac{24}{s^{3}+9s^{2}+26s+24}")
        )

        problemStatement.arrange(DOWN, buff=MED_LARGE_BUFF)
        problemStatement.to_corner(UL)
        self.add(problemStatement[0])
        self.play(Write(problemStatement[0]))
        self.wait(0.2)
        self.play(Write(problemStatement[1]))
        self.wait(3)
        self.play(FadeOut(problemStatement))


class ProblemSolution(Scene):
    def construct(self):
        lines = VGroup(

        )
