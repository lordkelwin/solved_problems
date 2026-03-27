from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=75)
        MathTex.set_default(font_size=85)

        statement = VGroup(
            Tex(r"\begin{minipage}{5cm}"
                r"A point $P(x,y)$ moves so as its distance from the point $(3,2)$ is twice its distance from the "
                r"y-axis." 
                r"\end{minipage}")
        )

        statement.move_to(4 * UP)
        self.play(Write(statement))
        self.wait(3)
        self.play(FadeOut(statement))
