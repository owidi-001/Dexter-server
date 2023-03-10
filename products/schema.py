import coreschema
from rest_framework.schemas import AutoSchema
import coreapi


class ProductSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.upper() == "POST":
            extra_fields = [
                coreapi.Field("name", required=True, location="form",
                              schema=coreschema.String( description="Product name is required")),
                coreapi.Field("price",  location="form", example="KSH 300",
                              schema=coreschema.Number( description="Product price is required")),

                coreapi.Field("quantity", required=False, location="form", example="2",
                              schema=coreschema.Integer( description="Enter quantity in stock")),

                coreapi.Field("minQuantity", required=False, location="form", example="2",
                              schema=coreschema.Integer( description="Enter minimum acceptable stock")),

                coreapi.Field("type",  location="form",
                              schema=coreschema.String( description="type"))
            ]

            if method.upper() == "PUT":
                extra_fields = [
                    coreapi.Field("name", required=True, location="form",
                              schema=coreschema.Object(required=True, description="Product name is required")),
                coreapi.Field("price", required=True, location="form", example="20.99",
                              schema=coreschema.Object(required=True, description="Product price is required")),
                coreapi.Field("quantity", required=False, location="form", example="2",
                              schema=coreschema.Object(required=True, description="Enter quantity in stock")),
                            coreapi.Field("minQuantity", required=False, location="form", example="2",
                              schema=coreschema.Object(required=True, description="Enter minimum acceptable stock")),
                coreapi.Field("category", required=True, location="form",
                              schema=coreschema.Object(required=True, description="Category"))
                ]
            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields