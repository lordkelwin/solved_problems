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
        equations = VGroup(
            MathTex(r"\mathbf{\dot{x}_{1}} = -2x_{1}+x_{2}+0x_{3}+0r", color=GREEN).move_to(3.25 * UP),
            MathTex(r"\mathbf{\dot{x}_{2}} = 0x_{1}-3x_{2}+1x_{3}+0r", color=RED).move_to(3.25 * UP),
            MathTex(r"\mathbf{\dot{x}_{3}} = -3x_{1}-4x_{2}-5x_{3}+r").move_to(3.25 * UP),
            MathTex(r"y=0x_{1}+x_{2}+0x_{3}").move_to(3.25 * UP)
        )

        nodes = VGroup(
            Circle(radius=0.25, color=WHITE).move_to(7 * LEFT),
            Circle(radius=0.25, color=WHITE).move_to(5 * LEFT),
            Circle(radius=0.25, color=WHITE).move_to(3 * LEFT),
            Circle(radius=0.25, color=WHITE).move_to(LEFT),
            Circle(radius=0.25, color=WHITE).move_to(RIGHT),
            Circle(radius=0.25, color=WHITE).move_to(3 * RIGHT),
            Circle(radius=0.25, color=WHITE).move_to(5 * RIGHT),
            Circle(radius=0.25, color=WHITE).move_to(7 * RIGHT),
        )

        stateVariables = VGroup(
            MathTex(r"R(s)").next_to(nodes[0], UP, MED_SMALL_BUFF),
            MathTex(r"sX_{3}(s)").next_to(nodes[1], UP, MED_SMALL_BUFF),
            MathTex(r"X_{3}(s)").next_to(nodes[2], UP, MED_SMALL_BUFF),
            MathTex(r"sX_{2}(s)").next_to(nodes[3], UP, MED_SMALL_BUFF),
            MathTex(r"X_{2}(s)").next_to(nodes[4], UP, MED_SMALL_BUFF),
            MathTex(r"sX_{1}(s)").next_to(nodes[5], UP, MED_SMALL_BUFF),
            MathTex(r"X_{1}(s)").next_to(nodes[6], UP, MED_SMALL_BUFF),
            MathTex(r"Y(s)").next_to(nodes[7], UP, MED_SMALL_BUFF),
        )

        arrows = VGroup(
            Arrow(nodes[1].get_right(), nodes[2].get_left(), color=BLUE, buff=0),
            Arrow(nodes[3].get_right(), nodes[4].get_left(), color=BLUE, buff=0),
            Arrow(nodes[5].get_right(), nodes[6].get_left(), color=BLUE, buff=0),
            CurvedArrow(nodes[6].get_top(), nodes[5].get_top(), radius=1, color=GREEN),
            CurvedArrow(nodes[4].get_top(), nodes[5].get_top(), radius=-1, color=GREEN)
        )

        signals = VGroup(
            MathTex(r"\frac{1}{s}", color=YELLOW).next_to(arrows[0], DOWN, MED_SMALL_BUFF),
            MathTex(r"\frac{1}{s}", color=YELLOW).next_to(arrows[1], DOWN, MED_SMALL_BUFF),
            MathTex(r"\frac{1}{s}", color=YELLOW).next_to(arrows[2], DOWN, MED_SMALL_BUFF)
        )

        for i in range(8):
            self.play(Create(nodes[i]))
            self.play(Write(stateVariables[i]))
            self.wait(0.2)

        for i in range(3):
            self.play(Create(arrows[i]))
            self.play(Write(signals[i]))
            self.wait(0.2)

        self.wait(0.5)

        equations[0]
        self.play(Write(equations[0]))

        for i in range(3, 5):
            self.play(Create(arrows[i]))
            self.wait(0.2)

        self.wait(0.5)
        self.play(ReplacementTransform(equations[0], equations[1]))

        self.wait(1.5)
        return super().construct()
