from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_kind import OperationKind
from ..models.operation_model_kind import OperationModelKind

if TYPE_CHECKING:
    from ..models.comment_create import CommentCreate
    from ..models.comment_reaction_create import CommentReactionCreate
    from ..models.comment_reaction_update import CommentReactionUpdate
    from ..models.comment_update import CommentUpdate
    from ..models.dartboard_create import DartboardCreate
    from ..models.dartboard_update import DartboardUpdate
    from ..models.doc_create import DocCreate
    from ..models.doc_update import DocUpdate
    from ..models.event_create import EventCreate
    from ..models.event_subscription_create import EventSubscriptionCreate
    from ..models.event_subscription_update import EventSubscriptionUpdate
    from ..models.event_update import EventUpdate
    from ..models.folder_create import FolderCreate
    from ..models.folder_update import FolderUpdate
    from ..models.layout_create import LayoutCreate
    from ..models.layout_update import LayoutUpdate
    from ..models.option_create import OptionCreate
    from ..models.option_update import OptionUpdate
    from ..models.property_create import PropertyCreate
    from ..models.property_update import PropertyUpdate
    from ..models.relationship_create import RelationshipCreate
    from ..models.relationship_kind_create import RelationshipKindCreate
    from ..models.relationship_kind_update import RelationshipKindUpdate
    from ..models.relationship_update import RelationshipUpdate
    from ..models.space_create import SpaceCreate
    from ..models.space_update import SpaceUpdate
    from ..models.status_create import StatusCreate
    from ..models.status_update import StatusUpdate
    from ..models.task_attachment_create import TaskAttachmentCreate
    from ..models.task_attachment_update import TaskAttachmentUpdate
    from ..models.task_create import TaskCreate
    from ..models.task_doc_relationship_create import TaskDocRelationshipCreate
    from ..models.task_doc_relationship_update import TaskDocRelationshipUpdate
    from ..models.task_link_create import TaskLinkCreate
    from ..models.task_link_update import TaskLinkUpdate
    from ..models.task_update import TaskUpdate
    from ..models.tenant_create import TenantCreate
    from ..models.tenant_update import TenantUpdate
    from ..models.user_create import UserCreate
    from ..models.user_dartboard_layout_create import UserDartboardLayoutCreate
    from ..models.user_dartboard_layout_update import UserDartboardLayoutUpdate
    from ..models.user_update import UserUpdate
    from ..models.view_create import ViewCreate
    from ..models.view_update import ViewUpdate


T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """
    Attributes:
        kind (OperationKind): * `create` - CREATE
            * `delete` - DELETE
            * `update` - UPDATE
            * `update_list_add` - UPDATE_LIST_ADD
            * `update_list_remove` - UPDATE_LIST_REMOVE
        model (OperationModelKind): * `comment` - COMMENT
            * `comment_reaction` - COMMENT_REACTION
            * `dartboard` - DARTBOARD
            * `doc` - DOC
            * `event` - EVENT
            * `folder` - FOLDER
            * `layout` - LAYOUT
            * `event_subscription` - EVENT_SUBSCRIPTION
            * `option` - OPTION
            * `property` - PROPERTY
            * `relationship` - RELATIONSHIP
            * `relationship_kind` - RELATIONSHIP_KIND
            * `space` - SPACE
            * `status` - STATUS
            * `task` - TASK
            * `task_attachment` - TASK_ATTACHMENT
            * `task_doc_relationship` - TASK_DOC_RELATIONSHIP
            * `task_link` - TASK_LINK
            * `tenant` - TENANT
            * `user` - USER
            * `user_dartboard_layout` - USER_DARTBOARD_LAYOUT
            * `view` - VIEW
        data (Union['CommentCreate', 'CommentReactionCreate', 'CommentReactionUpdate', 'CommentUpdate',
            'DartboardCreate', 'DartboardUpdate', 'DocCreate', 'DocUpdate', 'EventCreate', 'EventSubscriptionCreate',
            'EventSubscriptionUpdate', 'EventUpdate', 'FolderCreate', 'FolderUpdate', 'LayoutCreate', 'LayoutUpdate',
            'OptionCreate', 'OptionUpdate', 'PropertyCreate', 'PropertyUpdate', 'RelationshipCreate',
            'RelationshipKindCreate', 'RelationshipKindUpdate', 'RelationshipUpdate', 'SpaceCreate', 'SpaceUpdate',
            'StatusCreate', 'StatusUpdate', 'TaskAttachmentCreate', 'TaskAttachmentUpdate', 'TaskCreate',
            'TaskDocRelationshipCreate', 'TaskDocRelationshipUpdate', 'TaskLinkCreate', 'TaskLinkUpdate', 'TaskUpdate',
            'TenantCreate', 'TenantUpdate', 'UserCreate', 'UserDartboardLayoutCreate', 'UserDartboardLayoutUpdate',
            'UserUpdate', 'ViewCreate', 'ViewUpdate']):
    """

    kind: OperationKind
    model: OperationModelKind
    data: Union[
        "CommentCreate",
        "CommentReactionCreate",
        "CommentReactionUpdate",
        "CommentUpdate",
        "DartboardCreate",
        "DartboardUpdate",
        "DocCreate",
        "DocUpdate",
        "EventCreate",
        "EventSubscriptionCreate",
        "EventSubscriptionUpdate",
        "EventUpdate",
        "FolderCreate",
        "FolderUpdate",
        "LayoutCreate",
        "LayoutUpdate",
        "OptionCreate",
        "OptionUpdate",
        "PropertyCreate",
        "PropertyUpdate",
        "RelationshipCreate",
        "RelationshipKindCreate",
        "RelationshipKindUpdate",
        "RelationshipUpdate",
        "SpaceCreate",
        "SpaceUpdate",
        "StatusCreate",
        "StatusUpdate",
        "TaskAttachmentCreate",
        "TaskAttachmentUpdate",
        "TaskCreate",
        "TaskDocRelationshipCreate",
        "TaskDocRelationshipUpdate",
        "TaskLinkCreate",
        "TaskLinkUpdate",
        "TaskUpdate",
        "TenantCreate",
        "TenantUpdate",
        "UserCreate",
        "UserDartboardLayoutCreate",
        "UserDartboardLayoutUpdate",
        "UserUpdate",
        "ViewCreate",
        "ViewUpdate",
    ]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.comment_create import CommentCreate
        from ..models.comment_reaction_create import CommentReactionCreate
        from ..models.comment_reaction_update import CommentReactionUpdate
        from ..models.comment_update import CommentUpdate
        from ..models.dartboard_create import DartboardCreate
        from ..models.dartboard_update import DartboardUpdate
        from ..models.doc_create import DocCreate
        from ..models.doc_update import DocUpdate
        from ..models.event_create import EventCreate
        from ..models.event_subscription_create import EventSubscriptionCreate
        from ..models.event_subscription_update import EventSubscriptionUpdate
        from ..models.event_update import EventUpdate
        from ..models.folder_create import FolderCreate
        from ..models.folder_update import FolderUpdate
        from ..models.layout_create import LayoutCreate
        from ..models.layout_update import LayoutUpdate
        from ..models.option_create import OptionCreate
        from ..models.option_update import OptionUpdate
        from ..models.property_create import PropertyCreate
        from ..models.property_update import PropertyUpdate
        from ..models.relationship_create import RelationshipCreate
        from ..models.relationship_kind_create import RelationshipKindCreate
        from ..models.relationship_kind_update import RelationshipKindUpdate
        from ..models.relationship_update import RelationshipUpdate
        from ..models.space_create import SpaceCreate
        from ..models.space_update import SpaceUpdate
        from ..models.status_create import StatusCreate
        from ..models.status_update import StatusUpdate
        from ..models.task_attachment_create import TaskAttachmentCreate
        from ..models.task_attachment_update import TaskAttachmentUpdate
        from ..models.task_create import TaskCreate
        from ..models.task_doc_relationship_create import TaskDocRelationshipCreate
        from ..models.task_doc_relationship_update import TaskDocRelationshipUpdate
        from ..models.task_link_create import TaskLinkCreate
        from ..models.task_link_update import TaskLinkUpdate
        from ..models.task_update import TaskUpdate
        from ..models.tenant_create import TenantCreate
        from ..models.tenant_update import TenantUpdate
        from ..models.user_create import UserCreate
        from ..models.user_dartboard_layout_create import UserDartboardLayoutCreate
        from ..models.user_dartboard_layout_update import UserDartboardLayoutUpdate
        from ..models.user_update import UserUpdate
        from ..models.view_create import ViewCreate

        kind = self.kind.value

        model = self.model.value

        data: Dict[str, Any]

        if isinstance(self.data, CommentCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, CommentUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, CommentReactionCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, CommentReactionUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, DartboardCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, DartboardUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, DocCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, DocUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, EventCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, EventUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, FolderCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, FolderUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, LayoutCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, LayoutUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, EventSubscriptionCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, EventSubscriptionUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, OptionCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, OptionUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, PropertyCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, PropertyUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, RelationshipCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, RelationshipUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, RelationshipKindCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, RelationshipKindUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, SpaceCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, SpaceUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, StatusCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, StatusUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, TaskCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, TaskUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, TaskAttachmentCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, TaskAttachmentUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, TaskDocRelationshipCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, TaskDocRelationshipUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, TaskLinkCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, TaskLinkUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, TenantCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, TenantUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, UserCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, UserUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, UserDartboardLayoutCreate):
            data = self.data.to_dict()

        elif isinstance(self.data, UserDartboardLayoutUpdate):
            data = self.data.to_dict()

        elif isinstance(self.data, ViewCreate):
            data = self.data.to_dict()

        else:
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "model": model,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_create import CommentCreate
        from ..models.comment_reaction_create import CommentReactionCreate
        from ..models.comment_reaction_update import CommentReactionUpdate
        from ..models.comment_update import CommentUpdate
        from ..models.dartboard_create import DartboardCreate
        from ..models.dartboard_update import DartboardUpdate
        from ..models.doc_create import DocCreate
        from ..models.doc_update import DocUpdate
        from ..models.event_create import EventCreate
        from ..models.event_subscription_create import EventSubscriptionCreate
        from ..models.event_subscription_update import EventSubscriptionUpdate
        from ..models.event_update import EventUpdate
        from ..models.folder_create import FolderCreate
        from ..models.folder_update import FolderUpdate
        from ..models.layout_create import LayoutCreate
        from ..models.layout_update import LayoutUpdate
        from ..models.option_create import OptionCreate
        from ..models.option_update import OptionUpdate
        from ..models.property_create import PropertyCreate
        from ..models.property_update import PropertyUpdate
        from ..models.relationship_create import RelationshipCreate
        from ..models.relationship_kind_create import RelationshipKindCreate
        from ..models.relationship_kind_update import RelationshipKindUpdate
        from ..models.relationship_update import RelationshipUpdate
        from ..models.space_create import SpaceCreate
        from ..models.space_update import SpaceUpdate
        from ..models.status_create import StatusCreate
        from ..models.status_update import StatusUpdate
        from ..models.task_attachment_create import TaskAttachmentCreate
        from ..models.task_attachment_update import TaskAttachmentUpdate
        from ..models.task_create import TaskCreate
        from ..models.task_doc_relationship_create import TaskDocRelationshipCreate
        from ..models.task_doc_relationship_update import TaskDocRelationshipUpdate
        from ..models.task_link_create import TaskLinkCreate
        from ..models.task_link_update import TaskLinkUpdate
        from ..models.task_update import TaskUpdate
        from ..models.tenant_create import TenantCreate
        from ..models.tenant_update import TenantUpdate
        from ..models.user_create import UserCreate
        from ..models.user_dartboard_layout_create import UserDartboardLayoutCreate
        from ..models.user_dartboard_layout_update import UserDartboardLayoutUpdate
        from ..models.user_update import UserUpdate
        from ..models.view_create import ViewCreate
        from ..models.view_update import ViewUpdate

        d = src_dict.copy()
        kind = OperationKind(d.pop("kind"))

        model = OperationModelKind(d.pop("model"))

        def _parse_data(
            data: object,
        ) -> Union[
            "CommentCreate",
            "CommentReactionCreate",
            "CommentReactionUpdate",
            "CommentUpdate",
            "DartboardCreate",
            "DartboardUpdate",
            "DocCreate",
            "DocUpdate",
            "EventCreate",
            "EventSubscriptionCreate",
            "EventSubscriptionUpdate",
            "EventUpdate",
            "FolderCreate",
            "FolderUpdate",
            "LayoutCreate",
            "LayoutUpdate",
            "OptionCreate",
            "OptionUpdate",
            "PropertyCreate",
            "PropertyUpdate",
            "RelationshipCreate",
            "RelationshipKindCreate",
            "RelationshipKindUpdate",
            "RelationshipUpdate",
            "SpaceCreate",
            "SpaceUpdate",
            "StatusCreate",
            "StatusUpdate",
            "TaskAttachmentCreate",
            "TaskAttachmentUpdate",
            "TaskCreate",
            "TaskDocRelationshipCreate",
            "TaskDocRelationshipUpdate",
            "TaskLinkCreate",
            "TaskLinkUpdate",
            "TaskUpdate",
            "TenantCreate",
            "TenantUpdate",
            "UserCreate",
            "UserDartboardLayoutCreate",
            "UserDartboardLayoutUpdate",
            "UserUpdate",
            "ViewCreate",
            "ViewUpdate",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_0 = CommentCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_1 = CommentUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_2 = CommentReactionCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_3 = CommentReactionUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_4 = DartboardCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_5 = DartboardUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_6 = DocCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_7 = DocUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_8 = EventCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_9 = EventUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_10 = FolderCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_11 = FolderUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_12 = LayoutCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_13 = LayoutUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_14 = EventSubscriptionCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_15 = EventSubscriptionUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_16 = OptionCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_17 = OptionUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_18 = PropertyCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_19 = PropertyUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_20 = RelationshipCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_21 = RelationshipUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_21
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_22 = RelationshipKindCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_22
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_23 = RelationshipKindUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_23
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_24 = SpaceCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_24
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_25 = SpaceUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_25
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_26 = StatusCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_26
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_27 = StatusUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_27
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_28 = TaskCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_28
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_29 = TaskUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_29
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_30 = TaskAttachmentCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_30
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_31 = TaskAttachmentUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_31
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_32 = TaskDocRelationshipCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_32
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_33 = TaskDocRelationshipUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_33
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_34 = TaskLinkCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_34
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_35 = TaskLinkUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_35
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_36 = TenantCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_36
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_37 = TenantUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_37
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_38 = UserCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_38
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_39 = UserUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_39
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_40 = UserDartboardLayoutCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_40
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_41 = UserDartboardLayoutUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_41
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_42 = ViewCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_42
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_operation_model_data_type_43 = ViewUpdate.from_dict(data)

            return componentsschemas_operation_model_data_type_43

        data = _parse_data(d.pop("data"))

        operation = cls(
            kind=kind,
            model=model,
            data=data,
        )

        operation.additional_properties = d
        return operation

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
