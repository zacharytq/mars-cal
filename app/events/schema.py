from importlib.metadata import requires
import graphene
from graphene_django import DjangoObjectType
from .models import Event

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'start_date_time',
            'end_date_time',
            'created_date_time',
            'all_day',
            'location',
            'description',
        )


class UpdateEvent(graphene.Mutation):
    class Arguments:
        input = EventInput()
        id = graphene.ID()

    event = graphene.Field(EventType)

    @classmethod
    def mutate(cls, root, info, input, id):
        event = Event.objects.get(pk=id)
        event.title = input.title
        event.start_date_time = input.start_date_time
        event.end_date_time = input.end_date_time
        event.all_day = input.all_day
        event.location = input.location
        event.description = input.description
        event.save()
        return UpdateEvent(event=event)

class CreateEvent(graphene.Mutation):
    class Arguments:
        input = EventInput()
    
    event = graphene.Field(EventType)

    @classmethod
    def mutate(cls, root, info, input):
        event = Event()
        event.title = input.title
        event.start_date_time = input.start_date_time
        event.end_date_time = input.end_date_time
        event.all_day = input.all_day
        event.location = input.location
        event.description = input.description
        event.save()
        return CreateEvent(event=event)

class Mutation(graphene.ObjectType):
    update_event = UpdateEvent.Field()
    create_event = CreateEvent.Field()

class Query(graphene.ObjectType):
    events = graphene.List(EventType)

    def resolve_events(root, info, **kwargs):
        return Event.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)