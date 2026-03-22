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
            MathTex(r"\frac{1}{(dt)(I)(100-I)} \times \frac{dI}{dt} = kI(100-I) \times \frac{1}{(dt)(I)(100-I)}"),
            MathTex(r"\frac{dI}{I(100-I)}=k\:dt"),
            Tex(r"Integrating both sides:"),
            MathTex(r"\int \left[\frac{dI}{I(100-I)}=k\:dt\right]"),
            MathTex(r"\int \frac{dI}{I(100-I)} = \int k\:dt"),
            Tex(r"Solving for the partial fraction decomposition:"),
            MathTex(r"\frac{1}{I(100-I)}=\frac{A}{I}+\frac{B}{100-I}"),
            Tex(r"\begin{minipage}{5.5cm}"
                r"To solve for the coefficients, Heaviside Method is used:"
                r"\end{minipage}"),
            MathTex(r"A = \lim_{I->0} \frac{1}{100-I}"),
            MathTex(r"A = \frac{1}{100-0}"),
            MathTex(r"A = \frac{1}{100}"),
            MathTex(r"B = \lim_{I->100} \frac{1}{I}"),
            MathTex(r"B = \frac{1}{100}"),
            Tex(r"\begin{minipage}{5.5cm}"
                r"Substitute the coefficients and evaluate the integral:"
                r"\end{minipage}"),
            MathTex(r"\int \left[\frac{1}{100}\left(\frac{1}{I}+\frac{1}{100-I}\,dI\right)\right]=\int k\:dt"),
            MathTex(r"\frac{1}{100}\left[\int\frac{dI}{I}+\int\frac{dI}{100-I}\right]=\int k\:dt"),
            MathTex(r"100 \times \frac{1}{100}\left[\int\frac{dI}{I}+\int\frac{dI}{100-I}\right]=\int k\:dt "
                    r"\times 100"),
            MathTex(r"\int\frac{dI}{I}+\int\frac{dI}{100-I}=100 \int k\:dt"),
            MathTex(r"\ln{I}-\ln{(100-I)}=100kt + C"),
            MathTex(r"\ln{\left(\frac{I}{100-I}\right)}=100kt+C"),
            MathTex(r"e^{\ln{\left(\frac{I}{100-I}\right)}}=e^{(100kt+C)}"),
            MathTex(r"\frac{I}{100-I}=e^{100kt)e^{C}"),
            Tex(r"Let c=e^{C}:"),
            MathTex(r"\frac{I}{100-I}=ce^{100kt}"),
            MathTex(r"(100-I)\times\frac{I}{100-I}=ce^{100kt}\times{(100-I)}"),
            MathTex(r"I=\left(ce^{100kt}\right)(100-I)"),
            MathTex(r"I=100ce^{100kt}-Ice^{100kt}"),
            MathTex(r"I+Ice^{100kt}=100ce^{100kt}"),
            MathTex(r"I\left(1+e^{100kt}\right)=100ce^{100kt}"),
            MathTex(r"\frac{1}{1+e^{100kt}}\times{I\left(1+e^{100kt}\right)}=\left(100ce^{100kt}\right)"
                    r"\times{\frac{1}{1+e^{100kt}}"),
            MathTex(r"I=\frac{100ce^{100kt}}{1+e^{100kt}}"),
            Tex(r"Solving for c, when $t=0$, $I=1$:")
        )
