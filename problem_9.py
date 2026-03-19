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
                    r"x=b/a"
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
            Tex(r"Since $dx/dt=x(b-ax)$:"),
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
            MathTex(r"x = "
                    r"\begin{cases}"
                    r"0 \\"
                    r"b/a \\"
                    r"b/2a"
                    r"\end{cases}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"Substituting the values of x to \\determine the maximum rate of change:"
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
                    r"0 \qquad \qquad \mathrm{if} \, x = 0 \\"
                    r"0 \qquad \qquad \mathrm{if} \, x = b/a \\"
                    r"b^{2}/4a \qquad \mathrm{if} \, x = b/2a"
                    r"\end{cases}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"Therefore, the maximum rate of growth is:"
                r"\end{minipage}"),
            MathTex(r"x = \frac{b}{2a}"),
            Tex(r"\begin{minipage}{6 cm}"
                r"To prove that the maximum rate of growth is half of the equilibrium size:"
                r"\end{minipage}"),
            MathTex(r"x = \frac{b}{2a}"),
            MathTex(r"x = \left(\frac{1}{2}\right)\left(\frac{b}{a}\right)"),
            Tex("Since $n_{eq}=b/a$:"),
            MathTex(r"x = \frac{1}{2}{n_{eq}}")
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
            self.play(ReplacementTransform(solutionLines[i - 1], solutionLines[i].next_to(solutionLines[0], DOWN,
                                                                                          LARGE_BUFF)))
            self.wait(0.5)

        for i in range(6, 8):
            self.play(Write(solutionLines[i].next_to(solutionLines[i - 1], DOWN, LARGE_BUFF)))
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
            self.play(ReplacementTransform(solutionLines[i - 1], solutionLines[i].next_to(solutionLines[9], DOWN,
                                                                                          LARGE_BUFF)))
            if i == 14:
                solutionLines[i][0][0:7].set_color(BLUE)
                arrowLines = Arrow(solutionLines[i][0][0:7].get_corner(DL),
                                   solutionLines[i][0][0:7].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"0", font_size=50, color=BLUE)
                self.play(Create(arrowLines))
                self.play(Write(tempText.next_to(solutionLines[i][0][0:7].get_corner(UR), UP, SMALL_BUFF)))
                self.wait(0.5)
                self.play(FadeOut(arrowLines, tempText, run_time=0.5))
            else:
                self.wait(0.5)
        self.play(Write(solutionLines[17].next_to(solutionLines[16], DOWN, LARGE_BUFF)))
        solutionLines[17][0][5:].set_color(BLUE)
        self.wait(0.3)
        self.play(ReplacementTransform(solutionLines[16], solutionLines[18].next_to(solutionLines[17], DOWN,
                                                                                    LARGE_BUFF)))
        self.play(solutionLines[17].animate.move_to(4 * UP))
        self.play(solutionLines[18].animate.move_to(2 * UP))
        self.wait(0.3)
        self.play(Write(solutionLines[19].next_to(solutionLines[18], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionLines[20].next_to(solutionLines[19], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(21, 24):
            self.play(ReplacementTransform(solutionLines[i - 1], solutionLines[i].next_to(solutionLines[19], DOWN,
                                                                                          LARGE_BUFF)))
            self.wait(0.5)
        boxRectangle = SurroundingRectangle(solutionLines[23], buff=0.5)
        self.play(Create(boxRectangle))
        self.wait(1.25)
        self.play(FadeOut(solutionLines[9], solutionLines[23], solutionLines[17:20], boxRectangle))

        solutionLines[24].move_to(3 * UP)
        self.play(Write(solutionLines[24]))
        self.wait(0.3)
        self.play(Write(solutionLines[25].next_to(solutionLines[24], DOWN, LARGE_BUFF)))
        solutionLines[25][0][2:].set_color(BLUE)
        self.wait(0.3)
        self.play(Write(solutionLines[26].next_to(solutionLines[25], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(27, 29):
            self.play(ReplacementTransform(solutionLines[i - 1], solutionLines[i].next_to(solutionLines[25], DOWN,
                                                                                          LARGE_BUFF)))
            if i == 27:
                solutionLines[i][0][6:].set_color(YELLOW)
                arrowLines = Arrow(solutionLines[i][0][6:].get_corner(DL),
                                   solutionLines[i][0][6:].get_corner(UR), color=BLUE)
                tempText = MathTex(r"0", font_size=50, color=BLUE)
                self.play(Create(arrowLines))
                self.play(Write(tempText.next_to(solutionLines[i][0][6:].get_corner(UR), UP, SMALL_BUFF)))
                self.wait(0.5)
                self.play(FadeOut(arrowLines, tempText, run_time=0.4))
            else:
                self.wait(0.5)
        boxRectangle = SurroundingRectangle(solutionLines[28], buff=0.5)
        self.play(Create(boxRectangle))
        self.wait(1)
        self.play(FadeOut(solutionLines[25], solutionLines[28], boxRectangle))
        self.wait(0.2)

        self.play(Write(solutionLines[29]))
        solutionLines[29][0][2:].set_color(YELLOW)
        self.wait(0.3)
        self.play(Write(solutionLines[30].next_to(solutionLines[29], DOWN, LARGE_BUFF)))
        for i in range(31, 35):
            self.play(ReplacementTransform(solutionLines[i - 1], solutionLines[i].next_to(solutionLines[29], DOWN,
                                                                                          LARGE_BUFF)))
            if i == 31:
                solutionLines[i][0][14].set_color(BLUE)
                solutionLines[i][0][18].set_color(YELLOW)
                arrowLines = Line(solutionLines[i][0][14].get_corner(DL),
                                  solutionLines[i][0][14].get_corner(UR), color=YELLOW)
                arrowLines_1 = Line(solutionLines[i][0][18].get_corner(DL),
                                    solutionLines[i][0][18].get_corner(UR), color=BLUE)
                self.play(Create(arrowLines), Create(arrowLines_1))
                self.wait(0.5)
                self.play(FadeOut(arrowLines, arrowLines_1, run_time=0.35))
            elif i == 32:
                solutionLines[i][0][12:15].set_color(BLUE)
                arrowLines = Arrow(solutionLines[i][0][12:15].get_corner(DL),
                                   solutionLines[i][0][12:15].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"0", font_size=50, color=YELLOW)
                self.play(Create(arrowLines))
                self.wait(0.3)
                self.play(Write(tempText.next_to(solutionLines[i][0][12:15].get_corner(UR), UP, SMALL_BUFF)))
                self.wait(0.5)
                self.play(FadeOut(arrowLines, tempText, run_time=0.35))
            else:
                self.wait(0.5)
        boxRectangle = SurroundingRectangle(solutionLines[34], buff=0.5)
        self.play(Create(boxRectangle))
        self.wait(1)
        self.play(FadeOut(boxRectangle, solutionLines[34], solutionLines[29]))

        self.play(Write(solutionLines[35]))
        solutionLines[35][0][2:].set_color(YELLOW)
        self.wait(0.3)
        self.play(Write(solutionLines[36].next_to(solutionLines[35], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(37, 41):
            self.play(ReplacementTransform(solutionLines[i - 1], solutionLines[i].next_to(solutionLines[35], DOWN,
                                                                                          LARGE_BUFF)))
            if i == 37:
                solutionLines[i][0][15].set_color(YELLOW)
                solutionLines[i][0][20].set_color(BLUE)
                arrowLines = Line(solutionLines[i][0][15].get_corner(DL), solutionLines[i][0][15].get_corner(UR),
                                   color=BLUE)
                arrowLines_1 = Line(solutionLines[i][0][20].get_corner(DL), solutionLines[i][0][20].get_corner(UR),
                                     color=YELLOW)
                self.play(Create(arrowLines), Create(arrowLines_1))
                self.wait(0.5)
                self.play(FadeOut(arrowLines, arrowLines_1, run_time=0.35))
            elif i == 38:
                solutionLines[i][0][13:18].set_color(BLUE)
                arrowLines = Arrow(solutionLines[i][0][13:18].get_corner(DL),
                                   solutionLines[i][0][13:18].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"\frac{b}{2}", font_size=50, color=YELLOW)
                self.play(Create(arrowLines))
                self.wait(0.2)
                self.play(Write(tempText.next_to(solutionLines[i][0][13:18].get_corner(UR), UP, SMALL_BUFF)))
                self.wait(0.5)
                self.play(FadeOut(arrowLines, tempText, run_time=0.35))
            else:
                self.wait(0.5)
        boxRectangle = SurroundingRectangle(solutionLines[40], buff=0.5)
        self.play(Create(boxRectangle))
        self.wait(1.25)
        self.play(FadeOut(boxRectangle, solutionLines[40], solutionLines[35], solutionLines[24]))

        solutionLines[41].move_to(3 * UP)
        self.play(Write(solutionLines[41]))
        self.wait(0.3)
        self.play(Write(solutionLines[42].next_to(solutionLines[41], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(FadeTransform(solutionLines[41], solutionLines[43].move_to(3 * UP)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutionLines[42], solutionLines[44].next_to(solutionLines[43], DOWN,
                                                                                    LARGE_BUFF)))
        boxRectangle = SurroundingRectangle(solutionLines[42], buff=0.5)
        self.play(Create(boxRectangle))
        self.wait(1.25)
        self.play(FadeOut(boxRectangle, solutionLines[44], solutionLines[43]))

        solutionLines[45].move_to(2 * UP)
        self.play(Write(solutionLines[45]))
        self.wait(0.3)
        self.play(Write(solutionLines[46].next_to(solutionLines[45], DOWN, LARGE_BUFF)))
        self.play(ReplacementTransform(solutionLines[46], solutionLines[47].next_to(solutionLines[45], DOWN,
                                                                                    LARGE_BUFF)))
        self.wait(0.5)
        self.play(solutionLines[47].animate.move_to(3 * DOWN))
        self.play(Write(solutionLines[48].next_to(solutionLines[45], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutionLines[47], solutionLines[49].next_to(solutionLines[48], DOWN,
                                                                                    LARGE_BUFF)))
        boxRectangle = SurroundingRectangle(solutionLines[49], buff=0.5)
        self.play(Create(boxRectangle))
        self.wait(1.25)
        self.play(FadeOut(boxRectangle, solutionLines[48:50], solutionLines[45]))
