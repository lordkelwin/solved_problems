from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=90)
        statement = VGroup(
            Tex(r"\begin{minipage}{6 cm}"
                r"Find the inverse Laplace Transform of the function using convolution theorem:"
                r"\end{minipage}"),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{240}{(s^{2}+1)(s^{2}+25)}\bigg\}")
        )

        statement[0].move_to(3 * UP)

        self.play(Write(statement[0]))
        self.wait(0.5)
        self.play(Write(statement[1].next_to(statement[0], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(statement))


class ProblemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=90)
        solutionDetails = VGroup(
            Tex("Convolution theorem can be used when finding the inverse Laplace Transform"),
            MathTex(r"\mathcal{L}^{-1}\{F(s)G(s)\}={f(t)}\ast{g(t)}=\int_{0}^{t}f(x)g{t-x}\,dx"),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{240}{(s^{2}+1)(s^{2}+25)\bigg\}=\mathcal{L}^{-1}\bigg\{48\times{"
                    r"\frac{1}{s^{2}+1}}\times{\frac{5}{s^{2}+25}}\bigg\}"),
            Tex("Where:"),
            MathTex(r"F(s)=\frac{1}{s^{2}+1}\\G(s)=\frac{5}{s^{2}+25}")
        )
