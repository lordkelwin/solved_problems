from manim import *


class ProblemStatement(Scene):
    def construct(self):
        problem = VGroup(
            Tex(r"\begin{minipage}{9 cm}"
                r"An RL circuit has an emf given (in volts) by $3\sin{2t}$, a resistance of $10\,\mathrm{ohms}$, an "
                r"inductance of $0.5\,\mathrm{henry}$, and an initial current of $6\,\mathrm{amperes}$. Find the "
                r"current in the circuit at any time $t$."
                r"\end{minipage}")
        )

        problem.arrange(DOWN, buff=MED_LARGE_BUFF)
        problem[0].move_to(2*UP)
        self.add(problem[0])
        self.play(Write(problem[0]))
        self.wait(3)
        self.play(FadeOut(problem))
