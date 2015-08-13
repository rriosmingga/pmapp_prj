from django.db import models

class Equipo(models.Model):
	name_text = models.CharField(max_length=50)
	def __str__(self):
		return self.name_text
		
class Partido(models.Model):
    team1 = models.ForeignKey(Equipo, related_name='local')
    team2 = models.ForeignKey(Equipo, related_name='visit')
    def __str__(self):
        return "%s vs %s" % (self.team1, self.team2)
	