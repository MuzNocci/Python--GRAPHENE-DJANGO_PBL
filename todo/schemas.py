import graphene
from graphene_django import DjangoObjectType
from todo.models import Todo



class TodoType(DjangoObjectType):

    class Meta:

        fields = '__all__'
        model = Todo


class Query(graphene.ObjectType):

    todo = graphene.Field(TodoType, id=graphene.Int())
    todos = graphene.List(TodoType)

    def resolve_todo(root, info, id):
        user = info.context.user
        return Todo.objects.get(id=id, user=user)
    

schema = graphene.Schema(query=Query)