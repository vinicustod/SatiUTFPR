# -*- coding: utf-8 -*-
from sati.models import Person, Session, Participant, Event
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from sati.serializers import *
from django.db import Error


def confirm_participant(request):
    sessions = request.POST.get('sessions')
    user_id = request.POST.get('user_id')
    errors_array = []
    success_array = []
    has_error = False
    if sessions is not None:
        for session in sessions:
            participants = Participant.objects.filter(session_id=session.id, user_id=user_id)
            if get_session_available_spots(session.id) > 0:
                for participant in participants:
                    participant.is_confirmed = not participant.is_confirmed
                    try:
                        participant.save()
                        success_array.append(str(session.id))
                    except Error:
                        has_error = True
                        errors_array.append(str(session.id))
            else:
                errors_array.append('Turma cheia:' + str(session.id))
                has_error = True
        if has_error:
            return JsonResponse({
                'error': True,
                'error_messages': errors_array,
                'success_message': success_array,
            })
        else:
            return JsonResponse({
                'error': False,
                'success_message': success_array,
                'status': status.HTTP_100_CONTINUE
            })
    else:
        return JsonResponse({
            'error': True,
            'error_messages': ['ID da turma não encontrado'],
        })


def get_all_participants(request):
    events = Event.objects.all()

    events_array = []
    for event in events:
        sessions = Session.objects.filter(event_id=event.id)
        sessions_array = []
        for session in sessions:
            participants = Participant.objects.filter(session_id=session.id, status=True)
            participants_array = []
            for participant in participants:
                participants_array.append(create_participant_json(participant))

            sessions_array.append(create_session_json(session, participants_array))
        events_array.append(create_event_json(event, sessions_array))

    # print create_response('events', events_array, False, {})
    return JsonResponse(create_response('events', events_array, False, {}))


def create_response(response_key, response, error, error_messages):
    return{
        response_key: response,
        'error': error,
        'error_messages': error_messages,
        'status_code' : status.HTTP_100_CONTINUE,

    }


def create_event_json(event, sessions_array):
    return {
        'event_name': event.name,
        'event_fee': event.fee,
        'event_category': event.category.name,
        'sessions': sessions_array,
    }


def create_session_json(session, participant_array):
    occurrences = Occurrence.objects.filter(session_id=session.id)
    occurrences_array = []
    for occurrence in occurrences:
        occurrences_array.append(create_occurrence_json(occurrence))
    return {
        'session_instructor': session.instructor.name,
        'session_spots': session.spots,
        'session_spots_available': get_session_available_spots(session.id),
        'has_spots': get_session_available_spots(session.id) > 0,
        'occurrences': occurrences_array,
        'participants': participant_array,
    }


def create_occurrence_json(occurrence):
    return {
        'begin_date_time': occurrence.begin_date_time,
        'end_date_time': occurrence.end_date_time
    }


def create_participant_json(participant):
    return {
        'participant_id': participant.id,
        'participant_is_confirmed': participant.is_confirmed,
        'person_name': participant.person.name,
        'person_cpf': participant.person.cpf,
        'person_academic_registry': participant.person.academic_registry
    }


def get_session_available_spots(session_id):
    participants = Participant.objects.filter(is_confirmed=True, session_id=session_id)
    session = Session.objects.get(id=session_id)

    if session:
        available_spots = session.spots - len(participants)
        if available_spots > 0:
            response = available_spots
        else:
            response = 0
    else:
            response = 0

    return response


def session_available_spots(session_id):
    participants = Participant.objects.filter(is_confirmed=True, session_id=session_id)
    session = Session.objects.get(id=session_id)

    response = 0

    if session:
        available_spots_session = session.spots - len(participants)
        if available_spots_session > 0:
            response = available_spots_session

    return response


def event_available_spots(event_id):
    sessions = Session.objects.filter(event_id=event_id)

    response = 0

    if sessions:
        available_spots_event = 0
        for session in sessions:
            available_spots_event += session_available_spots(session.id)

        if event_available_spots > 0:
            response = available_spots_event

    return response

