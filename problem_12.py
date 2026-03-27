from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=75)
        MathTex.set_default(font_size=85)

        statement = VGroup(
            Tex(r"\begin{minipage}{5cm}"
                r"A point $P(x,y)$ moves so as its distance from the point $(3,2)$ is twice its distance from the "
                r"y-axis." 
                r"\end{minipage}")
        )

        statement.move_to(4 * UP)
        self.play(Write(statement))
        self.wait(3)
        self.play(FadeOut(statement))


class ProblemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=75)
        MathTex.set_default(font_size=80)

        ax = Axes(x_range=[-1, 5, 1], y_range=[-1, 8, 1])

        x_val = [3, 1.5]
        y_val = [2, 5]

        dots = VGroup(
            Dot(color=YELLOW).move_to(ax.c2p(x_val[0], y_val[0])),
            Dot(color=BLUE).move_to(ax.c2p(x_val[1], y_val[1])),
        )

        lines = VGroup(
            Line(ax.c2p(x_val[0], y_val[0]),
                 ax.c2p(x_val[1], y_val[1]), color=YELLOW),
            Line(ax.c2p(x_val[1], y_val[1]),
                 ax.c2p(0, y_val[1]), color=BLUE)
        )

        labels = VGroup(
            Tex(f"$P({x_val[0]}, {y_val[0]})$", font_size=60).next_to(dots[0], DOWN, buff=0.1),
            Tex("$(x,y)$", font_size=60).next_to(dots[1], UP, buff=0.1),
            MathTex(r"d_{1}", font_size=70).next_to(lines[0].get_midpoint(), UP, MED_SMALL_BUFF),
            MathTex(r"d_{2}", font_size=70).next_to(lines[1].get_midpoint(), UP, MED_SMALL_BUFF)
        )

        self.play(Create(ax))
        self.wait(0.3)
        self.play(FadeIn(dots[0]), Write(labels[0]))
        self.wait(0.3)
        self.play(FadeIn(dots[1]), Write(labels[1]))
        self.wait(0.3)
        self.play(Create(lines[0]))
        self.wait(0.1)
        self.play(Write(labels[2]))
        self.wait(0.3)
        self.play(Create(lines[1]))
        self.wait(0.1)
        self.play(Write(labels[3]))
        self.wait(1.25)
        self.play(FadeOut(ax, dots, labels, lines))
