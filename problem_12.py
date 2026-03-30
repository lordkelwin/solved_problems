import numpy as np
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

        ax = Axes(x_range=[-1, 5, 1], y_range=[-1, 8, 1], y_length=14)

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
            self.play(ReplacementTransform(lines[i - 1], lines[i].next_to(lines[3], DOWN, LARGE_BUFF)))
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
            self.play(ReplacementTransform(lines[i - 1], lines[i].next_to(lines[8], DOWN, LARGE_BUFF)))
            if i == 14:
                lines[i][0][:14].set_color(YELLOW)
                arrowLines_1 = CurvedArrow(lines[i][0][:14].get_bottom(),
                                           lines[i][0][14:].get_bottom(), color=BLUE)
                self.play(Create(arrowLines_1))
                self.wait(0.5)
                self.play(FadeOut(arrowLines_1, run_time=0.3))
            self.wait(0.5)
        lines[16].set_color(BLUE)
        BoxRectangle = SurroundingRectangle(lines[16], buff=0.5)
        self.play(Create(BoxRectangle))
        self.wait(1.25)
        self.play(FadeOut(lines[:2], lines[8], lines[16], BoxRectangle))

        ax = Axes(x_range=[-1, 6, 1], y_range=[-9, 13, 1], y_length=22)
        locus = ax.plot(
            lambda x: np.sqrt(3 * x ** 2 + 6 * x - 9) + 2,
            color=BLUE,
            x_range=[1, 5],
            use_smoothing=True
        )

        locus_1 = ax.plot(
            lambda x: -np.sqrt(3 * x ** 2 + 6 * x - 9) + 2,
            color=BLUE,
            x_range=[1, 5],
            use_smoothing=True
        )

        def locusFunction(x):
            return np.sqrt(3 * x ** 2 + 6 * x - 9) + 2

        def locusFunctionNegative(x):
            return -np.sqrt(3 * x ** 2 + 6 * x - 9) + 2

        def distanceLocusFunction(x):
            return np.round(np.sqrt((3 - x) ** 2 + (2 - locusFunction(x)) ** 2), 0)

        def distanceLocusFunctionNegative(x):
            return np.round(np.sqrt((3 - x) ** 2 + (2 - locusFunctionNegative(x)) ** 2), 0)

        dots = VGroup(
            Dot(color=YELLOW).move_to(ax.c2p(x_val[0], y_val[0])),
            Dot(color=BLUE).move_to(ax.c2p(x_val[1], y_val[1])),
        )

        linesDistance = VGroup(
            Line(ax.c2p(3, 2),
                 ax.c2p(1, locusFunction(1)), color=GREY),
            Line(ax.c2p(3, 2),
                 ax.c2p(2, locusFunction(2)), color=GREY),
            Line(ax.c2p(3, 2),
                 ax.c2p(2, locusFunctionNegative(2)), color=GREY),
            Line(ax.c2p(3, 2),
                 ax.c2p(3, locusFunction(3)), color=GREY),
            Line(ax.c2p(3, 2),
                 ax.c2p(3, locusFunctionNegative(3)), color=GREY),
            Line(ax.c2p(3, 2),
                 ax.c2p(4, locusFunction(4)), color=GREY),
            Line(ax.c2p(3, 2),
                 ax.c2p(4, locusFunctionNegative(4)), color=GREY),
            Line(ax.c2p(3, 2),
                 ax.c2p(5, locusFunction(5)), color=GREY),
            Line(ax.c2p(3, 2),
                 ax.c2p(5, locusFunctionNegative(5)), color=GREY)
        )

        linesAxis = VGroup(
            Line(ax.c2p(1, locusFunction(1)),
                 ax.c2p(0, locusFunction(1)), color=RED),
            Line(ax.c2p(2, locusFunction(2)),
                 ax.c2p(0, locusFunction(2)), color=RED),
            Line(ax.c2p(2, locusFunctionNegative(2)),
                 ax.c2p(0, locusFunctionNegative(2)), color=RED),
            Line(ax.c2p(3, locusFunction(3)),
                 ax.c2p(0, locusFunction(3)), color=RED),
            Line(ax.c2p(3, locusFunctionNegative(3)),
                 ax.c2p(0, locusFunctionNegative(3)), color=RED),
            Line(ax.c2p(4, locusFunction(4)),
                 ax.c2p(0, locusFunction(4)), color=RED),
            Line(ax.c2p(4, locusFunctionNegative(4)),
                 ax.c2p(0, locusFunctionNegative(4)), color=RED),
            Line(ax.c2p(5, locusFunction(5)),
                 ax.c2p(0, locusFunction(5)), color=RED),
            Line(ax.c2p(5, locusFunctionNegative(5)),
                 ax.c2p(0, locusFunctionNegative(5)), color=RED)
        )

        distances = VGroup()
        distanceLine = VGroup()
        dots_new = VGroup()
        labels_new = VGroup()
        dots_y_axis = VGroup()
        labels_y_axis = VGroup()
        x = 1
        for i in range(9):
            if i > 0:
                if i % 2 == 1:
                    distances.add(MathTex(f"{distanceLocusFunction(x)}", font_size=40, color=YELLOW))
                    distanceLine.add(MathTex(f"{x}", font_size=40, color=BLUE))
                    dots_new.add(Dot(color=BLUE, radius=0.10).move_to(ax.c2p(x, locusFunction(x))))
                    labels_new.add(MathTex(f"({x},{np.round(locusFunction(x), 1)})", font_size=40))
                    dots_y_axis.add(Dot(color=BLUE, radius=0.10).move_to(ax.c2p(0, locusFunction(x))))
                    labels_y_axis.add(MathTex(f"(0,{np.round(locusFunction(x), 1)})", font_size=40))
                else:
                    distances.add(MathTex(f"{distanceLocusFunctionNegative(x)}", font_size=40, color=YELLOW))
                    distanceLine.add(MathTex(f"{x}", font_size=40, color=BLUE))
                    dots_new.add(Dot(color=BLUE, radius=0.10).move_to(ax.c2p(x, locusFunctionNegative(x))))
                    labels_new.add(MathTex(f"({x},{np.round(locusFunctionNegative(x), 1)})", font_size=40))
                    dots_y_axis.add(Dot(color=BLUE, radius=0.10).move_to(ax.c2p(0, locusFunctionNegative(x))))
                    labels_y_axis.add(MathTex(f"(0,{np.round(locusFunctionNegative(x), 1)})", font_size=40))
                    x += 1
            else:
                distances.add(MathTex(f"{distanceLocusFunction(x)}", font_size=40, color=YELLOW))
                distanceLine.add(MathTex(f"{x}", font_size=40, color=BLUE))
                dots_new.add(Dot(color=BLUE, radius=0.10).move_to(ax.c2p(x, locusFunction(x))))
                labels_new.add(MathTex(f"({x},{np.round(locusFunction(x), 1)})", font_size=40))
                dots_y_axis.add(Dot(color=BLUE, radius=0.10).move_to(ax.c2p(0, locusFunction(x))))
                labels_y_axis.add(MathTex(f"(0,{np.round(locusFunction(x), 1)})", font_size=40))
                x += 1

        dots_new.add(Dot(color=YELLOW, radius=0.10).move_to(ax.c2p(3, 2)))
        labels_new.add(MathTex(r"(3,2)", font_size=40).next_to(dots_new[9], RIGHT, SMALL_BUFF))
        self.play(Create(ax))
        self.wait(0.3)
        self.play(Create(dots_new[9]))
        self.play(Write(labels_new[9]))
        self.wait(0.2)
        self.play(Create(locus))
        self.play(Create(locus_1))
        for i in range(9):
            self.play(Create(dots_new[i]))
            self.play(Write(labels_new[i].next_to(dots_new[i], UP, SMALL_BUFF)))
            self.wait(0.3)
            self.play(Create(linesDistance[i]))
            self.wait(0.3)
            self.play(Write(distances[i].next_to(linesDistance[i].get_midpoint(), UP, MED_SMALL_BUFF)))
            self.wait(0.3)
            self.play(Create(dots_y_axis[i]))
            self.play(Write(labels_y_axis[i].next_to(dots_y_axis[i], LEFT, SMALL_BUFF)))
            self.wait(0.3)
            self.play(Create(linesAxis[i]))
            self.wait(0.3)
            self.play(Write(distanceLine[i].next_to(linesAxis[i].get_midpoint(), UP, MED_SMALL_BUFF)))
            self.wait(0.3)
        self.wait(1.25)
        self.play(FadeOut(distanceLine, linesAxis, labels_new, dots_new, locus, locus_1, ax, distances,
                          linesDistance, dots_y_axis, labels_y_axis))
