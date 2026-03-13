from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=90)
        statement = VGroup(
            Tex(r"\begin{minipage}{6 cm}"
                r"Find the inverse Laplace Transform of the function using convolution theorem:"
                r"\end{minipage}"),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{1}{(s-1)^{2}}\bigg\}")
        )

        statement[0].move_to(3 * UP)

        self.play(Write(statement[0]))
        self.wait(0.5)
        self.play(Write(statement[1].next_to(statement[0], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(statement))
