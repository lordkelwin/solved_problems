from manim import * 


config.pixel_width = 1920
config.pixel_height = 1080


class ProblemStatement(Scene):
    def construct(self):
        statement = VGroup(
            Tex(r"\begin{minipage}{9cm}" \
            r"Make the Routh table and tell how many roots of the following polynomial are in the right half-plane and in the left-hand plane" \
            r"\end{minipage}").move_to(2.5 * UP),
            MathTex(r"P(s) = 3s^{7} + 9s^{6} + 6s^{5} + 4s^{4} + 7s^{3} + 8s^{2} + 2s + 6")
        )

        self.play(Write(statement[0]))
        self.wait(0.25)
        self.play(Write(statement[1].next_to(statement[0], DOWN, MED_LARGE_BUFF)))
        self.wait(2.5)
        self.play(FadeOut(statement))
        return super().construct()
    

class ProblemSolution(Scene):
    def construct(self):
        routhTable = MathTable(
            [
                ["s^{7}", 3, 6, 7, 2, 0],
                ["s^{6}", 9, 4, 8, 6, 0],
                ["s^{5}", "a_{31}", "a_{32}", "a_{33}", "a_{34}", 0],
                ["s^{4}", "a_{41}", "a_{42}", "a_{43}", "a_{44}", 0],
                ["s^{3}", "a_{51}", "a_{52}", "a_{53}", "a_{54}", 0],
                ["s^{2}", "a_{61}", "a_{62}", "a_{63}", "a_{64}", 0],
                ["s^{1}", "a_{71}", "a_{72}", "a_{73}", "a_{74}", 0],
                ["s^{0}", "a_{81}", "a_{82}", "a_{83}", "a_{84}", 0]
            ]
        ).scale(0.80).set_row_colors(BLUE, BLUE).set_column_colors(YELLOW)

        self.play(Create(routhTable))
        self.wait(1.25)
        self.play(routhTable.animate.shift(3.0 * LEFT))
        self.wait(1.0)

        highlight = VGroup(
            SurroundingRectangle(VGroup(routhTable.get_cell((1,2)), routhTable.get_cell((2,2))), color=GREEN),
            SurroundingRectangle(VGroup(routhTable.get_cell((1,3)), routhTable.get_cell((2,3))), color=GREEN),
            SurroundingRectangle(routhTable.get_cell((3,2)), color=YELLOW)
        )

        solution = VGroup(
            MathTex(r"a_{31}=-\frac{\begin{vmatrix} a_{7} & a_{5} \\ a_{6} & a_{4} \end{vmatrix}}{a_{6}}"),
            MathTex(r"a_{31}=-\frac{\begin{vmatrix} 3 & 6 \\ 9 & 4 \end{vmatrix}}{9}"),
            MathTex(r"a_{31}=-\frac{[(3)(4)]-[(6)(9)]}{9}"),
            MathTex(r"a_{31}=-\frac{12-54}{9}"),
            MathTex(r"a_{31}=-\frac{-42}{9}"),
            MathTex(r"a_{31}=\frac{14}{3}"),
        ).move_to(routhTable.get_right() + 3.5 * RIGHT)

        self.play(Create(highlight))
        self.wait(0.5)
        self.play(Write(solution[0]))
        self.wait(0.25)
        for i in range(1, 6):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((3,2)), MathTex(r"\frac{14}{3}", color=RED).move_to(routhTable.get_entries((3,2)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.55 * RIGHT))
        self.wait(2.0)
        return super().construct()
