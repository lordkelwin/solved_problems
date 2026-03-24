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


class ProblemSolution(Scene):
    def construct(self):
        MathTex.set_default(font_size=75)
        Tex.set_default(font_size=80)
        solution = VGroup(
            Tex(r"\begin{minipage}{5cm}"
                r"It was stated that the rate of change with respect to time of the number of infected student $I$ is"
                r"proportional to the number of uninfected students, $100-I$:"
                r"\end{minipage}"),
            MathTex(r"\frac{dI}{dt}=kI(100-I)"),
            MathTex(r"\frac{dt}{(I)(100-I)} \times \frac{dI}{dt} =\\kI(100-I) \times \frac{dt}{(I)(100-I)}"),
            MathTex(r"\frac{dI}{I(100-I)}=k\:dt"),
            Tex(r"Integrating both sides:"),
            MathTex(r"\int \left[\frac{dI}{I(100-I)}=k\:dt\right]"),
            MathTex(r"\int \frac{dI}{I(100-I)} = \int k\:dt"),
            Tex(r"\begin{minipage}{5.5cm}"
                r"The left-hand side of the equation requires partial fraction decomposition to integrate:"
                r"\end{minipage}"),
            MathTex(r"\frac{1}{I(100-I)}=\frac{A}{I}+\frac{B}{100-I}"),
            Tex(r"\begin{minipage}{5.5cm}"
                r"To solve for the coefficients, since this a case 1 partial fraction, "
                r"\\Heaviside Cover-Up Method is used:"
                r"\end{minipage}"),
            MathTex(r"A = \lim\limits_{I \to 0} \frac{1}{100-I}"),
            MathTex(r"A = \frac{1}{100-0}"),
            MathTex(r"A = \frac{1}{100}"),
            MathTex(r"B = \lim\limits_{I \to 100} \frac{1}{I}"),
            MathTex(r"B = \frac{1}{100}"),
            Tex(r"\begin{minipage}{5.5cm}"
                r"Substitute the coefficients and \\evaluate the integral:"
                r"\end{minipage}"),
            MathTex(r"\int \left[\frac{1}{100}\left(\frac{1}{I}+\frac{1}{100-I}\,dI\right)\right]=\int k\:dt"),
            MathTex(r"\frac{1}{100}\left[\int\frac{dI}{I}+\int\frac{dI}{100-I}\right]=\int k\:dt"),
            MathTex(r"100 \times \frac{1}{100}\left[\int\frac{dI}{I}+\int\frac{dI}{100-I}\right]\\=\int k\:dt "
                    r"\times 100"),
            MathTex(r"\int\frac{dI}{I}+\int\frac{dI}{100-I}=100 \int k\:dt"),
            MathTex(r"\ln{I}-\ln{(100-I)}=100kt + C"),
            MathTex(r"\ln{\left(\frac{I}{100-I}\right)}=100kt+C"),
            MathTex(r"e^{\ln{\left(\frac{I}{100-I}\right)}}=e^{(100kt+C)}"),
            MathTex(r"\frac{I}{100-I}=e^{100kt}e^{C}"),
            Tex(r"Let $c=e^{C}$:"),
            MathTex(r"\frac{I}{100-I}=ce^{100kt}"),
            MathTex(r"(100-I)\times\frac{I}{100-I}=ce^{100kt}\times{(100-I)}"),
            MathTex(r"I=\left(ce^{100kt}\right)(100-I)"),
            MathTex(r"I=100ce^{100kt}-Ice^{100kt}"),
            MathTex(r"I+Ice^{100kt}=100ce^{100kt}"),
            MathTex(r"I\left(1+ce^{100kt}\right)=100ce^{100kt}"),
            MathTex(r"\frac{1}{1+ce^{100kt}}\times{I\left(1+e^{100kt}\right)}=\\\left(100ce^{100kt}\right)"
                    r"\times{\frac{1}{1+ce^{100kt}}"),
            MathTex(r"I=\frac{100ce^{100kt}}{1+ce^{100kt}}"),
            Tex(r"Solving for c, when $t=0$, $I=1$:"),
            MathTex(r"1=\frac{100ce^{100k(0)}}{1+ce^{100k(0)}}"),
            MathTex(r"1=\frac{100ce^{0}}{1+ce^{0}"),
            MathTex(r"1=\frac{100c}{1+c}"),
            MathTex(r"(1+c)\times{1}=\frac{100c}{1+c}\times{(1+c)}"),
            MathTex(r"1+c=100c"),
            MathTex(r"100c-c=1"),
            MathTex(r"99c=1"),
            MathTex(r"\frac{1}{99}\times{99c}=1\times{\frac{1}{99}}"),
            MathTex(r"c=\frac{1}{99}"),
            Tex(r"Substitute $c=1/99$ in the equation:"),
            MathTex(r"I=\frac{\frac{100}{99}e^{100kt}}{1+\frac{1}{99}e^{100kt}}"),
            MathTex(r"I=\frac{\frac{100}{99}e^{100kt}}{1+\frac{1}{99}e^{100kt}}\times{\frac{99}{99}}"),
            MathTex(r"I=\frac{100e^{100kt}}{99+e^{100kt}}")
        )

        solution[0].move_to(5 * UP)
        self.play(Write(solution[0]))
        self.wait(0.3)
        self.play(Write(solution[1].next_to(solution[0], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(2, 4):
            self.play(ReplacementTransform(solution[i-1], solution[i].next_to(solution[0], DOWN, LARGE_BUFF)))
            if i == 2:
                solution[i][0][:2].set_color(YELLOW)
                solution[i][0][17:19].set_color(BLUE)
                solution[i][0][21:29].set_color(BLUE)
                solution[i][0][33:].set_color(YELLOW)
                arrowLine_1 = Line(solution[i][0][:2].get_corner(DL),
                                   solution[i][0][:2].get_corner(UR), color=BLUE)
                arrowLine_2 = Line(solution[i][0][17:19].get_corner(DL),
                                   solution[i][0][17:19].get_corner(UR), color=YELLOW)
                arrowLine_3 = Line(solution[i][0][21:29].get_corner(DL),
                                   solution[i][0][21:29].get_corner(UR), color=YELLOW)
                arrowLine_4 = Line(solution[i][0][33:].get_corner(DL),
                                   solution[i][0][33:].get_corner(UR), color=BLUE)
                self.play(Create(arrowLine_1), Create(arrowLine_2), Create(arrowLine_3), Create(arrowLine_4))
                self.wait(0.5)
                self.play(FadeOut(arrowLine_1, arrowLine_2, arrowLine_3, arrowLine_4, run_time=0.35))
            else:
                self.wait(0.5)

        self.play(solution[3].animate.shift(DOWN * 2))
        self.wait(0.3)
        self.play(Write(solution[4].next_to(solution[0], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solution[3], solution[5].next_to(solution[4], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solution[5], solution[6].next_to(solution[4], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        for i in range(7, 9):
            self.play(Write(solution[i].next_to(solution[i-1], DOWN, LARGE_BUFF)))
            self.wait(0.3)
        self.wait(1.25)
        self.play(FadeOut(solution[0], solution[4], solution[6:8]))
        self.play(solution[8].animate.shift(UP * 13))
        self.play(Write(solution[9].next_to(solution[8], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solution[10].next_to(solution[9], DOWN, LARGE_BUFF)))
        for i in range(11, 13):
            self.play(ReplacementTransform(solution[i-1], solution[i].next_to(solution[9], DOWN, LARGE_BUFF)))
            self.wait(0.5)
        BoxRectangle = SurroundingRectangle(solution[12], buff=0.25)
        self.play(Create(BoxRectangle))
        self.wait(0.3)
        self.play(Write(solution[13].next_to(solution[12], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solution[13], solution[14].next_to(solution[12], DOWN, LARGE_BUFF)))
        BoxRectangle_2 = SurroundingRectangle(solution[14], buff=0.25)
        self.play(Create(BoxRectangle_2))
        self.wait(1.25)
        self.play(FadeOut(BoxRectangle, BoxRectangle_2, solution[14], solution[12], solution[8:10]))
        solution[15].move_to(4 * UP)
        self.play(Write(solution[15]))
        self.wait(0.3)
        self.play(Write(solution[16].next_to(solution[15], DOWN, LARGE_BUFF)))
        self.wait(0.5)

        tempText = VGroup(
            Tex(r"Remember the formula:\\$\int (du/u) = \ln{u} + C$"),
            Tex(r"From the logarithm property:\\$\ln{(x/y)}=\ln{x}-\ln{y}$"),
            Tex(r"Raising both sides by\\natural logarithm:"),
            Tex(r"Remember the logarithm property:\\$e^{\ln{x}}=x$")
        )
        for i in range(17, 24):
            if i == 17 or i == 18:
                self.play(ReplacementTransform(solution[i-1], solution[i].next_to(solution[15], DOWN, LARGE_BUFF)))
                self.wait(0.5)

            if i == 18:
                solution[i][0][:3].set_color(BLUE)
                solution[i][0][6:9].set_color(YELLOW)
                arrowLine_1 = Line(solution[i][0][:3].get_corner(DL),
                                   solution[i][0][:3].get_corner(UR), color=YELLOW)
                arrowLine_2 = Line(solution[i][0][6:9].get_corner(DL),
                                   solution[i][0][6:9].get_corner(UR), color=BLUE)
                self.play(Create(arrowLine_1), Create(arrowLine_2))
                self.wait(0.5)
                self.play(FadeOut(arrowLine_1, arrowLine_2, run_time=0.35))
            elif i == 19:
                self.play(ReplacementTransform(solution[i - 1], solution[i].next_to(solution[15], DOWN, LARGE_BUFF)))
                self.play(solution[i].animate.shift(3 * DOWN))
                self.play(Write(tempText[0].next_to(solution[15], DOWN, LARGE_BUFF)))
                self.wait(0.5)
            elif i == 20:
                self.play(ReplacementTransform(solution[i - 1], solution[i].next_to(tempText[0], DOWN, LARGE_BUFF)))
                self.wait(0.5)
                self.play(ReplacementTransform(tempText[0], tempText[1].next_to(solution[15], DOWN, LARGE_BUFF)))
                self.wait(0.5)
            elif i == 21:
                self.play(ReplacementTransform(solution[i - 1], solution[i].next_to(tempText[1], DOWN, LARGE_BUFF)))
                self.wait(0.5)
                self.play(ReplacementTransform(tempText[1], tempText[2].next_to(solution[15], DOWN, LARGE_BUFF)))
                self.wait(0.5)
            elif i == 22:
                self.play(ReplacementTransform(solution[i - 1], solution[i].next_to(tempText[2], DOWN, LARGE_BUFF)))
                self.wait(0.5)
                self.play(ReplacementTransform(tempText[2], tempText[3].next_to(solution[15], DOWN, LARGE_BUFF)))
                self.wait(0.5)
            elif i == 23:
                self.play(ReplacementTransform(solution[i - 1], solution[i].next_to(tempText[3], DOWN, LARGE_BUFF)))
                self.wait(0.5)
        self.play(ReplacementTransform(tempText[3], solution[24].next_to(solution[15], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solution[23], solution[25].next_to(solution[24], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(26, 33):
            self.play(ReplacementTransform(solution[i-1], solution[i].next_to(solution[24], DOWN, LARGE_BUFF)))
            if i == 26:
                solution[i][0][1:6].set_color(BLUE)
                solution[i][0][10:15].set_color(YELLOW)
                arrowLine_1 = Line(solution[i][0][1:6].get_corner(DL),
                                   solution[i][0][1:6].get_corner(UR), color=YELLOW)
                arrowLine_2 = Line(solution[i][0][10:15].get_corner(DL),
                                   solution[i][0][10:15].get_corner(UR), color=BLUE)
                self.play(Create(arrowLine_1), Create(arrowLine_2))
                self.wait(0.5)
                self.play(FadeOut(arrowLine_1, arrowLine_2, run_time=0.35))
            elif i == 27:
                solution[i][0][3].set_color(BLUE)
                solution[i][0][4:10].set_color(YELLOW)
                solution[i][0][11:].set_color(GREEN)
                arrowLine_1 = CurvedArrow(solution[i][0][11:].get_top(),
                                          solution[i][0][3].get_top(), color=YELLOW)
                arrowLine_2 = CurvedArrow(solution[i][0][11:].get_top(),
                                          solution[i][0][4:10].get_top(), color=BLUE)
                self.play(Create(arrowLine_1), Create(arrowLine_2))
                self.wait(0.5)
                self.play(FadeOut(arrowLine_1, arrowLine_2, run_time=0.35))
            elif i == 28:
                solution[i][0][13:].set_color(BLUE)
                arrowLine_1 = CurvedArrow(solution[i][0][13:].get_center(),
                                          solution[i][0][0].get_center(), color=YELLOW)
                self.play(Create(arrowLine_1))
                self.wait(0.5)
                self.play(FadeOut(arrowLine_1, run_time=0.35))
            elif i == 31:
                solution[i][0][2:10].set_color(BLUE)
                solution[i][0][13:22].set_color(YELLOW)
                arrowLine_1 = Line(solution[i][0][2:11].get_corner(DL),
                                   solution[i][0][2:11].get_corner(UR), color=YELLOW)
                arrowLine_2 = Line(solution[i][0][13:22].get_corner(DL),
                                   solution[i][0][13:22].get_corner(UR), color=BLUE)
                self.play(Create(arrowLine_1), Create(arrowLine_2))
                self.wait(0.5)
                self.play(FadeOut(arrowLine_1, arrowLine_2, run_time=0.35))
            else:
                self.wait(0.5)
        BoxRectangle = SurroundingRectangle(solution[32], buff=0.5)
        self.play(Create(BoxRectangle))
        self.wait(1.25)
