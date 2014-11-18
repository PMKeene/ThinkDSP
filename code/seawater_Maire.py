
import thinkdsp
import thinkplot
import math

def Underwater(wave, temp, depth):
	print("Who Would Do Such A Thing?")
	# extract a segment of that violin recording
	segment = wave.segment(0, 3)
	# make the spectrum
	spectrum = segment.make_spectrum()
	spectrum.plot()
	print(spectrum.hs)

	for i in xrange(len(spectrum.fs)):
		alpha=.00049*spectrum.fs[i]**2*math.exp(-temp/27-depth/17) #dB/km
		#attenuation factor at 1 km distance
		if alpha<9000: 
			attenuate=math.sqrt(10**(alpha/10))
			spectrum.amps[i]/=attenuate
		else:
			spectrum.amps[i]=0
		
	spectrum.plot()
	return spectrum.make_wave()

		
def main():
	print("A Stradavarius In Desperate Straits")
	# wave = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')
	# #thinkdsp.play_wave(filename='92002__jcveliz__violin-origional.wav')
	# T= 10 #Seawater temp in Celsius
	# D= 5.556*1/20 #km, 1/20 of a League under the ocean. It seemed appropriate.

	# Horror=Underwater(wave, T, D)
	# #Horror.normalize()
	# Horror.apodize()
	# Horror.write(filename='DesperateStraits.wav')

	thinkdsp.play_wave(filename='campfire-1.wav')

if __name__ == '__main__':
    main()