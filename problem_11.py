from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=80)
        MathTex.set_default(font_size=75)
        statement = VGroup(
            Tex(r"\begin{minipage}{5.5cm}"
                r"A college dormitory houses 100 students, each of whom is susceptible to a certain virus infection. A "
                r"simple model of epidemics assumes that during the course of an epidemic the rate of change with "
                r"respect to time of the number of infected students $I$ is proportional to the number of infected "
                r"students and also proportional to the number of uninfected students, $100 - I$. If at time $t=0$, "
                r"a single student becomes infected, show that the number of infected students at time $t$ is given by:"
                r"\end{minipage}"),
            MathTex(r"I = \frac{100e^{100kt}}{99+e^{100kt}}")
        )

        statement[0].move_to(5 * UP)
        self.play(Write(statement[0]))
        self.wait(0.2)
        self.play(Write(statement[1].next_to(statement[0], DOWN, LARGE_BUFF)))
        self.wait(3)
        self.play(FadeOut(statement))

