from manim import *


class problemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=80)
        statement = VGroup(
            Tex(r"\begin{minipage}{5.5cm}"
                r"A thermometer reading $10^{\circ}F$ is brought into a room where the temperature is $70^{\circ}F$; "
                r"1 min later, the thermometer reading is $31^{\circ}F$. Determine the temperature reading as a "
                r"function of time and find the temperature reading 5 min after the thermometer is first brought into "
                r"the room."
                r"\end{minipage}")
        )

        statement.move_to(4 * UP)
        self.play(Write(statement))
        self.wait(3)
        self.play(FadeOut(statement))

