from manim import *


class ProblemStatement(Scene):
    def construct(self):
        problemStatement = VGroup(
            Tex(
                r"\begin{minipage}{9 cm}"
                r"Find the state-space representation in phase-variable form for the transfer function:\\"
                r"\end{minipage}"),
            MathTex(r"\frac{C(s)}{R(s)} = \frac{24}{s^{3}+9s^{2}+26s+24}")
        )

        problemStatement.arrange(DOWN, buff=MED_LARGE_BUFF)
        problemStatement.to_corner(UL)
        self.add(problemStatement[0])
        self.play(Write(problemStatement[0]))
        self.wait(0.2)
        self.play(Write(problemStatement[1]))
        self.wait(3)
        self.play(FadeOut(problemStatement))


class ProblemSolution(Scene):
    def construct(self):
        lines = VGroup(
            Tex("Multiplying both sides by the denominator:"),
            MathTex(r"[(s^{3}+9s^{2}+26s+24)R(s)]\times\bigg[\frac{C(s)}{R(s)} = \\\frac{24}{s^{3}+9s^{"
                    r"2}+26s+24}\bigg]\times[(s^{3}+9s^{2}+26s+24)R(s)]"),
            Tex("Applying Inverse Laplace Transform in both sides:"),
            MathTex(r"\mathcal{L}^{-1}[s^{3}C(s)+9s^{2}C(s)+26sC(s)+24C(s)=24R(s)]")
        )

        lines_extra = VGroup(
            MathTex(r"(s^{3}+9s^{2}+26s+24)C(s)=24R(s)"),
            MathTex(r"s^{3}C(s)+9s^{2}C(s)+26sC(s)+24C(s)=24R(s)"),
            MathTex(r"\frac{d^{3}c(t)}{dt^{3}}+9\frac{d^{2}c(t)}{dt^{2}}+26\frac{dc(t)}{dt}+24c(t)=24r(t)")
        )
        numeratorCancel = VGroup(lines[1][0][16:20].set_color(BLUE), lines[1][0][36:49].set_color(YELLOW))
        denominatorCancel = VGroup(lines[1][0][28:32].set_color(BLUE), lines[1][0][53:66].set_color(YELLOW))

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        line_1 = Line(numeratorCancel[0].get_corner(DL),
                      numeratorCancel[0].set_color(BLUE).get_corner(UR), color=YELLOW)
        line_2 = Line(denominatorCancel[0].set_color(BLUE).get_corner(DL),
                      denominatorCancel[0].set_color(BLUE).get_corner(UR), color=YELLOW)
        line_3 = Line(numeratorCancel[1].get_corner(DL),
                      numeratorCancel[1].set_color(YELLOW).get_corner(UR), color=BLUE)
        line_4 = Line(denominatorCancel[1].set_color(YELLOW).get_corner(DL),
                      denominatorCancel[1].set_color(YELLOW).get_corner(UR), color=BLUE)

        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1]))
        self.play(Create(line_1),
                  Create(line_2),
                  Create(line_3),
                  Create(line_4),
                  FadeOut(numeratorCancel),
                  FadeOut(denominatorCancel))
        self.wait(0.3)
        self.play(FadeOut(line_1, line_2, line_3, line_4))
        self.play(ReplacementTransform(lines[1], lines_extra[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines_extra[0],
                                       lines_extra[1].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[2].next_to(lines_extra[1], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[3].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[3], lines_extra[2].next_to(lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(1)
        self.play(FadeOut(lines[0:3:2], lines_extra[1:3]))

        lines = VGroup(
            Tex("Assign $x_{1} = c(t)$, and it follows:"),
            MathTex(r"x_{1} = c(t)"),
            MathTex(r"x_{2} = \frac{dc(t)}{dt}"),
            MathTex(r"x_{3} = \frac{d^{2}c(t)}{dt^{2}}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1]))
        self.wait(0.3)
        self.play(Write(lines[2]))
        self.wait(0.3)
        self.play(Write(lines[3]))
        self.wait(1)
        self.play(FadeOut(lines))

        lines = VGroup(
            Tex("Apply derivative in both sides of the equations:"),
            MathTex(r"\frac{d}{dt}[x_{1}=c(t)]"),
            MathTex(r"\frac{d}{dt}\bigg[x_{2}=\frac{dc(t)}{dt}\bigg]"),
            MathTex(r"\frac{d}{dt}\bigg[x_{3}=\frac{d^{2}c(t)}{dt^{2}}\bigg]")
        )

        lines_extra = VGroup(
            MathTex(r"\frac{dx_{1}}{dt} = \frac{dc(t)}{dt} = x_{2}"),
            MathTex(r"\frac{dx_{2}}{dt} = \frac{d^{2}c(t)}{dt^{2}} = x_{3}"),
            MathTex(r"\frac{dx_{3}}{dt} = \frac{d^{3}c(t)}{dt^{3}}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1]))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[1], lines_extra[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[2].next_to(lines_extra[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[2], lines_extra[1].next_to(lines_extra[0],
                                                                        direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[3].next_to(lines_extra[1], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[3], lines_extra[2].next_to(lines_extra[1], direction=DOWN,
                                                                        buff=MED_LARGE_BUFF)))
        self.wait(1)
        self.play(FadeOut(lines[0], lines_extra))

        lines = VGroup(
            Tex("Substitute to the equation and solve for $\\frac{dx_{3}}{dt}$:"),
            MathTex(r"\frac{dx_{3}}{dt} + 9x_{3} + 26x_{2} + 24x_{1} = 24r(t)")
        )

        lines_extra = VGroup(
            MathTex(r"\frac{dx_{3}}{dt} = -24x_{1} - 26x_{2} - 9x_{3} + 24r(t)")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1]))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[1], lines_extra[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(1)
        self.play(FadeOut(lines[0], lines_extra))

        lines = VGroup(
            Tex("Consolidating the state equations:"),
            MathTex(r"\frac{dx_{1}}{dt} = x_{2}"),
            MathTex(r"\frac{dx_{2}}{dt} = x_{3}"),
            MathTex(r"\frac{dx_{3}}{dt} = -24x_{1} - 26x_{2} - 9x_{3} + 24r(t)"),
            Tex("With its output equation of:"),
            MathTex(r"y = x_{1}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1:4]))
        self.wait(1)
        self.play(FadeOut(lines))

        lines = VGroup(
            Tex("The Phase-Variable Form of the Transfer Function:"),
            MathTex(r"\begin{bmatrix} \dot{x}_{1} \\ \dot{x}_{2} \\ \dot{x}_{3} \end{bmatrix} ="
                    r"\begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -24 & -26 & -9 \end{bmatrix}"
                    r"\begin{bmatrix} x_{1} \\ x_{2} \\ x_{3} \end{bmatrix} + "
                    r"\begin{bmatrix} 0 \\ 0 \\ 24 \end{bmatrix} r(t)"),
            MathTex(r"y = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix} "
                    r"\begin{bmatrix} x_{1} \\ x_{2} \\ x_{3} \end{bmatrix}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1]))
        self.wait(0.3)
        self.play(Write(lines[2]))
        framebox = SurroundingRectangle(lines[1:3], buff=0.25)
        self.play(Create(framebox))
        self.wait(1)
        self.play(FadeOut(lines))
