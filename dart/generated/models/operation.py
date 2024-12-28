from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_kind import OperationKind
from ..models.operation_model_kind import OperationModelKind

if TYPE_CHECKING:
    from ..models.attachment_create import AttachmentCreate
    from ..models.attachment_update import AttachmentUpdate
    from ..models.brainstorm_create import BrainstormCreate
    from ..models.brainstorm_update import BrainstormUpdate
    from ..models.comment_create import CommentCreate
    from ..models.comment_reaction_create import CommentReactionCreate
    from ..models.comment_reaction_update import CommentReactionUpdate
    from ..models.comment_update import CommentUpdate
    from ..models.dartboard_create import DartboardCreate
    from ..models.dartboard_update import DartboardUpdate
    from ..models.dashboard_create import DashboardCreate
    from ..models.dashboard_update import DashboardUpdate
    from ..models.doc_create import DocCreate
    from ..models.doc_update import DocUpdate
    from ..models.event_create import EventCreate
    from ..models.event_subscription_update import EventSubscriptionUpdate
    from ..models.folder_create import FolderCreate
    from ..models.folder_update import FolderUpdate
    from ..models.form_create import FormCreate
    from ..models.form_field_create import FormFieldCreate
    from ..models.form_field_update import FormFieldUpdate
    from ..models.form_update import FormUpdate
    from ..models.layout_create import LayoutCreate
    from ..models.layout_update import LayoutUpdate
    from ..models.notification_update import NotificationUpdate
    from ..models.option_create import OptionCreate
    from ..models.option_update import OptionUpdate
    from ..models.property_create import PropertyCreate
    from ..models.property_update import PropertyUpdate
    from ..models.relationship_create import RelationshipCreate
    from ..models.relationship_kind_create import RelationshipKindCreate
    from ..models.relationship_kind_update import RelationshipKindUpdate
    from ..models.space_create import SpaceCreate
    from ..models.space_update import SpaceUpdate
    from ..models.status_create import StatusCreate
    from ..models.status_update import StatusUpdate
    from ..models.task_create import TaskCreate
    from ..models.task_doc_relationship_create import TaskDocRelationshipCreate
    from ..models.task_kind_create import TaskKindCreate
    from ..models.task_kind_update import TaskKindUpdate
    from ..models.task_link_create import TaskLinkCreate
    from ..models.task_link_update import TaskLinkUpdate
    from ..models.task_update import TaskUpdate
    from ..models.tenant_update import TenantUpdate
    from ..models.user_dartboard_layout_create import UserDartboardLayoutCreate
    from ..models.user_update import UserUpdate
    from ..models.view_create import ViewCreate
    from ..models.view_update import ViewUpdate
    from ..models.webhook_create import WebhookCreate
    from ..models.webhook_update import WebhookUpdate


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
        model (OperationModelKind): * `attachment` - ATTACHMENT
            * `brainstorm` - BRAINSTORM
            * `comment` - COMMENT
            * `comment_reaction` - COMMENT_REACTION
            * `dartboard` - DARTBOARD
            * `dashboard` - DASHBOARD
            * `doc` - DOC
            * `event` - EVENT
            * `event_subscription` - EVENT_SUBSCRIPTION
            * `folder` - FOLDER
            * `form` - FORM
            * `form_field` - FORM_FIELD
            * `layout` - LAYOUT
            * `notification` - NOTIFICATION
            * `option` - OPTION
            * `property` - PROPERTY
            * `relationship` - RELATIONSHIP
            * `relationship_kind` - RELATIONSHIP_KIND
            * `space` - SPACE
            * `status` - STATUS
            * `task` - TASK
            * `task_doc_relationship` - TASK_DOC_RELATIONSHIP
            * `task_kind` - TASK_KIND
            * `task_link` - TASK_LINK
            * `tenant` - TENANT
            * `user` - USER
            * `user_dartboard_layout` - USER_DARTBOARD_LAYOUT
            * `view` - VIEW
            * `webhook` - WEBHOOK
        data (Union['AttachmentCreate', 'AttachmentUpdate', 'BrainstormCreate', 'BrainstormUpdate', 'CommentCreate',
            'CommentReactionCreate', 'CommentReactionUpdate', 'CommentUpdate', 'DartboardCreate', 'DartboardUpdate',
            'DashboardCreate', 'DashboardUpdate', 'DocCreate', 'DocUpdate', 'EventCreate', 'EventSubscriptionUpdate',
            'FolderCreate', 'FolderUpdate', 'FormCreate', 'FormFieldCreate', 'FormFieldUpdate', 'FormUpdate',
            'LayoutCreate', 'LayoutUpdate', 'NotificationUpdate', 'OptionCreate', 'OptionUpdate', 'PropertyCreate',
            'PropertyUpdate', 'RelationshipCreate', 'RelationshipKindCreate', 'RelationshipKindUpdate', 'SpaceCreate',
            'SpaceUpdate', 'StatusCreate', 'StatusUpdate', 'TaskCreate', 'TaskDocRelationshipCreate', 'TaskKindCreate',
            'TaskKindUpdate', 'TaskLinkCreate', 'TaskLinkUpdate', 'TaskUpdate', 'TenantUpdate', 'UserDartboardLayoutCreate',
            'UserUpdate', 'ViewCreate', 'ViewUpdate', 'WebhookCreate', 'WebhookUpdate']):
    """

    kind: OperationKind
    model: OperationModelKind
    data: Union[
        "AttachmentCreate",
        "AttachmentUpdate",
        "BrainstormCreate",
        "BrainstormUpdate",
        "CommentCreate",
        "CommentReactionCreate",
        "CommentReactionUpdate",
        "CommentUpdate",
        "DartboardCreate",
        "DartboardUpdate",
        "DashboardCreate",
        "DashboardUpdate",
        "DocCreate",
        "DocUpdate",
        "EventCreate",
        "EventSubscriptionUpdate",
        "FolderCreate",
        "FolderUpdate",
        "FormCreate",
        "FormFieldCreate",
        "FormFieldUpdate",
        "FormUpdate",
        "LayoutCreate",
        "LayoutUpdate",
        "NotificationUpdate",
        "OptionCreate",
        "OptionUpdate",
        "PropertyCreate",
        "PropertyUpdate",
        "RelationshipCreate",
        "RelationshipKindCreate",
        "RelationshipKindUpdate",
        "SpaceCreate",
        "SpaceUpdate",
        "StatusCreate",
        "StatusUpdate",
        "TaskCreate",
        "TaskDocRelationshipCreate",
        "TaskKindCreate",
        "TaskKindUpdate",
        "TaskLinkCreate",
        "TaskLinkUpdate",
        "TaskUpdate",
        "TenantUpdate",
        "UserDartboardLayoutCreate",
        "UserUpdate",
        "ViewCreate",
        "ViewUpdate",
        "WebhookCreate",
        "WebhookUpdate",
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attachment_create import AttachmentCreate
        from ..models.attachment_update import AttachmentUpdate
        from ..models.brainstorm_create import BrainstormCreate
        from ..models.brainstorm_update import BrainstormUpdate
        from ..models.comment_create import CommentCreate
        from ..models.comment_reaction_create import CommentReactionCreate
        from ..models.comment_reaction_update import CommentReactionUpdate
        from ..models.comment_update import CommentUpdate
        from ..models.dartboard_create import DartboardCreate
        from ..models.dartboard_update import DartboardUpdate
        from ..models.dashboard_create import DashboardCreate
        from ..models.dashboard_update import DashboardUpdate
        from ..models.doc_create import DocCreate
        from ..models.doc_update import DocUpdate
        from ..models.event_create import EventCreate
        from ..models.event_subscription_update import EventSubscriptionUpdate
        from ..models.folder_create import FolderCreate
        from ..models.folder_update import FolderUpdate
        from ..models.form_create import FormCreate
        from ..models.form_field_create import FormFieldCreate
        from ..models.form_field_update import FormFieldUpdate
        from ..models.form_update import FormUpdate
        from ..models.layout_create import LayoutCreate
        from ..models.layout_update import LayoutUpdate
        from ..models.notification_update import NotificationUpdate
        from ..models.option_create import OptionCreate
        from ..models.option_update import OptionUpdate
        from ..models.property_create import PropertyCreate
        from ..models.property_update import PropertyUpdate
        from ..models.relationship_create import RelationshipCreate
        from ..models.relationship_kind_create import RelationshipKindCreate
        from ..models.relationship_kind_update import RelationshipKindUpdate
        from ..models.space_create import SpaceCreate
        from ..models.space_update import SpaceUpdate
        from ..models.status_create import StatusCreate
        from ..models.status_update import StatusUpdate
        from ..models.task_create import TaskCreate
        from ..models.task_doc_relationship_create import TaskDocRelationshipCreate
        from ..models.task_kind_create import TaskKindCreate
        from ..models.task_kind_update import TaskKindUpdate
        from ..models.task_link_create import TaskLinkCreate
        from ..models.task_link_update import TaskLinkUpdate
        from ..models.task_update import TaskUpdate
        from ..models.tenant_update import TenantUpdate
        from ..models.user_dartboard_layout_create import UserDartboardLayoutCreate
        from ..models.user_update import UserUpdate
        from ..models.view_create import ViewCreate
        from ..models.view_update import ViewUpdate
        from ..models.webhook_create import WebhookCreate

        kind = self.kind.value

        model = self.model.value

        data: dict[str, Any]
        if isinstance(self.data, AttachmentCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, AttachmentUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, BrainstormCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, BrainstormUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, CommentCreate):
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
        elif isinstance(self.data, DashboardCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, DashboardUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, DocCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, DocUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, EventCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, EventSubscriptionUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, FolderCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, FolderUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, FormCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, FormUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, FormFieldCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, FormFieldUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, LayoutCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, LayoutUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, NotificationUpdate):
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
        elif isinstance(self.data, TaskDocRelationshipCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, TaskKindCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, TaskKindUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, TaskLinkCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, TaskLinkUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, TenantUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, UserUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, UserDartboardLayoutCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, ViewCreate):
            data = self.data.to_dict()
        elif isinstance(self.data, ViewUpdate):
            data = self.data.to_dict()
        elif isinstance(self.data, WebhookCreate):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.attachment_create import AttachmentCreate
        from ..models.attachment_update import AttachmentUpdate
        from ..models.brainstorm_create import BrainstormCreate
        from ..models.brainstorm_update import BrainstormUpdate
        from ..models.comment_create import CommentCreate
        from ..models.comment_reaction_create import CommentReactionCreate
        from ..models.comment_reaction_update import CommentReactionUpdate
        from ..models.comment_update import CommentUpdate
        from ..models.dartboard_create import DartboardCreate
        from ..models.dartboard_update import DartboardUpdate
        from ..models.dashboard_create import DashboardCreate
        from ..models.dashboard_update import DashboardUpdate
        from ..models.doc_create import DocCreate
        from ..models.doc_update import DocUpdate
        from ..models.event_create import EventCreate
        from ..models.event_subscription_update import EventSubscriptionUpdate
        from ..models.folder_create import FolderCreate
        from ..models.folder_update import FolderUpdate
        from ..models.form_create import FormCreate
        from ..models.form_field_create import FormFieldCreate
        from ..models.form_field_update import FormFieldUpdate
        from ..models.form_update import FormUpdate
        from ..models.layout_create import LayoutCreate
        from ..models.layout_update import LayoutUpdate
        from ..models.notification_update import NotificationUpdate
        from ..models.option_create import OptionCreate
        from ..models.option_update import OptionUpdate
        from ..models.property_create import PropertyCreate
        from ..models.property_update import PropertyUpdate
        from ..models.relationship_create import RelationshipCreate
        from ..models.relationship_kind_create import RelationshipKindCreate
        from ..models.relationship_kind_update import RelationshipKindUpdate
        from ..models.space_create import SpaceCreate
        from ..models.space_update import SpaceUpdate
        from ..models.status_create import StatusCreate
        from ..models.status_update import StatusUpdate
        from ..models.task_create import TaskCreate
        from ..models.task_doc_relationship_create import TaskDocRelationshipCreate
        from ..models.task_kind_create import TaskKindCreate
        from ..models.task_kind_update import TaskKindUpdate
        from ..models.task_link_create import TaskLinkCreate
        from ..models.task_link_update import TaskLinkUpdate
        from ..models.task_update import TaskUpdate
        from ..models.tenant_update import TenantUpdate
        from ..models.user_dartboard_layout_create import UserDartboardLayoutCreate
        from ..models.user_update import UserUpdate
        from ..models.view_create import ViewCreate
        from ..models.view_update import ViewUpdate
        from ..models.webhook_create import WebhookCreate
        from ..models.webhook_update import WebhookUpdate

        d = src_dict.copy()
        kind = OperationKind(d.pop("kind"))

        model = OperationModelKind(d.pop("model"))

        def _parse_data(
            data: object,
        ) -> Union[
            "AttachmentCreate",
            "AttachmentUpdate",
            "BrainstormCreate",
            "BrainstormUpdate",
            "CommentCreate",
            "CommentReactionCreate",
            "CommentReactionUpdate",
            "CommentUpdate",
            "DartboardCreate",
            "DartboardUpdate",
            "DashboardCreate",
            "DashboardUpdate",
            "DocCreate",
            "DocUpdate",
            "EventCreate",
            "EventSubscriptionUpdate",
            "FolderCreate",
            "FolderUpdate",
            "FormCreate",
            "FormFieldCreate",
            "FormFieldUpdate",
            "FormUpdate",
            "LayoutCreate",
            "LayoutUpdate",
            "NotificationUpdate",
            "OptionCreate",
            "OptionUpdate",
            "PropertyCreate",
            "PropertyUpdate",
            "RelationshipCreate",
            "RelationshipKindCreate",
            "RelationshipKindUpdate",
            "SpaceCreate",
            "SpaceUpdate",
            "StatusCreate",
            "StatusUpdate",
            "TaskCreate",
            "TaskDocRelationshipCreate",
            "TaskKindCreate",
            "TaskKindUpdate",
            "TaskLinkCreate",
            "TaskLinkUpdate",
            "TaskUpdate",
            "TenantUpdate",
            "UserDartboardLayoutCreate",
            "UserUpdate",
            "ViewCreate",
            "ViewUpdate",
            "WebhookCreate",
            "WebhookUpdate",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_0 = AttachmentCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_1 = AttachmentUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_2 = BrainstormCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_3 = BrainstormUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_4 = CommentCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_5 = CommentUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_6 = CommentReactionCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_7 = CommentReactionUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_8 = DartboardCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_9 = DartboardUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_10 = DashboardCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_11 = DashboardUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_12 = DocCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_13 = DocUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_14 = EventCreate.from_dict(data)

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
                componentsschemas_operation_model_data_type_16 = FolderCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_17 = FolderUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_18 = FormCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_19 = FormUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_20 = FormFieldCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_21 = FormFieldUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_21
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_22 = LayoutCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_22
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_23 = LayoutUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_23
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_24 = NotificationUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_24
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_25 = OptionCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_25
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_26 = OptionUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_26
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_27 = PropertyCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_27
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_28 = PropertyUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_28
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_29 = RelationshipCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_29
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_30 = RelationshipKindCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_30
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_31 = RelationshipKindUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_31
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_32 = SpaceCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_32
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_33 = SpaceUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_33
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_34 = StatusCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_34
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_35 = StatusUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_35
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_36 = TaskCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_36
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_37 = TaskUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_37
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_38 = TaskDocRelationshipCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_38
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_39 = TaskKindCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_39
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_40 = TaskKindUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_40
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_41 = TaskLinkCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_41
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_42 = TaskLinkUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_42
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_43 = TenantUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_43
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_44 = UserUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_44
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_45 = UserDartboardLayoutCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_45
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_46 = ViewCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_46
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_47 = ViewUpdate.from_dict(data)

                return componentsschemas_operation_model_data_type_47
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_model_data_type_48 = WebhookCreate.from_dict(data)

                return componentsschemas_operation_model_data_type_48
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_operation_model_data_type_49 = WebhookUpdate.from_dict(data)

            return componentsschemas_operation_model_data_type_49

        data = _parse_data(d.pop("data"))

        operation = cls(
            kind=kind,
            model=model,
            data=data,
        )

        operation.additional_properties = d
        return operation

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
