import thinkdsp
import thinkplot
import math
import numpy

PI2 = math.pi * 2

class SawtoothChirp(thinkdsp.Chirp):
	def evaluate(self, ts):
		"""Evaluates the signal at the given times.

		ts: float array of times
        
 		returns: float wave array
		"""
		freqs = numpy.linspace(self.start, self.end, len(ts)-1)
		return self._evaluate(ts, freqs)

	def _evaluate(self, ts, freqs):
		dts = numpy.diff(ts)
		dps = freqs * dts
		phases = numpy.cumsum(dps)
		phases = numpy.insert(phases, 0, 0)

		cycles = phases

		frac, _ = numpy.modf(cycles)
		ys = thinkdsp.normalize(thinkdsp.unbias(frac), self.amp)
		
		return ys


def main():

	Buzz=SawtoothChirp(start=440, end=880)
	BuzzWave=Buzz.make_wave()
	filename='BuzzCut'
	BuzzWave.write(filename)
	thinkdsp.play_wave(filename)
	BuzzCut=BuzzWave.segment()
	spectrum=BuzzCut.make_spectrum()
	spectrum.plot()


if __name__ == '__main__':
    main()
