from manim import *

config.pixel_width = 1920
config.pixel_height = 1080


class ProblemStatement(Scene):
    def construct(self):
        statement = VGroup(
            Tex(r"\begin{minipage}{9cm}" \
            r"Draw a signal-flow graph for the following state and output equations:" \
            r"\end{minipage}"),
            MathTex(r"\mathbf{\dot{x}} = \begin{bmatrix}" \
            r"-2 & 1 & 0 \\ 0 & -3 & 1 \\ -3 & -4 & -5" \
            r"\end{bmatrix} \mathbf{x} + \begin{bmatrix}" \
            r"0 \\ 0 \\ 1" \
            r"\end{bmatrix} r"),
            MathTex(r"y = \begin{bmatrix}" \
            r"0 & 1 & 0" \
            r"\end{bmatrix} \mathbf{x}")
        )

        statement[0].move_to(2 * UP)
        self.play(Write(statement[0]))
        self.wait(0.25)
        self.play(Write(statement[1].next_to(statement[0], DOWN, MED_LARGE_BUFF)),
                  Write(statement[2].next_to(statement[1], DOWN, MED_LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(statement))
        return super().construct()
    

class ProblemSolution(Scene):
    def construct(self):
        return super().construct()
