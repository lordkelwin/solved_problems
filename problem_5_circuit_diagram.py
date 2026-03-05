import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as d:
    d.config(unit=5)
    S1 = elm.SourceSin().label(r'$3\sin{2t}\,\mathrm{V}$', fontsize=20)
    L1 = elm.Inductor2().right().label(r'$0.5\,\mathrm{H}$', fontsize=20)
    R1 = elm.Resistor().down().label(r'$10\,\Omega$', fontsize=20, loc='bot')
    line_1 = elm.Line().tox(S1.start)
    elm.LoopCurrent([L1, R1, line_1, S1], pad=1).label(r'$i(t)$', fontsize=20)
    d.save('problem_5_circuit.svg')
