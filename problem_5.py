from manim import *


class ProblemStatement(Scene):
    def construct(self):
        problem = VGroup(
            Tex(r"\begin{minipage}{9 cm}"
                r"An RL circuit has an emf given (in volts) by $3\sin{2t}$, a resistance of $10\,\mathrm{ohms}$, an "
                r"inductance of $0.5\,\mathrm{henry}$, and an initial current of $6\,\mathrm{amperes}$. Find the "
                r"current in the circuit at any time $t$."
                r"\end{minipage}")
        )
        image = ImageMobject("problem_5_circuit.jpeg")

        image.height = 3
        image.move_to(0.75 * DOWN)

        problem.arrange(DOWN, buff=MED_LARGE_BUFF)
        problem[0].move_to(2 * UP)
        self.add(problem[0])
        self.play(Write(problem[0]))
        self.wait(0.4)
        self.add(image)
        self.play(FadeIn(image))
        self.wait(3)
        self.play(FadeOut(problem, image))


class ProblemSolution(Scene):
    def construct(self):
        image = ImageMobject("problem_5_circuit_v1.jpeg")
        image.height = 3
        image.move_to(2 * UP)

        lines = VGroup(
            Tex("The sum of all voltages in a loop is equal to zero."),
            MathTex(r"v-v_{L}-v_{R}=0"),
            Tex("Voltage drop in different components:"),
            MathTex(r"\mathrm{Inductor:}\,\,v_{L}=L\frac{di}{dt}"),
            MathTex(r"\mathrm{Resistor:}\,\,v_{R}=Ri")
        )

        extra_lines = VGroup(
            Tex("Substituting, it yields to:"),
            MathTex(r"v-L\frac{di}{dt}-Ri=0"),
            MathTex(r"L\frac{di}{dt}+Ri=v"),
            MathTex(r"0.5\frac{di}{dt}+10i=3\sin{2t}")
        )

        lines.arrange(DOWN)
        self.add(image)
        self.play(FadeIn(image))
        self.wait(0.3)
        self.add(lines[0])
        self.play(Write(lines[0].next_to(image, direction=DOWN, buff=SMALL_BUFF)))
        for i in range(1, 5):
            self.play(Write(lines[i].next_to(lines[i-1], direction=DOWN, buff=MED_SMALL_BUFF)))
            self.wait(0.3)
        self.wait(0.7)
        self.play(FadeOut(lines[2:5]))
        self.play(Write(extra_lines[0].next_to(lines[1], direction=DOWN, buff=MED_SMALL_BUFF)))
        self.wait(0.3)
        self.play(Write(extra_lines[1].next_to(extra_lines[0], direction=DOWN, buff=MED_SMALL_BUFF)))
        self.wait(0.3)
        self.play(TransformMatchingTex(extra_lines[1], extra_lines[2].next_to(extra_lines[0], direction=DOWN,
                                                                              buff=MED_SMALL_BUFF)))
        self.wait(0.5)
        self.play(TransformMatchingTex(extra_lines[2], extra_lines[3].next_to(extra_lines[0], direction=DOWN,
                                                                              buff=MED_SMALL_BUFF)))
        self.wait(2)
        self.play(FadeOut(image, lines[:2], extra_lines[0], extra_lines[3]))

        lines = VGroup(
            Tex("Multiplying the sides by 2:"),
            MathTex(r"2\bigg[0.5\frac{di}{dt}+10i=3\sin{2t}\bigg]"),
            Tex("The differential equation is a form of Linear DE:"),
            MathTex(r"\frac{dy}{dx}+p(x)y=q(x)")
        )

        extra_lines = VGroup(
            MathTex(r"\frac{di}{dt}+20i=6\sin{2t}"),
            Tex("With its integrating factor of:"),
            MathTex(r"I=e^{\int{p(x)dx}}"),
            Tex("Where:"),
            MathTex(r"p(t)=20", r"q(t)=6\sin{2t}"),
            Tex("Solving for the integrating factor:"),
            MathTex(r"I=e^{\int{20 dt}}"),
            MathTex(r"I=e^{20t}")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1]))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[1], extra_lines[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        for i in range(2, 4):
            self.play(Write(lines[i]))
            self.wait(0.3)
        self.wait(0.2)
        self.play(FadeOut(lines[2:4]))
        self.wait(0.2)
        self.play(Write(extra_lines[1].next_to(extra_lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.play(Write(extra_lines[2].next_to(extra_lines[1], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(Unwrite(extra_lines[1:3]))
        self.wait(0.2)
        self.play(Write(extra_lines[3].next_to(extra_lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.play(Write(extra_lines[4][0].next_to(extra_lines[3], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.play(Write(extra_lines[4][1].next_to(extra_lines[4][0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(1)
        self.play(Unwrite(extra_lines[3:5]))
        self.wait(0.2)
        self.play(Write(extra_lines[5].next_to(extra_lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.2)
        self.play(Write(extra_lines[6].next_to(extra_lines[5], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(extra_lines[6], extra_lines[7].next_to(extra_lines[5], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(lines[0], extra_lines[0], extra_lines[5], extra_lines[7]))

        lines = VGroup(
            Tex("Multiplying both sides by the integrating factor, $I$:"),
            MathTex(r"{I}\times{\bigg[\frac{di}{dt}+20i\bigg]}={6\sin{2t}}\times{I}")
        )

        extra_lines = VGroup(
            MathTex(r"{e^{20t}}\times{\bigg[\frac{di}{dt}+20i\bigg]}={6\sin{2t}}\times{e^{20t}}"),
            MathTex(r"e^{20t}\frac{di}{dt}+20e^{20t}i=6e^{20t}\sin{2t}"),
            Tex("From the Product rule: $d[uv]=ud[v]+vd[u]$"),
            MathTex(r"\frac{d}{dt}[ie^{20t}]=6e^{20t}\sin{2t}"),
            MathTex(r"{dt}\times{\frac{d}{dt}[ie^{20t}]}={6e^{20t}\sin{2t}}\times{dt}"),
            MathTex(r"d[ie^{20t}]=6e^{20t}\sin{2t}\,dt")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.add(lines[0])
        self.play(Write(lines[0].move_to(UP * 2)))
        self.wait(0.2)
        self.play(Write(lines[1].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.4)
        self.play(ReplacementTransform(lines[1], extra_lines[0].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.4)
        self.play(ReplacementTransform(extra_lines[0], extra_lines[1].next_to(lines[0], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(extra_lines[2].next_to(extra_lines[1], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(extra_lines[3].next_to(extra_lines[2], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(extra_lines[3], extra_lines[4].next_to(extra_lines[2], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(extra_lines[4], extra_lines[5].next_to(extra_lines[2], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(lines[0], extra_lines[1:3], extra_lines[5]))

        lines = VGroup(
            Tex("Integrating both sides:"),
            MathTex(r"\int{d[ie^{20t}]=6e^{20t}\sin{2t}\,dt}"),
            MathTex(r"\int{d[ie^{20t}]}=\int{6e^{20t}\sin{2t}\,dt}"),
            MathTex(r"ie^{20t}=\int{6e^{20t}\sin{2t}\,dt")
        )

