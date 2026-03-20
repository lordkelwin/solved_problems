from manim import *


class ProblemStatement(Scene):
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


class ProblemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=80)
        solutions = VGroup(
            Tex(r"\begin{minipage}{5.5cm}"
                r"According to Newton's Law of \\Cooling, the time rate of change of temperature is proportional to the"
                r" temperature difference."
                r"\end{minipage}"),
            MathTex(r"\frac{dT}{dt}=-k(T-T_{a})"),
            Tex("It was stated that:"),
            Tex(r"Ambient Temperature, $T_{a} = 70^{\circ}F$"),
            MathTex(r"\mathrm{At}\:t=0 \quad T=18^{\circ}F"),
            MathTex(r"\mathrm{At}\:t=1 \quad T=31^{\circ}F"),
            Tex(r"\begin{minipage}{5 cm}"
                r"Solving for the temperature reading as a function of time."
                r"\end{minipage}"),
            MathTex(r"\frac{dT}{dt}=-k(T-70)"),
            MathTex(r"\frac{dt}{T-70} \times \frac{dT}{dt} = -k(T-70) \times \frac{dt}{T-70}"),
            MathTex(r"\frac{dT}{T-70}=-k\,dt"),
            Tex("Integrating both sides of the equation"),
            MathTex(r"\int\left[\frac{dT}{T-70}=-k\,dt\right]"),
            MathTex(r"\int\frac{dT}{T-70}=-k \int dt"),
            MathTex(r"\ln{(T-70)}=-kt+C"),
            Tex(r"Raise both sides by $\mathrm{e}$:"),
            MathTex(r"e^{\ln{(T-70)}}=e^{(-kt+C)}"),
            Tex(r"\begin{minipage}{5cm}"
                r"Take note some of the exponential identities:"
                r"\end{minipage}"),
            MathTex(r"e^{\ln{x}}=x \quad e^{(a+b)}=e^{a} e^{b}"),
            MathTex(r"T-70=e^{-kt}e^{C}"),
            Tex(r"Let $c=e^{c}$:"),
            MathTex(r"T-70=ce^{-kt}"),
            MathTex(r"T=70+ce^{-kt}"),
            Tex(r"Let $t=0$ and $T=18$, to solve for $c$:"),
            MathTex(r"T_{0}=70+ce^{-k(0)}"),
            MathTex(r"18=70+ce^{0}"),
            MathTex(r"18=70+c"),
            MathTex(r"c=18-70"),
            MathTex(r"c=-52"),
            Tex(r"Let $t=1$ and $T=31$ to solve for $k$:"),
            MathTex(r"T_{1}=70-52e^{-k(1)}"),
            MathTex(r"31=70-52e^{-k}"),
            MathTex(r"52e^{-k}=70-31"),
            MathTex(r"52e^{-k}=39"),
            MathTex(r"\frac{1}{52} \times 52e^{-k}=39 \times \frac{1}{52}"),
            MathTex(r"e^{-k}=\frac{39}{52}"),
            Tex(r"Applying natural logarithm to \\both sides:"),
            MathTex(r"\ln{e^{-k}}=\ln{\left(\frac{39}{52}\right)"),
            MathTex(r"-k\ln{e}=\ln{\left(\frac{39}{52}\right)}"),
            MathTex(r"-k=\ln{\left(\frac{39}{52}\right)"),
            MathTex(r"-1 \times -k=\ln{\left(\frac{39}{52}\right)} \times -1"),
            MathTex(r"k=-\ln{\left(\frac{39}{52}\right)}"),
            Tex("The equation of temperature as a function of time:"),
            MathTex(r"T=70-52e^{-t(-\ln{\left(\frac{39}{52}\right)}"),
            MathTex(r"T=70-52e^{t\ln{\left(\frac{39}{52}\right)}"),
            Tex(r"Solving for the temperature at $t=5$:"),
            MathTex(r"T_{5}=70-52e^{5\ln{\left(\frac{39}{52}\right)}"),
            MathTex(r"T_{5}=70-52e^{\ln{\left(\frac{39}{52}\right)^{5}}"),
            MathTex(r"T_{5}=70-52\left(\frac{39}{52}\right)^{5}"),
            MathTex(r"T_{5}=57.66^{\circ}F")
        )

        solutions[0].move_to(5 * UP)
        self.play(Write(solutions[0]))
        self.wait(0.3)
        for i in range(1, 6):
            self.play(Write(solutions[i].next_to(solutions[i-1], DOWN, LARGE_BUFF)))
            self.wait(0.3)
        self.wait(1.25)
        self.play(FadeOut(solutions[:6]))

        solutions[6].move_to(3 * UP)
        self.play(Write(solutions[6]))
        self.wait(0.3)
        self.play(Write(solutions[7].next_to(solutions[6], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(8, 10):
            self.play(ReplacementTransform(solutions[i-1], solutions[i].next_to(solutions[6], DOWN, LARGE_BUFF)))
            if i == 8:
                solutions[i][0][:2].set_color(YELLOW)
                solutions[i][0][11:13].set_color(BLUE)
                solutions[i][0][17:21].set_color(BLUE)
                solutions[i][0][26:].set_color(YELLOW)
                arrowLines_1 = Line(solutions[i][0][:2].get_corner(DL),
                                    solutions[i][0][:2].get_corner(UR), color=BLUE)
                arrowLines_2 = Line(solutions[i][0][11:13].get_corner(DL),
                                    solutions[i][0][11:13].get_corner(UR), color=YELLOW)
                arrowLines_3 = Line(solutions[i][0][17:21].get_corner(DL),
                                    solutions[i][0][17:21].get_corner(UR), color=YELLOW)
                arrowLines_4 = Line(solutions[i][0][26:].get_corner(DL),
                                    solutions[i][0][26:].get_corner(UR), color=BLUE)
                self.play(Create(arrowLines_1), Create(arrowLines_2), Create(arrowLines_3), Create(arrowLines_4))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_4, arrowLines_3, arrowLines_2, arrowLines_1, run_time=0.35))
            else:
                self.wait(0.5)
        self.play(solutions[9].animate.move_to(2 * DOWN))
        self.play(Write(solutions[10].next_to(solutions[6], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutions[9], solutions[11].next_to(solutions[10], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(12, 14):
            self.play(ReplacementTransform(solutions[i-1], solutions[i].next_to(solutions[10], DOWN, LARGE_BUFF)))
            self.wait(0.5)
        self.play(ReplacementTransform(solutions[10], solutions[14].next_to(solutions[6], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutions[13], solutions[15].next_to(solutions[14], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(solutions[15].animate.move_to(4 * DOWN))
        self.play(ReplacementTransform(solutions[14], solutions[16].next_to(solutions[6], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutions[17].next_to(solutions[16], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutions[15], solutions[18].next_to(solutions[17], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(solutions[17]))
        self.play(ReplacementTransform(solutions[16], solutions[19].next_to(solutions[6], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutions[18], solutions[20].next_to(solutions[19], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutions[20], solutions[21].next_to(solutions[19], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutions[19], solutions[22].next_to(solutions[6], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutions[21], solutions[23].next_to(solutions[22], DOWN, LARGE_BUFF)))
        solutions[23][0][8:].set_color(BLUE)
        arrowLines_1 = Arrow(solutions[23][0][8:].get_corner(DL),
                             solutions[23][0][8:].get_corner(UR), color=YELLOW)
        tempText = MathTex(r"0", font_size=50, color=YELLOW)
        self.play(Create(arrowLines_1))
        self.play(Write(tempText.next_to(solutions[23][0][8:].get_corner(UR), UP, SMALL_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(arrowLines_1, tempText, run_time=0.35))
        for i in range(24, 28):
            self.play(ReplacementTransform(solutions[i-1], solutions[i].next_to(solutions[22], DOWN, LARGE_BUFF)))
            if i == 24:
                solutions[i][0][7:].set_color(BLUE)
                arrowLines_1 = Arrow(solutions[i][0][7:].get_corner(DL),
                                     solutions[i][0][7:].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"1", font_size=50, color=YELLOW)
                self.play(Create(arrowLines_1))
                self.play(Write(tempText.next_to(solutions[i][0][7:], UP, SMALL_BUFF)))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_1, tempText, run_time=0.35))
            elif i == 25:
                solutions[i][0][3:5].set_color(YELLOW)
                solutions[i][0][0:2].set_color(BLUE)
                arrowLines_1 = CurvedArrow(solutions[i][0][3:5].get_top(),
                                           solutions[i][0][0:2].get_top(), color=BLUE)
                self.play(Create(arrowLines_1))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_1, run_time=0.35))
            elif i == 26:
                solutions[i][0][2:].set_color(BLUE)
                arrowLines_1 = Arrow(solutions[i][0][2:].get_corner(DL),
                                     solutions[i][0][2:].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"-52", font_size=50, color=YELLOW)
                self.play(Create(arrowLines_1))
                self.play(Write(tempText.next_to(solutions[i][0][2:].get_corner(UR))))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_1, tempText, run_time=0.35))
            else:
                self.wait(0.5)
        BoxRectangle_1 = SurroundingRectangle(solutions[27], buff=0.5)
        self.play(Create(BoxRectangle_1))
        self.wait(0.3)
        self.play(Write(solutions[28].next_to(solutions[27], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutions[20].next_to(solutions[28], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutions[20], solutions[29].next_to(solutions[28], DOWN, LARGE_BUFF)))
        solutions[29][0][9:].set_color(BLUE)
        arrowLines_1 = Arrow(solutions[29][0][9:].get_corner(DL),
                             solutions[29][0][9:].get_corner(UR), color=YELLOW)
        tempText = MathTex(r"-k", font_size=50, color=YELLOW)
        self.play(Create(arrowLines_1))
        self.play(Write(tempText.next_to(solutions[29][0][9:].get_corner(UR), UP, SMALL_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(arrowLines_1, tempText, run_time=0.35))
        for i in range(30, 35):
            self.play(ReplacementTransform(solutions[i-1], solutions[i].next_to(solutions[28], DOWN, LARGE_BUFF)))
            if i == 30:
                solutions[i][0][:2].set_color(BLUE)
                solutions[i][0][3:5].set_color(YELLOW)
                arrowLines_1 = CurvedArrow(solutions[i][0][3:5].get_top(),
                                           solutions[i][0][:2].get_top(), color=YELLOW)
                self.play(Create(arrowLines_1))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_1, run_time=0.35))
            elif i == 31:
                solutions[i][0][6:].set_color(BLUE)
                arrowLines_1 = Arrow(solutions[i][0][6:].get_corner(DL),
                                     solutions[i][0][6:].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"39", font_size=50, color=YELLOW)
                self.play(Create(arrowLines_1))
                self.play(Write(tempText.next_to(solutions[i][0][6:].get_corner(UR), UP, SMALL_BUFF)))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_1, tempText, run_time=0.35))
            elif i == 33:
                solutions[i][0][2:4].set_color(BLUE)
                solutions[i][0][5:7].set_color(YELLOW)
                arrowLines_1 = Line(solutions[i][0][2:4].get_corner(DL),
                                    solutions[i][0][2:4].get_corner(UR), color=YELLOW)
                arrowLines_2 = Line(solutions[i][0][5:7].get_corner(DL),
                                    solutions[i][0][5:7].get_corner(UR), color=BLUE)
                self.play(Create(arrowLines_1), Create(arrowLines_2))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_1, arrowLines_2, run_time=0.35))
            else:
                self.wait(0.5)
        self.play(solutions[34].animate.move_to(8 * DOWN))
        self.play(Write(solutions[35].next_to(solutions[28], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutions[34], solutions[36].next_to(solutions[35], DOWN, LARGE_BUFF)))
        arrowLines_1 = CurvedArrow(solutions[36][0][3:5].get_top(), solutions[36][0][0].get_top(), color=BLUE)
        self.play(Circumscribe(solutions[36][0][3:5], shape=Circle, color=YELLOW, fade_out=True, run_time=2),
                  Create(arrowLines_1))
        self.wait(0.5)
        self.play(FadeOut(arrowLines_1))
        for i in range(37, 41):
            self.play(ReplacementTransform(solutions[i-1], solutions[i].next_to(solutions[35], DOWN, LARGE_BUFF)))
            if i == 37:
                solutions[i][0][2:5].set_color(BLUE)
                arrowLines_1 = Arrow(solutions[i][0][2:5].get_corner(DL),
                                     solutions[i][0][2:5].get_corner(UR), color=YELLOW)
                tempText = MathTex(r"1", font_size=50, color=YELLOW)
                self.play(Create(arrowLines_1))
                self.play(Write(tempText.next_to(solutions[i][0][2:5].get_corner(UR), UP, SMALL_BUFF)))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_1, tempText, run_time=0.35))
            else:
                self.wait(0.5)
        BoxRectangle_2 = SurroundingRectangle(solutions[40], buff=0.5)
        self.play(Create(BoxRectangle_1))
        self.wait(1.25)
        self.play(FadeOut(BoxRectangle_1, BoxRectangle_2, solutions[40], solutions[35], solutions[28],
                          solutions[27], solutions[22], solutions[6]))

        solutions[41].move_to(6 * UP)
        self.play(Write(solutions[41]))
        self.wait(0.3)
        self.play(Write(solutions[42].next_to(solutions[41], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutions[42], solutions[43].next_to(solutions[41], DOWN,
                                                                            LARGE_BUFF)))
        BoxRectangle_1 = SurroundingRectangle(solutions[43], buff=0.5)
        self.play(Create(BoxRectangle_1))
        self.wait(0.5)
        self.play(Write(solutions[44].next_to(solutions[43], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutions[45].next_to(solutions[44], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(46, 49):
            self.play(ReplacementTransform(solutions[i-1], solutions[i].next_to(solutions[44], DOWN, LARGE_BUFF)))
            self.wait(0.5)
        BoxRectangle_2 = SurroundingRectangle(solutions[48], buff=0.5)
        self.play(Create(BoxRectangle_2))
        self.wait(2)
        self.play(FadeOut(BoxRectangle_2, BoxRectangle_1, solutions[48], solutions[43:45], solutions[41]))
