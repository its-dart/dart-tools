from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TaskDocRelationshipCreate")


@_attrs_define
class TaskDocRelationshipCreate:
    """
    Attributes:
        duid (str):
        task_duid (str):
        doc_duid (str):
    """

    duid: str
    task_duid: str
    doc_duid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        task_duid = self.task_duid

        doc_duid = self.doc_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "taskDuid": task_duid,
                "docDuid": doc_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        task_duid = d.pop("taskDuid")

        doc_duid = d.pop("docDuid")

        task_doc_relationship_create = cls(
            duid=duid,
            task_duid=task_duid,
            doc_duid=doc_duid,
        )

        task_doc_relationship_create.additional_properties = d
        return task_doc_relationship_create

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
