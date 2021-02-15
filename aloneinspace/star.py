from body import Body


class Star(Body):
	def __init__(
		self,
		mass,
		r,
		g,
		color,
		has_atmosphere,
		surface_temp,
		atmosphere_temp=0,
		has_quakes=False
	):
		super().__init__(mass,r,g,color)
		self.has_atmosphere = has_atmosphere
		self.surface_temp = surface_temp
		self.atmosphere_temp = atmosphere_temp
		self.has_quakes = has_quakes