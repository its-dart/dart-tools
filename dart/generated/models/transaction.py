from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_kind import TransactionKind

if TYPE_CHECKING:
    from ..models.operation import Operation


T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """
    Attributes:
        duid (str):
        kind (TransactionKind): * `comment_create` - COMMENT_CREATE
            * `comment_update` - COMMENT_UPDATE
            * `comment_delete` - COMMENT_DELETE
            * `comment_reaction_create` - COMMENT_REACTION_CREATE
            * `comment_reaction_delete` - COMMENT_REACTION_DELETE
            * `cycle_rollover` - CYCLE_ROLLOVER
            * `dartboard_create` - DARTBOARD_CREATE
            * `dartboard_delete` - DARTBOARD_DELETE
            * `dartboard_update` - DARTBOARD_UPDATE
            * `doc_create` - DOC_CREATE
            * `doc_delete` - DOC_DELETE
            * `doc_update` - DOC_UPDATE
            * `event_create` - EVENT_CREATE
            * `folder_create` - FOLDER_CREATE
            * `folder_delete` - FOLDER_DELETE
            * `folder_update` - FOLDER_UPDATE
            * `layout_create` - LAYOUT_CREATE
            * `layout_delete` - LAYOUT_DELETE
            * `layout_update` - LAYOUT_UPDATE
            * `option_create` - OPTION_CREATE
            * `option_delete` - OPTION_DELETE
            * `option_update` - OPTION_UPDATE
            * `property_create` - PROPERTY_CREATE
            * `property_update` - PROPERTY_UPDATE
            * `property_delete` - PROPERTY_DELETE
            * `relationship_create` - RELATIONSHIP_CREATE
            * `relationship_update` - RELATIONSHIP_UPDATE
            * `relationship_delete` - RELATIONSHIP_DELETE
            * `space_create` - SPACE_CREATE
            * `space_update_perms` - SPACE_UPDATE_PERMS
            * `space_update_other` - SPACE_UPDATE_OTHER
            * `space_delete` - SPACE_DELETE
            * `status_create` - STATUS_CREATE
            * `status_delete` - STATUS_DELETE
            * `status_update` - STATUS_UPDATE
            * `task_complete` - TASK_COMPLETE
            * `task_create` - TASK_CREATE
            * `task_delete` - TASK_DELETE
            * `task_rename` - TASK_RENAME
            * `task_update` - TASK_UPDATE
            * `task_doc_relationship_create` - TASK_DOC_RELATIONSHIP_CREATE
            * `task_doc_relationship_delete` - TASK_DOC_RELATIONSHIP_DELETE
            * `tenant_update` - TENANT_UPDATE
            * `user_dartboard_layout_create` - USER_DARTBOARD_LAYOUT_CREATE
            * `user_dartboard_layout_delete` - USER_DARTBOARD_LAYOUT_DELETE
            * `user_dartboard_layout_update` - USER_DARTBOARD_LAYOUT_UPDATE
            * `user_update` - USER_UPDATE
            * `view_create` - VIEW_CREATE
            * `view_delete` - VIEW_DELETE
            * `view_update` - VIEW_UPDATE
        operations (List['Operation']):
    """

    duid: str
    kind: TransactionKind
    operations: List["Operation"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        kind = self.kind.value

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()

            operations.append(operations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "kind": kind,
                "operations": operations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operation import Operation

        d = src_dict.copy()
        duid = d.pop("duid")

        kind = TransactionKind(d.pop("kind"))

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = Operation.from_dict(operations_item_data)

            operations.append(operations_item)

        transaction = cls(
            duid=duid,
            kind=kind,
            operations=operations,
        )

        transaction.additional_properties = d
        return transaction

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
