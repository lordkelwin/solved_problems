from manim import *


class GraphFollower(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range=[-20, 20], y_range=[-2, 2])
        graph = ax.plot(lambda x: np.sin(x)/x, color=BLUE, x_range=[-15, 0])
        graph_1 = ax.plot(lambda x: np.sin(x)/x, color=YELLOW, x_range=[-15, 15])

        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph_1.t_min, graph_1))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        dot_3 = Dot(ax.i2gp(graph_1.t_max, graph_1))

        self.add(ax, graph, graph_1, dot_1, dot_2, dot_3, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear, run_time=10))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
