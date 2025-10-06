from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from adapters.controllers.graphql.bebida_resolver import query, mutation, BebidaGraphQLResolver

def create_graphql_app(
    obtener_bebidas_use_case,
    obtener_bebida_por_id_use_case, 
    crear_bebida_use_case
):
    # Cargar schema
    type_defs = load_schema_from_path("adapters/controllers/graphql/schema.graphql")
    
    # Configurar resolvers con dependencias inyectadas
    resolver = BebidaGraphQLResolver(
        obtener_bebidas_use_case=obtener_bebidas_use_case,
        obtener_bebida_por_id_use_case=obtener_bebida_por_id_use_case,
        crear_bebida_use_case=crear_bebida_use_case
    )
    
    # Crear schema ejecutable
    schema = make_executable_schema(type_defs, query, mutation)
    
    return GraphQL(schema, debug=True)