from drf_spectacular.extensions import OpenApiAuthenticationExtension


class BearerTokenScheme(OpenApiAuthenticationExtension):
    
    priority = 1            # priority in relation to the other swagger auth schemes
    name = 'Bearer token'   # name used in the schema

    def get_security_definition(self, auto_schema):
        return {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
