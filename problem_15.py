from manim import *


config.pixel_width = 1920
config.pixel_height = 1080


class ProblemStatement(Scene):
    def construct(self):
        blockDiagram = VGroup(
            Rectangle(width=3.0, height=5.0),
            Circle(radius=2.0)
        )

        arrows = VGroup(

        )

        texts = VGroup(
            MathTex(r"\frac{1}{s^{2}}").move_to(blockDiagram[0], ORIGIN),
        )

        self.play(Create(blockDiagram[0]), Write(texts[0]))
        self.wait(2)
        self.play(FadeOut(blockDiagram[0], texts[0]))
        return super().construct()
