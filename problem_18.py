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
            MathTex(r"a_{32}=-\frac{\begin{vmatrix} a_{7} & a_{3} \\ a_{6} & a_{2} \end{vmatrix}}{a_{6}}"),
            MathTex(r"a_{32}=-\frac{\begin{vmatrix} 3 & 7 \\ 9 & 8 \end{vmatrix}}{9}"),
            MathTex(r"a_{32}=-\frac{[(3)(8)]-[(7)(9)]}{9}"),
            MathTex(r"a_{32}=-\frac{24-63}{9}"),
            MathTex(r"a_{32}=-\frac{-39}{9}"),
            MathTex(r"a_{32}=\frac{13}{3}"),
            MathTex(r"a_{33}=-\frac{\begin{vmatrix} a_{7} & a_{1} \\ a_{6} & a_{0} \end{vmatrix}}{a_{6}}"),
            MathTex(r"a_{33}=-\frac{\begin{vmatrix} 3 & 2 \\ 9 & 6 \end{vmatrix}}{9}"),
            MathTex(r"a_{33}=-\frac{[(3)(6)]-[(2)(9)]}{9}"),
            MathTex(r"a_{33}=-\frac{18-18}{9}"),
            MathTex(r"a_{33}=\frac{0}{9}"),
            MathTex(r"a_{33}=0"),
            MathTex(r"a_{34}=-\frac{\begin{vmatrix} a_{7} & 0 \\ a_{6} & 0 \end{vmatrix}}{a_{6}}"),
            MathTex(r"a_{34}=-\frac{\begin{vmatrix} 3 & 0 \\ 9 & 0 \end{vmatrix}}{9}"),
            MathTex(r"a_{34}=-\frac{[(3)(0)]-[(0)(9)]}{9}"),
            MathTex(r"a_{34}=-\frac{0-0}{9}"),
            MathTex(r"a_{34}=\frac{0}{9}"),
            MathTex(r"a_{34}=0"),
            MathTex(r"a_{41}=-\frac{\begin{vmatrix} a_{6} & a_{4} \\ a_{31} & a_{32} \end{vmatrix}}{a_{31}}"),
            MathTex(r"a_{41}=-\frac{\begin{vmatrix} 9 & 4 \\ 14 & 13 \end{vmatrix}}{14}"),
            MathTex(r"a_{41}=-\frac{[(9)(13)]-[(4)(14)]}{9}"),
            MathTex(r"a_{41}=-\frac{117-56}{9}"),
            MathTex(r"a_{41}=-\frac{61}{9}"),
            MathTex(r"a_{42}=-\frac{\begin{vmatrix} a_{6} & a_{2} \\ a_{31} & a_{33} \end{vmatrix}}{a_{31}}"),
            MathTex(r"a_{42}=-\frac{\begin{vmatrix} 9 & 8 \\ 14 & 0 \end{vmatrix}}{14}"),
            MathTex(r"a_{42}=-\frac{[(9)(0)]-[(8)(14)]}{14}"),
            MathTex(r"a_{42}=-\frac{0-112}{14}"),
            MathTex(r"a_{42}=\frac{112}{14}"),
            MathTex(r"a_{42}=8"),
            MathTex(r"a_{43}=-\frac{\begin{vmatrix} a_{6} & a_{0} \\ a_{31} & a_{34} \end{vmatrix}}{a_{31}}"),
            MathTex(r"a_{43}=-\frac{\begin{vmatrix} 9 & 6 \\ 14 & 0 \end{vmatrix}}{14}"),
            MathTex(r"a_{43}=-\frac{[(9)(0)]-[(6)(14)]}{14}"),
            MathTex(r"a_{43}=-\frac{0-84}{14}"),
            MathTex(r"a_{43}=\frac{84}{9}"),
            MathTex(r"a_{43}=6"),
            MathTex(r"a_{44}=-\frac{\begin{vmatrix} a_{6} & 0 \\ a_{31} & 0 \end{vmatrix}}{a_{31}}"),
            MathTex(r"a_{44}=-\frac{\begin{vmatrix} 9 & 0 \\ 14 & 0 \end{vmatrix}}{14}"),
            MathTex(r"a_{44}=-\frac{[(9)(0)]-[(0)(14)]}{14}"),
            MathTex(r"a_{44}=-\frac{0-0}{14}"),
            MathTex(r"a_{44}=\frac{0}{14}"),
            MathTex(r"a_{44}=0"),
            MathTex(r"a_{51}=-\frac{\begin{vmatrix} a_{31} & a_{32} \\ a_{41} & a_{42} \end{vmatrix}}{a_{41}}"),
            MathTex(r"a_{51}=-\frac{\begin{vmatrix} 14 & 13 \\ -\frac{61}{14} & 8 \end{vmatrix}}{-\frac{61}{14}}"),
            MathTex(r"a_{51}=\frac{[(14)(8)]-[(-\frac{61}{14})(13)]}{\frac{61}{14}}"),
            MathTex(r"a_{51}=\frac{112+\frac{793}{14}}{\frac{61}{14}}"),
            MathTex(r"a_{51}=\frac{\frac{2361}{14}}{\frac{61}{14}}"),
            MathTex(r"a_{51}=\frac{2361}{61}"),
            MathTex(r"a_{52}=-\frac{\begin{vmatrix} a_{31} & a_{33} \\ a_{41} & a_{43} \end{vmatrix}}{a_{41}}"),
            MathTex(r"a_{52}=-\frac{\begin{vmatrix} 14 & 0 \\ -\frac{61}{14} & 6 \end{vmatrix}}{-\frac{61}{14}}"),
            MathTex(r"a_{52}=\frac{[(14)(6)]-[(0)(-\frac{61}{14})]}{\frac{61}{14}}"),
            MathTex(r"a_{52}=\frac{84+0}{\frac{61}{14}}"),
            MathTex(r"a_{52}=\frac{(84)(14)}{61}"),
            MathTex(r"a_{52}=\frac{1176}{61}"),
            MathTex(r"a_{53}=-\frac{\begin{vmatrix} a_{31} & a_{34} \\ a_{41} & a_{44} \end{vmatrix}}{a_{41}}"),
            MathTex(r"a_{53}=-\frac{\begin{vmatrix} 14 & 0 \\ -\frac{61}{14} & 0 \end{vmatrix}}{-\frac{61}{14}}"),
            MathTex(r"a_{53}=\frac{[(14)(0)]-[(0)(-\frac{61}{14})]}{\frac{61}{14}}"),
            MathTex(r"a_{53}=\frac{0+0}{\frac{61}{14}}"),
            MathTex(r"a_{53}=\frac{(0)(14)}{61}}"),
            MathTex(r"a_{53}=0"),
            MathTex(r"a_{54}=-\frac{\begin{vmatrix} a_{31} & 0 \\ a_{41} & 0 \end{vmatrix}}{a_{41}}"),
            MathTex(r"a_{54}=-\frac{\begin{vmatrix} 14 & 0 \\ -\frac{61}{14} & 0 \end{vmatrix}}{-\frac{61}{14}}"),
            MathTex(r"a_{54}=\frac{[(14)(0)]-[(0)(-\frac{61}{14})]}{\frac{61}{14}}"),
            MathTex(r"a_{54}=\frac{0-0}{\frac{61}{14}}"),
            MathTex(r"a_{54}=\frac{(0)(14)}{61}"),
            MathTex(r"a_{54}=0"),
            MathTex(r"a_{61}=-\frac{\begin{vmatrix} a_{41} & a_{42} \\ a_{51} & a_{52} \end{vmatrix}}{a_{51}}"),
            MathTex(r"a_{61}=-\frac{\begin{vmatrix} -\frac{61}{14} & 8 \\ 787 & 392 \end{vmatrix}}{787}"),
            MathTex(r"a_{61}=-\frac{[-(\frac{61}{14})(392)]-[(8)(787)]}{787}"),
            MathTex(r"a_{61}=-\frac{-1708-6296}{787}"),
            MathTex(r"a_{61}=-\frac{-8004}{787}"),
            MathTex(r"a_{61}=\frac{8004}{787}"),
            MathTex(r"a_{62}=-\frac{\begin{vmatrix} a_{41} & a_{43} \\ a_{51} & a_{53} \end{vmatrix}}{a_{51}}"),
            MathTex(r"a_{62}=-\frac{\begin{vmatrix} -\frac{61}{14} & 6 \\ 787 & 0 \end{vmatrix}}{787}"),
            MathTex(r"a_{62}=-\frac{[(-\frac{61}{14})(0)]-[(6)(787)]}{787}"),
            MathTex(r"a_{62}=-\frac{0-4722}{787}"),
            MathTex(r"a_{62}=-\frac{-4722}{787}"),
            MathTex(r"a_{62}=6"),
            MathTex(r"a_{63}=-\frac{\begin{vmatrix} a_{41} & a_{44} \\ a_{51} & a_{54} \end{vmatrix}}{a_{51}}"),
            MathTex(r"a_{63}=-\frac{\begin{vmatrix} -\frac{61}{14} & 0 \\ 787 & 0 \end{vmatrix}}{787}"),
            MathTex(r"a_{63}=-\frac{[(-\frac{61}{14})(0)]-[(0)(787)]}{787}"),
            MathTex(r"a_{63}=-\frac{-0-0}{787}"),
            MathTex(r"a_{63}=\frac{0}{787}}"),
            MathTex(r"a_{63}=0"),
            MathTex(r"a_{64}=-\frac{\begin{vmatrix} a_{41} & 0 \\ a_{51} & 0 \end{vmatrix}}{a_{51}}"),
            MathTex(r"a_{64}=-\frac{\begin{vmatrix} -\frac{61}{14} & 0 \\ 787 & 0 \end{vmatrix}}{787}"),
            MathTex(r"a_{64}=-\frac{[(-\frac{61}{14})(0)]-[(0)(787)]}{787}"),
            MathTex(r"a_{64}=-\frac{-0-0}{787}"),
            MathTex(r"a_{64}=\frac{0}{787}"),
            MathTex(r"a_{64}=0"),
            MathTex(r"a_{71}=-\frac{\begin{vmatrix} a_{51} & a_{52} \\ a_{61} & a_{62} \end{vmatrix}}{a_{61}}"),
            MathTex(r"a_{71}=-\frac{\begin{vmatrix} 787 & 392 \\ \frac{8004}{787} & 6 \end{vmatrix}}{\frac{8004}{787}}"),
            MathTex(r"a_{71}=-\frac{[(787)(6)]-[(392)(\frac{8004}{787})]}{\frac{8004}{787}}"),
            MathTex(r"a_{71}=-\frac{4722-\frac{3137586}{787}}{\frac{8004}{787}}"),
            MathTex(r"a_{71}=-\frac{\frac{578628}{787}}{\frac{8004}{787}}"),
            MathTex(r"a_{71}=-\frac{96441}{1334}"),
            MathTex(r"a_{72}=-\frac{\begin{vmatrix} a_{51} & a_{53} \\ a_{61} & a_{63} \end{vmatrix}}{a_{61}}"),
            MathTex(r"a_{72}=-\frac{\begin{vmatrix} 787 & 0 \\ \frac{8004}{787} & 0 \end{vmatrix}}{\frac{8004}{787}}"),
            MathTex(r"a_{72}=-\frac{[(787)(0)]-[(0)(\frac{8004}{787})]}{\frac{8004}{787}}"),
            MathTex(r"a_{72}=-\frac{0-0}{\frac{8004}{787}}"),
            MathTex(r"a_{72}=-\frac{(0)(787)}{8004}"),
            MathTex(r"a_{72}=0"),
            MathTex(r"a_{73}=-\frac{\begin{vmatrix} a_{51} & a_{54} \\ a_{61} & a_{64} \end{vmatrix}}{a_{61}}"),
            MathTex(r"a_{73}=-\frac{\begin{vmatrix} 787 & 0 \\ \frac{8004}{787} & 0 \end{vmatrix}}{\frac{8004}{787}}"),
            MathTex(r"a_{73}=-\frac{[(787)(0)]-[(0)(\frac{8004}{787})]}{\frac{8004}{787}}}"),
            MathTex(r"a_{73}=-\frac{0-0}{787}"),
            MathTex(r"a_{73}=-\frac{(0)(787)}{8004}}"),
            MathTex(r"a_{73}=0"),
            MathTex(r"a_{74}=-\frac{\begin{vmatrix} a_{51} & 0 \\ a_{61} & 0 \end{vmatrix}}{a_{61}}"),
            MathTex(r"a_{74}=-\frac{\begin{vmatrix} 787 & 0 \\ \frac{8004}{787} & 0 \end{vmatrix}}{\frac{8004}{787}}"),
            MathTex(r"a_{74}=-\frac{[(787)(0)]-[(0)(\frac{8004}{787}})]}{\frac{8004}{787}}}"),
            MathTex(r"a_{74}=-\frac{0-0}{\frac{8004}{787}}}"),
            MathTex(r"a_{74}=\frac{(0)(787)}{8004}"),
            MathTex(r"a_{74}=0"),
            MathTex(r"a_{81}=-\frac{\begin{vmatrix} a_{61} & a_{62} \\ a_{71} & a_{72} \end{vmatrix}}{a_{71}}"),
            MathTex(r"a_{81}=-\frac{\begin{vmatrix} \frac{8004}{787} & 6 \\ -1581 & 0 \end{vmatrix}}{-1581}"),
            MathTex(r"a_{81}=\frac{[(\frac{8004}{787})(0)]-[(6)(-1581)]}{1581}"),
            MathTex(r"a_{81}=\frac{0+9846}{1581}"),
            MathTex(r"a_{81}=\frac{9486}{1581}"),
            MathTex(r"a_{81}=6"),
            MathTex(r"a_{82}=-\frac{\begin{vmatrix} a_{61} & a_{63} \\ a_{71} & a_{73} \end{vmatrix}}{a_{71}}"),
            MathTex(r"a_{82}=-\frac{\begin{vmatrix} \frac{8004}{787} & 0 \\ -1581 & 0 \end{vmatrix}}{-1581}"),
            MathTex(r"a_{82}=\frac{[(\frac{8004}{787})(0)]-[(0)(-1581)]}{\frac{1581}{787}}"),
            MathTex(r"a_{82}=\frac{0+0}{1581}"),
            MathTex(r"a_{82}=\frac{0}{1581}"),
            MathTex(r"a_{82}=0"),
            MathTex(r"a_{83}=-\frac{\begin{vmatrix} a_{61} & a_{64} \\ a_{71} & a_{74} \end{vmatrix}}{a_{71}}"),
            MathTex(r"a_{83}=-\frac{\begin{vmatrix} \frac{8004}{787} & 0 \\ -1581 & 0 \end{vmatrix}}{-1581}"),
            MathTex(r"a_{83}=\frac{[(\frac{8004}{787})(0)]-[(0)(-1581)]}{1581}"),
            MathTex(r"a_{83}=\frac{0+0}{1581}"),
            MathTex(r"a_{83}=\frac{0}{1581}}"),
            MathTex(r"a_{83}=0"),
            MathTex(r"a_{84}=-\frac{\begin{vmatrix} a_{61} & 0 \\ a_{71} & 0 \end{vmatrix}}{a_{71}}"),
            MathTex(r"a_{84}=-\frac{\begin{vmatrix} \frac{8004}{787} & 0 \\ -1581 & 0 \end{vmatrix}}{-1581}"),
            MathTex(r"a_{84}=\frac{[(\frac{8004}{787})(0)]-[(0)(-1581)]}{\frac{8004}{787}}}"),
            MathTex(r"a_{84}=\frac{0+0}{1581}"),
            MathTex(r"a_{84}=\frac{0}{1581}"),
            MathTex(r"a_{84}=0"),
        ).move_to(routhTable.get_right() + 3.5 * RIGHT).scale(0.825)

        routhEntries = VGroup(
            MathTex(r"\frac{14}{3}", color=RED),
            MathTex(r"\frac{13}{3}", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"-\frac{61}{14}", color=RED),
            MathTex(r"8", color=RED),
            MathTex(r"6", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"\frac{2361}{61}", color=RED),
            MathTex(r"\frac{1176}{61}", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"\frac{8004}{787}", color=RED),
            MathTex(r"6", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"-\frac{96441}{1334}", color=RED),
            MathTex(r"6", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"6", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"0", color=RED),
            MathTex(r"0", color=RED),
        )

        routhSimplifiedEntries = VGroup(
            MathTex(r"14", color=RED),
            MathTex(r"13", color=RED),
            MathTex(r"787", color=RED),
            MathTex(r"392", color=RED),
            MathTex(r"-1581", color=RED),
        )

        arrows = VGroup()

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
        self.play(ReplacementTransform(routhTable.get_entries((3,2)), routhEntries[0].move_to(routhTable.get_entries((3,2)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(7, 12):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((3,3)), routhEntries[1].move_to(routhTable.get_entries((3,3)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(13, 18):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((3,4)), routhEntries[2].move_to(routhTable.get_entries((3,4)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(19, 24):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((3,5)), routhEntries[3].move_to(routhTable.get_entries((3,5)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[0].animate.shift(1.0 * DOWN), highlight[1:3].animate.shift(4.575 * LEFT + 1.0 * DOWN))
        self.wait(0.5)
        
        arrows.add(Arrow(routhTable.get_cell((3,2)).get_corner(DL), routhTable.get_cell((3,2)).get_corner(UR), color=YELLOW))
        arrows.add(Arrow(routhTable.get_cell((3,3)).get_corner(DL), routhTable.get_cell((3,3)).get_corner(UR), color=YELLOW))

        self.play(Create(arrows[0]), Create(arrows[1]))
        self.play(Write(routhSimplifiedEntries[0].next_to(arrows[0].get_end(), UP, buff=0).scale(0.5)), 
                  Write(routhSimplifiedEntries[1].next_to(arrows[1].get_end(), UP, buff=0).scale(0.5)))
        
        self.wait(0.25)
        self.play(FadeOut(arrows))
        self.play(FadeOut(routhSimplifiedEntries[:2]))
        
        self.play(ReplacementTransform(routhEntries[0], routhSimplifiedEntries[0].move_to(routhTable.get_entries((3,2)), ORIGIN).scale(1.5)),
                  ReplacementTransform(routhEntries[1], routhSimplifiedEntries[1].move_to(routhTable.get_entries((3,3)), ORIGIN).scale(1.5)))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(25, 29):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((4,2)), routhEntries[4].move_to(routhTable.get_entries((4,2)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(30, 35):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((4,3)), routhEntries[5].move_to(routhTable.get_entries((4,3)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(36, 41):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((4,4)), routhEntries[6].move_to(routhTable.get_entries((4,4)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(42, 47):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((4,5)), routhEntries[7].move_to(routhTable.get_entries((4,5)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[0].animate.shift(1.0 * DOWN), highlight[1:3].animate.shift(4.575 * LEFT + 1.0 * DOWN))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(48, 53):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((5,2)), routhEntries[8].move_to(routhTable.get_entries((5,2)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(54, 59):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((5,3)), routhEntries[9].move_to(routhTable.get_entries((5,3)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(60, 65):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((5,4)), routhEntries[10].move_to(routhTable.get_entries((5,4)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(66, 71):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((5,5)), routhEntries[11].move_to(routhTable.get_entries((5,5)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[0].animate.shift(1.0 * DOWN), highlight[1:3].animate.shift(4.575 * LEFT + 1.0 * DOWN))
        self.wait(0.5)

        arrows.add(Arrow(routhTable.get_cell((5,2)).get_corner(DL), routhTable.get_cell((5,2)).get_corner(UR), color=YELLOW))
        arrows.add(Arrow(routhTable.get_cell((5,3)).get_corner(DL), routhTable.get_cell((5,3)).get_corner(UR), color=YELLOW))

        self.play(Create(arrows[2]), Create(arrows[3]))
        self.play(Write(routhSimplifiedEntries[2].next_to(arrows[2].get_end(), UP, buff=0).scale(0.5)), 
                  Write(routhSimplifiedEntries[3].next_to(arrows[3].get_end(), UP, buff=0).scale(0.5)))
        
        self.wait(0.25)
        self.play(FadeOut(arrows[2:4]))
        self.play(FadeOut(routhSimplifiedEntries[2:4]))
        
        self.play(ReplacementTransform(routhEntries[8], routhSimplifiedEntries[2].move_to(routhTable.get_entries((5,2)), ORIGIN).scale(1.5)),
                  ReplacementTransform(routhEntries[9], routhSimplifiedEntries[3].move_to(routhTable.get_entries((5,3)), ORIGIN).scale(1.5)))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(72, 77):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((6,2)), routhEntries[12].move_to(routhTable.get_entries((6,2)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(78, 83):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((6,3)), routhEntries[13].move_to(routhTable.get_entries((6,3)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(84, 89):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((6,4)), routhEntries[14].move_to(routhTable.get_entries((6,4)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(90, 95):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((6,5)), routhEntries[15].move_to(routhTable.get_entries((6,5)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[0].animate.shift(1.0 * DOWN), highlight[1:3].animate.shift(4.575 * LEFT + 1.0 * DOWN))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(96, 101):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((7,2)), routhEntries[16].move_to(routhTable.get_entries((7,2)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(102, 107):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((7,3)), routhEntries[17].move_to(routhTable.get_entries((7,3)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(108, 113):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((7,4)), routhEntries[18].move_to(routhTable.get_entries((7,4)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(114, 119):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((7,5)), routhEntries[19].move_to(routhTable.get_entries((7,5)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[0].animate.shift(1.0 * DOWN), highlight[1:3].animate.shift(4.575 * LEFT + 1.0 * DOWN))
        self.wait(0.5)

        arrows.add(Arrow(routhTable.get_cell((7,2)).get_corner(DL), routhTable.get_cell((7,2)).get_corner(UR), color=YELLOW))
        
        self.play(Create(arrows[4]))
        self.play(Write(routhSimplifiedEntries[4].next_to(arrows[2].get_end(), UP, buff=0).scale(0.5)))
        
        self.wait(0.25)
        self.play(FadeOut(arrows[4]))
        self.play(FadeOut(routhSimplifiedEntries[4]))
        
        self.play(ReplacementTransform(routhEntries[16], routhSimplifiedEntries[4].move_to(routhTable.get_entries((7,2)), ORIGIN).scale(1.5)))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(120, 123):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((8,2)), routhEntries[20].move_to(routhTable.get_entries((8,2)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(124, 129):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((8,3)), routhEntries[21].move_to(routhTable.get_entries((8,3)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(130, 135):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((8,4)), routhEntries[22].move_to(routhTable.get_entries((8,4)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i]))
        self.play(highlight[1:3].animate.shift(1.525 * RIGHT))
        self.wait(0.5)

        self.play(Write(solution[i+1]))
        self.wait(0.25)
        for i in range(136, 141):
            self.play(ReplacementTransform(solution[i-1], solution[i]))
            self.wait(0.5)
        self.wait(1.25)
        surroundAnswer = SurroundingRectangle(solution[i], buff=0.25, color=YELLOW)
        self.play(Create(surroundAnswer))
        self.wait(0.25)
        self.play(ReplacementTransform(routhTable.get_entries((8,5)), routhEntries[23].move_to(routhTable.get_entries((8,5)), ORIGIN).scale(0.75)))
        self.wait(0.75)
        self.play(FadeOut(surroundAnswer, solution[i], highlight))

        self.wait(2.0)
        return super().construct()
