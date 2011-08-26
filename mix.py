class gasMix:
    n2Pressure = 0
    he2Pressure = 0
    o2Pressure = 0
    maxDepth = 0
    absolutePressure = 1
    waterVapourPressure = 0
    maxO2Pressure = 1.4
    
    def __init__ ( self, percentOfN2, percentOfHe2, percentOfO2 ):
        self.n2Pressure = self.calculatePartialPressureOfAGas(percentOfN2)
        self.he2Pressure =(percentOfHe2/100.00)*(self.absolutePressure-self.waterVapourPressure) 
        self.o2Pressure = (percentOfO2/100.00)*(self.absolutePressure-self.waterVapourPressure)
    
    def getMaxDepth ( self ):
        if self.o2Pressure == 0:
            self.o2Pressure = 1.4
        self.maxDepth =( (self.maxO2Pressure/self.o2Pressure)-self.absolutePressure)*10
        return self.maxDepth;
        
    def  calculatePartialPressureOfAGas( self, percentOfGas ):
        return (percentOfGas/100.00)*(self.absolutePressure-self.waterVapourPressure) 
        
    

myMix = gasMix(79,0,21)
print myMix.getMaxDepth()
