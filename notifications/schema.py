from rest_framework.schemas import AutoSchema
import coreapi
import coreschema

class NotificationSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.upper() in ["PATCH","POST","PUT"]:
            extra_fields = [
                coreapi.Field(
                    "title", required=False, location="form", schema=coreschema.String()
                ),
                coreapi.Field(
                    "body",
                    required=False,
                    location="form",
                    schema=coreschema.String(
                        description="message content.",
                    ),
                )
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields