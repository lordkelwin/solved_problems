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
            Tex("Finding the derivative \\\\ of the original curve:"),
            MathTex(r"\frac{d}{dx}[x^2 + y^2 = c^2]"),
            MathTex(r"2x + 2y\frac{dy}{dx}=0"),
            MathTex(r"2y\frac{dy}{dx}=-2x"),
            MathTex(r"\frac{1}{2y}\times{2y}\frac{dy}{dx}=-2x\times{\frac{1}{2y}}"),
            MathTex(r"\frac{dy}{dx} = -\frac{x}{y}"),
            Tex("Finding the slope of the family of \\\\ orthogonal trajectories."),
            MathTex(r"\bigg(\frac{dy}{dx}\bigg)_{new}=-\frac{1}{-\frac{x}{y}}"),
            MathTex(r"\bigg(\frac{dy}{dx}\bigg)_{new}=\frac{y}{x}"),
            Tex("Solving for the orthogonal trajectories:"),
            MathTex(r"\frac{dy}{dx}=\frac{y}{x}"),
            MathTex(r"\frac{dx}{y}\times{\frac{dy}{dx}}=\frac{y}{x}\times{\frac{dx}{y}}"),
            MathTex(r"\frac{dy}{y}=\frac{dx}{x}"),
            MathTex(r"\int{\bigg[\frac{dy}{y}=\frac{dx}{x}\bigg]}"),
            MathTex(r"\int{\frac{dy}{y}}=\int{\frac{dx}{x}}"),
            MathTex(r"\ln{y}=\ln{x}+\ln{k}"),
            Tex("Logarithm property: $\\ln{xy}=\\ln{x}+\\ln{y}$"),
            MathTex(r"\ln{y}=\ln{ky}"),
            Tex("Logarithm property: $e^{\\ln{x}}=x$"),
            MathTex(r"e^{\ln{y}}=e^{\ln{ky}}"),
            Tex("The Orthogonal Trajectories of the curve \\\\ $x^{2}+y^{2}=c^{2}$ is:"),
            MathTex(r"y=kx")
        )

        lines[0].move_to(ORIGIN)
        lines[0].move_to(UP * 2)
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1].next_to(lines[0], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(lines[:2]))

        lines[2].move_to(ORIGIN)
        lines[2].move_to(UP * 5)
        self.play(Write(lines[2]))
        self.wait(0.3)
        self.play(Write(lines[3].next_to(lines[2], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.5)
        for i in range(4, 8):
            self.play(ReplacementTransform(lines[i-1], lines[i].next_to(lines[2], direction=DOWN, buff=LARGE_BUFF)))
            if i == 6:
                crossLine_1 = Line(lines[6][0][2:4].get_corner(DL), lines[6][0][2:4].get_corner(UR), color=YELLOW)
                crossLine_2 = Line(lines[6][0][5:7].get_corner(DL), lines[6][0][5:7].get_corner(UR), color=BLUE)
                self.play(Create(crossLine_1), Create(crossLine_2))
                self.wait(0.3)
                self.play(FadeOut(crossLine_1, crossLine_2))
            self.wait(0.5)
        self.play(Write(lines[8].next_to(lines[7], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[9].next_to(lines[8], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[9], lines[10].next_to(lines[8], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(lines[2], lines[7:9], lines[10]))

        lines[11].move_to(ORIGIN)
        lines[11].move_to(5 * UP)
        self.play(Write(lines[11]))
        self.wait(0.3)
        self.play(Write(lines[12].next_to(lines[11], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.5)
        for i in range(13, 18):
            self.play(ReplacementTransform(lines[i-1], lines[i].next_to(lines[11], direction=DOWN, buff=LARGE_BUFF)))
            if i == 13:
                crossLine_1 = Line(lines[i][0][0:2].get_corner(DL), lines[i][0][0:2].get_corner(UR), color=YELLOW)
                crossLine_2 = Line(lines[i][0][8:10].get_corner(DL), lines[i][0][8:10].get_corner(UR), color=BLUE)
                crossLine_3 = Line(lines[i][0][11].get_corner(DL), lines[i][0][11].get_corner(UR), color=YELLOW)
                crossLine_4 = Line(lines[i][0][18].get_corner(DL), lines[i][0][18].get_corner(UR), color=BLUE)
                self.play(Create(crossLine_1), Create(crossLine_2), Create(crossLine_3), Create(crossLine_4))
                self.wait(0.3)
                self.play(FadeOut(crossLine_1, crossLine_2, crossLine_3, crossLine_4))
            self.wait(0.5)
        self.play(Write(lines[18].next_to(lines[17], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[19].next_to(lines[18], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[20].next_to(lines[19], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[21].next_to(lines[20], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(lines[11], lines[17:22]))

        lines[22].move_to(ORIGIN)
        lines[22].move_to(UP * 2)
        self.play(Write(lines[22]))
        self.wait(0.3)
        self.play(Write(lines[23].next_to(lines[22], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.3)
        surroundRectangle = SurroundingRectangle(lines[23], buff=0.3)
        self.play(Create(surroundRectangle))
        self.wait(1.5)
        self.play(FadeOut(lines[22:24], surroundRectangle))
