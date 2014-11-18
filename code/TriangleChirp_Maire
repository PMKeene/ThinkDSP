import thinkdsp as dsp
import thinkplot
import math
import numpy

PI2 = math.pi * 2

class TriangleChirp(dsp.Chirp):

	def _evaluate(self, ts, freqs):
		dts = numpy.diff(ts)
		dps = PI2 * freqs * dts
		phases = numpy.cumsum(dps)
		phases = numpy.insert(phases, 0, 0)
		cycles=phases/PI2
		# cycles = self.freq * ts + self.offset / PI2
		frac, _ = numpy.modf(cycles)
		ys = numpy.abs(frac - 0.5)
		ys = dsp.normalize(dsp.unbias(ys), self.amp)
		return ys

def main():

	Mountains=TriangleChirp(start=440, end=880)
	MountianRange=Mountains.make_wave()
	filename='TriangleChirp'
	MountianRange.write(filename)
	dsp.play_wave(filename)

	# BuzzCut=BuzzWave.segment()
	# spectrum=BuzzCut.make_spectrum()
	# spectrum.plot()


if __name__ == '__main__':
    main()