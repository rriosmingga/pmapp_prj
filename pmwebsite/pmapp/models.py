from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
	name_text = models.CharField(max_length=50)
	def __str__(self):
		return self.name_text
		
class Partido(models.Model):
	team1 = models.ForeignKey(Equipo, related_name='local')
	team2 = models.ForeignKey(Equipo, related_name='visit')
	date = models.DateTimeField(null=True)
	gteam1 = models.SmallIntegerField(null=True, blank=True)
	gteam2 = models.SmallIntegerField(null=True, blank=True)
	definition = models.BooleanField(default=False)
	def __str__(self):
		return "%s vs %s" % (self.team1, self.team2)
	
class PartidoPronostico(models.Model):
	match = models.ForeignKey(Partido)
	user = models.ForeignKey(User)
	gteam1 = models.SmallIntegerField(null=True, blank=True)
	gteam2 = models.SmallIntegerField(null=True, blank=True)
	
	class Meta:
		unique_together = ("match", "user")
		
	def __str__(self):
		return "%s %s | %s - %s" % (self.user, self.match, self.gteam1, self.gteam2)
	