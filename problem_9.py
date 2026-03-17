from manim import *


class problemStatement(Scene):
    def construct(self):
        statements = VGroup(
            Tex(r"\begin{minipage}{6cm}"
                r"A certain population is known to be growing at a rate given by the logistic equation "
                r"$dx/dt=x(b-ax)$. Show that the maximum rate of growth will occur when the population is "
                r"equal to half its equilibrium size, that is, when the population is $b/2a$."
                r"\end{minipage}")
        )

        statements.move_to(3 * UP)
        self.play(Write(statements))
        self.wait(3)
        self.play(FadeOut(statements))


class problemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set(font_size=75)

