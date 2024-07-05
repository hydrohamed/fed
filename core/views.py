from django.shortcuts import render, get_object_or_404

from core.forms import FloodEventFilterForm
from .models import FloodEvent
from django.http import JsonResponse


def index(request):
    filter_form = FloodEventFilterForm(request.GET or None)
    flood_events = FloodEvent.objects.all()

    if filter_form.is_valid():
        if filter_form.cleaned_data['start_datetime_from']:
            flood_events = flood_events.filter(
                start_datetime__gte=filter_form.cleaned_data['start_datetime_from'])
        if filter_form.cleaned_data['start_datetime_to']:
            flood_events = flood_events.filter(
                start_datetime__lte=filter_form.cleaned_data['start_datetime_to'])
        if filter_form.cleaned_data['type']:
            flood_events = flood_events.filter(
                type=filter_form.cleaned_data['type'])
        if filter_form.cleaned_data['cause']:
            flood_events = flood_events.filter(
                cause=filter_form.cleaned_data['cause'])
        if filter_form.cleaned_data['severity']:
            flood_events = flood_events.filter(
                severity=filter_form.cleaned_data['severity'])

    context = {
        'filter_form': filter_form,
        'flood_events': flood_events,
    }
    return render(request, 'core/index.html', context)


def filtered_flood_events(request):
    filter_form = FloodEventFilterForm(request.GET or None)
    flood_events = FloodEvent.objects.all()

    if filter_form.is_valid():
        if filter_form.cleaned_data['start_datetime_from']:
            flood_events = flood_events.filter(
                start_datetime__gte=filter_form.cleaned_data['start_datetime_from'])
        if filter_form.cleaned_data['start_datetime_to']:
            flood_events = flood_events.filter(
                start_datetime__lte=filter_form.cleaned_data['start_datetime_to'])
        if filter_form.cleaned_data['type']:
            flood_events = flood_events.filter(
                type=filter_form.cleaned_data['type'])
        if filter_form.cleaned_data['cause']:
            flood_events = flood_events.filter(
                cause=filter_form.cleaned_data['cause'])
        if filter_form.cleaned_data['severity']:
            flood_events = flood_events.filter(
                severity=filter_form.cleaned_data['severity'])

    events = [{
        'id': event.id,
        'location': {'x': event.location.x, 'y': event.location.y},
        'start_date': event.start_datetime,
        'type': event.get_type_display(),
        'cause': event.get_cause_display(),
        'severity': event.get_severity_display(),
        'detail_url': event.get_absolute_url(),


    } for event in flood_events]

    return JsonResponse({'events': events})


def detail(request, pk):
    flood_event = get_object_or_404(FloodEvent, pk=pk)
    return render(request, 'core/detail.html', {'flood_event': flood_event})
