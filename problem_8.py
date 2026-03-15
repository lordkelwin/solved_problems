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
            Tex("Convolution theorem can be used when finding the inverse Laplace Transform"),
            MathTex(r"\mathcal{L}^{-1}\{F(s)G(s)\}={f(t)}\ast{g(t)}=\int_{0}^{t}f(x)g{t-x}\,dx"),
            MathTex(r"\mathcal{L}^{-1}\bigg\{\frac{240}{(s^{2}+1)(s^{2}+25)\bigg\}=\mathcal{L}^{-1}\bigg\{48\times{"
                    r"\frac{1}{s^{2}+1}}\times{\frac{5}{s^{2}+25}}\bigg\}"),
            Tex("Where:"),
            MathTex(r"F(s)=\frac{1}{s^{2}+1}\\G(s)=\frac{5}{s^{2}+25}"),
            Tex("And their corresponding inverse Laplace Transforms:"),
            MathTex(r"f(t)=\sin{t}\\g(t)=\sin{5t}"),
            Tex("Solving for the Inverse Laplace Transform:"),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}\sin{x}\sin{5(t-x)}\,dx"),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}\sin{x}\sin{(5t-5x)}\,dx"),
            Tex(r"Using the identity:\\$\sin{(a-b)}=\sin{a}\cos{b}-\cos{a}\sin{b}$"),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}\sin{x}[\sin{(5t)}\cos{(5x)}-\cos{(5t)}\sin{(5x)}]\,dx"),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}[\sin{(5t)}\sin{x}\sin{(5x)}-\cos{(5t)}\sin{x}\sin{(5x)}]\,dx"),
            MathTex(r"f(t)\ast{g(t)} = \int_{0}^{t}\sin{(5t)}\sin{x}\sin{(5x)}\,dx - \int_{0}^{t}\cos{(5t)}\sin{"
                    r"x}\sin{(5x)}\,dx"),
            MathTex(r"f(t)\ast{g(t)} = \sin{(5t)}\int_{0}^{t}\sin{x}\cos{(5x)}\,dx - \cos{(5t)}\int_{0}^{t}\sin{"
                    r"x}\sin{(5x)}\,dx"),
            Tex(r"To simplify the integral, some identities are required:"),
            MathTex(r"\sin{a}\cos{b}=\frac{1}{2}[\sin{(a+b)}+\sin{(a-b)}]"),
            MathTex(r"\sin{a}\sin{b}=\frac{1}{2}[\cos{(a-b)}-\cos{(a+b)}]"),
            Tex("Applying the identities, we have:"),
            MathTex(r"\sin{x}\cos{(5x)}=\frac{1}{2}[\sin{(x+5x)}+\sin{(x-5x)}]"),
            MathTex(r"\sin{x}\cos{(5x)}=\frac{1}{2}[\sin{(6x)}+\sin{(-4x)}]"),
            Tex(r"Since $\sin{(-x)}=-\sin{x}$"),
            MathTex(r"\sin{x}\cos{(5x)}=\frac{1}{2}[\sin{(6x)}-\sin{(4x)}]"),
            MathTex(r"\sin{x}\sin{(5x)}=\frac{1}{2}[\cos{(x-5x)}-\cos{(x+5x)}]"),
            MathTex(r"\sin{x}\sin{(5x)}=\frac{1}{2}[\cos{(-4x)}-\cos{(6x)}]"),
            Tex(r"Since $\cos{(-x)}=\cos{x}$"),
            MathTex(r"\sin{x}\sin{(5x)}=\frac{1}{2}[\cos{(4x)}-\cos{(6x)}]"),
            Tex("Applying to the integral:"),
            MathTex(r"f(t)\ast{g(t)}=\sin{(5t)}\int_{0}^{t}\bigg[\frac{1}{2}(\sin{(6x)}-\sin{(4x)})\bigg]\,dx -"
                    r"\cos{(5t)}\int_{0}^{t}\bigg[\frac{1}{2}(\cos{(4x)}-\cos{(6x)})\bigg]\,dx"),
            Tex("Integrating:"),
            MathTex(r"f(t)\ast{g(t)}=\frac{\sin{(5t)}}{2}\left[-\frac{\cos{(6x)}}{6}+\frac{\cos{(4x)}}{4}\right]_{0}^"
                    r"{t} - \frac{\cos{(5t)}}{2}\left[\frac{\sin{(4x)}}{4}-\frac{\sin{(6x)}}{6}\right]_{0}^{t}"),
            MathTex(r"f(t)\ast{g(t)}=\frac{\sin{(5t)}}{2}\left[\left(\frac{\cos{(4t)}}{4}-\frac{\cos{(6t)}{6}\right)-"
                    r"\left(\frac{cos{0}}{4}-\frac{cos{0}}{6}\right)\right]-\frac{\cos{(5t)}}{2}\left[\left("
                    r"\frac{\sin{(4t)}}{4}-\frac{\sin{(6t)}}{6}\right)-\left(\frac{\sin{0}}{4}-\frac{\sin{0}}{6}"
                    r"\right)\right]"),
            MathTex(r"f(t)\ast{g(t)}=\frac{\sin{(5t)}}{2}\left[\frac{\cos{(4t)}}{4}-\frac{\cos{(6t)}}{6}-\frac{1}{4}+"
                    r"\frac{1}{6}\right]-\frac{\cos{(5t)}}{2}\left[\frac{\sin{(4t)}}{4}-\frac{\sin{(6t)}}{6}\right]"),
            MathTex(r"f(t)\ast{g(t)}=\frac{1}{8}\sin{(5t)}\cos{(4t)}-\frac{1}{12}\cos{(6t)}\sin{(5t)}-"
                    r"\frac{1}{12}\sin{(5t)}-\frac{1}{8}\cos{(5t)}\sin{(4t)}+\frac{1}{12}\sin{(6t)}\cos{(5t)}"),
            MathTex(r"f(t)\ast{g(t)}=\frac{1}{8}[\sin{(5t)}\cos{(4t)}-\cos{(5t)}\sin{(4t)}]-\frac{1}{12}[\sin{(6t)}"
                    r"\cos{(5t)}-\cos{(6t)}\sin{(5t)}]-\frac{1}{12}\sin{(5t)}"),
            Tex("To simplify, using a certain trigonometric identity:"),
            MathTex(r"\sin{(a-b)}=\sin{a}\cos{b}-\cos{a}\sin{b}"),
            Tex("Utilizing the identity to simplify:"),
            MathTex(r"f(t)\ast{g(t)}=\frac{1}{8}\sin{5t-4t}+\frac{1}{12}\sin{(6t-5t)-\frac{1}{12}\sin{(5t)}"),
            MathTex(r"f(t)\ast{g(t)}=\frac{1}{8}\sin{t}+\frac{1}{12}\sin{t}-\frac{1}{12}\sin{(5t)}"),
            MathTex(r"f(t)\ast{g(t)}=\left(\frac{1}{8}+\frac{1}{12}\right)\sin{t}-\frac{1}{12}\sin{(5t)}"),
            MathTex(r"f(t)\ast{g(t)}=\frac{5}{24}\sin{t}-\frac{1}{12}\sin{(5t)}"),
            Tex("Solving for the Inverse Laplace Transform:"),
            MathTex(r"\mathcal{L}^{-1}\left\{\frac{240}{(s^{2}+1)(s^{2}+25)}\right\}=48(f(t)\ast{g(t)})"),
            MathTex(r"\mathcal{L}^{-1}\left\{\frac{240}{(s^{2}+1)(s^{2}+25)}\right\}=48\left[\frac{5}{24}\sin{t}-"
                    r"\frac{1}{12}\sin{(5t)}\right]"),
            MathTex(r"\mathcal{L}^{-1}\left\{\frac{240}{(s^{2}+1)(s^{2}+25)}\right\}=10\sin{t}-2\sin{(5t)}")
        )
