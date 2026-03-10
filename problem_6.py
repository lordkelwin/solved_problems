from manim import *


class ProblemStatement(Scene):
    def construct(self):
        lines = VGroup(
            Tex(r"\begin{minipage}{6 cm}"
                r"Find the orthogonal trajectories of the family of curves $x^2 + y^2 = c^2.$"
                r"\end{minipage}", font_size=80)
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        lines.move_to(UP * 9)
        self.add(lines)
        self.play(Write(lines))
        self.wait(3)
        self.play(FadeOut(lines))


class ProblemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=90)

        lines = VGroup(
            Tex(r"\begin{minipage}{5 cm}"
                r"Orthogonal Trajectories are the family of curves where the slope is negative reciprocal to the"
                r" original curve."
                r"\end{minipage}"),
            MathTex(r"\bigg(\frac{dy}{dx}\bigg)_{new}=-\frac{1}{\frac{dy}{dx}}"),
            Tex("Finding the derivative of the original curve:"),
            MathTex(r"\frac{d}{dx}[x^2 + y^2 = c^2]"),
            MathTex(r"2x + 2y\frac{dy}{dx}=0"),
            MathTex(r"2y\frac{dy}{dx}=-2x"),
            MathTex(r"\frac{1}{2y}\times{2y}\frac{dy}{dx}=-2x\times{\frac{1}{2y}}"),
            MathTex(r"\frac{dy}{dx} = -\frac{x}{y}"),
            MathTex(r"\frac{dy}{dx}_{new}=-\frac{1}{-\frac{x}{y}}"),
            MathTex(r"\frac{dy}{dx}_{new}=\frac{y}{x}"),
            Tex("Solving for the orthogonal trajectories:"),
            MathTex(r"\frac{dy}{dx}=\frac{y}{x}"),
            MathTex(r"\frac{dx}{y}\times{frac{dy}{dx}}=\frac{y}{x}\times{\frac{dx}{y}}"),
            MathTex(r"\frac{dy}{y}=\frac{dx}{x}"),
            MathTex(r"\int{\bigg[\frac{dy}{y}=\frac{dx}{x}\bigg]}"),
            MathTex(r"\int{\frac{dy}{y}}=\int{\frac{dx}{x}}"),
            MathTex(r"\ln{y}=\ln{x}+\ln{k}"),
            Tex("Logarithm property: $\\ln{xy}=\\ln{x}+\\ln{y}$"),
            MathTex(r"\ln{y}=\ln{ky}"),
            MathTex(r"e^{\ln{y}}=e^{\ln{ky}}"),
            Tex("Logarithm property: $e^{\\ln{x}}=x$"),
            MathTex(r"y=kx")
        )

        lines[0].move_to(ORIGIN)
        lines[0].move_to(UP * 3)
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1].next_to(lines[0], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(lines[:2]))
