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

        lines = VGroup(
            Tex(r"\begin{minipage}{5cm}"
                r"The distance from the point $(3,2)$ to $P(x,y)$ is twice the \\ distance from point "
                r"$P(x,y)$ to the y-axis."
                r"\end{minipage}"),
            MathTex(r"d_{1}=2d_{2}"),
            Tex(r"Where:"),
            MathTex(r"d_{1}=\sqrt{(x-3)^{2}+(y-2)^{2}}"),
            MathTex(r"d_{2}=\sqrt{(x-0)^{2}+(y-y)^{2}}"),
            MathTex(r"d_{2}=\sqrt{x^{2}+0^{2}}"),
            MathTex(r"d_{2}=\sqrt{x^{2}}"),
            MathTex(r"d_{2}=x"),
            Tex(r"Substituting $d_{1}$ and $d_{2}$:"),
            MathTex(r"\sqrt{(x-3)^{2}+(y-2)^{2}}=2x"),
            MathTex(r"\left[\sqrt{(x-3)^{2}+(y-2)^{2}}=2x\right]^{2}"),
            MathTex(r"(x-3)^{2}+(y-2)^{2}=(2x)^{2}"),
            MathTex(r"(x-3)^{2}+(y-2)^{2}=4x^{2}"),
            MathTex(r"(x^{2}-6x+9)+(y^{2}-4y+4)=4x^{2}"),
            MathTex(r"x^{2}+y^{2}-6x-4y+13=4x^{2}"),
            MathTex(r"4x^{2}-x^{2}-y^{2}+6x+4y-13=0"),
            MathTex(r"3x^{2}-y^{2}+6x+4y-13=0")
        )

        lines[0].move_to(4 * UP)
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1].next_to(lines[0], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[2].next_to(lines[1], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[3].next_to(lines[2], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[4].next_to(lines[3], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[4], lines[5].next_to(lines[3], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(6, 8):
            self.play(ReplacementTransform(lines[i-1], lines[i].next_to(lines[3], DOWN, LARGE_BUFF)))
            self.wait(0.5)
        self.wait(1.25)
        self.play(FadeOut(lines[3], lines[7]))
        self.play(ReplacementTransform(lines[2], lines[8].next_to(lines[1], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[9].next_to(lines[8], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[9], lines[10].next_to(lines[8], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(11, 17):
            self.play(ReplacementTransform(lines[i-1], lines[i].next_to(lines[8], DOWN, LARGE_BUFF)))
            self.wait(0.5)
        self.wait(1.25)
        self.play(FadeOut(lines[:2], lines[8], lines[16]))
