from manim import *

config.pixel_width = 1920
config.pixel_height = 1080


class ProblemStatement(Scene):
    def construct(self):
        statement = VGroup(
            Tex(r"\begin{minipage}{9cm}" \
            r"Draw a signal-flow graph for the following state and output equations:" \
            r"\end{minipage}"),
            MathTex(r"\mathbf{\dot{x}} = \begin{bmatrix}" \
            r"-2 & 1 & 0 \\ 0 & -3 & 1 \\ -3 & -4 & -5" \
            r"\end{bmatrix} \mathbf{x} + \begin{bmatrix}" \
            r"0 \\ 0 \\ 1" \
            r"\end{bmatrix} r"),
            MathTex(r"y = \begin{bmatrix}" \
            r"0 & 1 & 0" \
            r"\end{bmatrix} \mathbf{x}")
        )

        statement[0].move_to(2 * UP)
        self.play(Write(statement[0]))
        self.wait(0.25)
        self.play(Write(statement[1].next_to(statement[0], DOWN, MED_LARGE_BUFF)),
                  Write(statement[2].next_to(statement[1], DOWN, MED_LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(statement))
        return super().construct()
    

class ProblemSolution(Scene):
    def construct(self):
        MathTex.set_default(font_size=40)
        equations = VGroup(
            MathTex(r"\mathbf{\dot{x}_{1}} = -2x_{1}+x_{2}+0x_{3}+0r", color=GREEN).move_to(3.75 * DOWN),
            MathTex(r"\mathbf{\dot{x}_{2}} = 0x_{1}-3x_{2}+1x_{3}+0r", color=RED).move_to(3.75 * DOWN),
            MathTex(r"\mathbf{\dot{x}_{3}} = -3x_{1}-4x_{2}-5x_{3}+r", color=GRAY).move_to(3.75 * DOWN),
            MathTex(r"y=0x_{1}+x_{2}+0x_{3}", color=YELLOW).move_to(3.75 * DOWN)
        )

        nodes = VGroup(
            Circle(radius=0.25, color=WHITE).move_to(7 * LEFT + 2 * DOWN),
            Circle(radius=0.25, color=WHITE).move_to(5 * LEFT + 2 * DOWN),
            Circle(radius=0.25, color=WHITE).move_to(3 * LEFT + 2 * DOWN),
            Circle(radius=0.25, color=WHITE).move_to(LEFT + 2 * DOWN),
            Circle(radius=0.25, color=WHITE).move_to(RIGHT + 2 * DOWN),
            Circle(radius=0.25, color=WHITE).move_to(3 * RIGHT + 2 * DOWN),
            Circle(radius=0.25, color=WHITE).move_to(5 * RIGHT + 2 * DOWN),
            Circle(radius=0.25, color=WHITE).move_to(7 * RIGHT + 2 * DOWN),
        )

        stateVariables = VGroup(
            MathTex(r"R(s)").next_to(nodes[0], DOWN, MED_SMALL_BUFF),
            MathTex(r"sX_{3}(s)").next_to(nodes[1], DOWN, MED_SMALL_BUFF),
            MathTex(r"X_{3}(s)").next_to(nodes[2], DOWN, MED_SMALL_BUFF),
            MathTex(r"sX_{2}(s)").next_to(nodes[3], DOWN, MED_SMALL_BUFF),
            MathTex(r"X_{2}(s)").next_to(nodes[4], DOWN, MED_SMALL_BUFF),
            MathTex(r"sX_{1}(s)").next_to(nodes[5], DOWN, MED_SMALL_BUFF),
            MathTex(r"X_{1}(s)").next_to(nodes[6], DOWN, MED_SMALL_BUFF),
            MathTex(r"Y(s)").next_to(nodes[7], DOWN, MED_SMALL_BUFF),
        )

        arrows = VGroup(
            Arrow(nodes[1].get_right(), nodes[2].get_left(), color=BLUE, buff=0),
            Arrow(nodes[3].get_right(), nodes[4].get_left(), color=BLUE, buff=0),
            Arrow(nodes[5].get_right(), nodes[6].get_left(), color=BLUE, buff=0),
            CurvedArrow(nodes[6].get_top(), nodes[5].get_top(), radius=1, color=GREEN),
            CurvedArrow(nodes[4].get_top(), nodes[5].get_top(), radius=-1, color=GREEN),
            CurvedArrow(nodes[4].get_top(), nodes[3].get_top(), radius=1, color=RED),
            CurvedArrow(nodes[2].get_top(), nodes[3].get_top(), radius=-1, color=RED),
            CurvedArrow(nodes[6].get_top(), nodes[1].get_top(), radius=5, color=GRAY),
            CurvedArrow(nodes[4].get_top(), nodes[1].get_top(), radius=3, color=GRAY),
            CurvedArrow(nodes[2].get_top(), nodes[1].get_top(), radius=1, color=GRAY),
            CurvedArrow(nodes[0].get_top(), nodes[1].get_top(), radius=-1, color=GRAY),
            CurvedArrow(nodes[4].get_top(), nodes[7].get_top(), radius=-3, color=YELLOW)
        )

        signals = VGroup(
            MathTex(r"\frac{1}{s}", color=YELLOW),
            MathTex(r"\frac{1}{s}", color=YELLOW),
            MathTex(r"\frac{1}{s}", color=YELLOW),
            MathTex(r"-2", color=GREEN),
            MathTex(r"1", color=GREEN),
            MathTex(r"-3", color=RED),
            MathTex(r"1", color=RED),
            MathTex(r"-3", color=GRAY),
            MathTex(r"-4", color=GRAY),
            MathTex(r"-5", color=GRAY),
            MathTex(r"1", color=GRAY),
            MathTex(r"1", color=YELLOW),
        )

        for i in range(8):
            self.play(Create(nodes[i]))
            self.play(Write(stateVariables[i]))
            self.wait(0.2)

        for i in range(3):
            self.play(Create(arrows[i]))
            self.play(Write(signals[i].next_to(arrows[i], UP, MED_SMALL_BUFF)))
            self.wait(0.2)

        self.wait(0.5)
        self.play(Write(equations[0]))
        for i in range(3, 5):
            self.play(Create(arrows[i]))
            self.play(Write(signals[i].next_to(arrows[i], UP, MED_SMALL_BUFF)))
            self.wait(0.2)

        self.wait(1.0)
        self.play(ReplacementTransform(equations[0], equations[1]))

        for i in range(5, 7):
            self.play(Create(arrows[i]))
            self.play(Write(signals[i].next_to(arrows[i], UP, MED_SMALL_BUFF)))
            self.wait(0.5)
        
        self.wait(1.0)
        self.play(ReplacementTransform(equations[1], equations[2]))

        for i in range(7, 11):
            self.play(Create(arrows[i]))
            self.play(Write(signals[i].next_to(arrows[i], UP, MED_SMALL_BUFF)))
            self.wait(0.5)

        self.wait(1.0)
        self.play(ReplacementTransform(equations[2], equations[3]))

        self.play(Create(arrows[11]))
        self.play(Write(signals[11].next_to(arrows[11], UP, MED_SMALL_BUFF)))

        self.wait(2.5)
        self.play(FadeOut(arrows, signals, nodes, equations[3], stateVariables))
        return super().construct()
