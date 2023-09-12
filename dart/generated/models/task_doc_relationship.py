from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskDocRelationship")


@_attrs_define
class TaskDocRelationship:
    """
    Attributes:
        duid (str):
        task_duid (str):
        doc_duid (str):
        updated_by_client_duid (Union[Unset, None, str]):
    """

    duid: str
    task_duid: str
    doc_duid: str
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        task_duid = self.task_duid
        doc_duid = self.doc_duid
        updated_by_client_duid = self.updated_by_client_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "taskDuid": task_duid,
                "docDuid": doc_duid,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        task_duid = d.pop("taskDuid")

        doc_duid = d.pop("docDuid")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        task_doc_relationship = cls(
            duid=duid,
            task_duid=task_duid,
            doc_duid=doc_duid,
            updated_by_client_duid=updated_by_client_duid,
        )

        task_doc_relationship.additional_properties = d
        return task_doc_relationship

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
