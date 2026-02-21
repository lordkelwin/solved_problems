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
        self.play(ReplacementTransform(lines[3], lines_1[3]))
        self.wait()
        self.play(ReplacementTransform(lines_1[3], lines_2[3]))
        self.wait()
        self.play(FadeOut(lines[0:3], lines_2[3]))

        lines = VGroup(
            Tex("Integrating both sides:"),
            MathTex(r"\int_{0}^{s} \mathrm{d}x = \int_0^{t_1} \frac{t^2 - t + 1}{(t + 2)^2(t^2 + 1)}\,\mathrm{d}t"),
            Tex("Before performing the integration, a partial fraction \\\\ decomposition must be performed. "
                "This equation is under case 3 \\\\ (at least 1 Quadratic factors)."),
            MathTex(r"\frac{t^2 - t + 1}{(t + 2)^2(t^2 + 1)} = \frac{A}{t + 2} + \frac{B}{(t + 2)^2} + "
                    r"\frac{Ct + D}{t^2 + 1}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait()
        self.play(Write(lines[1]))
        self.wait()
        self.play(Write(lines[2]))
        self.wait()
        self.play(Write(lines[3]))
        self.wait(2)
        self.play(FadeOut(lines))

        lines = VGroup(
            Tex("Multiplying both sides by its denominator \\\\ and simplify:"),
            MathTex(r"t^2 - t + 1 = A(t + 2)(t^2 + 1) + B(t^2 + 1) + (Ct + D)(t + 2)^2"),
        )

        lines_1 = [
            MathTex(r"t^2 - t + 1 = A(t^3 + 2t^2 + t + 2) + B(t^2 + 1) + \\ (Ct + D)(t^2 + 4t + 4)"),
            MathTex(r"t^2 - t + 1 = A(t^3 + 2t^2 + t + 2) + B(t^2 + 1) + \\ (Ct^3 + 4Ct^2 + 4Ct + Dt^2 + 4Dt + 4D)"),
            MathTex(r"t^2 - t + 1 = (At^3 + 2At^2 + At + 2A) + (Bt^2 + B) + \\ (Ct^3 + 4Ct^2 + 4Ct)  + "
                    r"(Dt^2 + 4Dt + 4D)"),
            MathTex(r"t^2 - t + 1 =(A + C)t^3 + (2A + B + 4C + D)t^2 + \\ (A + B + 4C + 4D)t + (2A + B + 4D)")
        ]

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        lines[0].move_to(UP * 2)
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait()
        self.play(Write(lines[1]))
        self.wait()
        self.play(ReplacementTransform(lines[1], lines_1[0]))
        self.wait()
        self.play(ReplacementTransform(lines_1[0], lines_1[1]))
        self.wait()
        self.play(ReplacementTransform(lines_1[1], lines_1[2]))
        self.wait()
        self.play(ReplacementTransform(lines_1[2], lines_1[3]))
        self.wait(2)
        self.play(FadeOut(lines[0], lines_1[3]))

        lines = VGroup(
            Tex("Equating the coefficients in both sides:"),
            MathTex(r"t^3:\,A + C = 0"),
            MathTex(r"t^2:\,2A + B + 4C + D = 1"),
            MathTex(r"t:\,A + B + 4C + 4D = -1"),
            MathTex(r"t^0:\,2A + B + 4D = 1")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.5)
        for i in range(1, 5):
            self.play(Write(lines[i]))
            self.wait(0.5)
        self.wait(0.5)
        self.play(FadeOut(lines))

