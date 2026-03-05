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
