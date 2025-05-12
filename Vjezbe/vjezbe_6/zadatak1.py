from harmonijskioscilator import HarmonicOscillator


if __name__ == "__main__":
    oscilator = HarmonicOscillator(m=1.0, k=1.0, x0=1.0, v0=0.0, dt=0.01)
    oscilator.simulacija(t_max=20)
    oscilator.graf()
    period = oscilator.izracunaj_period()
    print('period oscilacije: ',period)
    
