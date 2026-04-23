from manim import *


config.pixel_width = 1920
config.pixel_height = 1080


class ProblemStatement(Scene):
    def construct(self):
        statement = VGroup(
            Tex(r"\begin{minipage}{9cm}" \
            r"Make the Routh table for the system shown in the figure." \
            r"\end{minipage}"),
        )

        statement[0].move_to(UP * 2)

        blockDiagram = VGroup(
            Circle(radius=0.25, color=WHITE).move_to(LEFT * 3),
            Rectangle(width=5.0, height=1.75).move_to(RIGHT)
        )

        lines = VGroup(
            Line(blockDiagram[0].get_left(), blockDiagram[0].get_right(), buff=0).rotate(45 * DEGREES),
            Line(blockDiagram[0].get_top(), blockDiagram[0].get_bottom(), buff=0).rotate(45 * DEGREES),
        )

        arrows = VGroup(
            Arrow(blockDiagram[0].get_left()+2.5 * LEFT, blockDiagram[0].get_left(), buff=0),
            Arrow(blockDiagram[0].get_right(), blockDiagram[1].get_left(), buff=0),
            Arrow(blockDiagram[1].get_right(), blockDiagram[1].get_right() + 2.5 * RIGHT, buff=0)
        )

        feedbackLoop = VGroup(
            Line(arrows[2].get_midpoint(), arrows[2].get_midpoint() + 2 * DOWN, buff=0),
            Line(arrows[2].get_midpoint() + 2 * DOWN, [blockDiagram[0].get_bottom()[0], arrows[2].get_midpoint()[1]-2, 0], buff=0),
            Arrow([blockDiagram[0].get_bottom()[0], arrows[2].get_midpoint()[1]-2, 0], blockDiagram[0].get_bottom(), buff=0)
        )

        texts = VGroup(
            MathTex(r"R(s)").next_to(arrows[0].get_start() + 0.5 * RIGHT, UP, MED_SMALL_BUFF),
            MathTex(r"E(s)").next_to(arrows[1].get_midpoint(), UP, MED_SMALL_BUFF),
            MathTex(r"\frac{1000}{(s+2)(s+3)(s+5)}").move_to(blockDiagram[1], ORIGIN),
            MathTex(r"C(s)").next_to(arrows[2].get_end() + 0.5 * LEFT, UP, MED_SMALL_BUFF)
        )

        signs = VGroup(
            MathTex(r"+").next_to(arrows[0].get_end()+0.25 * LEFT, UP, MED_SMALL_BUFF),
            MathTex(r"-").next_to(feedbackLoop[2].get_end()+0.25 * DOWN, LEFT, MED_SMALL_BUFF)
        )

        self.play(Write(statement[0]))
        self.wait(0.3)
        self.play(Create(arrows[0]))
        self.play(Write(texts[0]))
        self.play(Write(signs[0]))
        self.play(Create(blockDiagram[0]), Create(lines[0]), Create(lines[1]))
        self.play(Create(arrows[1]))
        self.play(Write(texts[1]))
        self.play(Create(blockDiagram[1]), Write(texts[2]))
        self.play(Create(arrows[2]))
        self.play(Write(texts[3]))
        self.play(Create(feedbackLoop))
        self.play(Write(signs[1]))
        self.wait(3)
        self.play(FadeOut(statement, blockDiagram, lines, signs, texts, arrows, feedbackLoop))
        return super().construct()
