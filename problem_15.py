from manim import *


config.pixel_width = 1920
config.pixel_height = 1080


class ProblemStatement(Scene):
    def construct(self):
        blockDiagram = VGroup(
            Rectangle(width=1.0, height=1.75).move_to(LEFT * 4),
            Circle(radius=0.25, color=WHITE).move_to(LEFT * 6),
            Circle(radius=0.25, color=WHITE).move_to(LEFT * 2),
            Rectangle(width=2.0, height=1.75).move_to(RIGHT),
            Rectangle(width=1.0, height=1.75).move_to(RIGHT * 4),
            Circle(radius=0.25, color=WHITE).move_to(RIGHT * 6),
            Rectangle(width=1.0, height=1.75),
            Rectangle(width=1.0, height=1.75),
        )

        blockDiagram[6].move_to(blockDiagram[3], ORIGIN).shift(DOWN * 3)
        blockDiagram[7].move_to(blockDiagram[4], ORIGIN).shift(DOWN * 3 + RIGHT * 0.25)

        arrows = VGroup(
            Arrow(blockDiagram[1].get_right(), blockDiagram[0].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[0].get_right(), blockDiagram[2].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[2].get_right(), blockDiagram[3].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[3].get_right(), blockDiagram[4].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[4].get_right(), blockDiagram[5].get_left(), color=YELLOW, buff=0),
        )

        arrowFeedback = VGroup(
            Line(arrows[3].get_center() + 0.2 * LEFT, [arrows[3].get_center()[0]-0.2, blockDiagram[6].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([arrows[3].get_center()[0]-0.19, blockDiagram[6].get_right()[1], 0], blockDiagram[6].get_right(), color=YELLOW, buff=0),
            Line(blockDiagram[6].get_left(), [blockDiagram[2].get_bottom()[0], blockDiagram[6].get_left()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([blockDiagram[2].get_bottom()[0], blockDiagram[6].get_left()[1], 0], blockDiagram[2].get_bottom(), color=YELLOW, buff=0,
                  stroke_width=6),
            Line(arrows[3].get_center() + 0.1 * RIGHT, [arrows[3].get_center()[0]+0.1, blockDiagram[7].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([arrows[3].get_center()[0]+0.09, blockDiagram[7].get_right()[1], 0], blockDiagram[7].get_left(), color=YELLOW, buff=0,
                  stroke_width=6),
            Line(blockDiagram[7].get_right(), [blockDiagram[5].get_bottom()[0], blockDiagram[7].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([blockDiagram[5].get_bottom()[0], blockDiagram[7].get_right()[1], 0], blockDiagram[5].get_bottom(), color=YELLOW, buff=0,
                  stroke_width=6),
        )

        lines = VGroup(
            Line(blockDiagram[1].get_top(), blockDiagram[1].get_bottom()).rotate(45 * DEGREES),
            Line(blockDiagram[1].get_left(), blockDiagram[1].get_right()).rotate(45 * DEGREES),
            Line(blockDiagram[2].get_top(), blockDiagram[2].get_bottom()).rotate(45 * DEGREES),
            Line(blockDiagram[2].get_left(), blockDiagram[2].get_right()).rotate(45 * DEGREES),
            Line(blockDiagram[5].get_top(), blockDiagram[5].get_bottom()).rotate(45 * DEGREES),
            Line(blockDiagram[5].get_left(), blockDiagram[5].get_right()).rotate(45 * DEGREES),
        )

        texts = VGroup(
            MathTex(r"\frac{1}{s^{2}}").move_to(blockDiagram[0], ORIGIN),
            MathTex(r"\frac{50}{s+1}").move_to(blockDiagram[3], ORIGIN),
            MathTex(r"s").move_to(blockDiagram[4], ORIGIN),
            MathTex(r"\frac{2}{s}"),
            MathTex(r"2"),
        )

        self.play(Create(blockDiagram[1]), Create(lines[0]), Create(lines[1]))
        self.play(Create(arrows[0]))
        self.play(Create(blockDiagram[0]), Write(texts[0]))
        self.play(Create(arrows[1]))
        self.play(Create(blockDiagram[2]), Create(lines[2]), Create(lines[3]))
        self.play(Create(arrows[2]))
        self.play(Create(blockDiagram[3]), Write(texts[1]))
        self.play(Create(arrows[3]))
        self.play(Create(blockDiagram[4]), Write(texts[2]))
        self.play(Create(arrows[4]))
        self.play(Create(blockDiagram[5]), Create(lines[4]), Create(lines[5]))
        self.play(Create(arrowFeedback[0]))
        self.play(Create(arrowFeedback[1]))
        self.play(Create(blockDiagram[6]), Write(texts[3].move_to(blockDiagram[6], ORIGIN)))
        self.play(Create(arrowFeedback[2]))
        self.play(Create(arrowFeedback[3]))
        self.play(Create(arrowFeedback[4]))
        self.play(Create(arrowFeedback[5]))
        self.play(Create(blockDiagram[7]), Write(texts[4].move_to(blockDiagram[7], ORIGIN)))
        self.wait(2)
        self.play(FadeOut(blockDiagram, texts, arrows, lines))
        return super().construct()
