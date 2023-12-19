from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment import Comment
    from ..models.comment_reaction import CommentReaction
    from ..models.dartboard import Dartboard
    from ..models.doc import Doc
    from ..models.event_subscription import EventSubscription
    from ..models.folder import Folder
    from ..models.form import Form
    from ..models.form_field import FormField
    from ..models.layout import Layout
    from ..models.option import Option
    from ..models.property_ import Property
    from ..models.relationship import Relationship
    from ..models.relationship_kind import RelationshipKind
    from ..models.space import Space
    from ..models.status import Status
    from ..models.task import Task
    from ..models.task_attachment import TaskAttachment
    from ..models.task_doc_relationship import TaskDocRelationship
    from ..models.task_link import TaskLink
    from ..models.tenant import Tenant
    from ..models.user import User
    from ..models.user_dartboard_layout import UserDartboardLayout
    from ..models.view import View


T = TypeVar("T", bound="PaginatedUserDataEntityList")


@_attrs_define
class PaginatedUserDataEntityList:
    """
    Attributes:
        count (Union[Unset, int]):  Example: 123.
        next_ (Union[Unset, None, str]):  Example: http://api.example.org/accounts/?offset=400&limit=100.
        previous (Union[Unset, None, str]):  Example: http://api.example.org/accounts/?offset=200&limit=100.
        results (Union[Unset, List[Union['Comment', 'CommentReaction', 'Dartboard', 'Doc', 'EventSubscription',
            'Folder', 'Form', 'FormField', 'Layout', 'Option', 'Property', 'Relationship', 'RelationshipKind', 'Space',
            'Status', 'Task', 'TaskAttachment', 'TaskDocRelationship', 'TaskLink', 'Tenant', 'User', 'UserDartboardLayout',
            'View']]]):
    """

    count: Union[Unset, int] = UNSET
    next_: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    results: Union[
        Unset,
        List[
            Union[
                "Comment",
                "CommentReaction",
                "Dartboard",
                "Doc",
                "EventSubscription",
                "Folder",
                "Form",
                "FormField",
                "Layout",
                "Option",
                "Property",
                "Relationship",
                "RelationshipKind",
                "Space",
                "Status",
                "Task",
                "TaskAttachment",
                "TaskDocRelationship",
                "TaskLink",
                "Tenant",
                "User",
                "UserDartboardLayout",
                "View",
            ]
        ],
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.comment import Comment
        from ..models.comment_reaction import CommentReaction
        from ..models.dartboard import Dartboard
        from ..models.doc import Doc
        from ..models.event_subscription import EventSubscription
        from ..models.folder import Folder
        from ..models.form import Form
        from ..models.form_field import FormField
        from ..models.layout import Layout
        from ..models.option import Option
        from ..models.property_ import Property
        from ..models.relationship import Relationship
        from ..models.relationship_kind import RelationshipKind
        from ..models.space import Space
        from ..models.status import Status
        from ..models.task import Task
        from ..models.task_attachment import TaskAttachment
        from ..models.task_doc_relationship import TaskDocRelationship
        from ..models.task_link import TaskLink
        from ..models.tenant import Tenant
        from ..models.user import User
        from ..models.user_dartboard_layout import UserDartboardLayout

        count = self.count
        next_ = self.next_
        previous = self.previous
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: Dict[str, Any]

                if isinstance(results_item_data, Comment):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, CommentReaction):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, User):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Dartboard):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Doc):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, EventSubscription):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Folder):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Form):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, FormField):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Layout):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Option):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Property):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Relationship):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, RelationshipKind):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Space):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Status):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Task):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, TaskAttachment):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, TaskDocRelationship):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, TaskLink):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, Tenant):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, UserDartboardLayout):
                    results_item = results_item_data.to_dict()

                else:
                    results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment import Comment
        from ..models.comment_reaction import CommentReaction
        from ..models.dartboard import Dartboard
        from ..models.doc import Doc
        from ..models.event_subscription import EventSubscription
        from ..models.folder import Folder
        from ..models.form import Form
        from ..models.form_field import FormField
        from ..models.layout import Layout
        from ..models.option import Option
        from ..models.property_ import Property
        from ..models.relationship import Relationship
        from ..models.relationship_kind import RelationshipKind
        from ..models.space import Space
        from ..models.status import Status
        from ..models.task import Task
        from ..models.task_attachment import TaskAttachment
        from ..models.task_doc_relationship import TaskDocRelationship
        from ..models.task_link import TaskLink
        from ..models.tenant import Tenant
        from ..models.user import User
        from ..models.user_dartboard_layout import UserDartboardLayout
        from ..models.view import View

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:

            def _parse_results_item(
                data: object,
            ) -> Union[
                "Comment",
                "CommentReaction",
                "Dartboard",
                "Doc",
                "EventSubscription",
                "Folder",
                "Form",
                "FormField",
                "Layout",
                "Option",
                "Property",
                "Relationship",
                "RelationshipKind",
                "Space",
                "Status",
                "Task",
                "TaskAttachment",
                "TaskDocRelationship",
                "TaskLink",
                "Tenant",
                "User",
                "UserDartboardLayout",
                "View",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_0 = Comment.from_dict(data)

                    return componentsschemas_user_data_entity_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_1 = CommentReaction.from_dict(data)

                    return componentsschemas_user_data_entity_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_2 = User.from_dict(data)

                    return componentsschemas_user_data_entity_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_3 = Dartboard.from_dict(data)

                    return componentsschemas_user_data_entity_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_4 = Doc.from_dict(data)

                    return componentsschemas_user_data_entity_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_5 = EventSubscription.from_dict(data)

                    return componentsschemas_user_data_entity_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_6 = Folder.from_dict(data)

                    return componentsschemas_user_data_entity_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_7 = Form.from_dict(data)

                    return componentsschemas_user_data_entity_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_8 = FormField.from_dict(data)

                    return componentsschemas_user_data_entity_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_9 = Layout.from_dict(data)

                    return componentsschemas_user_data_entity_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_10 = Option.from_dict(data)

                    return componentsschemas_user_data_entity_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_11 = Property.from_dict(data)

                    return componentsschemas_user_data_entity_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_12 = Relationship.from_dict(data)

                    return componentsschemas_user_data_entity_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_13 = RelationshipKind.from_dict(data)

                    return componentsschemas_user_data_entity_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_14 = Space.from_dict(data)

                    return componentsschemas_user_data_entity_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_15 = Status.from_dict(data)

                    return componentsschemas_user_data_entity_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_16 = Task.from_dict(data)

                    return componentsschemas_user_data_entity_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_17 = TaskAttachment.from_dict(data)

                    return componentsschemas_user_data_entity_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_18 = TaskDocRelationship.from_dict(data)

                    return componentsschemas_user_data_entity_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_19 = TaskLink.from_dict(data)

                    return componentsschemas_user_data_entity_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_20 = Tenant.from_dict(data)

                    return componentsschemas_user_data_entity_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_data_entity_type_21 = UserDartboardLayout.from_dict(data)

                    return componentsschemas_user_data_entity_type_21
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_22 = View.from_dict(data)

                return componentsschemas_user_data_entity_type_22

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        paginated_user_data_entity_list = cls(
            count=count,
            next_=next_,
            previous=previous,
            results=results,
        )

        paginated_user_data_entity_list.additional_properties = d
        return paginated_user_data_entity_list

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
