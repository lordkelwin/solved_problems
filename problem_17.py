from manim import *


config.pixel_width = 1920
config.pixel_height = 1080


class ProblemStatement(Scene):
    def construct(self):
        statement = VGroup(
            Tex(r"\begin{minipage}{9cm}" \
            r"Make the Routh table for the system shown in the figure." \
            r"\end{minipage}"),
        )

        statement[0].move_to(UP * 2)

        blockDiagram = VGroup(
            Circle(radius=0.25, color=WHITE).move_to(LEFT * 3),
            Rectangle(width=5.0, height=1.75).move_to(RIGHT)
        )

        lines = VGroup(
            Line(blockDiagram[0].get_left(), blockDiagram[0].get_right(), buff=0).rotate(45 * DEGREES),
            Line(blockDiagram[0].get_top(), blockDiagram[0].get_bottom(), buff=0).rotate(45 * DEGREES),
        )

        arrows = VGroup(
            Arrow(blockDiagram[0].get_left()+2.5 * LEFT, blockDiagram[0].get_left(), buff=0),
            Arrow(blockDiagram[0].get_right(), blockDiagram[1].get_left(), buff=0),
            Arrow(blockDiagram[1].get_right(), blockDiagram[1].get_right() + 2.5 * RIGHT, buff=0)
        )

        feedbackLoop = VGroup(
            Line(arrows[2].get_midpoint(), arrows[2].get_midpoint() + 2 * DOWN, buff=0),
            Line(arrows[2].get_midpoint() + 2 * DOWN, [blockDiagram[0].get_bottom()[0], arrows[2].get_midpoint()[1]-2, 0], buff=0),
            Arrow([blockDiagram[0].get_bottom()[0], arrows[2].get_midpoint()[1]-2, 0], blockDiagram[0].get_bottom(), buff=0)
        )

        texts = VGroup(
            MathTex(r"R(s)").next_to(arrows[0].get_start() + 0.5 * RIGHT, UP, MED_SMALL_BUFF),
            MathTex(r"E(s)").next_to(arrows[1].get_midpoint(), UP, MED_SMALL_BUFF),
            MathTex(r"\frac{1000}{(s+2)(s+3)(s+5)}").move_to(blockDiagram[1], ORIGIN),
            MathTex(r"C(s)").next_to(arrows[2].get_end() + 0.5 * LEFT, UP, MED_SMALL_BUFF)
        )

        signs = VGroup(
            MathTex(r"+").next_to(arrows[0].get_end()+0.25 * LEFT, UP, MED_SMALL_BUFF),
            MathTex(r"-").next_to(feedbackLoop[2].get_end()+0.25 * DOWN, LEFT, MED_SMALL_BUFF)
        )

        self.play(Write(statement[0]))
        self.wait(0.3)
        self.play(Create(arrows[0]))
        self.play(Write(texts[0]))
        self.play(Write(signs[0]))
        self.play(Create(blockDiagram[0]), Create(lines[0]), Create(lines[1]))
        self.play(Create(arrows[1]))
        self.play(Write(texts[1]))
        self.play(Create(blockDiagram[1]), Write(texts[2]))
        self.play(Create(arrows[2]))
        self.play(Write(texts[3]))
        self.play(Create(feedbackLoop))
        self.play(Write(signs[1]))
        self.wait(3)
        self.play(FadeOut(statement, blockDiagram, lines, signs, texts, arrows, feedbackLoop))
        return super().construct()
    

class ProblemSolution(Scene):
    def construct(self):
        blockDiagram = VGroup(
            Circle(radius=0.25, color=WHITE).move_to(LEFT * 3 + UP * 2.0),
            Rectangle(width=5.0, height=1.75).move_to(RIGHT + UP * 2.0)
        )

        lines = VGroup(
            Line(blockDiagram[0].get_left(), blockDiagram[0].get_right(), buff=0).rotate(45 * DEGREES),
            Line(blockDiagram[0].get_top(), blockDiagram[0].get_bottom(), buff=0).rotate(45 * DEGREES),
        )

        arrows = VGroup(
            Arrow(blockDiagram[0].get_left()+2.5 * LEFT, blockDiagram[0].get_left(), buff=0),
            Arrow(blockDiagram[0].get_right(), blockDiagram[1].get_left(), buff=0),
            Arrow(blockDiagram[1].get_right(), blockDiagram[1].get_right() + 2.5 * RIGHT, buff=0)
        )

        feedbackLoop = VGroup(
            Line(arrows[2].get_midpoint(), arrows[2].get_midpoint() + 2 * DOWN, buff=0),
            Line(arrows[2].get_midpoint() + 2 * DOWN, [blockDiagram[0].get_bottom()[0], arrows[2].get_midpoint()[1]-2, 0], buff=0),
            Arrow([blockDiagram[0].get_bottom()[0], arrows[2].get_midpoint()[1]-2, 0], blockDiagram[0].get_bottom(), buff=0)
        )

        texts = VGroup(
            MathTex(r"R(s)").next_to(arrows[0].get_start() + 0.5 * RIGHT, UP, MED_SMALL_BUFF),
            MathTex(r"E(s)").next_to(arrows[1].get_midpoint(), UP, MED_SMALL_BUFF),
            MathTex(r"\frac{1000}{(s+2)(s+3)(s+5)}").move_to(blockDiagram[1], ORIGIN),
            MathTex(r"C(s)").next_to(arrows[2].get_end() + 0.5 * LEFT, UP, MED_SMALL_BUFF)
        )

        signs = VGroup(
            MathTex(r"+").next_to(arrows[0].get_end()+0.25 * LEFT, UP, MED_SMALL_BUFF),
            MathTex(r"-").next_to(feedbackLoop[2].get_end()+0.25 * DOWN, LEFT, MED_SMALL_BUFF)
        )

        self.play(Create(VGroup(blockDiagram, lines, arrows, feedbackLoop, texts, signs)))
        self.wait(1)

        transferFunction = VGroup(
            MathTex(r"T(s) = \frac{G(s)}{1+G(s)H(s)}"),
            MathTex(r"T(s)= \frac{\frac{1000}{(s+2)(s+3)(s+5)}}{1+\left[\frac{1000}{(s+2)(s+3)(s+5)}\right][1]}"),
            MathTex(r"T(s)= \frac{\frac{1000}{(s+2)(s+3)(s+5)}}{1+\left[\frac{1000}{(s+2)(s+3)(s+5)}\right]} \times \frac{(s+2)(s+3)(s+5)}{(s+2)(s+3)(s+5)}"),
            MathTex(r"T(s) = \frac{1000}{(s+2)(s+3)(s+5)+1000}"),
            MathTex(r"T(s) = \frac{1000}{(s^{2}+5s+6)(s+5)+1000}"),
            MathTex(r"T(s) = \frac{1000}{s^{3}+5s^{2}+6s+5s^{2}+25s+30+1000}"),
            MathTex(r"T(s) = \frac{1000}{s^{3}+10s^{2}+31s+1030}"),
        )

        self.play(Write(transferFunction[0].next_to(feedbackLoop[1], DOWN, LARGE_BUFF)))
        self.wait(0.5)
        for i in range(1, 7):
            self.play(ReplacementTransform(transferFunction[i-1], transferFunction[i].next_to(feedbackLoop[1], DOWN, LARGE_BUFF)))
            if i == 2:
                transferFunction[i][0][10:25].set_color(YELLOW)
                transferFunction[i][0][34:49].set_color(YELLOW)
                transferFunction[i][0][51:66].set_color(BLUE)
                transferFunction[i][0][67:].set_color(BLUE)
                crossLines = VGroup(
                    Line(transferFunction[i][0][10:25].get_corner(DL), transferFunction[i][0][10:25].get_corner(UR), color=BLUE),
                    Line(transferFunction[i][0][34:49].get_corner(DL), transferFunction[i][0][34:49].get_corner(UR), color=BLUE),
                    Line(transferFunction[i][0][51:66].get_corner(DL), transferFunction[i][0][51:66].get_corner(UR), color=YELLOW),
                    Line(transferFunction[i][0][67:].get_corner(DL), transferFunction[i][0][67:].get_corner(UR), color=YELLOW),
                )

                self.play(Create(crossLines[0]), Create(crossLines[1]), Create(crossLines[2]), Create(crossLines[3]))
                self.wait(0.5)
                self.play(FadeOut(crossLines))
            else:
                self.wait(0.75)
        
        self.wait(1.5)

        blockDiagramNew = Rectangle(width=5.5, height=1.75).move_to(UP * 2.0)

        arrowsNew = VGroup(
            Arrow(blockDiagramNew.get_left() + 2.5 * LEFT, blockDiagramNew.get_left(), buff=0),
            Arrow(blockDiagramNew.get_right(), blockDiagramNew.get_right() + 2.5 * RIGHT, buff=0),
        )

        textNew = VGroup(
            MathTex(r"\frac{1000}{s^{3}+10s^{2}+31s+1030}").move_to(blockDiagramNew, ORIGIN),
            MathTex(r"R(s)").next_to(arrowsNew[0].get_start()+0.5*RIGHT, UP, MED_SMALL_BUFF),
            MathTex(r"C(s)").next_to(arrowsNew[1].get_end()+0.5*LEFT, UP, MED_SMALL_BUFF),
        )

        simplifiedBlock = VGroup(blockDiagramNew, arrowsNew, textNew)
        self.play(ReplacementTransform(VGroup(blockDiagram, lines, arrows, feedbackLoop, texts, signs), simplifiedBlock))
        self.wait(1.0)
        self.play(FadeOut(transferFunction[6]), simplifiedBlock.animate.shift(0.75 * UP))
        self.wait(1.5)

        routhTable = MathTable(
            [
                ["s^{3}", 1, 31, 0, 0],
                ["s^{2}", 10, 1030, 0, 0],
                ["s^{1}", "a_{31}", "a_{32}", "a_{33}", 0],
                ["s^{0}", "a_{41}", "a_{42}", "a_{43}", 0],
            ]
        )
        routhTable.next_to(simplifiedBlock, DOWN, MED_LARGE_BUFF)
        self.play(Create(routhTable))
        self.play(routhTable.animate.shift(3.0 * LEFT))
        self.wait(1.5)

        arrows = VGroup(
            Arrow(routhTable.get_cell((2,2)).get_corner(DL), routhTable.get_cell((2,2)).get_corner(UR), color=BLUE),
            Arrow(routhTable.get_cell((2,3)).get_corner(DL), routhTable.get_cell((2,3)).get_corner(UR), color=BLUE),
        )

        labels = VGroup(
            MathTex(r"1", font_size=36).next_to(arrows[0].get_corner(UR), UP, SMALL_BUFF),
            MathTex(r"103", font_size=36).next_to(arrows[1].get_corner(UR), UP, SMALL_BUFF),
        )

        self.play(Create(arrows[0]), Create(arrows[1]))
        self.wait(0.5)
        self.play(Write(labels[0]), Write(labels[1]))
        self.wait(1.0)
        self.play(FadeOut(arrows, labels))
        textReplace = VGroup(
            MathTex(r"1").move_to(routhTable.get_cell((2,2)), ORIGIN),
            MathTex(r"103").move_to(routhTable.get_cell((2,3)), ORIGIN),
        )
        
        self.play(ReplacementTransform(routhTable.get_entries((2, 2)), textReplace[0]),
                  ReplacementTransform(routhTable.get_entries((2, 3)), textReplace[1]))

        routhValues = VGroup(
            MathTex(r"a_{31} = \frac{-\begin{vmatrix} a_{4} & a_{2} \\ a_{3} & a_{1} \end{vmatrix}}{a_3}"),
            MathTex(r"a_{31} = \frac{-\begin{vmatrix} 1 & 1 \\ 31 & 103 \end{vmatrix}}{1}"),
            MathTex(r"a_{31} = -\frac{[(1)(103)]-[(1)(31)]}{1}", font_size=40),
            MathTex(r"a_{31} = -\frac{103-31}{1}"),
            MathTex(r"a_{31} = -\frac{72}{1}"),
            MathTex(r"a_{31} = -72"),
            MathTex(r"a_{32} = \frac{-\begin{vmatrix} a_{4} & 0 \\ a_{3} & 0 \end{vmatrix}}{a_3}"),
            MathTex(r"a_{32} = \frac{-\begin{vmatrix} 1 & 0 \\ 31 & 0 \end{vmatrix}}{1}"),
            MathTex(r"a_{32} = -\frac{[(1)(0)]-[(0)(31)]}{1}", font_size=40),
            MathTex(r"a_{32} = \frac{0-0}{1}"),
            MathTex(r"a_{32} = \frac{0}{1}"),
            MathTex(r"a_{32} = 0"),
            MathTex(r"a_{33} = \frac{-\begin{vmatrix} a_{4} & 0 \\ a_{3} & 0 \end{vmatrix}}{a_3}"),
            MathTex(r"a_{33} = \frac{-\begin{vmatrix} 1 & 0 \\ 31 & 0 \end{vmatrix}}{1}"),
            MathTex(r"a_{33} = -\frac{[(1)(0)]-[(0)(31)]}{1}", font_size=40),
            MathTex(r"a_{33} = \frac{0-0}{10}"),
            MathTex(r"a_{33} = \frac{0}{10}"),
            MathTex(r"a_{33} = 0"),
            MathTex(r"a_{41} = \frac{-\begin{vmatrix} a_{2} & a_{31} \\ a_{0} & a_{32} \end{vmatrix}}{a_{31}}"),
            MathTex(r"a_{41} = \frac{-\begin{vmatrix} 1 & 103 \\ -72 & 0 \end{vmatrix}}{-72}"),
            MathTex(r"a_{41} = -\frac{[(1)(0)]-[(103)(-72)]}{-72}", font_size=40),
            MathTex(r"a_{41} = -\frac{0+7416}{-72}"),
            MathTex(r"a_{41} = \frac{7416}{72}"),
            MathTex(r"a_{41} = 103"),
            MathTex(r"a_{42} = \frac{-\begin{vmatrix} a_{2} & a_{31} \\ 0 & 0 \end{vmatrix}}{a_{31}}"),
            MathTex(r"a_{42} = \frac{-\begin{vmatrix} 1 & 103 \\ 0 & 0 \end{vmatrix}}{-72}"),
            MathTex(r"a_{42} = -\frac{[(1)(0)]-[(103)(0)]}{-72}", font_size=40),
            MathTex(r"a_{42} = \frac{0-0}{72}"),
            MathTex(r"a_{42} = \frac{0}{72}"),
            MathTex(r"a_{42} = 0"),
            MathTex(r"a_{43} = \frac{-\begin{vmatrix} a_{2} & a_{31} \\ 0 & 0 \end{vmatrix}}{a_{31}}"),
            MathTex(r"a_{43} = \frac{-\begin{vmatrix} 1 & 103 \\ 0 & 0 \end{vmatrix}}{-72}"),
            MathTex(r"a_{43} = -\frac{[(1)(0)]-[(103)(0)]}{-72}", font_size=40),
            MathTex(r"a_{43} = \frac{0-0}{72}"),
            MathTex(r"a_{43} = \frac{0}{72}"),
            MathTex(r"a_{43} = 0"),
        )

        routhValues.move_to(routhTable.get_right() + 3.5 * RIGHT)

        highlight = VGroup(
            SurroundingRectangle(VGroup(routhTable.get_cell((1, 2)), routhTable.get_cell((2, 2))), color=YELLOW),
            SurroundingRectangle(VGroup(routhTable.get_cell((1, 3)), routhTable.get_cell((2, 3))), color=YELLOW),
            SurroundingRectangle(routhTable.get_cell((3,2)), color=BLUE)
        )

        self.play(FadeIn(highlight))       
        self.play(Write(routhValues[0]))
        for i in range(1, 6):
            self.play(ReplacementTransform(routhValues[i-1], routhValues[i]))
            self.wait(0.5)
        
        self.play(ReplacementTransform(routhTable.get_entries((3, 2)), MathTex(r"-72", color=YELLOW).move_to(routhTable.get_cell((3, 2)), ORIGIN)))
        self.wait(1.0)
        self.play(FadeOut(routhValues[5]))
        self.wait(0.5)

        self.play(highlight[1].animate.shift(2.1 * RIGHT),
                  highlight[2].animate.shift(2.075  * RIGHT))
        self.play(Write(routhValues[6]))
        for i in range(7, 12):
            self.play(ReplacementTransform(routhValues[i-1], routhValues[i]))
            self.wait(0.5)

        self.play(ReplacementTransform(routhTable.get_entries((3, 3)), MathTex(r"0", color=YELLOW).move_to(routhTable.get_cell((3, 3)), ORIGIN)))
        self.wait(1.0)        
        self.play(FadeOut(routhValues[11]))
        self.wait(0.5)

        self.play(highlight[1].animate.shift(RIGHT * 1.75),
                  highlight[2].animate.shift(RIGHT * 2.1))
        self.play(Write(routhValues[12]))
        for i in range(13, 18):
            self.play(ReplacementTransform(routhValues[i-1], routhValues[i]))
            self.wait(0.5)

        self.play(ReplacementTransform(routhTable.get_entries((3, 4)), MathTex(r"0", color=YELLOW).move_to(routhTable.get_cell((3, 4)), ORIGIN)))
        self.wait(0.5)        
        self.play(FadeOut(routhValues[17]))
        self.wait(0.5)
        self.play(highlight[2].animate.shift(4.175 * LEFT + 1.225 * DOWN),
                  highlight[0].animate.shift(1.225 * DOWN),
                  highlight[1].animate.shift(3.85 * LEFT + 1.225 * DOWN))
        
        self.wait(1.0)
        self.play(Write(routhValues[18]))
        for i in range(19, 24):
            self.play(ReplacementTransform(routhValues[i-1], routhValues[i]))
            self.wait(0.5)
        
        self.play(ReplacementTransform(routhTable.get_entries((4, 2)), MathTex(r"103", color=YELLOW).move_to(routhTable.get_cell((4, 2)), ORIGIN)))
        self.wait(1.0)
        self.play(FadeOut(routhValues[23]))
        self.wait(0.5)

        self.play(highlight[1].animate.shift(2.1 * RIGHT),
                  highlight[2].animate.shift(2.075  * RIGHT))
        self.play(Write(routhValues[24]))
        for i in range(25, 30):
            self.play(ReplacementTransform(routhValues[i-1], routhValues[i]))
            self.wait(0.5)

        self.play(ReplacementTransform(routhTable.get_entries((4, 3)), MathTex(r"0", color=YELLOW).move_to(routhTable.get_cell((4, 3)), ORIGIN)))
        self.wait(1.0)        
        self.play(FadeOut(routhValues[29]))
        self.wait(0.5)

        self.play(highlight[1].animate.shift(RIGHT * 1.75),
                  highlight[2].animate.shift(RIGHT * 2.1))
        self.play(Write(routhValues[31]))
        for i in range(32, 36):
            self.play(ReplacementTransform(routhValues[i-1], routhValues[i]))
            self.wait(0.5)

        self.play(ReplacementTransform(routhTable.get_entries((4, 4)), MathTex(r"0", color=YELLOW).move_to(routhTable.get_cell((4, 4)), ORIGIN)))
        self.wait(0.5)        
        self.play(FadeOut(routhValues[35]), FadeOut(highlight))
        self.wait(0.25)
        self.play(routhTable.animate.shift(3.0 * RIGHT))
        self.wait(2.0)
        self.play(FadeOut(routhTable, simplifiedBlock))
        return super().construct()
