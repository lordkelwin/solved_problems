from manim import *


class ProblemStatement(Scene):
    def construct(self):
        lines = VGroup(
            Tex(r"\begin{minipage}{9 cm}"
                r"Find the orthogonal trajectories of the family of curves \\ $x^2 + y^2 = c^2.$"
                r"\end{minipage}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        lines.move_to(UP * 2.5)
        self.add(lines)
        self.play(Write(lines))
        self.wait(3)
        self.play(FadeOut(lines))
