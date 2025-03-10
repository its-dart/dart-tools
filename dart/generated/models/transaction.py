from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_kind import TransactionKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation import Operation


T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """
    Attributes:
        kind (TransactionKind): * `brainstorm_create` - BRAINSTORM_CREATE
            * `brainstorm_delete` - BRAINSTORM_DELETE
            * `brainstorm_update` - BRAINSTORM_UPDATE
            * `comment_create` - COMMENT_CREATE
            * `comment_update` - COMMENT_UPDATE
            * `comment_delete` - COMMENT_DELETE
            * `comment_reaction_create` - COMMENT_REACTION_CREATE
            * `comment_reaction_delete` - COMMENT_REACTION_DELETE
            * `sprint_rollover` - SPRINT_ROLLOVER
            * `undo_sprint_rollover` - UNDO_SPRINT_ROLLOVER
            * `dartboard_create` - DARTBOARD_CREATE
            * `dartboard_delete` - DARTBOARD_DELETE
            * `dartboard_update` - DARTBOARD_UPDATE
            * `dashboard_create` - DASHBOARD_CREATE
            * `dashboard_delete` - DASHBOARD_DELETE
            * `dashboard_update` - DASHBOARD_UPDATE
            * `doc_create` - DOC_CREATE
            * `doc_delete` - DOC_DELETE
            * `doc_update` - DOC_UPDATE
            * `event_create` - EVENT_CREATE
            * `folder_create` - FOLDER_CREATE
            * `folder_delete` - FOLDER_DELETE
            * `folder_update` - FOLDER_UPDATE
            * `form_create` - FORM_CREATE
            * `form_delete` - FORM_DELETE
            * `form_update` - FORM_UPDATE
            * `layout_create` - LAYOUT_CREATE
            * `layout_delete` - LAYOUT_DELETE
            * `layout_update` - LAYOUT_UPDATE
            * `notification_update` - NOTIFICATION_UPDATE
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
            * `task_kind_create` - TASK_KIND_CREATE
            * `task_kind_delete` - TASK_KIND_DELETE
            * `task_kind_update` - TASK_KIND_UPDATE
            * `tenant_update` - TENANT_UPDATE
            * `user_dartboard_layout_create` - USER_DARTBOARD_LAYOUT_CREATE
            * `user_dartboard_layout_delete` - USER_DARTBOARD_LAYOUT_DELETE
            * `user_dartboard_layout_update` - USER_DARTBOARD_LAYOUT_UPDATE
            * `user_update` - USER_UPDATE
            * `view_create` - VIEW_CREATE
            * `view_delete` - VIEW_DELETE
            * `view_update` - VIEW_UPDATE
            * `webhook_create` - WEBHOOK_CREATE
            * `webhook_delete` - WEBHOOK_DELETE
            * `webhook_update` - WEBHOOK_UPDATE
        operations (List['Operation']):
        duid (Union[Unset, str]):
    """

    kind: TransactionKind
    operations: List["Operation"]
    duid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind.value

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)

        duid = self.duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "operations": operations,
            }
        )
        if duid is not UNSET:
            field_dict["duid"] = duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operation import Operation

        d = src_dict.copy()
        kind = TransactionKind(d.pop("kind"))

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = Operation.from_dict(operations_item_data)

            operations.append(operations_item)

        duid = d.pop("duid", UNSET)

        transaction = cls(
            kind=kind,
            operations=operations,
            duid=duid,
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
