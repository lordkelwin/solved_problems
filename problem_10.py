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
                r"According to Newton's Law of Cooling, the time rate of change of temperature is proportional to the "
                r"temperature difference."
                r"\end{minipage}"),
            MathTex(r"\frac{dT}{dt}=-k(T-T_{a})"),
            Tex("It was stated that:"),
            Tex(r"Ambient Temperature, $T_{a} = 70^{\circ}F$"),
            MathTex(r"At t=0 \quad T=18^{\circ}F"),
            MathTex(r"At t=1 \quad T=31^{\circ}F"),
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
            MathTex(r"e^{\ln{(T-70)}=e^{(-kt+C)}"),
            Tex(r"Take note some of the exponential identities:"),
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
            Tex(r"Applying natural logarithm to both sides:"),
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
