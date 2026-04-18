from manim import *


config.pixel_width = 1920
config.pixel_height = 1080


class ProblemStatement(Scene):
    def construct(self):
        statement = VGroup(
            Tex(r"\begin{minipage}{9cm}" \
            "Reduce the block diagram shown in the figure below to a single transfer function, $T(s)=C(s)/R(s)$. Use " \
            "Block Diagram Reduction method." \
            "\end{minipage}"
            )
        )

        statement.move_to(ORIGIN + UP * 2.5)
        self.play(Write(statement))

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
            Arrow([blockDiagram[1].get_left()[0]-1, blockDiagram[1].get_left()[1], 0], blockDiagram[1].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[1].get_right(), blockDiagram[0].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[0].get_right(), blockDiagram[2].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[2].get_right(), blockDiagram[3].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[3].get_right(), blockDiagram[4].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[4].get_right(), blockDiagram[5].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[5].get_right(), [blockDiagram[5].get_right()[0]+1, blockDiagram[5].get_right()[1], 0], color=YELLOW, buff=0),
        )

        arrowFeedback = VGroup(
            Line(arrows[4].get_center() + 0.2 * LEFT, [arrows[4].get_center()[0]-0.2, blockDiagram[6].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([arrows[4].get_center()[0]-0.19, blockDiagram[6].get_right()[1], 0], blockDiagram[6].get_right(), color=YELLOW, buff=0),
            Line(blockDiagram[6].get_left(), [blockDiagram[2].get_bottom()[0], blockDiagram[6].get_left()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([blockDiagram[2].get_bottom()[0], blockDiagram[6].get_left()[1], 0], blockDiagram[2].get_bottom(), color=YELLOW, buff=0,
                  stroke_width=6),
            Line(arrows[4].get_center() + 0.1 * RIGHT, [arrows[4].get_center()[0]+0.1, blockDiagram[7].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([arrows[4].get_center()[0]+0.09, blockDiagram[7].get_right()[1], 0], blockDiagram[7].get_left(), color=YELLOW, buff=0,
                  stroke_width=6),
            Line(blockDiagram[7].get_right(), [blockDiagram[5].get_bottom()[0], blockDiagram[7].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([blockDiagram[5].get_bottom()[0], blockDiagram[7].get_right()[1], 0], blockDiagram[5].get_bottom(), color=YELLOW, buff=0,
                  stroke_width=6),
            Line(arrows[6].get_center(), [arrows[6].get_center()[0], blockDiagram[7].get_bottom()[1]-0.25, 0], stroke_width=6, 
                 color=YELLOW),
            Line([arrows[6].get_center()[0], blockDiagram[7].get_bottom()[1]-0.25, 0], [blockDiagram[1].get_bottom()[0], blockDiagram[7].get_bottom()[1]-0.25, 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([blockDiagram[1].get_bottom()[0], blockDiagram[7].get_bottom()[1]-0.25, 0], blockDiagram[1].get_bottom(), color=YELLOW, buff=0,
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

        labels = VGroup(
            MathTex(r"R(s)", font_size=40).next_to(arrows[0].get_start(), UP, SMALL_BUFF),
            MathTex(r"+", font_size=35).next_to(arrows[0].get_end(), UP, MED_SMALL_BUFF),
            MathTex(r"+", font_size=35).next_to(arrows[2].get_end(), UP, MED_SMALL_BUFF),
            MathTex(r"+", font_size=35).next_to(arrows[5].get_end(), UP, MED_SMALL_BUFF),
            MathTex(r"C(s)", font_size=40).next_to(arrows[6].get_end(), UP, SMALL_BUFF),
            MathTex(r"-", font_size=35).next_to(arrowFeedback[3].get_end(), LEFT, MED_SMALL_BUFF),
            MathTex(r"-", font_size=35).next_to(arrowFeedback[7].get_end(), LEFT, MED_SMALL_BUFF),
            MathTex(r"-", font_size=35).next_to(arrowFeedback[10].get_end(), LEFT, MED_SMALL_BUFF),
        )

        self.play(Write(labels[0]))
        self.play(Create(arrows[0]))
        self.play(Write(labels[1]))
        self.play(Create(blockDiagram[1]), Create(lines[0]), Create(lines[1]))
        self.play(Create(arrows[1]))
        self.play(Create(blockDiagram[0]), Write(texts[0]))
        self.play(Create(arrows[2]))
        self.play(Write(labels[2]))
        self.play(Create(blockDiagram[2]), Create(lines[2]), Create(lines[3]))
        self.play(Create(arrows[3]))
        self.play(Create(blockDiagram[3]), Write(texts[1]))
        self.play(Create(arrows[4]))
        self.play(Create(blockDiagram[4]), Write(texts[2]))
        self.play(Create(arrows[5]))
        self.play(Write(labels[3]))
        self.play(Create(blockDiagram[5]), Create(lines[4]), Create(lines[5]))
        self.play(Create(arrows[6]))
        self.play(Write(labels[4]))
        self.play(Create(arrowFeedback[0]))
        self.play(Create(arrowFeedback[1]))
        self.play(Create(blockDiagram[6]), Write(texts[3].next_to(blockDiagram[6], ORIGIN)))
        self.play(Create(arrowFeedback[2]))
        self.play(Create(arrowFeedback[3]))
        self.play(Write(labels[5]))
        self.play(Create(arrowFeedback[4]))
        self.play(Create(arrowFeedback[5]))
        self.play(Create(blockDiagram[7]), Write(texts[4].move_to(blockDiagram[7], ORIGIN)))
        self.play(Create(arrowFeedback[6]))
        self.play(Create(arrowFeedback[7]))
        self.play(Write(labels[6]))
        self.play(Create(arrowFeedback[8]))
        self.play(Create(arrowFeedback[9]))
        self.play(Create(arrowFeedback[10]))
        self.play(Write(labels[7]))
        self.wait(2)
        self.play(FadeOut(statement, blockDiagram, arrowFeedback, texts, arrows, lines, labels))
        return super().construct()
    

class ProblemSolution(Scene):
    def construct(self):
        blockDiagram = VGroup(
            Rectangle(width=1.0, height=1.75).move_to(LEFT * 4 + UP * 2),
            Circle(radius=0.25, color=WHITE).move_to(LEFT * 6 + UP * 2),
            Circle(radius=0.25, color=WHITE).move_to(LEFT * 2 + UP * 2),
            Rectangle(width=2.0, height=1.75).move_to(RIGHT + UP * 2),
            Rectangle(width=1.0, height=1.75).move_to(RIGHT * 4 + UP * 2),
            Circle(radius=0.25, color=WHITE).move_to(RIGHT * 6 + UP * 2),
            Rectangle(width=1.0, height=1.75),
            Rectangle(width=1.0, height=1.75),
        )

        blockDiagram[6].move_to(blockDiagram[3], ORIGIN).shift(DOWN * 3)
        blockDiagram[7].move_to(blockDiagram[4], ORIGIN).shift(DOWN * 3 + RIGHT * 0.25)

        arrows = VGroup(
            Arrow([blockDiagram[1].get_left()[0]-1, blockDiagram[1].get_left()[1], 0], blockDiagram[1].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[1].get_right(), blockDiagram[0].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[0].get_right(), blockDiagram[2].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[2].get_right(), blockDiagram[3].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[3].get_right(), blockDiagram[4].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[4].get_right(), blockDiagram[5].get_left(), color=YELLOW, buff=0),
            Arrow(blockDiagram[5].get_right(), [blockDiagram[5].get_right()[0]+1, blockDiagram[5].get_right()[1], 0], color=YELLOW, buff=0),
        )

        arrowFeedback = VGroup(
            Line(arrows[4].get_center() + 0.2 * LEFT, [arrows[4].get_center()[0]-0.2, blockDiagram[6].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([arrows[4].get_center()[0]-0.19, blockDiagram[6].get_right()[1], 0], blockDiagram[6].get_right(), color=YELLOW, buff=0),
            Line(blockDiagram[6].get_left(), [blockDiagram[2].get_bottom()[0], blockDiagram[6].get_left()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([blockDiagram[2].get_bottom()[0], blockDiagram[6].get_left()[1], 0], blockDiagram[2].get_bottom(), color=YELLOW, buff=0,
                  stroke_width=6),
            Line(arrows[4].get_center() + 0.1 * RIGHT, [arrows[4].get_center()[0]+0.1, blockDiagram[7].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([arrows[4].get_center()[0]+0.09, blockDiagram[7].get_right()[1], 0], blockDiagram[7].get_left(), color=YELLOW, buff=0,
                  stroke_width=6),
            Line(blockDiagram[7].get_right(), [blockDiagram[5].get_bottom()[0], blockDiagram[7].get_right()[1], 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([blockDiagram[5].get_bottom()[0], blockDiagram[7].get_right()[1], 0], blockDiagram[5].get_bottom(), color=YELLOW, buff=0,
                  stroke_width=6),
            Line(arrows[6].get_center(), [arrows[6].get_center()[0], blockDiagram[7].get_bottom()[1]-0.25, 0], stroke_width=6, 
                 color=YELLOW),
            Line([arrows[6].get_center()[0], blockDiagram[7].get_bottom()[1]-0.25, 0], [blockDiagram[1].get_bottom()[0], blockDiagram[7].get_bottom()[1]-0.25, 0], stroke_width=6, 
                 color=YELLOW),
            Arrow([blockDiagram[1].get_bottom()[0], blockDiagram[7].get_bottom()[1]-0.25, 0], blockDiagram[1].get_bottom(), color=YELLOW, buff=0,
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
            MathTex(r"\frac{2}{s}").next_to(blockDiagram[6], ORIGIN),
            MathTex(r"2").next_to(blockDiagram[7], ORIGIN),
        )

        labels = VGroup(
            MathTex(r"R(s)", font_size=40).next_to(arrows[0].get_start(), UP, SMALL_BUFF),
            MathTex(r"+", font_size=35).next_to(arrows[0].get_end(), UP, MED_SMALL_BUFF),
            MathTex(r"+", font_size=35).next_to(arrows[2].get_end(), UP, MED_SMALL_BUFF),
            MathTex(r"+", font_size=35).next_to(arrows[5].get_end(), UP, MED_SMALL_BUFF),
            MathTex(r"C(s)", font_size=40).next_to(arrows[6].get_end(), UP, SMALL_BUFF),
            MathTex(r"-", font_size=35).next_to(arrowFeedback[3].get_end(), LEFT, MED_SMALL_BUFF),
            MathTex(r"-", font_size=35).next_to(arrowFeedback[7].get_end(), LEFT, MED_SMALL_BUFF),
            MathTex(r"-", font_size=35).next_to(arrowFeedback[10].get_end(), LEFT, MED_SMALL_BUFF),
        )
        self.play(FadeIn(blockDiagram, arrowFeedback, texts, arrows, lines, labels))

        surroundGroup = VGroup(
            texts[4].copy(), texts[2].copy(), blockDiagram[4:6].copy(), blockDiagram[7].copy(), labels[3].copy(), labels[6].copy(), arrowFeedback[4:8].copy(),
            arrows[5].copy(), lines[4:6].copy() 
        )

        box = SurroundingRectangle(surroundGroup, buff=0.25, color=BLUE)
        self.play(Create(box))
        self.wait(2)
        self.play(FadeOut(blockDiagram, arrowFeedback, texts, arrows, lines, labels, box))
        surroundGroup.add(arrows[4].copy())
        surroundGroup.add(arrows[6].copy())
        surroundGroup.add(labels[4].copy())
        tempLabel = MathTex(r"X_{1}(s)", font_size=40).next_to(arrows[4].get_start(), UP, SMALL_BUFF)
        surroundGroup.add(tempLabel)
        surroundGroup.move_to(ORIGIN + UP * 1)
        self.play(FadeIn(surroundGroup)) 
        self.wait(1.25)

        linesSolution = VGroup(
            MathTex(r"sX_{1}(s)-2X_{1}(s)=C(s)"),
            MathTex(r"(s-2)X_{1}(s)=C(s)")
        )

        linesSolution[0].next_to(surroundGroup, DOWN, MED_LARGE_BUFF)
        self.play(Write(linesSolution[0]))
        self.wait(0.3)
        self.play(ReplacementTransform(linesSolution[0], linesSolution[1].next_to(surroundGroup, DOWN, MED_LARGE_BUFF)))
        self.wait(1.25)

        soloBlock = Rectangle(width=1.5, height=1.75).move_to(UP * 1)

        newArrow = VGroup(
            Arrow([soloBlock.get_left()[0]-2.0, soloBlock.get_left()[1], 0], soloBlock.get_left(), color=YELLOW, buff=0),
            Arrow(soloBlock.get_right(), [soloBlock.get_right()[0]+2.0, soloBlock.get_right()[1], 0], color=YELLOW, buff=0)
        )

        newLabels = VGroup(
            MathTex(r"X_{1}(s)", font_size=40).next_to(newArrow[0].get_start(), UP, SMALL_BUFF),
            MathTex(r"C(s)", font_size=40).next_to(newArrow[1].get_end(), UP, SMALL_BUFF),
            MathTex(r"s-2").move_to(soloBlock, ORIGIN)
        )

        surroundGroupNew = VGroup(
            soloBlock, newArrow, newLabels
        )

        self.play(ReplacementTransform(surroundGroup, surroundGroupNew), linesSolution[1].animate.shift(UP))
        self.wait(2)
        self.play(FadeOut(surroundGroupNew, linesSolution[1]))
        self.play(FadeIn(blockDiagram, arrowFeedback, texts, arrows, lines, labels))

        blockReplacement = VGroup(
            Rectangle(width=1.5, height=1.75).move_to([blockDiagram[3].get_right()[0]+2.75, blockDiagram[3].get_right()[1], 0])
        )

        arrowReplacement =VGroup(
            Arrow(blockDiagram[3].get_right(), blockReplacement[0].get_left(), color=YELLOW, buff=0),
            Arrow(blockReplacement[0].get_right(), [blockReplacement[0].get_right()[0]+2.0, blockReplacement[0].get_right()[1], 0], color=YELLOW, buff=0)
        )

        labelReplacement = VGroup(
            MathTex(r"s-2").move_to(blockReplacement[0], ORIGIN)
        )

        self.play(ReplacementTransform(VGroup(texts[4], texts[2], blockDiagram[4:6], blockDiagram[7], labels[3], labels[6], arrowFeedback[4:8],
            arrows[4:7], lines[4:6]), VGroup(blockReplacement, arrowReplacement, labelReplacement)))
        
        self.wait(2)

        surroundGroup = VGroup(
            texts[1].copy(), texts[3].copy(), blockDiagram[2:4].copy(), blockDiagram[6].copy(), labels[2].copy(), labels[5].copy(), arrowFeedback[0:4].copy(),
            arrows[3].copy(), lines[2:4].copy() 
        )

        box = SurroundingRectangle(surroundGroup, buff=0.45, color=BLUE)
        self.play(Create(box))
        self.wait(2)
        surroundGroup.add(arrows[2].copy())
        surroundGroup.add(arrowReplacement[0].copy())
        tempLabel = VGroup(
            MathTex(r"X_{2}(s)", font_size=40).next_to(arrows[2].get_start(), UP, SMALL_BUFF),
            MathTex(r"X_{1}(s)", font_size=40).next_to(arrowReplacement[0].get_end(), UP, SMALL_BUFF)
        )
        surroundGroup.add(tempLabel)
        texts.remove(texts[2], texts[4])
        blockDiagram.remove(blockDiagram[4:6], blockDiagram[7])
        labels.remove(labels[3], labels[6])
        arrowFeedback.remove(arrowFeedback[4:8])
        arrows.remove(arrows[4:7])
        lines.remove(lines[2:4])
        self.play(FadeOut(blockDiagram, arrowFeedback, texts, arrows, lines, labels, box, VGroup(blockReplacement, arrowReplacement, labelReplacement)))
        surroundGroup.move_to(ORIGIN + UP * 1)
        self.play(FadeIn(surroundGroup)) 
        self.wait(1.25)

        linesSolution = VGroup(
            MathTex(r"\frac{X_{1}(s)}{X_{2}(s)}=\frac{G(s)}{1+G(s)H(s)}"),
            MathTex(r"\frac{X_{1}(s)}{X_{2}(s)}=\frac{\frac{50}{s+1}}{1+\left(\frac{50}{s+1}\right)\left(\frac{2}{s}\right)}"),
            MathTex(r"\frac{X_{1}(s)}{X_{2}(s)}=\frac{\frac{50}{s+1}}{1+\left(\frac{50}{s+1}\right)\left(\frac{2}{s}\right)} \times \frac{s(s+1)}{s(s+1)}"),
            MathTex(r"\frac{X_{1}(s)}{X_{2}(s)}=\frac{50s}{s(s+1)+100}"),
            MathTex(r"\frac{X_{1}(s)}{X_{2}(s)}=\frac{50s}{s^{2}+s+100}")
        )

        linesSolution[0].next_to(surroundGroup, DOWN, MED_LARGE_BUFF)
        self.play(Write(linesSolution[0]))
        self.wait(0.3)
        for i in range(1, len(linesSolution)):
            self.play(ReplacementTransform(linesSolution[i-1], linesSolution[i].next_to(surroundGroup, DOWN, MED_LARGE_BUFF)))
            self.wait(0.3)
        self.wait(1.25)
        soloBlock = Rectangle(width=3.25, height=1.75).move_to(UP * 1)
        newArrow = VGroup(
            Arrow([soloBlock.get_left()[0]-2.0, soloBlock.get_left()[1], 0], soloBlock.get_left(), color=YELLOW, buff=0),
            Arrow(soloBlock.get_right(), [soloBlock.get_right()[0]+2.0, soloBlock.get_right()[1], 0], color=YELLOW, buff=0)
        )
        newLabels = VGroup(
            MathTex(r"X_{2}(s)", font_size=40).next_to(newArrow[0].get_start(), UP, SMALL_BUFF),
            MathTex(r"X_{1}(s)", font_size=40).next_to(newArrow[1].get_end(), UP, SMALL_BUFF),
            MathTex(r"\frac{50s}{s^{2}+s+100}").move_to(soloBlock, ORIGIN)
        )
        surroundGroupNew = VGroup(
            soloBlock, newArrow, newLabels
        )
        self.play(ReplacementTransform(surroundGroup, surroundGroupNew), linesSolution[4].animate.shift(UP))
        self.wait(2)
        self.play(FadeOut(surroundGroupNew, linesSolution[4]))

        self.play(FadeIn(blockDiagram, arrowFeedback, texts, arrows, lines, labels, box, VGroup(blockReplacement, arrowReplacement, labelReplacement)))
        
        return super().construct()
