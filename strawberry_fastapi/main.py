import strawberry
from fastapi import FastAPI, Depends, Request, WebSocket, BackgroundTasks
from strawberry.fastapi import GraphQLRouter
from gql.schema import Query


def custom_context_dependency() -> str:
    return "John"


async def get_context(
    custom_value=Depends(custom_context_dependency),
):
    return {
        "custom_value": custom_value,
    }

schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")