from manim import *


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
            MathTex(r"\int_{0}^{s} \mathrm{d}s = \int_0^{t_1} \frac{t^2 - t + 1}{(t + 2)^2(t^2 + 1)}\,\mathrm{d}t"),
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
            MathTex(r"t^2 - t + 1 =(A + C)t^3 + (2A + B + 4C + D)t^2 + \\ (A + 4C + 4D)t + (2A + B + 4D)")
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
            MathTex(r"t^3:\,A + C = 0\,\,\,\,\mathrm{(eq. 1)}"),
            MathTex(r"t^2:\,2A + B + 4C + D = 1\,\,\,\mathrm{(eq. 2)}"),
            MathTex(r"t:\,A + 4C + 4D = -1\,\,\,\mathrm{(eq. 3)}"),
            MathTex(r"t^0:\,2A + B + 4D = 1\,\,\,\mathrm{(eq. 4)}")
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

        lines = VGroup(
            Tex("Manipulating equation 1: "),
            MathTex(r"A + C = 0"),
            Tex("Substitute equation 5 in equations 2, 3, and 4:"),
            MathTex(r"A + 2B + 4C + D = 1"),
            MathTex(r"A + 4C + 4D = -1"),
            MathTex(r"2A + B + 4D = 1")
        )

        lines_extra = VGroup(
            MathTex(r"A = -C"),
            MathTex(r"A = -C\,\,\,\mathrm{(eq. 5)}"),
            MathTex(r"-2C + B + 4C + D = 1"),
            MathTex(r"B + 2C + D = 1\,\,\,\mathrm{(eq. 6)}"),
            MathTex(r"-C + 4C + 4D = -1"),
            MathTex(r"3C + 4D = -1\,\,\,\mathrm{(eq. 7)}"),
            MathTex(r"2(-C) + B + 4D = 1"),
            MathTex(r"B - 2C + 4D = 1\,\,\,\mathrm{(eq. 8)}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait()
        self.play(Write(lines[1]))
        self.play(ReplacementTransform(lines[1], lines_extra[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait()
        self.play(ReplacementTransform(lines_extra[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[1].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait()
        self.play(Write(lines[2].next_to(lines_extra[1], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait()
        self.play(Write(lines[3]))
        self.wait()
        self.play(ReplacementTransform(lines[3], lines_extra[2].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait()
        self.play(ReplacementTransform(lines_extra[2].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[3].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait()
        self.play(Write(lines[4]))
        self.wait()
        self.play(ReplacementTransform(lines[4], lines_extra[4].next_to(lines[3], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait()
        self.play(ReplacementTransform(lines_extra[4].next_to(lines[3], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[5].next_to(lines[3], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait()
        self.play(Write(lines[5]))
        self.wait()
        self.play(ReplacementTransform(lines[5], lines_extra[6].next_to(lines[4], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait()
        self.play(ReplacementTransform(lines_extra[6].next_to(lines[4], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[7].next_to(lines[4], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(lines[0], lines[2], lines_extra[1:8:2]))

        lines = VGroup(
            Tex("Subtracting equations 6 and 8:"),
            MathTex(r"(B + 2C + D) - (B - 2C + 4D) = 1 - 1"),
            Tex("Substitute equation 9 in equation 7:"),
            MathTex(r"3C + 4D = -1")
        )

        lines_extra = [
            MathTex(r"B + 2C + D - B + 2C - 4D = -1 - 1"),
            MathTex(r"4C - 3D = 0"),
            MathTex(r"4C = 3D"),
            MathTex(r"\frac{1}{4}\times 4C = 3D \times \frac{1}{4}"),
            MathTex(r"C = \frac{3}{4} D\,\,\, \mathrm{(eq. 9)}"),
            MathTex(r"3(\frac{3}{4}D) + 4D = -1"),
            MathTex(r"\frac{9}{4}D + 4D = -1"),
            MathTex(r"4\times\bigg(\frac{9}{4}D + 4D\bigg) = -1 \times 4"),
            MathTex(r"9D + 16D = -4"),
            MathTex(r"25D = -4"),
            MathTex(r"\frac{1}{25}\times 25D = -4 \times \frac{1}{25}"),
            MathTex(r"D = -\frac{4}{25}")
        ]

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait()
        self.play(Write(lines[1]))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[1], lines_extra[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[1].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[1].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[2].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[2].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[3].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[3].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[4].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[2].next_to(lines_extra[4], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[3].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[3], lines_extra[5].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[5].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[6].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[6].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[7].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[7].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[8].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[8].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[9].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[9].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[10].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines_extra[10].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF),
                                       lines_extra[11].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(1)
        self.play(FadeOut(lines[0:3:2], lines_extra[4], lines_extra[11]))

        lines = VGroup(
            Tex("Substitute $D = -\\frac{4}{25}$ in equation 9:"),
            MathTex(r"C = \frac{3}{4} \bigg(-\frac{4}{25}\bigg)"),
            Tex("Substitute $C = -\\frac{3}{25}$ in equation 5:"),
            MathTex(r"A= -\bigg(-\frac{3}{25}\bigg)"),
        )

        lines_extra = [
            MathTex(r"C = -\frac{3}{25}"),
            MathTex(r"A = \frac{3}{25}")
        ]

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.5)
        self.play(Write(lines[1]))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[1], lines_extra[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[2].next_to(lines_extra[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[3]))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[3], lines_extra[1].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(1)
        self.play(FadeOut(lines[0:4:2], lines_extra[0], lines_extra[1]))

        lines = VGroup(

        )
