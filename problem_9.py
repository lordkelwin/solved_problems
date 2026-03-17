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
        MathTex.set(font_size=75)
        solutionLines = VGroup(
            Tex(r"\begin{minipage}{6 cm}"
                r"To determine the equilibrium size, the growth rate must be equal to zero:"
                r"\end{minipage}"),
            MathTex(r"\frac{dx}{dt}=x(b-ax)"),
            MathTex(r"\frac{dx}{dt}=bx-ax^{2}"),
            Tex("Differentiate both sides with respect to $t$:"),
            MathTex(r"\frac{d}{dt}\left[\frac{dx}{dt}=bx-ax^{2}\right]"),
            MathTex(r"\frac{d^{2}x}{dt^{2}}=\frac{d}{dt}[bx-ax^{2}]"),
            MathTex(r"\frac{d^{2}x}{dt^{2}}=b\frac{dx}{dt}-2ax\frac{dx}{dt}"),
            Tex(r"For maximum rate of growth, the second derivative must be equal to zero:"),

        )

