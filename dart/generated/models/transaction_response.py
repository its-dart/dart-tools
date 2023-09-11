from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.models_response import ModelsResponse


T = TypeVar("T", bound="TransactionResponse")


@_attrs_define
class TransactionResponse:
    """
    Attributes:
        duid (str):
        success (bool):
        message (str):
        models (ModelsResponse): This is a helper serializer for OpenAPI schema generation for all available models.
            E.g.:
            {
                "dartboards": [...],
                "layouts": [...],
                "relationships": [...],
                ...
                "views": [...],
            }
    """

    duid: str
    success: bool
    message: str
    models: "ModelsResponse"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        success = self.success
        message = self.message
        models = self.models.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "success": success,
                "message": message,
                "models": models,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.models_response import ModelsResponse

        d = src_dict.copy()
        duid = d.pop("duid")

        success = d.pop("success")

        message = d.pop("message")

        models = ModelsResponse.from_dict(d.pop("models"))

        transaction_response = cls(
            duid=duid,
            success=success,
            message=message,
            models=models,
        )

        transaction_response.additional_properties = d
        return transaction_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
