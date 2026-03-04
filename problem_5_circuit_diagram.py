import schemdraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use('Agg')


with schemdraw.Drawing() as d:
    elm.Inductor2().label(r'$0.5\,\mathrm{H}$')
    elm.Resistor().down().label(r'$10\,\Omega$')
    elm.Line().left()
    elm.SourceSin().up().label(r'$3\sin{2t}\,\mathrm{V}$')
    d.draw()
    d.save('problem_5_circuit.svg')
