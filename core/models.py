from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class FloodEvent(models.Model):
    TYPE_CHOICES = [
        ('river', _('River Flood')),
        ('flash', _('Flash Flood')),
        ('coastal', _('Coastal Flood')),
        ('other', _('Other')),
    ]

    CAUSE_CHOICES = [
        ('rain', _('Heavy Rain')),
        ('dam_break', _('Dam Break')),
        ('storm_surge', _('Storm Surge')),
        ('snowmelt', _('Snowmelt')),
        ('other', _('Other')),
    ]

    SEVERITY_CHOICES = [
        ('minor', _('Minor')),
        ('moderate', _('Moderate')),
        ('major', _('Major')),
    ]

    VALIDATION_STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('rejected', _('Rejected')),
    ]

    location = models.PointField(geography=True, help_text=_(
        "This should be the points where the flood was first detected or the most significantly impacted locations."))
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    cause = models.CharField(max_length=20, choices=CAUSE_CHOICES)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)

    # Impact Data
    affected_area = models.PolygonField(
        geography=True, null=True, blank=True, help_text=_("Specify area of the affected area."))
    affected_area_km2 = models.FloatField(validators=[MinValueValidator(
        0)], null=True, blank=True, help_text=_("Total area affected (in square kilometers)"))
    population_affected = models.PositiveIntegerField(
        null=True, blank=True, help_text=_("Number of people affected"))
    injuries = models.PositiveIntegerField(
        null=True, blank=True, help_text=_("Number of injuries"))
    fatalities = models.PositiveIntegerField(
        null=True, blank=True, help_text=_("Number of fatalities"))
    property_damage_local_currency = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=2, help_text=_("Estimated cost of damage in local currency"))
    property_damage_usd = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=2, help_text=_("Estimated cost of damage in USD"))
    property_types_damaged = models.JSONField(null=True, blank=True, help_text=_(
        "Types of property damaged (e.g., residential, commercial, agricultural)"))

    # Infrastructure Damage
    transportation_impact = models.TextField(
        null=True, blank=True, help_text=_("Impact on transportation (roads, bridges)"))
    utilities_impact = models.TextField(null=True, blank=True, help_text=_(
        "Impact on utilities (water supply, electricity)"))

    # Environmental Impact
    ecosystem_impact = models.TextField(null=True, blank=True, help_text=_(
        "Effects on local ecosystems and wildlife"))
    water_contamination_details = models.TextField(
        null=True, blank=True, help_text=_("Details about water contamination"))

    # Response and Recovery
    emergency_response = models.JSONField(null=True, blank=True, help_text=_(
        "Agencies involved in the response and number of rescue operations conducted"))
    evacuations = models.JSONField(null=True, blank=True, help_text=_(
        "Number of people evacuated and details of evacuation centers and shelters"))
    relief_measures = models.JSONField(null=True, blank=True, help_text=_(
        "Aid provided (food, water, medical assistance) and support from government and NGOs"))

    # Data Sources
    primary_data_sources = models.JSONField(null=True, blank=True, help_text=_(
        "Government reports, meteorological agencies, satellite data"))
    secondary_data_sources = models.JSONField(null=True, blank=True, help_text=_(
        "News articles, social media reports, eyewitness accounts"))

    validation_status = models.CharField(
        max_length=10, choices=VALIDATION_STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(
        User, related_name='flood_events_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, related_name='flood_events_updated', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FloodEvent {self.id} at {self.location}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])

    class Meta:
        ordering = ['-start_datetime']
        verbose_name = _("Flood Event")
        verbose_name_plural = _("Flood Events")
