from manim import *


class problemStatement(Scene):
    def construct(self):
        statements = VGroup(
            Tex(r"\begin{minipage}{6cm}"
                r"A certain population is known to be growing at a rate given by the logistic equation "
                r"$dx/dt=x(b-ax)$. Show that the maximum rate of growth will occur when the population is "
                r"equal to half its equilibrium size, that is, when the \\population is $b/2a$."
                r"\end{minipage}", font_size=80)
        )

        statements.move_to(3 * UP)
        self.play(Write(statements))
        self.wait(3)
        self.play(FadeOut(statements))


class problemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=75)
        solutionLines = VGroup(
            Tex(r"\begin{minipage}{6 cm}"
                r"To determine the equilibrium size, the growth rate must be equal to zero:"
                r"\end{minipage}"),
            MathTex(r"\frac{dx}{dt}=x(b-ax)"),
            MathTex(r"0=x(b-ax)"),
            MathTex(r"\begin{cases}"
                    r"x=0 \\"
                    r"b-ax=0"
                    r"\end{cases}"),
            MathTex(r"\begin{cases}"
                    r"x=0 \\"
                    r"ax=b"
                    r"\end{cases}"),
            MathTex(r"\begin{cases}"
                    r"x=0 \\"
                    r"x=\frac{b}{a}"
                    r"\end{cases}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"The equilibrium size must be non-zero, therefore:"
                r"\end{minipage}"),
            MathTex(r"x=\frac{b}{a}"),
            MathTex(r"n_{eq}=\frac{b}{a}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"For maximum rate of growth, the \\second derivative must be equal to zero:"
                r"\end{minipage}"),
            MathTex(r"\frac{dx}{dt}=x(b-ax)"),
            MathTex(r"\frac{dx}{dt}=bx-ax^{2}"),
            MathTex(r"\frac{d}{dt}\left[\frac{dx}{dt}=bx-ax^{2}\right]"),
            MathTex(r"\frac{d^{2}x}{dt^{2}}=\frac{d}{dt}[bx-ax^{2}]"),
            MathTex(r"\frac{d^{2}x}{dt^{2}}=b\frac{dx}{dt}-2ax\frac{dx}{dt}"),
            MathTex(r"0=b\frac{dx}{dt}-2ax\frac{dx}{dt}"),
            MathTex(r"0=(b-2ax)\frac{dx}{dt}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"Since $dx/dt=x(b-ax)$:"
                r"\end{minipage}"),
            MathTex(r"0=(b-2ax)(x)(b-ax)"),
            Tex(r"Solving for $x$:"),
            MathTex(r"0 = "
                    r"\begin{cases}"
                    r"x \\"
                    r"b-ax \\"
                    r"b-2ax"
                    r"\end{cases}"),
            MathTex(r"\begin{cases}"
                    r"x = 0 \\"
                    r"b-ax = 0 \\"
                    r"b-2ax = 0"
                    r"\end{cases}"),
            MathTex(r"\begin{cases}"
                    r"x = 0 \\"
                    r"ax = b \\"
                    r"2ax = b"
                    r"\end{cases}"),
            MathTex(r"\begin{cases}"
                    r"x = 0 \\"
                    r"x = \frac{b}{a} \\"
                    r"x = \frac{b}{2a}"
                    r"\end{cases}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"Substituting the values of x to determine the maximum rate of change:"
                r"\end{minipage}"),
            Tex(r"if $x=0$"),
            MathTex(r"\frac{dx}{dt}=x(b-ax)"),
            MathTex(r"\frac{dx}{dt}=0[b-a(0)]"),
            MathTex(r"\frac{dx}{dt}=0"),
            Tex("if $x = b/a$"),
            MathTex(r"\frac{dx}{dt}=x(b-ax)"),
            MathTex(r"\frac{dx}{dt}=\left(\frac{b}{a}\right)\left[b-a\left(\frac{b}{a}\right)\right]"),
            MathTex(r"\frac{dx}{dt}=\left(\frac{b}{a}\right)(b-b)"),
            MathTex(r"\frac{dx}{dt}=\left(\frac{b}{a}\right)(0)"),
            MathTex(r"\frac{dx}{dt}=0"),
            Tex("if $x = b/2a$"),
            MathTex(r"\frac{dx}{dt}=x(b-ax)"),
            MathTex(r"\frac{dx}{dt}=\left(\frac{b}{2a}\right)\left[b-a\left(\frac{b}{2a}\right)\right]"),
            MathTex(r"\frac{dx}{dt}=\left(\frac{b}{2a}\right)\left(b-\frac{b}{2}\right)"),
            MathTex(r"\frac{dx}{dt}=\left(\frac{b}{2a}\right)\left(\frac{b}{2}\right)"),
            MathTex(r"\frac{dx}{dt}=\frac{b^{2}}{4a}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"By comparing different values, we have:"
                r"\end{minipage}"),
            MathTex(r"\frac{dx}{dt} = "
                    r"\begin{cases}"
                    r"0 \quad \mathrm{if } x = 0 \\"
                    r"0 \quad \mathrm{if } x = b/a"
                    r"\frac{b^{2}}{4a} & \quad \mathrm{if } x = b/2a"
                    r"\end{cases}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"Therefore, the maximum rate of growth is:"
                r"\end{minipage}"),
            MathTex(r"x = \frac{b}{2a}")
        )

        solutionLines[0].move_to(5 * UP)
        self.play(Write(solutionLines[0]))
        self.wait(0.3)
        self.play(Write(solutionLines[1].next_to(solutionLines[0], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        solutionLines[1][0][0:5].set_color(YELLOW)
        arrowLines = Arrow(solutionLines[1][0][0:5].get_corner(DL),
                           solutionLines[1][0][0:5].get_corner(UR), color=BLUE)
        tempText = MathTex(r"0", font_size=50, color=BLUE)
        self.play(Create(arrowLines))
        self.play(Write(tempText.next_to(solutionLines[1][0][0:5].get_corner(UR), UP, SMALL_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(arrowLines, tempText, run_time=0.5))
        self.play(ReplacementTransform(solutionLines[1], solutionLines[2].next_to(solutionLines[0], DOWN,
                                                                                  LARGE_BUFF)))
        self.wait(0.5)
        for i in range(3, 6):
            self.play(ReplacementTransform(solutionLines[i-1], solutionLines[i].next_to(solutionLines[0], DOWN,
                                                                                        LARGE_BUFF)))
            self.wait(0.5)

        for i in range(6, 8):
            self.play(Write(solutionLines[i].next_to(solutionLines[i-1], DOWN, LARGE_BUFF)))
            self.wait(0.3)
        self.play(ReplacementTransform(solutionLines[7], solutionLines[8].next_to(solutionLines[6], DOWN, LARGE_BUFF)))
        boxRectangle = SurroundingRectangle(solutionLines[8], buff=0.5)
        self.play(Create(boxRectangle))
        self.wait(1.25)
        self.play(FadeOut(solutionLines[0], solutionLines[5:7], solutionLines[8], boxRectangle))

        solutionLines[9].move_to(6 * UP)
        self.play(Write(solutionLines[9]))
        self.wait(0.3)
        self.play(Write(solutionLines[10].next_to(solutionLines[9], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(11, 17):
            self.play(ReplacementTransform(solutionLines[i-1], solutionLines[i].next_to(solutionLines[9], DOWN,
                                                                                        LARGE_BUFF)))
            self.wait(0.5)
        self.wait(1.25)
