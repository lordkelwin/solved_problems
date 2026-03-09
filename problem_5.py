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
                                                                              buff=MED_SMALL_BUFF), path_arc=90*DEGREES))
        self.wait(0.5)
        self.play(TransformMatchingTex(extra_lines[2], extra_lines[3].next_to(extra_lines[0], direction=DOWN,
                                                                              buff=MED_SMALL_BUFF), path_arc=90*DEGREES))
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
        self.wait(1.25)
        self.play(FadeOut(lines[0], extra_lines[0], extra_lines[5], extra_lines[7]))

        lines = VGroup(
            Tex("Multiplying both sides by the integrating factor, $I$:"),
            MathTex(r"{I}\times{\bigg[\frac{di}{dt}+20i\bigg]}={6\sin{2t}}\times{I}")
        )

        extra_lines = VGroup(
            MathTex(r"{e^{20t}}\times{\bigg[\frac{di}{dt}+20i\bigg]}={6\sin{2t}}\times{e^{20t}}"),
            MathTex(r"e^{20t}\frac{di}{dt}+20ie^{20t}=6e^{20t}\sin{2t}"),
            Tex("From the Product rule: $d[uv]=ud[v]+vd[u]$"),
            MathTex(r"\frac{d}{dt}[ie^{20t}]=e^{20t}\frac{di}{dt}+20ie^{20t}"),
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
        self.wait(0.5)
        self.play(ReplacementTransform(extra_lines[5], extra_lines[6].next_to(extra_lines[2], direction=DOWN,
                                                                              buff=MED_LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(lines[0], extra_lines[1:3], extra_lines[6]))

        lines = VGroup(
            Tex("Integrating both sides:"),
            MathTex(r"\int{d[ie^{20t}]=6e^{20t}\sin{2t}\,dt}"),
            MathTex(r"\int{d[ie^{20t}]}=\int{6e^{20t}\sin{2t}\,dt}"),
            MathTex(r"ie^{20t}=\int{6e^{20t}\sin{2t}\,dt"),
            Tex("To integrate the right-hand side part of the equation,\\\\ use integration by parts"),
            Tex("Let $M$ be the right-hand side of the equation."),
            MathTex(r"M=\int{6e^{20t}\sin{2t}\,dt"),
            Tex('Using the LIATE priority for determining the $u$'),
            MathTex(r"u=\sin{2t},\,\,\,dv=e^{20t}\,dt\\du=2\cos{2t}\,dt,\,\,\,v=\frac{1}{20}e^{20t}"),
            MathTex(r"M=6\bigg[\frac{1}{20}e^{20t}\sin{2t}-\int{\bigg(\frac{1}{20}e^{20t}\bigg)(2\cos{2t}\,dt)}\bigg]"),
            MathTex(r"M=6\bigg[\frac{1}{20}e^{20t}\sin{2t}-\frac{1}{10}\int{e^{20t}\cos{2t}\,dt}\bigg]"),
            MathTex(r"M=\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{5}\int{e^{20t}\cos{2t}\,dt}"),
            Tex('The second term of the equation requires to \\\\ redo integration by parts:'),
            MathTex(r"u=\cos{2t},\,\,\,dv=e^{20t}\,dt\\du=-2\sin{2t}\,dt,\,\,\,v=\frac{1}{20}e^{20t}"),
            MathTex(r"M=\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{5}\bigg[\frac{1}{20}e^{20t}\cos{2t}-\int{\bigg(\frac{1}{"
                    r"20}e^{20t}\bigg)(-2\sin{2t}\,dt)}\bigg]"),
            MathTex(r"M=\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{5}\bigg[\frac{1}{20}e^{20t}\cos{2t}+\frac{1}{10}\int{e^{"
                    r"20t}\sin{2t}\,dt}\bigg]"),
            MathTex(r"M=\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{100}e^{20t}\cos{2t}-\frac{3}{50}\int{e^{20t}\sin{2t}\,"
                    r"dt}"),
            Tex("Since $M=6\\int{e^{20t}\\sin{2t}\\,dt}$ or $\\frac{M}{6}=\\int{e^{20t}\\sin{2t}\\,dt}$"),
            MathTex(r"M=\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{100}e^{20t}\cos{2t}-\bigg(\frac{3}{50}\bigg)\bigg(\frac{"
                    r"M}{6}\bigg)"),
            MathTex(r"M=\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{100}e^{20t}\cos{2t}-\frac{1}{100}M"),
            MathTex(r"M+\frac{1}{100}M=\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{100}e^{20t}\cos{2t}"),
            MathTex(r"\frac{101}{100}M=\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{100}e^{20t}\cos{2t}"),
            MathTex(r"{\frac{100}{101}}\times{\frac{101}{100}}M=\bigg[\frac{3}{10}e^{20t}\sin{2t}-\frac{3}{100}e^{"
                    r"20t}\cos{2t}\bigg]\times{\frac{100}{101}}"),
            MathTex(r"M=\frac{30}{101}e^{20t}\sin{2t}-\frac{3}{101}e^{20t}\cos{2t}+C"),
            Tex('Substituting back to the original equation:'),
            MathTex(r"{ie^{20t}}\times{e^{-20t}}=\bigg[\frac{30}{101}e^{20t}\sin{2t}-\frac{3}{101}e^{20t}\cos{"
                    r"2t}+C\bigg]\times{e^{-20t}}"),
            MathTex(r"i(t)=\frac{30}{101}\sin{2t}-\frac{3}{101}\cos{2t}+Ce^{-20t}"),
            Tex('Solving for C, using the initial conditions, $t=0,\\,i=6$'),
            MathTex(r"i(0)=\frac{30}{101}\sin{[2(0)]}-\frac{3}{101}\cos{[2(0)]}+Ce^{-20(0)}"),
            MathTex(r"6=-\frac{3}{101}+C"),
            MathTex(r"6+\frac{3}{101}=C"),
            MathTex(r"C=\frac{609}{101}"),
            Tex('The equation of current $i$ at any time $t$ is:'),
            MathTex(r"i(t)=\frac{30}{101}\sin{2t}-\frac{3}{101}\cos{2t}+\frac{609}{101}e^{-20t}")
        )

        self.add(lines[0])
        lines[0].move_to(ORIGIN)
        lines[0].move_to(UP * 2)
        self.play(Write(lines[0]))
        self.wait(0.3)
        self.play(Write(lines[1].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[1], lines[2].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(lines[2], lines[3].next_to(lines[0], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[4].next_to(lines[3], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(lines[4]))
        self.wait(0.2)
        self.play(Write(lines[5].next_to(lines[3], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[6].next_to(lines[5], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(lines[0], lines[3], lines[5:7]))

        lines[7].move_to(ORIGIN)
        lines[7].move_to(UP * 2)
        self.play(Write(lines[7]))
        self.wait(0.3)
        self.play(Write(lines[8].next_to(lines[7], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[9].next_to(lines[8], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[9], lines[10].next_to(lines[8], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[10], lines[11].next_to(lines[8], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(lines[7:9], lines[11]))

        lines[12].move_to(ORIGIN)
        lines[12].move_to(UP * 2)
        self.play(Write(lines[12]))
        self.wait(0.3)
        self.play(Write(lines[13].next_to(lines[12], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[14].next_to(lines[13], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[14], lines[15].next_to(lines[13], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[15], lines[16].next_to(lines[13], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(lines[12:14], lines[16]))

        lines[17].move_to(ORIGIN)
        lines[17].move_to(UP)
        self.play(Write(lines[17]))
        self.wait(0.3)
        self.play(Write(lines[18].next_to(lines[17], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        for i in range(19, 24):
            self.play(ReplacementTransform(lines[i-1], lines[i].next_to(lines[17], direction=DOWN,
                                                                        buff=MED_LARGE_BUFF)))
            self.wait(0.5)
        self.wait(0.75)
        self.play(FadeOut(lines[17], lines[23]))

        lines[24].move_to(ORIGIN)
        lines[24].move_to(UP * 2)
        self.play(Write(lines[24]))
        self.wait(0.3)
        self.play(Write(lines[25].next_to(lines[24], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(lines[25], lines[26].next_to(lines[24], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        self.play(Write(lines[27].next_to(lines[26], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(lines[28].next_to(lines[27], direction=DOWN, buff=MED_LARGE_BUFF)))
        self.wait(0.5)
        for i in range(29, 32):
            self.play(ReplacementTransform(lines[i-1], lines[i].next_to(lines[27], direction=DOWN,
                                                                        buff=MED_LARGE_BUFF)))
            self.wait(0.5)
        self.wait(0.75)
        self.play(FadeOut(lines[24], lines[26:28], lines[31]))

        lines[32].move_to(ORIGIN)
        lines[32].move_to(UP)
        self.play(Write(lines[32]))
        self.wait(0.3)
        self.play(Write(lines[33].next_to(lines[32], direction=DOWN, buff=MED_LARGE_BUFF)))
        frameBox = SurroundingRectangle(lines[33], buff=0.25)
        self.play(Create(frameBox))
        self.wait(2)
        self.play(FadeOut(lines[32:34], frameBox))
