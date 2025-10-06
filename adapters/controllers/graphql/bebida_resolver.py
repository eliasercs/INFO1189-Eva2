from ariadne import ObjectType, convert_kwargs_to_snake_case
from adapters.presenters.graphql_presenter import GraphQLPresenter

query = ObjectType("Query")
mutation = ObjectType("Mutation")

class BebidaGraphQLResolver:
    def __init__(self, obtener_bebidas_use_case, obtener_bebida_por_id_use_case, crear_bebida_use_case):
        self.obtener_bebidas_use_case = obtener_bebidas_use_case
        self.obtener_bebida_por_id_use_case = obtener_bebida_por_id_use_case
        self.crear_bebida_use_case = crear_bebida_use_case
        self._setup_resolvers()
    
    def _setup_resolvers(self):
        query.set_field("bebidas", self.resolve_bebidas)
        query.set_field("bebida", self.resolve_bebida)
        mutation.set_field("createBebida", self.resolve_create_bebida)
    
    @convert_kwargs_to_snake_case
    def resolve_bebidas(self, *_) -> list:
        bebidas_data = self.obtener_bebidas_use_case.execute()
        # Convertir cada bebida a formato GraphQL
        return [GraphQLPresenter.present_bebida(bebida) for bebida in bebidas_data if bebida]
    
    @convert_kwargs_to_snake_case
    def resolve_bebida(self, _, info, id: int):
        try:
            bebida_data = self.obtener_bebida_por_id_use_case.execute(id)
            return GraphQLPresenter.present_bebida(bebida_data)
        except ValueError:
            return None
    
    @convert_kwargs_to_snake_case
    def resolve_create_bebida(self, _, info, input: dict):
        resultado = self.crear_bebida_use_case.execute(input)
        
        # ✅ Usar el presentador para manejar cualquier tipo de respuesta
        resultado_formateado = GraphQLPresenter.present_use_case_result(resultado)
        
        if not resultado_formateado["success"]:
            raise ValueError(resultado_formateado["msg"])
        
        return resultado_formateado["data"]