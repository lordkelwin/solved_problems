from manim import *
import numpy as np


class VelocityProblemStatement(Scene):
    def construct(self):
        problem_statement = Tex(
            r"\begin{minipage}{9 cm}"
            r"A particle is moving along a straight line so that if $v$ ft/sec "
            r"is the velocity of the particle at $t$ sec, then \\"
            r"$v = \frac{t^2 - t + 1}{(t + 2)^2(t^2 +1)}$\\"
            r"Find a formula for the distance traveled by the particle from the time when "
            r"$t = 0$ to the time when $t = t_1$."
            r"\end{minipage}"
        )
        problem_statement.to_corner(UL)
        problem_statement.set_stroke(width=0.5)
        self.add(problem_statement)
        self.play(Write(problem_statement))
        self.wait(5)
        self.play(FadeOut(problem_statement))


class VelocityProblemSolution(Scene):
    def construct(self):
        lines = VGroup(
            Tex("Remember the relationship between velocity and displacement:"),
            MathTex(r"v = \frac{ds}{dt}"),
            Tex("Rewriting the equation:"),
            MathTex(r"\frac{\mathrm{d}s}{\mathrm{d}t} = \frac{t^2 - t + 1}{(t + 2)^2(t^2 + 1)}")
        )

        lines_1 = VGroup(
            Tex("Remember the relationship between velocity and displacement:"),
            MathTex(r"v = \frac{ds}{dt}"),
            Tex("Rewriting the equation:"),
            MathTex(r"\mathrm{d}t\times\frac{\mathrm{d}s}{\mathrm{d}t} = \bigg(\frac{t^2 - t + 1}{(t + 2)^2(t^2 + "
                    r"1)}\bigg)\times\mathrm{d}t")
        )

        lines_2 = VGroup(
            Tex("Remember the relationship between velocity and displacement:"),
            MathTex(r"v = \frac{ds}{dt}"),
            Tex("Rewriting the equation:"),
            MathTex(r"\mathrm{d}s = \frac{t^2 - t + 1}{(t + 2)^2(t^2 + 1)}\,\mathrm{d}t")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        lines_1.arrange(DOWN, buff=MED_LARGE_BUFF)
        lines_2.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(lines[0]))
        self.wait()
        self.play(Write(lines[1]))
        self.wait()
        self.play(Write(lines[2]))
        self.wait()
        self.play(Write(lines[3]))
        self.play(ReplacementTransform(lines[2], lines_1[2]))
        self.wait()
        self.play(ReplacementTransform(lines_1[2], lines_2[2]))
        self.wait()
        self.play(FadeOut(lines[0:2], lines_2[3]))
