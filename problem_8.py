from manim import *


class ProblemStatement(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=90)
        statement = VGroup(
            Tex(r"\begin{minipage}{6 cm}"
                r"Find the inverse Laplace Transform of the function using convolution theorem:"
                r"\end{minipage}"),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{240}{(s^{2}+1)(s^{2}+25)}\bigg\}")
        )

        statement[0].move_to(3 * UP)

        self.play(Write(statement[0]))
        self.wait(0.5)
        self.play(Write(statement[1].next_to(statement[0], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(2)
        self.play(FadeOut(statement))


class ProblemSolution(Scene):
    def construct(self):
        Tex.set_default(font_size=85)
        MathTex.set_default(font_size=90)
        solutionDetails = VGroup(
            Tex("Convolution theorem can be used when \\\\ finding the inverse Laplace Transform \\\\"
                "of a product."),
            MathTex(r"\mathcal{L}^{-1}\{F(s)G(s)\}={f(t)}\ast{g(t)}\\=\int_{0}^{t}f(x)g{(t-x)}\,dx"),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{240}{(s^{2}+1)(s^{2}+25)}\bigg\}= \\\mathcal{L}^{-1}\bigg\{48\times{"
                    r"\frac{1}{s^{2}+1}}\times{\frac{5}{s^{2}+25}}\bigg\} =\\\mathcal{L}^{-1}\{48F(s)G(s)\} = "
                    r"48[f(t)\ast{g(t)}]"),
            Tex("Where:"),
            MathTex(r"F(s)=\frac{1}{s^{2}+1}\\G(s)=\frac{5}{s^{2}+25}"),
            Tex("And their corresponding \\\\ Inverse Laplace Transforms:"),
            MathTex(r"\mathcal{L}^{-1}\left\{F(s)=\frac{1}{s^{2}+1}\right\}\\"
                    r"\mathcal{L}^{-1}\left\{G(s)=\frac{5}{s^{2}+25}\right\}"),
            MathTex(r"f(t)=\sin{t}\\g(t)=\sin{5t}"),
            Tex("Solving for the \\\\ Inverse Laplace Transform:"),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}\sin{x}\sin{5(t-x)}\,dx"),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}\sin{x}\sin{(5t-5x)}\,dx"),
            Tex(r"Using the identity:\\$\sin{(a-b)}=\sin{a}\cos{b}-\cos{a}\sin{b}$"),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}\sin{x}[\sin{(5t)}\cos{(5x)}-\\\cos{(5t)}\sin{(5x)}]\,dx",
                    font_size=80),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}[\sin{(5t)}\sin{x}\sin{(5x)}-\\\cos{(5t)}\sin{x}\sin{(5x)}]\,dx",
                    font_size=80),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}\sin{(5t)}\sin{x}\sin{(5x)}\,dx -\\\int_{0}^{t}\cos{(5t)}\sin{"
                    r"x}\sin{(5x)}\,dx",
                    font_size=80),
            MathTex(r"f(t)\ast{g(t)} = \sin{(5t)}\int_{0}^{t}\sin{x}\cos{(5x)}\,dx -\\\cos{(5t)}\int_{0}^{t}\sin{"
                    r"x}\sin{(5x)}\,dx", font_size=80),
            Tex(r"To simplify the integral, \\ some identities are required:"),
            MathTex(r"\sin{a}\cos{b}=\frac{1}{2}[\sin{(a+b)}+\sin{(a-b)}]", font_size=80),
            MathTex(r"\sin{a}\sin{b}=\frac{1}{2}[\cos{(a-b)}-\cos{(a+b)}]", font_size=80),
            Tex("Applying the identities, we have:"),
            MathTex(r"\sin{x}\cos{(5x)}=\frac{1}{2}[\sin{(x+5x)}+\sin{(x-5x)}]", font_size=80),
            MathTex(r"\sin{x}\cos{(5x)}=\frac{1}{2}[\sin{(6x)}+\sin{(-4x)}]", font_size=80),
            Tex(r"Since $\sin{(-x)}=-\sin{x}$"),
            MathTex(r"\sin{x}\cos{(5x)}=\frac{1}{2}[\sin{(6x)}-\sin{(4x)}]", font_size=80),
            MathTex(r"\sin{x}\sin{(5x)}=\frac{1}{2}[\cos{(x-5x)}-\cos{(x+5x)}]", font_size=75),
            MathTex(r"\sin{x}\sin{(5x)}=\frac{1}{2}[\cos{(-4x)}-\cos{(6x)}]", font_size=75),
            Tex(r"Since $\cos{(-x)}=\cos{x}$"),
            MathTex(r"\sin{x}\sin{(5x)}=\frac{1}{2}[\cos{(4x)}-\cos{(6x)}]", font_size=75),
            Tex("Substitute to the integral:"),
            MathTex(r"f(t)\ast{g(t)}=\sin{(5t)}\int_{0}^{t}\bigg[\frac{1}{2}(\sin{(6x)}-\sin{(4x)})\bigg]\,dx "
                    r"-\\\cos{(5t)}\int_{0}^{t}\bigg[\frac{1}{2}(\cos{(4x)}-\cos{(6x)})\bigg]\,dx", font_size=65),
            MathTex(r"f(t)\ast{g(t)}=\frac{\sin{(5t)}}{2}\int_{0}^{t}[\sin{(6x)}-\sin{(4x)}]\,dx "
                    r"-\\\frac{\cos{(5t)}}{2}\int_{0}^{t}[\cos{(4x)}-\cos{(6x)}]\,dx", font_size=65),
            MathTex(r"f(t)\ast{g(t)}=\frac{\sin{(5t)}}{2}\bigg[\int_{0}^{t}\sin{(6x)}\,dx-"
                    r"\int_{0}^{t}\sin{(4x)}\,dx\bigg]"
                    r"-\\\frac{\cos{(5t)}}{2}\bigg[\int_{0}^{t}\cos{(4x)}\,dx-\int_{0}^{t}\cos{(6x)}\,dx\bigg]",
                    font_size=62),
            Tex("Integrating:"),
            MathTex(r"f(t)\ast{g(t)}=\frac{\sin{(5t)}}{2}\bigg[-\frac{\cos{(6x)}}{6}+\frac{\cos{(4x)}}{4}\bigg]_{0}^"
                    r"{t} - \\\frac{\cos{(5t)}}{2}\bigg[\frac{\sin{(4x)}}{4}-\frac{\sin{(6x)}}{6}\bigg]_{0}^{t}",
                    font_size=68),
            MathTex(r"f(t)\ast{g(t)}=\frac{\sin{(5t)}}{2}\bigg[\bigg(\frac{\cos{(4t)}}{4}-\frac{\cos{(6t)}}{6}\bigg)-\\"
                    r"\bigg(\frac{\cos{0}}{4}-\frac{\cos{0}}{6}\bigg)\bigg]-\frac{\cos{(5t)}}{2}\bigg[\bigg("
                    r"\frac{\sin{(4t)}}{4}-\\\frac{\sin{(6t)}}{6}\bigg)-\bigg(\frac{\sin{0}}{4}-\frac{\sin{0}}{6}"
                    r"\bigg)\bigg]", font_size=60),
            MathTex(r"f(t)\ast{g(t)}=\frac{\sin{(5t)}}{2}\bigg[\frac{\cos{(4t)}}{4}-\frac{\cos{(6t)}}{6}\\-\frac{1}{4}+"
                    r"\frac{1}{6}\bigg]-\frac{\cos{(5t)}}{2}\bigg[\frac{\sin{(4t)}}{4}-\\\frac{\sin{(6t)}}{6}\bigg]",
                    font_size=60),
            MathTex(r"f(t)\ast{g(t)}=\frac{1}{8}\sin{(5t)}\cos{(4t)}-\frac{1}{12}\cos{(6t)}\sin{(5t)}-\\"
                    r"\frac{1}{12}\sin{(5t)}-\frac{1}{8}\cos{(5t)}\sin{(4t)}+\frac{1}{12}\sin{(6t)}\cos{(5t)}",
                    font_size=60),
            MathTex(r"f(t)\ast{g(t)}=\frac{1}{8}[\sin{(5t)}\cos{(4t)}-\cos{(5t)}\sin{(4t)}]-\\\frac{1}{12}[\sin{(6t)}"
                    r"\cos{(5t)}-\cos{(6t)}\sin{(5t)}]-\\\frac{1}{12}\sin{(5t)}", font_size=65),
            Tex("To simplify, using a \\\\ trigonometric identity:"),
            MathTex(r"\sin{(a-b)}=\sin{a}\cos{b}-\cos{a}\sin{b}"),
            Tex("Utilizing the identity to simplify:"),
            MathTex(r"f(t)\ast{g(t)}=\frac{1}{8}\sin{(5t-4t)}+\frac{1}{12}\sin{(6t-5t)}-\\\frac{1}{12}\sin{(5t)}",
                    font_size=75),
            MathTex(r"f(t)\ast{g(t)}=\frac{1}{8}\sin{t}+\frac{1}{12}\sin{t}-\frac{1}{12}\sin{(5t)}",
                    font_size=75),
            MathTex(r"f(t)\ast{g(t)}=\bigg(\frac{1}{8}+\frac{1}{12}\bigg)\sin{t}-\frac{1}{12}\sin{(5t)}",
                    font_size=75),
            MathTex(r"f(t)\ast{g(t)}=\frac{5}{24}\sin{t}-\frac{1}{12}\sin{(5t)}"),
            Tex("Solving for the Inverse \\\\ Laplace Transform:"),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{240}{(s^{2}+1)(s^{2}+25)}\bigg\}=48[f(t)\ast{g(t)}]",
                    font_size=70),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{240}{(s^{2}+1)(s^{2}+25)}\bigg\}=\\48\bigg[\frac{5}{24}\sin{t}-"
                    r"\frac{1}{12}\sin{(5t)}\bigg]", font_size=70),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{240}{(s^{2}+1)(s^{2}+25)}\bigg\}=10\sin{t}-2\sin{(5t)}")
        )

        solutionDetails[0].move_to(UP * 7)
        self.play(Write(solutionDetails[0]))
        self.wait(0.3)
        self.play(Write(solutionDetails[1].next_to(solutionDetails[0], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutionDetails[1], solutionDetails[2].next_to(solutionDetails[0],
                                                                                      direction=DOWN,
                                                                                      buff=LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[3].next_to(solutionDetails[2], direction=DOWN, buff=LARGE_BUFF)),
                  Write(solutionDetails[4].next_to(solutionDetails[3], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(1)
        self.play(solutionDetails[4].animate.shift(DOWN))
        self.play(ReplacementTransform(solutionDetails[3],
                                       solutionDetails[5].next_to(solutionDetails[2], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.3)
        self.play(ReplacementTransform(solutionDetails[4], solutionDetails[6].next_to(solutionDetails[5],
                                                                                      direction=DOWN,
                                                                                      buff=LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutionDetails[6], solutionDetails[7].next_to(solutionDetails[5],
                                                                                      direction=DOWN,
                                                                                      buff=LARGE_BUFF)))
        self.wait(1.25)
        self.play(FadeOut(solutionDetails[0], solutionDetails[2], solutionDetails[5], solutionDetails[7]))

        solutionDetails[8].move_to(6 * UP)
        self.play(Write(solutionDetails[8]))
        self.wait(0.3)
        self.play(Write(solutionDetails[9].next_to(solutionDetails[8], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.5)
        self.play(TransformMatchingTex(solutionDetails[9], solutionDetails[10].next_to(solutionDetails[8],
                                                                                       direction=DOWN,
                                                                                       buff=LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[11].next_to(solutionDetails[10], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[12].next_to(solutionDetails[11], direction=DOWN, buff=LARGE_BUFF)))
        self.wait(0.5)
        for i in range(13, 16):
            self.play(TransformMatchingTex(solutionDetails[i - 1], solutionDetails[i].next_to(solutionDetails[11],
                                                                                              direction=DOWN,
                                                                                              buff=LARGE_BUFF)))
            self.wait(0.5)
        self.wait(0.75)
        self.play(FadeOut(solutionDetails[8], solutionDetails[10:12], solutionDetails[15]))

        solutionDetails[16].move_to(7 * UP)
        self.play(Write(solutionDetails[16]))
        self.wait(0.3)
        self.play(Write(solutionDetails[17].next_to(solutionDetails[16], DOWN, LARGE_BUFF)),
                  Write(solutionDetails[18].next_to(solutionDetails[17], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[19].next_to(solutionDetails[18], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[20].next_to(solutionDetails[19], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutionDetails[20], solutionDetails[21].next_to(solutionDetails[19],
                                                                                        DOWN,
                                                                                        LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[22].next_to(solutionDetails[21], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[23].next_to(solutionDetails[22], DOWN, LARGE_BUFF)))
        rectangleBox = SurroundingRectangle(solutionDetails[23], buff=0.25)
        self.play(Create(rectangleBox))
        self.wait(1.25)
        self.play(FadeOut(solutionDetails[21:24], rectangleBox))
        self.play(Write(solutionDetails[24].next_to(solutionDetails[19], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(TransformMatchingTex(solutionDetails[24], solutionDetails[25].next_to(solutionDetails[19],
                                                                                        DOWN,
                                                                                        LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[26].next_to(solutionDetails[25], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[27].next_to(solutionDetails[26], DOWN, LARGE_BUFF)))
        rectangleBox = SurroundingRectangle(solutionDetails[27], buff=0.25)
        self.play(Create(rectangleBox))
        self.wait(1.25)
        self.play(FadeOut(rectangleBox, solutionDetails[25:28], solutionDetails[16:20]))

        solutionDetails[28].move_to(6 * UP)
        self.play(Write(solutionDetails[28]))
        self.wait(0.3)
        self.play(Write(solutionDetails[29].next_to(solutionDetails[28], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(30, 32):
            self.play(ReplacementTransform(solutionDetails[i - 1], solutionDetails[i].next_to(solutionDetails[28],
                                                                                              DOWN, LARGE_BUFF)))
            self.wait(0.5)
        self.play(Write(solutionDetails[32].next_to(solutionDetails[31], DOWN, LARGE_BUFF)))
        self.wait(0.3)
        self.play(Write(solutionDetails[33].next_to(solutionDetails[32], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(34, 37):
            match i:
                case 34:
                    self.play(
                        ReplacementTransform(solutionDetails[i - 1], solutionDetails[i].next_to(solutionDetails[32],
                                                                                                DOWN, LARGE_BUFF)))
                    self.wait(0.3)
                    solutionDetails[i][0][43:47].set_color(BLUE)
                    solutionDetails[i][0][50:54].set_color(BLUE)
                    solutionDetails[i][0][92:96].set_color(YELLOW)
                    solutionDetails[i][0][99:103].set_color(YELLOW)
                    linesDetail_1 = Arrow(solutionDetails[i][0][43:47].get_corner(DL),
                                          solutionDetails[i][0][43:47].get_corner(UR), color=YELLOW, stroke_width=2)
                    linesDetail_2 = Arrow(solutionDetails[i][0][50:54].get_corner(DL),
                                          solutionDetails[i][0][50:54].get_corner(UR), color=YELLOW, stroke_width=2)
                    linesDetail_3 = Arrow(solutionDetails[i][0][92:96].get_corner(DL),
                                          solutionDetails[i][0][92:96].get_corner(UR), color=BLUE, stroke_width=2)
                    linesDetail_4 = Arrow(solutionDetails[i][0][99:103].get_corner(DL),
                                          solutionDetails[i][0][99:103].get_corner(UR), color=BLUE, stroke_width=2)
                    tempText = VGroup(MathTex(r"1", font_size=30, color=YELLOW),
                                      MathTex(r"1", font_size=30, color=YELLOW),
                                      MathTex(r"0", font_size=30, color=BLUE),
                                      MathTex(r"0", font_size=30, color=BLUE))
                    self.wait(0.2)
                    self.play(Create(linesDetail_1), Create(linesDetail_2), Create(linesDetail_3),
                              Create(linesDetail_4))
                    self.wait(0.2)
                    self.play(Write(tempText[0].next_to(solutionDetails[i][0][43:47].get_corner(UR), UP, SMALL_BUFF)),
                              Write(tempText[1].next_to(solutionDetails[i][0][50:54].get_corner(UR), UP, SMALL_BUFF)),
                              Write(tempText[2].next_to(solutionDetails[i][0][92:96].get_corner(UR), UP, SMALL_BUFF)),
                              Write(tempText[3].next_to(solutionDetails[i][0][99:103].get_corner(UR), UP, SMALL_BUFF)))
                    self.wait(0.5)
                    self.play(FadeOut(linesDetail_1, linesDetail_2, linesDetail_3, linesDetail_4, tempText, run_time=0.5),
                              ReplacementTransform(solutionDetails[i],
                                                   solutionDetails[i + 1].next_to(solutionDetails[32],
                                                                                  DOWN, LARGE_BUFF))
                              )
                case 35:
                    self.wait(0.2)
                    solutionDetails[i][0][39:47].set_color(BLUE)
                    linesDetail_1 = Arrow(solutionDetails[i][0][39:47].get_corner(DL),
                                          solutionDetails[i][0][39:47].get_corner(UR), color=YELLOW, stroke_width=2)
                    tempText = MathTex(r"-\frac{1}{12}", font_size=30, color=YELLOW)
                    self.wait(0.2)
                    self.play(Create(linesDetail_1))
                    self.wait(0.2)
                    self.play(Write(tempText.next_to(solutionDetails[i][0][39:47].get_corner(UR), UP, SMALL_BUFF)))
                    self.wait(0.5)
                    self.play(FadeOut(linesDetail_1, tempText, run_time=0.5),
                              ReplacementTransform(solutionDetails[i],
                                                   solutionDetails[i + 1].next_to(solutionDetails[32],
                                                                                  DOWN, LARGE_BUFF))
                              )
                    self.wait(0.5)
                case 36:
                    self.play(ReplacementTransform(solutionDetails[i], solutionDetails[i+1].next_to(solutionDetails[32],
                                                                                                    DOWN, LARGE_BUFF)))

        self.wait(1.25)
        self.play(FadeOut(solutionDetails[28], solutionDetails[31:33], solutionDetails[37]))

        solutionDetails[38].move_to(5 * UP)
        self.play(Write(solutionDetails[38]))
        self.wait(0.3)
        for i in range(39, 41):
            self.play(Write(solutionDetails[i].next_to(solutionDetails[i-1], DOWN, LARGE_BUFF)))
            self.wait(0.3)
        self.play(Write(solutionDetails[37].next_to(solutionDetails[40], DOWN, LARGE_BUFF)))
        self.wait(0.2)
        solutionDetails[37][0][14:43].set_color(BLUE)
        solutionDetails[37][0][50:79].set_color(YELLOW)
        linesDetail_1 = Arrow(solutionDetails[37][0][14:43].get_corner(DL),
                              solutionDetails[37][0][14:43].get_corner(UR), color=YELLOW, stroke_width=2)
        linesDetail_2 = Arrow(solutionDetails[37][0][50:79].get_corner(DL),
                              solutionDetails[37][0][50:79].get_corner(UR), color=BLUE, stroke_width=2)
        tempText = VGroup(
            MathTex(r"\sin{(5t-4t)}", font_size=50, color=YELLOW),
            MathTex(r"\sin{(6t-5t)}", font_size=50, color=BLUE)
        )
        self.play(Create(linesDetail_1), Create(linesDetail_2))
        self.play(Write(tempText[0].next_to(solutionDetails[37][0][14:43].get_corner(UR), UP, SMALL_BUFF)),
                  Write(tempText[1].next_to(solutionDetails[37][0][50:79].get_corner(UR), UP, SMALL_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(linesDetail_1, linesDetail_2, tempText, run_time=0.5),
                  ReplacementTransform(solutionDetails[37], solutionDetails[41].next_to(solutionDetails[40], DOWN,
                                                                                        LARGE_BUFF)))
        self.wait(0.3)
        solutionDetails[41][0][17:22].set_color(BLUE)
        solutionDetails[41][0][32:37].set_color(YELLOW)
        linesDetail_1 = Arrow(solutionDetails[41][0][17:22].get_corner(DL),
                              solutionDetails[41][0][17:22].get_corner(UR), color=YELLOW, stroke_width=2)
        linesDetail_2 = Arrow(solutionDetails[41][0][32:37].get_corner(DL),
                              solutionDetails[41][0][32:37].get_corner(UR), color=BLUE, stroke_width=2)
        tempText = VGroup(
            MathTex(r"t", font_size=50, color=YELLOW),
            MathTex(r"t", font_size=50, color=BLUE)
        )
        self.play(Create(linesDetail_1), Create(linesDetail_2))
        self.play(Write(tempText[0].next_to(solutionDetails[41][0][17:22].get_corner(UR), UP, SMALL_BUFF)),
                  Write(tempText[1].next_to(solutionDetails[41][0][32:37].get_corner(UR), UP, SMALL_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(linesDetail_1, linesDetail_2, tempText, run_time=0.5),
                  ReplacementTransform(solutionDetails[41], solutionDetails[42].next_to(solutionDetails[40], DOWN,
                                                                                        LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutionDetails[42], solutionDetails[43].next_to(solutionDetails[40], DOWN,
                                                                                        LARGE_BUFF)))
        solutionDetails[43][0][11:19].set_color(BLUE)
        linesDetail_1 = Arrow(solutionDetails[43][0][11:19].get_corner(DL),
                              solutionDetails[43][0][11:19].get_corner(UR), color=YELLOW, stroke_width=3)
        tempText = MathTex(r"\frac{5}{24}", font_size=50, color=YELLOW)
        self.play(Create(linesDetail_1))
        self.wait(0.3)
        self.play(Write(tempText.next_to(solutionDetails[43][0][11:19].get_corner(UR), UP, SMALL_BUFF)))
        self.wait(0.5)
        self.play(FadeOut(linesDetail_1, tempText, run_time=0.5),
                  ReplacementTransform(solutionDetails[43], solutionDetails[44].next_to(solutionDetails[40], DOWN,
                                                                                        LARGE_BUFF)))
        rectangleBox = SurroundingRectangle(solutionDetails[44], buff=0.4)
        self.play(Create(rectangleBox))
        self.wait(1.25)
        self.play(FadeOut(solutionDetails[38:41], solutionDetails[44], rectangleBox))

        solutionDetails[45].move_to(3 * UP)
        self.play(Write(solutionDetails[45]))
        self.wait(0.3)
        self.play(Write(solutionDetails[46].next_to(solutionDetails[45], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        self.play(ReplacementTransform(solutionDetails[46], solutionDetails[47].next_to(solutionDetails[45], DOWN,
                                                                                        LARGE_BUFF)))
        self.wait(0.3)
        solutionDetails[46][0][23:25].set_color(BLUE)
        solutionDetails[46][0][26:30].set_color(YELLOW)
        solutionDetails[46][0][35:39].set_color(YELLOW)
        linesDetail_1 = CurvedArrow(solutionDetails[46][0][23:25].get_top(),
                                    solutionDetails[46][0][26:30].get_top(), color=YELLOW)
        linesDetail_2 = CurvedArrow(solutionDetails[46][0][23:25].get_top(),
                                    solutionDetails[46][0][35:39].get_top(), color=BLUE)
        self.play(Create(linesDetail_1), Create(linesDetail_2))
        self.wait(1.25)
